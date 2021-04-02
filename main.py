from tkinter import *

BG_COLOR = 'SlateGray3'
BUTTON_COLOR = 'SlateGray4'
FONT = 'arial 12 bold'

root = Tk()
root.geometry('400x400')
root.config(bg=BG_COLOR)
root.resizable(0, 0)
root.title("Smart Readathon Tracker")

frame = Frame(root)
frame.pack(side = RIGHT)

# scroll bar and text area
scroll = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)

title = StringVar()
author = StringVar()

Label(root, text='Title', font=FONT, bg=BG_COLOR).place(x=30, y=20)
Entry(root, textvariable=title).place(x=100, y=20)
Label(root, text='Author', font=FONT, bg=BG_COLOR).place(x=30, y=70)
Entry(root, textvariable=author).place(x=130, y=70)

root.mainloop()