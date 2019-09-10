# Code taken from the tutorial found at: 
# https://realpython.com/pdf-python/#how-to-merge-pdfs

from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)
