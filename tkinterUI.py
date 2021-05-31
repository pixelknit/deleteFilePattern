import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk



def showImage():
	fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Imafe File", filetypes = (("JPG file", "*.jpg"),("PNG file", "*.png"), ("JPEG file", "*.jpeg"), ("All files", "*.*")))
	img = Image.open(fln)
	img.thumbnail((350,350))
	img = ImageTk.PhotoImage(img)
	lbl.configure(image=img)
	lbl.image = img

root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)


root.title("Image browser")
root.geometry("300x350")
root.mainloop()