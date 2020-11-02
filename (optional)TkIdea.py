#gui test
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog,Text
import os

root = tk.Tk()

def addApp():
    import ddos

canvas = tk.Canvas(root, height=700, width=700, bg="#082F03")
canvas.pack()

frame = tk.Frame(root, bg="#0A033F")
frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1)

Ddos = tk.Button(frame, text="DDoS", padx=700, pady=700, fg="white",bg="#0A033F", command=addApp)
Ddos.pack()

root.mainloop()

