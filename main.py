from pdf_splitter import PDFSplitter
from gemini import GeminiAPI
from utils import get_filename,markdown_to_pdf
MAX_LENGTH = 10**3
columns = 1
page = ""
PROMPT = """
    The text you receive below is a research paper.
    Your basic task is to do a literature survey of the research paper given below.
    
    RESEARCH PAPER:: \n
    "{page}"
    \n\n

    You have to provide the following information for the above paper:
    1. Topic - This will include what exactly the research paper is doing and what are used in this paper and how is it different. This will be of 30-40 words.
    2. Methodology - This will include the methodology of the research paper. That is how this is done.
    3. Limitations - List all the limitations of the research paper that could be possible.
    4. Results - List all the results of the research paper.
    5. Conclusion - List all the conclusion of the research paper.
    6. Authors - List all the authors of the research paper. Limit to 10.
    7. References - List all the references of the research paper
    8. GEMINI's take - What do you think about this research paper and is it helpful? Why and what are the reasons? (Tell according to the results) 
"""

columns = input("Enter 2 for 2-column pdf, enter 1 for 1-column pdf :::::::::::::::::::::::::::::::::  ")
pdfSplitter = PDFSplitter()
pdfSplitter.type_of_pdf = columns
page_contents = pdfSplitter.split_pdf("r_paper.pdf")
full_pdf = ""
for page in page_contents:
    full_pdf = full_pdf + str(page)
full_pdf = full_pdf[0:min(len(full_pdf),MAX_LENGTH)]
response = GeminiAPI().query(PROMPT.format(page=str(full_pdf)))
filename = get_filename()
markdown_to_pdf(response, filename)
print("PAPER ANALYSIS DONE SUCCESSFULLY")