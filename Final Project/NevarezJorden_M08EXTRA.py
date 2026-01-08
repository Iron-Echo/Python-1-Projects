# Name: Jorden Nevarez
# Class: INFO 1200
# Section: X02
# Professor: Noah Say
# Date: 11/11/2025
# Assignment #: M08 EXTRA

# Imports tkinter module and csv
import csv
import tkinter as tk
from tkinter import messagebox # Imports messagebox module from tkinter module
from tkinter import simpledialog # Imports simpledialog module from tkinter module

# define the csv inventory function with filename as a parameter
def inventory_from_csv(FILENAME):
    items = [] # Creats empty list
    with open(FILENAME, newline="") as file: # opens  and reads csv file
        reader = csv.reader(file) # reader object
        for row in reader: # for statement for csv file
            if row: # if statement for the row
                items.append(row[0])
    return items # returns result

# Defines the saved csv inventory function
def inventory_from_csv_saved(FILENAME, items):
    file = open(FILENAME, "w")
    for item in items:
        file.write(item + "\n")
    file.close()

# Code for using csv as the inventory
FILENAME = "C:/Users/jorde/OneDrive - Utah Valley University/Documents/INFO-1200/Final Project/inventory.csv"
inventory = inventory_from_csv(FILENAME)
if inventory == []:
# Creates base inventory variable
    inventory = ["Regular Mouse", "Regular Keyboard", "Regular Computer"]
    inventory_from_csv_saved(FILENAME, inventory)
# Base inventory size variable
inventory_size = 8

# Creates the store parts variable to add into inventory
store_parts = ["Logitech Mouse", "Corsair Keyboard", "Desktop Computer", "144 Hz OLED Monitor", "Laptop Computer", "Nvidia RTX 3060 Ti", "AMD Ryzen 5 3600x"]

# Creates root window
root = tk.Tk()
root.title("Computer Parts Store GUI") # Creates root window title
root.geometry("360x360") # Creates root window framing

# Creates lst variable and packs it to display
lst = tk.Listbox(root)
lst.pack(fill="both", expand=True, padx=10, pady=10) # Fills out when window is altered and framed 10 on the x and y

#
size_label = tk.Label(root, text="Inventory: 0 / 8")
size_label.pack(pady=5)

# Defines refresh list function
def refresh_list():
    lst.delete(0, tk.END) # Calls lst variable
    for i, item in enumerate(inventory, start=1): # Enumerates inventory
        lst.insert(tk.END, f"{i}, {item}") # Inserts the needed variables
    #
    size_label.config(text=f"Inventory: {len(inventory)} / {inventory_size}")

# Defines the show function
def on_show():
    inventory.sort()
    refresh_list() # Calls the refresh list function
    messagebox.showinfo("Show", "Inventory refreshed.") # Creates a messagebox

# Creates the on grab function
def on_grab():
    if len(inventory) >= inventory_size:
        messagebox.showerror("Error", "Your cant carry any more parts. Please drop something") # Creates a messagebox and displays message
        return # Return result
    #
    parts_list = ""
    for i, part in enumerate(store_parts, start=1):
        parts_list += f"{i}. {part}\n"
    choice = simpledialog.askstring("Grab", "Choose a part number to add:\n\n" + parts_list)
    if choice is None:
        return
    if not choice.isdigit():
        messagebox.showerror("Error, Please enter a valid number.")
        return
    choice = int(choice)
    if choice < 1 or choice > len(store_parts):
        messagebox.showerror("Error", "Invalid part number.")
        return
    name = store_parts[choice -1]
    inventory.append(name) # Appends name
    refresh_list() # Calls refresh list function
    messagebox.showinfo("Grab", f"{name} Part was added to your inventory.") # Creates messagebox to show info

# Created on edit function
def on_edit():
    if not inventory: # Creates if not statement
        messagebox.showinfo("Edit", "No parts to edit.") # Creates messagebox to show info
    sel = lst.curselection()
    if not sel: # Creates an if not statement
        messagebox.showerror("Error", "Select a part on the list to edit") # Creates a messsagebox to show error
        return # Returns
    idx = sel[0] # Binds variable to sel
    new_name = simpledialog.askstring("Edit", "Updated part name:") # Craetes new name variable
    if new_name: # Creates if statement
        new_name = new_name.strip() # Uses the strip method on new name variable
        if not new_name: # Creates an if not statement
            messagebox.showerror("Error", "part name cant be blank.") # Creates a messagebox to show error
            return # Returns
        inventory[idx] = new_name
        refresh_list() # Calls the refresh list function
        messagebox.showinfo("Edit", f"part number {idx+1} was updated.") # Creates messagebox to show info

#
def on_drop(): # Creates the on drop function
    if not inventory: # Creates an if not statement
        messagebox.showinfo("Drop", "No parts to drop.") # Creates a messagebox to show info
        return # Returns
    sel = lst.curselection()
    if not sel: # Creates an if not statement
        messagebox.showerror("Error", "Select a part on the list to drop.") # Creates a messagebox to show error
        return # Returns
    idx = sel[0]
    item = inventory.pop(idx) # Performas the pop method on inventory
    refresh_list() # Calls the refresh list function
    messagebox.showinfo("Drop", f"{item} as dropped.") # Creates a messagebox to show info

#
def set_size():
    global inventory_size
    new_size = simpledialog.askinteger("Inventory Size", "Enter a new max inventory size.")
    if new_size is None:
        return
    if new_size < 1:
        messagebox.showerror("Error", "Inventory  Size cannot be less than 1")
        return
    inventory_size = new_size
    refresh_list()
    messagebox.showinfo("Inventory Size", f"Inventory size changed to {inventory_size}.")
# Creates the root window exit
def on_exit():
    inventory_from_csv_saved("inventory.csv", inventory)
    messagebox.showinfo("Saved", "inventory has been saved to the csv file.")
    root.destroy() # Destroys root window

# Creates the framing
frame = tk.Frame(root)
frame.pack(pady=6) # y 6

# Creates the buttons
tk.Button(frame, text="Show", width=8, command=on_show).grid(row=0, column=0, padx=4)
tk.Button(frame, text="Grab", width=8, command=on_grab).grid(row=0, column=1, padx=4)
tk.Button(frame, text="Edit", width=8, command=on_edit).grid(row=0, column=2, padx=4)
tk.Button(frame, text="Drop", width=8, command=on_drop).grid(row=0, column=3, padx=4)
tk.Button(frame, text="Set Size", width=8, command=set_size).grid(row=1, column=0, pady=4)

# Seperate exit button
tk.Button(root, text="Exit", command=on_exit).pack(pady=6)

# Calls the refresh function and mainloop command displays the window
refresh_list()
root.mainloop()

