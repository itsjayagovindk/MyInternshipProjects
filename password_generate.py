import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid positive number.")
            return
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_display.config(state=tk.NORMAL)
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_display.get(1.0, tk.END))
    messagebox.showinfo("Copied", "Password has been copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

length_label = tk.Label(frame, text="Enter Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2, padx=5, pady=5)

password_display = tk.Text(frame, height=5, width=30, state=tk.DISABLED)
password_display.grid(row=2, columnspan=2, padx=5, pady=5)

copy_button = tk.Button(frame, text="Copy Password", command=copy_password)
copy_button.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
