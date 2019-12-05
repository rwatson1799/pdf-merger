# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pdf_merging import merge_pdfs
import os

fileDict = {}

# Helper functions
def merge():
    files = fileLB.get(0, END)
    outputFile = filedialog.asksaveasfilename(initialdir="/", title="Select save location", filetypes=[("PDF files", "*.pdf")])

    # append the file extension if it doesn't exist
    if outputFile[-4:] != ".pdf":
        outputFile += ".pdf"
    
    # create array of file paths from the dictionary
    paths = []
    for name in files:
        paths.append(fileDict[name])

    # if the output file string is not empty
    if outputFile != "":
        merge_pdfs(paths, output=outputFile, setBookmarks=bookmarkVar.get())


def open_file():
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=[("PDF files", "*.pdf")])
    
    for name in filenames:
        shortName = os.path.basename(name)
        fileDict[shortName] = name

        # fileLB.insert(END, name)
        fileLB.insert(END, os.path.basename(name))

def remove_file():
    fileLB.delete(ANCHOR)

def move_file_up():
    if fileLB.size() == 0:
        return

    index = fileLB.curselection()[0]

    if index > 0:
        filename = fileLB.get(index)
        fileLB.delete(index)
        fileLB.insert(index - 1, filename)

def move_file_down():
    if fileLB.size() == 0:
        return

    index = fileLB.curselection()[0]

    if index < fileLB.size():
        filename = fileLB.get(index)
        fileLB.delete(index)
        fileLB.insert(index + 1, filename)

# Initialise the window
bgColour = "light blue"
window = Tk()
window.title("PDF Merger")
window['bg'] = bgColour

# Create widgets
fileBtnFrame = Frame(window, background=bgColour)
moveBtnFrame = Frame(window, background=bgColour)
mergeOptionFrame = Frame(window, background=bgColour)

titleLabel = Label(window, text="PDF Merger", font=("Courier bold", 30), background=bgColour)
fileLB = Listbox(window, width=50)
moveUpBtn = Button(moveBtnFrame, text="Move Up", width=10, command=move_file_up)
moveDownBtn = Button(moveBtnFrame, text="Move Down", width=10, command=move_file_down)
openBtn = Button(fileBtnFrame, text="Open PDF", width=10, command=open_file)
removeBtn = Button(fileBtnFrame, text="Remove PDF", width=10, command=remove_file)
mergeBtn = Button(mergeOptionFrame, text="Merge", width=10, command=merge)

bookmarkVar = IntVar()
bookmarkCB = Checkbutton(mergeOptionFrame, text="Set Bookmarks", width=10,
onvalue=1, offvalue=0, variable=bookmarkVar, background=bgColour)

# Pack widgets
titleLabel.pack(padx=5, pady=5)
fileBtnFrame.pack(padx=5, pady=5)
fileLB.pack(fill=X, padx=5, pady=5)
moveBtnFrame.pack(padx=5, pady=5)
mergeOptionFrame.pack(padx=5, pady=5)
openBtn.pack(side=LEFT, padx=25, pady=5)
removeBtn.pack(side=RIGHT, padx=25, pady=5)
moveUpBtn.pack(padx=5, pady=5)
moveDownBtn.pack(padx=5, pady=5)
mergeBtn.pack(side=LEFT, padx=25, pady=5)
bookmarkCB.pack(side=RIGHT, padx=25, pady=5)

# Start the main loop
window.mainloop()