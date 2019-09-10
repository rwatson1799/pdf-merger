# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pdf_merging import merge_pdfs

# Helper functions
def merge():
    paths = fileLB.get(0, END)
    outputFile = filedialog.asksaveasfilename(initialdir="/", title="Select save location", filetypes=[("PDF files", "*.pdf")])

    # append the file extension if it doesn't exist
    if outputFile[-4:] != ".pdf":
        outputFile += ".pdf"

    # if the output file string is not empty
    if outputFile != "":
        merge_pdfs(paths, output=outputFile)


def open_file():
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=[("PDF files", "*.pdf")])
    
    for name in filenames:
        fileLB.insert(END, name)
    

# Initialise the window
window = Tk()
window.title("PDF Merger")
# window.geometry('200x200')

# Create widgets
fileLB = Listbox(window, width=50)
openFileBtn = Button(window, text='Open File', width=10, command=open_file)
mergeBtn = Button(window, text='Merge', width=10, command=merge)


openFileBtn.pack(padx=5, pady=5)
fileLB.pack(padx=5, pady=5)
mergeBtn.pack(padx=5, pady=5)

# Start the main loop
window.mainloop()

