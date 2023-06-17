import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

# Create GUI
root = tk.Tk()
root.title("Password Manager")
root.geometry("600x500")

# Load passwords from JSON file
def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    return passwords

# Save passwords to JSON file
def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to add a new password
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        if website in passwords:
            messagebox.showerror("Error", "Website already exists.")
        else:
            passwords[website] = {"username": username, "password": password}
            save_passwords(passwords)
            messagebox.showinfo("Success", "Password added successfully.")
            clear_entries()
            display_passwords()

# Function to retrieve a password
def get_password():
    website = website_entry.get()

    if website in passwords:
        username = passwords[website]["username"]
        password = passwords[website]["password"]
        messagebox.showinfo("Password Details", f"Website: {website}\nUsername: {username}\nPassword: {password}")
        clear_entries()
    else:
        messagebox.showerror("Error", "Website not found.")

# Function to delete a password
def delete_password():
    website = website_entry.get()

    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        messagebox.showinfo("Success", "Password deleted successfully.")
        clear_entries()
        display_passwords()
    else:
        messagebox.showerror("Error", "Website not found.")

# Function to clear the entry fields
def clear_entries():
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to display all passwords
def display_passwords():
    # Clear existing rows
    for row in passwords_table.get_children():
        passwords_table.delete(row)

    # Insert passwords into the table
    for website, data in passwords.items():
        username = data["username"]
        password = data["password"]
        passwords_table.insert("", "end", values=(website, username, password))

# Load passwords from JSON file
passwords = load_passwords()

# Create a frame for the password table
table_frame = ttk.Frame(root)
table_frame.pack(pady=10)

# Create a Treeview widget for the passwords table
passwords_table = ttk.Treeview(table_frame, columns=("Website", "Username", "Password"), show="headings")
passwords_table.column("Website", width=200)
passwords_table.column("Username", width=200)
passwords_table.column("Password", width=200)
passwords_table.heading("Website", text="Website")
passwords_table.heading("Username", text="Username")
passwords_table.heading("Password", text="Password")
passwords_table.pack()

# Website Label and Entry
website_label = ttk.Label(root, text="Website:")
website_label.pack()
website_entry = ttk.Entry(root)
website_entry.pack()

# Username Label and Entry
username_label = ttk.Label(root, text="Username:")
username_label.pack()
username_entry = ttk.Entry(root)
username_entry.pack()

# Password Label and Entry
password_label = ttk.Label(root, text="Password:")
password_label.pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

# Add Password Button
add_button = ttk.Button(root, text="Add Password", command=add_password)
add_button.pack()

# Get Password Button
get_button = ttk.Button(root, text="Get Password", command=get_password)
get_button.pack()

# Delete Password Button
delete_button = ttk.Button(root, text="Delete Password", command=delete_password)
delete_button.pack()

# Display all passwords
display_passwords()

# Start the GUI
root.mainloop()
