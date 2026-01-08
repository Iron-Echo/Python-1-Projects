#Name: Jorden Nevarez
#Class: INFO 1200
#Section: X02
#Professor: Say
#Date: 12/3/2025
#Assignment #: M10 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# Imports the the gui module
import tkinter as tk
# Imports the functions from the logic file
from NevarezJorden_M10 import read_contacts, write_contacts

# Load the contacts
contacts = read_contacts()

# Create the functions
def list_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, contact[0])

#
def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    contact = [name, email, phone]
    contacts.append(contact)
    write_contacts(contacts)

    list_contacts()

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

#
def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        write_contacts(contacts)
        list_contacts()

#
def exit_app():
    window.destroy()

# Creates root window
window = tk.Tk()
window.title("Contact Manager GUI") # Creates the title for the root window

#
listbox = tk.Listbox(window)
listbox.pack()

#
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window)
email_entry.pack()

tk.Label(window, text="Phone").pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Creates buttons for gui
tk.Button(window, text="List Contacts", command=list_contacts).pack()
tk.Button(window, text="Add Contact", command=add_contact).pack()
tk.Button(window, text="Delete Selected", command=delete_contact).pack()
tk.Button(window, text="Exit", command=exit_app).pack()

#
list_contacts()



# Displays root window
window.mainloop()