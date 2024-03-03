from mistletoe import Document, HTMLRenderer
from xhtml2pdf import pisa

def markdown_to_pdf(markdown_text, output_pdf):
  """
  Converts a markdown string to PDF and saves it to the specified file using mistletoe and xhtml2pdf.

  Args:
      markdown_text: The markdown text to be converted.
      output_pdf: The name of the output PDF file.
  """
  # Convert markdown to HTML
  md = Document(markdown_text)
  renderer = HTMLRenderer()
  html = renderer.render(md)

  # Create a PDF using xhtml2pdf
  with open(output_pdf, "wb") as f:
    pisa.CreatePDF(html, f)

def get_filename():
    return "paper_analysis.pdf"