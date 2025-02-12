import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import Combobox
import pyttsx3
import os

# Initialize tkinter window
root = tk.Tk()
root.geometry("1000x650+250+70")
root.resizable(False,False)

#set logo 
logo = PhotoImage(file="2.png")
root.iconphoto(False, logo)
root.title("Welcome to Text to Speech Convertor ")
root.configure(bg="#87CEEB")

# Title of window
title_label = Label(text="TEXT TO SPEECH CONVERTOR", bg="pink", fg="black", padx="10", pady="16", font="arial 16 bold", border=2, relief=SUNKEN)
title_label.pack(pady=20, padx=13,side=TOP)

# start pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 140) 
engine.setProperty('volume', 1)

# Getting available voices
voices = engine.getProperty('voices')

#function to set the voice based on selection
def set_voice(selected_voice):
    if selected_voice == 'Male':
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice

# function to speak text
def speak():
    text = text_area.get("1.0", END)
    if not text.strip():
        return
    selected_voice = select_combobox.get()
    set_voice(selected_voice)  # Set the voice
    engine.say(text)  # Speak the text
    engine.runAndWait()

# function to save text as speech to mp3 file
def save():
    text = text_area.get("1.0", END)
    if not text.strip():
        return
    selected_voice = select_combobox.get()
    set_voice(selected_voice)
    # Now select the directory and enter filename using a file dialog
    file_name = filedialog.asksaveasfilename(
        filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")],  
        title="Save As"
    )
    # check either file name is entered by user or not
    if file_name:
        engine.save_to_file(text, file_name)  
        engine.runAndWait() 
    else:
       messagebox.showwarning("select a file name")

# Text area
text_area = Text(root, font="arial 20", bg="white", relief=SUNKEN, wrap=WORD, padx=10, pady=10)
text_area.place(x=70, y=100, width=860, height=290)

# Voice type label
select_gender = Label(root, text="SELECT GENDER", font="arial 18 bold", bg="#87CEEB", fg="black", padx=10, pady=10)
select_gender.place(x=80, y=460)

# Combobox to select voice
select_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", width=17)
select_combobox.place(x=90, y=510)

# Speak button
button_1 = Button(root, text="SPEAK", bg="white", fg="black", width=15, borderwidth=2, 
                  font="arial 20 bold", relief=SUNKEN, command=speak)
button_1.place(x=350, y=495)

# Save button
button_2 = Button(root, text="SAVE", bg="white", fg="black", width=15,
                   borderwidth=2, font="arial 20 bold", relief=SUNKEN, command=save)
button_2.place(x=650, y=495)

root.mainloop()
