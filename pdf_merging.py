# Code adapted from the tutorial found at: 
# https://realpython.com/pdf-python/#how-to-merge-pdfs

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output, setBookmarks):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
            
            # If required, add a bookmark to the first page of each pdf
            if (page == 0) and (setBookmarks == 1):
                # The pdfName is truncated to remove the file extension
                pdfName = os.path.basename(path)[:-4]
                pageNum = pdf_writer.getNumPages() - 1
                pdf_writer.addBookmark(pdfName, pageNum)

    # Write the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)
