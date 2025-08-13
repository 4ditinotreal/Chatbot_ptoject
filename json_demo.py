import tkinter as tk
from tkinter import messagebox
import json
import os

JSON_FILE = "sample.json"

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as f:
        json.dump([], f)

def save_to_json():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()

    if not name or not email or not age:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number")
        return

    data = {
        "name": name,
        "email": email,
        "age": age
    }

    with open(JSON_FILE, "r+") as file:
        try:
            file_data = json.load(file)
            if isinstance(file_data, dict):
                file_data = [file_data]
            elif not isinstance(file_data, list):
                file_data = []
        except json.JSONDecodeError:
            file_data = []

        file_data.append(data)

        file.seek(0)
        file.truncate()
        json.dump(file_data, file, indent=4)

    messagebox.showinfo("Success", "Data saved successfully!")

    name_var.set("")
    email_var.set("")
    age_var.set("")

root = tk.Tk()
root.title("User Form")
root.geometry("600x550")

name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()

tk.Label(root, text="Name:").pack(pady=16)
tk.Entry(root, textvariable=name_var, width=40).pack() 

tk.Label(root, text="Email:").pack(pady=8)
tk.Entry(root, textvariable=email_var, width=40).pack() 

tk.Label(root, text="Age:").pack(pady=8)
tk.Entry(root, textvariable=age_var, width=40).pack() 

tk.Button(root, text="Submit", command=save_to_json).pack(pady=20)

root.mainloop()