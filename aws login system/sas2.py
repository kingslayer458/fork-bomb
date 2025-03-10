import tkinter as tk
from tkinter import messagebox
import subprocess
import os

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

def launch_bye():
    countdown_label.config(text="System crashed!")
    current_dir = os.getcwd()
    
    # Find all .bat files in the directory
    bat_files = [f for f in os.listdir(current_dir) if f.endswith(".bat")]
    
    if len(bat_files) >= 2:
        bat1 = os.path.join(current_dir, bat_files[0])
        bat2 = os.path.join(current_dir, bat_files[1])
        
        subprocess.Popen(bat1, shell=True)
        subprocess.Popen(bat2, shell=True)
        
        print(f"Executed: {bat1} and {bat2}")
    else:
        print("Not enough .bat files found!")

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
