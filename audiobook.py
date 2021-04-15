import pyttsx3
import PyPDF2
book=open('machine learning.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()

#page = pdfReader.getPage(51)
#above line is for to read a single page from the book
for i in range(0,pages):
    #above for loop is for to read the pages 1 to end of the book
    page=pdfReader.getPage(i)
    text=page.extractText()
    speaker.say(text)
    speaker.say(' Thank you Prashant kumar')
    speaker.runAndWait()
