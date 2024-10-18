
import customtkinter
import tkinter as tk
from PIL import Image , ImageTk
from tkinter import *
from tkinter import messagebox
import re

root = tk.Tk()
root.geometry('800x800')
root.resizable(width=False, height=False)

app = customtkinter.CTk()
app.title('Password Strength Checker')
app.geometry('400x300+480+200')
app.config(bg='#000')
app.resizable(False,False)
app.iconbitmap('lock.ico')

title_font = ('Arial',20,'bold')
subtitle_font = ('Arial',17,'bold')
button_font = ('Arial',18,'bold')

app.mainloop()