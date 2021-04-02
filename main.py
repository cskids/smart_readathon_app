import tkinter as tk

BG_COLOR = 'SlateGray3'

window = tk.Tk()
window.geometry('400x400')
window.config(bg=BG_COLOR)
window.resizable(0, 0)
window.title("Smart Readathon Tracker")

window.mainloop()