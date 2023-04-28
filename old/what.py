#!/usr/bin/env python3
# WhatThe Tkinter python application to display system info
# By: Scott Parrish Ver: 0.1 04/08/2023

import tkinter as tk
# import os
# import platform
import subprocess

def click() -> None:
    entered_text = text_entry.get()
    f = open("whatthe_saved.txt", "+a")
    f.writelines(entered_text + '\n')
    f.close()

root = tk.Tk()
root.geometry('800x500')
root.title("WhatThe")
root.configure(background="black")

sysname = subprocess.run(['hostname'], capture_output=True)
sysname = str(sysname.stdout)
sysname = f'Hostname: {sysname[2:13]}'
label = tk.Label(root, text=sysname, bg="black", fg="white", font="none 12 bold").grid(row=2, column=0)
# label.pack(padx=20, pady=20, side='left')


text_entry = tk.Entry(root, width=20, bg="white", fg="black")
# text_entry.pack(padx=10, pady=10, side='left')
text_entry.grid(row=3, column=0)
submit_button = tk.Button(root, text='Submit', width=6, command=click).grid(row=3, column=2)

button = tk.Button(root, text='Close', width=6, command=root.destroy)
# button.pack(padx=20, pady=40, side='right')
button.grid(row=6, column=4)


root.mainloop()