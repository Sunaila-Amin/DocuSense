import pdfplumber
import pytesseract
from PIL import Image
from fastapi import UploadFile
from typing import Literal
import io


def detect_file_type(content_type: str) -> Literal["pdf", "image", "unsupported"]:
    if content_type == "application/pdf":
        return "pdf"
    if content_type.startswith("image/"):
        return "image"
    return "unsupported"


async def extract_text_from_pdf(file: UploadFile) -> str:
    """
    First try normal text extraction (pdfplumber).
    If nothing is extracted, fall back to OCR for each page (scanned PDFs).
    """
    text = ""

    # Load PDF into memory
    file_bytes = io.BytesIO(await file.read())

    # 1️⃣ Try direct text extraction
    with pdfplumber.open(file_bytes) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n"

    # If pdfplumber extracted nothing, fallback to OCR
    if text.strip():
        return text.strip()

    # 2️⃣ Fallback: OCR each page (for scanned PDFs)
    text = ""
    with pdfplumber.open(file_bytes) as pdf:
        for page in pdf.pages:
            # Convert PDF page to an image
            pil_image = page.to_image(resolution=200).original
            page_text = pytesseract.image_to_string(pil_image) or ""
            text += page_text + "\n"

    return text.strip()


async def extract_text_from_image(file: UploadFile) -> str:
    image = Image.open(file.file)
    text = pytesseract.image_to_string(image)
    return text.strip()
