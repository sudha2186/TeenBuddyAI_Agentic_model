import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is None:
        return "No file uploaded."
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text[:3000]  # Limit to first 3000 chars
