from tkinter import *
from datetime import date
from pathlib import Path

BG_COLOR = 'SlateGray3'
BUTTON_COLOR = 'SlateGray4'
FONT = 'arial 12 bold'
DATA_FILE = 'data.txt'

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
title_entry = Entry(root, textvariable=title)
title_entry.place(x=100, y=20)

Label(root, text='Author', font=FONT, bg=BG_COLOR).place(x=30, y=70)
author_entry = Entry(root, textvariable=author)
author_entry.place(x=130, y=70)

books = []

if Path(DATA_FILE).exists():
    with open(DATA_FILE) as f:
        for line in f:
            books.append(line.strip().split("|"))

def set_listbox():
    listbox.delete(0, END)
    for title, _, _ in books:
        listbox.insert(END, title)

def save():
    with open(DATA_FILE, 'w') as f:
        for title, author, complete_date in books:
            f.write(f"{title}|{author}|{complete_date}\n")

def reset():
    title.set('')
    author.set('')
    title_entry.focus_set()

def add_book():
    today = date.today()
    books.append([title.get(), author.get(), today.strftime("%Y-%m-%d")])
    set_listbox()
    reset()
    save()

Button(root, text='ADD', font=FONT, bg=BUTTON_COLOR, command=add_book).place(x=50, y=110)

set_listbox()
root.mainloop()