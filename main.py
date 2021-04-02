import tkinter as tk
import time

BG_COLOR = 'SlateGray3'
BUTTON_COLOR = 'SlateGray4'
FONT = 'arial 12 bold'
localtime = list(time.localtime())
date = f"{localtime[1]}/{localtime[2]}/{localtime[0]}"

window = tk.Tk()
window.geometry('400x400')
window.config(bg=BG_COLOR)
window.resizable(0, 0)
window.title("Smart Readathon Tracker")

frame = tk.Frame(window)
frame.pack(side=tk.BOTTOM)

scroll_bar = tk.Scrollbar(frame, orient=tk.VERTICAL)
listbox = tk.Listbox(frame, yscrollcommand=scroll_bar.set, height=12, width=100)
scroll_bar.config(command=listbox.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

title_text = tk.StringVar()
title_label = tk.Label(window, text="Title", font=FONT, bg=BG_COLOR)
title_label.place(x=30, y=20)
title_entry = tk.Entry(window, textvariable=title_text)
title_entry.place(x=100, y=20)

author_text = tk.StringVar()
author_label = tk.Label(window, text="Author", font=FONT, bg=BG_COLOR)
author_label.place(x=30, y=50)
author_entry = tk.Entry(window, textvariable=author_text)
author_entry.place(x=100, y=50)

books = []

def save_book():
    books.append([title_text.get(), author_text.get()])
    listbox.delete(0, tk.END)
    with open("books.txt", "w") as f:
        for title, author in books:
            listbox.insert(tk.END, title)
            print(f"{title}|{author}|{date}", file=f)
    title_text.set("")
    author_text.set("")
    title_entry.focus_set()


save_button = tk.Button(window, text="SAVE", bg=BUTTON_COLOR, command=save_book)
save_button.place(x=30, y=100)

window.mainloop()
