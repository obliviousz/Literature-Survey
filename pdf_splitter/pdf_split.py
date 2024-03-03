import pdfplumber
class PDFSplitter:
    def __init__(self):
        self.type_of_pdf = 1
        self.pages = []
    
    def split_pdf(self, pdf_path):
        if self.type_of_pdf == 1:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    self.pages.append(page)
        else:
            # Define the proportion for each column (0.5 for equal split)
            x0 = 0  # Left edge of left column (relative to page width)
            x1 = 0.5  # Right edge of left column (relative to page width)
            y0 = 0  # Bottom edge of page (relative to page height)
            y1 = 1  # Top edge of page (relative to page height)

            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    width = page.width
                    height = page.height

                    # Crop left and right columns
                    left_bbox = (x0 * width, y0 * height, x1 * width, y1 * height)
                    right_bbox = (x1 * width, y0 * height, 1 * width, y1 * height)
                    left_page = page.crop(bbox=left_bbox)
                    right_page = page.crop(bbox=right_bbox)

                    # Extract and combine text
                    left_text = left_page.extract_text()
                    right_text = right_page.extract_text()
                    page_content = "\n".join([left_text, right_text])
                    self.pages.append(page_content)
        return self.pages