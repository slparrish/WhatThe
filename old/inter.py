import tkinter as tk
import os
import platform

window = tk.Tk()
window.geometry("800x500")
window.title("WhatThe")

osname = os.name
osname = osname.capitalize()
system = f'Operating System: {platform.system()}'
print(system)


label = tk.Label(window, text=system)
label.pack(padx=20, pady=20)

textbox = tk.Text(window)
textbox.pack(padx=20, pady=20)

window.mainloop()