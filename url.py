import pyperclip
import pyshorteners
from tkinter import*
root = Tk()
root.geometry("500x500")
root.title("URL SHORTNER")
root.configure(bg="black")
url = StringVar()
url_address = StringVar()
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short) 
def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root,text="URL SHORTENER",font="TIMES",width=40).pack(pady=15) 
Entry(root, textvariable=url,width = 30).pack(pady=15)
Button(root, text="Generate Shortened URL",width=35, command=urlshortener).pack(pady=10)
Entry(root, textvariable=url_address,width = 30).pack( pady=10)
Button(root,text="copy url",bg="white", command= copyurl).pack(pady=15)
root.mainloop()
