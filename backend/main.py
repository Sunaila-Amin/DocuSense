from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from processor import (
    detect_file_type,
    extract_text_from_pdf,
    extract_text_from_image,
)
from summarizer import summarize_text

app = FastAPI(
    title="DocuSense API",
    description="API for document text extraction and summarization.",
    version="1.0.0",
)

# Allow frontend (React) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # you can restrict this to your frontend later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "DocuSense API is running"}


@app.post("/summarize")
async def summarize_document(file: UploadFile = File(...)) -> dict:
    """
    Accept a PDF or image file, extract its text, summarize it,
    and return both original text and summary.
    """
    file_type = detect_file_type(file.content_type)

    if file_type == "unsupported":
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {file.content_type}. Please upload a PDF or an image.",
        )

    # Extract text
    if file_type == "pdf":
        extracted_text = await extract_text_from_pdf(file)
    else:
        extracted_text = await extract_text_from_image(file)

    if not extracted_text:
        raise HTTPException(
            status_code=422,
            detail="Could not extract readable text from the document."
        )

    # Summarize text
    summary = summarize_text(extracted_text)

    if not summary:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate summary. Try with a different document."
        )

    return {
        "file_name": file.filename,
        "content_type": file.content_type,
        "original_text": extracted_text,
        "summary": summary,
        "original_length": len(extracted_text),
        "summary_length": len(summary),
        "model": "facebook/bart-large-cnn"
    }
