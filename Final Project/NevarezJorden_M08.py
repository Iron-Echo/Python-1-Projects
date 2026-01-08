#Name: Jorden Nevarez
#Class: INFO 1200
#Section: X02
#Professor: Noah Say
#Date: 11/11/2025
#Assignment #: M08
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# Imports the csv file
import csv

# Defines title function
def display_title(): # Creates title
    print("Jorden Nevarez's Computer Parts Store") # Displays message
    print() # Blank space

# Inventory size variable
inventory_size = 8

# Defines menu function
def display_menu(): # Creates menu
    global inventory_size # Calls the global variable called inventory size
    print("COMMAND MENU") # Displays message
    print() # Displays message
    print("show - show all computer parts") # Displays message
    print("grab - grab a computer part") # Displays message
    print("edit - edit a computer part") # Displays message
    print("drop - drop a computer part") # Displays message
    print("exit - exit program") # Displays message
    print(f"inventory size - change size of inventory (Current max: {inventory_size})") # Displays message and shows the current size from the inventory size variable
    print() # Blank space

# Defines grab item function
def grab_item(inventory): # Grab item function 
    global inventory_size # Inventory size variable
    if len(inventory) >= inventory_size: # If statement for function
        print("You can't carry any more parts. Drop a part first. \n") # Displays message
    else: # Else statement
        item = input("Name of computer part: ") # Item variable
        inventory.append(item) # Appends inventory
        print(f"{item} was added to your parts inventory. \n") # Displays message

# Defines edit item function
def edit_item(inventory): # Edit item function
    number = int(input("Part number: ")) # Creates number variable
    if number < 1 or number > len(inventory): # If statement
        print("Invalid item number. \n") # Displays message
    else: # Else statement
        item = input("Updated part name: ") # Item variable
        inventory[number-1] = item
        print(f"Part number {number} was updated. \n") # Displays message
    
# Defines drop item function
def drop_item(inventory): # Drop item function
    number = int(input("Part number: ")) # Creates number variable with integer input from user
    if number < 1 or number > len(inventory): # Creates if statment 
        print("Invalid item number. \n") # Displays message
    else: # Else statement
        item = inventory.pop(number-1) # Uses the pop method on the item variable
        print(f"{item} was removed from your parts inventory. \n") # Displays message

# Defines the inventory size change function
def change_inventory_size():
    global inventory_size # Gravs the inventory size global variable
    # Creates a while statement
    while True:
        # Creates a try statement
        try:
            new_size = int(input("Enter new max inventory size: ")) # Sets the new size variable equal to the input from user as an integer 
            if new_size < 1: # If statement for new size variable greater than 1
                print("Inventory size must be a minimum of 1.\n") # Displays message
            else: # Else statement 
                inventory_size = new_size # Sets the inventory size variable equal to the new size variable
                print(f"Inventory size changed to {inventory_size}.\n") # Prints the message binded to the inventory size variable
                display_menu() # Calls display menu function to the display menu 
                break # Breaks the try statement
        # Creates an exception statement with the ValueError module
        except ValueError:
            print("Invalid number, please enter a valid number.\n") # Prints error message for an invalid number input from user

# Defines the show function with inventory as a parameter
def show(inventory):
    # Show all the item functions
    if len(inventory) ==0: 
        print("Your inventory is empty.\n") # Display message
    else:
        inventory.sort()
        print("Inventory:") # Display message
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
        print() # Blank space

# Defines main function
def main(): # Main function
    display_title() # Calls title function
    display_menu() # Calls menu function
inventory = ["Logitech Mouse", "Corsair Keyboard", "Desktop Computer", "144 Hz OLED Monitor", "Laptop Computer", "Nvidia RTX 3060 Ti", "AMD Ryzen 5 3600x"] # Creates inventory variable

#  Creates while loop
while True:
    command = input("Command: ") # Created command variable binded with input from user
    if command == "show": # If command show
        show(inventory)
    elif command == "grab": # Else if command for grab
        grab_item(inventory)
    elif command == "edit": # Else if command for edit
        edit_item(inventory)
    elif command == "drop": # Else if command for drop
        drop_item(inventory)
    elif command == "exit": # Else if command for exit
        break # Breaks the while loop
    else: # Else command
        print("Not a valid command. Please try again. \n") # Displays erorr message
print("Bye!") # Displays exit message







if __name__ == "__main__":
    main()
