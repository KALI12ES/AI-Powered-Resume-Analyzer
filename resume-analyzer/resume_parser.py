import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(file_bytes):
    try:
        doc = fitz.open(stream=BytesIO(file_bytes), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise Exception(f"PDF Parsing Failed: {e}")
