import PyPDF2
import pyttsx3

pdf_file = open('sample.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ""
for page in pdf_reader.pages:
    text += page.extract_text()


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
