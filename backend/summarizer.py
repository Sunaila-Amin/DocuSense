from transformers import BartForConditionalGeneration, BartTokenizer
import torch

# Load model & tokenizer once at startup
MODEL_NAME = "facebook/bart-large-cnn"

tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)

# Use CPU
device = torch.device("cpu")
model.to(device)


def summarize_text(text: str, max_chunk_chars: int = 1200) -> str:
    """
    Summarize long text by splitting into chunks and summarizing each.
    Then merge all summaries into one.
    """
    text = text.strip()
    if not text:
        return ""

    # Split big text into smaller chunks (by characters, simple but works)
    chunks = []
    while len(text) > max_chunk_chars:
        # Break at last period before limit to avoid cutting sentences mid-way
        split_at = text.rfind(".", 0, max_chunk_chars)
        if split_at == -1:
            split_at = max_chunk_chars
        chunks.append(text[:split_at + 1])
        text = text[split_at + 1:]
    if text:
        chunks.append(text)

    summaries = []

    for chunk in chunks:
        inputs = tokenizer(
            chunk,
            max_length=1024,
            truncation=True,
            return_tensors="pt"
        ).to(device)

        summary_ids = model.generate(
            inputs["input_ids"],
            num_beams=4,
            length_penalty=2.0,
            max_length=180,
            min_length=40,
            early_stopping=True,
        )

        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )
        summaries.append(summary.strip())

    # Join individual summaries into one final paragraph
    final_summary = " ".join(summaries)
    return final_summary
