import sys
from PyPDF2 import PdfReader
from markdownify import markdownify as md

def extract_text_from_pdf(pdf_path):
    pdf = PdfReader(pdf_path)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def convert_to_markdown(text):
    return md(text)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    text = extract_text_from_pdf(pdf_path)
    markdown_text = convert_to_markdown(text)
    print(markdown_text)
