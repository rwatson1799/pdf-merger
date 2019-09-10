# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pdf_merging import merge_pdfs
import os

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
        # fileLB.insert(END, os.path.basename(name))

def remove_file():
    fileLB.delete(ANCHOR)

def move_file_up():
    index = fileLB.curselection()[0]

    if index > 0:
        filename = fileLB.get(index)
        fileLB.delete(index)
        fileLB.insert(index-1, filename)


def move_file_down():
    index = fileLB.curselection()[0]

    if index < fileLB.size():
        filename = fileLB.get(index)
        fileLB.delete(index)
        fileLB.insert(index+1, filename)

# Initialise the window
window = Tk()
window.title("PDF Merger")
# window.geometry("100x200")

# Create widgets
titleLabel = Label(window, text="PDF Merger", font=("Courier bold", 20))
fileLB = Listbox(window, width=50)
moveUpBtn = Button(window, text="Move Up", width=10, command=move_file_up)
moveDownBtn = Button(window, text="Move Down", width=10, command=move_file_down)
openBtn = Button(window, text="Open PDF", width=10, command=open_file)
removeBtn = Button(window, text="Remove PDF", width=10, command=remove_file)
mergeBtn = Button(window, text="Merge", width=10, command=merge)


# Pack widgets
titleLabel.pack(padx=5, pady=5)
openBtn.pack(padx=5, pady=5)
moveUpBtn.pack(padx=5, pady=5)
moveDownBtn.pack(padx=5, pady=5)
fileLB.pack(fill=X, padx=5, pady=5)
removeBtn.pack(padx=5, pady=5)
mergeBtn.pack(padx=5, pady=5)

# Start the main loop
window.mainloop()

