# 📄 DocuSense – AI Document Summarizer  
### OCR + PDF Extraction + BART Summarization | FastAPI Backend + React Frontend

DocuSense is an AI-powered document summarizer that can extract text from **PDFs (both normal & scanned)** or **images**, run them through **OCR**, and generate a clean, concise summary using **BART Large CNN** — one of the most powerful NLP summarization models.

It is a complete **full-stack AI application** built with:

- 🧠 **Transformers (BART)**
- 🔍 **OCR (Pytesseract)**
- 📄 **PDF extraction (pdfplumber)**
- ⚡ **FastAPI backend**
- 🎨 **React + Tailwind frontend**

---

## 🚀 Features

### 📑 Document Processing
- Upload **PDF** or **image**
- Extract text from:
  - Digital PDFs
  - **Scanned PDFs** (OCR fallback)
  - Images (PNG, JPG, JPEG)

### 🤖 AI Summarization
- Uses **BART Large CNN** for high-quality abstractive summaries
- Handles long documents by chunking intelligently
- Provides clean, readable summaries

### 🖥️ Frontend Features
- Drag-and-drop style upload box
- Animated loading spinner
- Dark mode UI
- Shows:
  - Extracted text
  - AI summary
  - Character counts
- "Download Summary" button

---

## 🏗️ System Architecture
User → React Frontend → FastAPI Backend →
├── pdfplumber (PDF extraction)
├── pytesseract (OCR)
└── BART Large CNN (Summarization)

---

## 🛠️ Tech Stack

### **Frontend**
- React (Vite)
- Tailwind CSS
- Fetch API

### **Backend**
- FastAPI
- Uvicorn
- Transformers (BART)
- PyTorch
- pdfplumber
- Pytesseract
- Pillow

---

## 📂 Project Structure

DocuSense/
│
├── backend/
│ ├── main.py
│ ├── summarizer.py
│ ├── processor.py
│ ├── requirements.txt
│ └── render.yaml
│
└── docusense-frontend/
├── src/
│ ├── App.jsx
│ ├── index.css
│ └── components/
│ ├── UploadBox.jsx
│ └── ResultBox.jsx
├── index.html
├── package.json
└── tailwind.config.js

---
⚙️ Installation & Setup

1️⃣ Backend Setup (FastAPI)

Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Set Tesseract path (Windows):
Edit in processor.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Run backend:
uvicorn main:app --reload

Visit API docs:
http://127.0.0.1:8000/docs

2️⃣ Frontend Setup (React + Tailwind)

Navigate to frontend folder:

cd docusense-frontend
npm install
npm run dev

The app runs at:
http://localhost:5173

👤 Author:

Sunaila Amin
B.Tech – Computer Science & AI
