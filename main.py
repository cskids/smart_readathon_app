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
frame.pack(side = BOTTOM)

# scroll bar and text area
scroll = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scroll.set, height=12, width=100, exportselection=False, selectmode=SINGLE)
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
    for book_title, _, _ in books:
        listbox.insert(END, book_title)

def save():
    if not title.get() or not author.get():
        return
    if listbox.curselection():
        edit_book()
    else:
        add_book()
    set_listbox()
    reset()
    with open(DATA_FILE, 'w') as f:
        for book_title, book_author, complete_date in books:
            f.write(f"{book_title}|{book_author}|{complete_date}\n")

def reset():
    title.set('')
    author.set('')
    title_entry.focus_set()

def add_book():
    today = date.today()
    books.append([title.get(), author.get(), today.strftime("%Y-%m-%d")])

def edit_book():
    selected = listbox.curselection()[0]
    read_date = books[selected][2]
    books[selected] = [title.get(), author.get(), read_date]

def delete_book():
    selection = listbox.curselection()
    if not selection:
        return
    selected = selection[0]
    del books[selected]
    set_listbox()
    reset()
    save()

def listbox_callback(event):
    selection = listbox.curselection()
    if selection:
        book_title, book_author, _ = books[selection[0]]
        title.set(book_title)
        author.set(book_author)

listbox.bind("<<ListboxSelect>>", listbox_callback)

Button(root, text='SAVE', font=FONT, bg=BUTTON_COLOR, command=save).place(x=30, y=110)
Button(root, text='DELETE', font=FONT, bg=BUTTON_COLOR, command=delete_book).place(x=150, y=110)

set_listbox()
root.mainloop()