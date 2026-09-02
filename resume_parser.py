import io
import pdfplumber

def extract_text_from_pdf(uploaded_file):
    """Extract text from all pages of an uploaded PDF."""
    data = uploaded_file.getvalue()
    text_parts = []
    with pdfplumber.open(io.BytesIO(data)) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts).strip()
