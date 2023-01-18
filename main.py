from tkinter import filedialog
import pyttsx3
import pdfplumber
import PyPDF2
from tkinter import *
speaker = pyttsx3.init()
voice = speaker.getProperty('voice')
speaker.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
# The step above sets the voice used in the audio. There are a bunch of different options online
def open_pdf():
#   Once the button "Open File" is clicked, the user will be prompted with their library, so for mac users it would be their finder. 
#   Then click on your desired file. 
    open_file = filedialog.askopenfilename(
        initialdir="/Users/downloads",
        title="Open PDF File",
        filetypes=(("PDF Files", "*.pdf"),("All Files", "*.*"))
    )

    if open_file:
#       This step will read the file selected, extract the desired information, and print it into the text window. 
        pdfFileObj = open(open_file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pages = pdfReader.numPages
        with pdfplumber.open(open_file) as pdf:
            for i in range(0, pages):
                page = pdf.pages[i]
                global text
                text = page.extract_text()
                my_text.insert('1.0', text)

def download_pdf_audio():
#   This step downloads the text as audio
    speaker.save_to_file(text, f"{NAME}.mp3")
    speaker.runAndWait()
def clear_pdf():
#   This function clears the textbox 
    my_text.delete(1.0, END)
NAME = input("What do you want the name of your audio to be? ")
# Below creates the pop-up and sets the conditions, which determine its appearance. 
root = Tk()
root.title("Text2Audio")
root.geometry('600x600')
my_text = Text(root, height=30, width=70)
my_text.pack(padx=30, pady=30)
my_menu = Menu(root)
root.config(menu=my_menu, bg="light blue")
# Below are the tool buttons to help navigate the pop-up display
open_button = Button(root, text="Open File", width=11, fg="black",  command=open_pdf).pack(side= TOP)
download_audio = Button(root, text="Download Audio", width=11, fg="black",  command=download_pdf_audio).pack(side= TOP)
clear_button = Button(root, text="Clear Text", width=11, fg="black", command=clear_pdf).pack(side= TOP)
exit_button = Button(root, text="Exit", width=11 , fg="black", command=root.quit).pack(side= TOP)
root.mainloop()
