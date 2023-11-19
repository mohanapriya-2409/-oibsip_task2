import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 8:
        password_label.config(text="Password length should be at least 8 characters", fg="red")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(characters, k=length))
        password_label.config(text="Generated Password: " + password, fg="green")

def reset_fields():
    length_entry.delete(0, tk.END)
    password_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x200")  # Setting window size

# Set background colors for widgets
root.configure(bg='lightgray')

# Create and place widgets
length_label = tk.Label(root, text="Enter Password Length:", bg='lightgray')
length_label.pack(anchor=tk.CENTER)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='cyan')
generate_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_fields, bg='orange')
reset_button.pack()

password_label = tk.Label(root, text="", bg='lightgray')
password_label.pack()

# Start the main loop
root.mainloop()
