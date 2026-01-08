#Name: Jorden Nevarez
#Class: INFO 1200
#Section: X02
#Professor: Say
#Date: 12/3/2025
#Assignment #: M10 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# Import csv module
import csv

# Creating the variable attache to the csv file
FILENAME = "contacts.csv"

# Define the display title function
def display_title():
    print("Jorden Nevarez's Contact Manager App") # Display title
    print() # Print blank space

# Define the display meny function
def display_menu():
    print("COMMAND MENU") # Display the command menu title
    print() # Print blank space
    print("list - Display all contacts") # Display list tab of menu
    print("view - View a contact") # Display view tab of menu
    print("add  - Add a contact") # Display add tab of menu
    print("del  - Delete a contact") # Display delete tab of menu
    print("exit - Exit program") # Display the exit tab for the menu
    print() # Print a blank space

# Define main function
def main():
    contacts = read_contacts() # Assign the contacts variable to the read contacts function
    # Calls the previous functions
    display_title()
    display_menu()
    # Creates a while loop for the command menu
    while True:
        command = input("Command: ") # Assign the command variable to the input of the user for the command question
        if command == "list": # If statement for the list command
            display(contacts) # Display function with contacts as a parameter
        elif command == "view": # Else if statement for the view command
            view(contacts) # View function with contacts as a parameter
        elif command == "add": # Else if statement for the add command
            add(contacts) # Add function with contacts as a parameter
        elif command == "del": # Else if statement for the delete command
            delete(contacts) # Delete function with contacts as a parameter
        elif command == 'exit': # Else if statement for the exit command
            break # Ends the while loop
        else: # Else statement
            print("Not a valid command. Please try again.\n") # Prints the error message
    print("Bye!") # Displays the exit message

# Defines the read contacts function
def read_contacts():
    contacts = [] # Sets the contacts variable to nothing
# Opens, reads, and closes the csv file
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file) # Creates the reader object with file as a parameter 
            for row in reader:
                contacts.append(row) # Appends the contacts variable with row as a parameter
    except FileNotFoundError: # Creates an exception statement with the file not found error function
        print("Could not find contacts file! Starting a new contacts file...") # Prints error message
    return contacts # Returns result of contacts
# Defines the display function with contacts as a parameter
def display(contacts):
    if len(contacts) == 0:
        print("There are no contacts in the list")
        print()
        return
    for i, row in enumerate(contacts, start=1): # Enumerates
        print(f"{i}. {row[0]}") # Display message with calculation
    print() # Print blank space

# Define the view function with contacts as a parameter
def view(contacts):
    number = get_contact_number(contacts) # Assings the number variable to the get contact number function with contacts as a parameter
    if number < 0: # If statement for the number variable being greater than 0
        contact = contacts[number-1] # Contact variable set to the contacts functioon with the number variable minus one as a parameter
        print("Name:", contact[0]) # Display the name message and the contact variable 0
        print("Email:", contact[1]) # Display the email message and the contact function variable 1
        print("Phone:", contact[2]) # Display the phone message and the contact function variable 2
        print() # Print a blank space

# Defines the get contact number variable with contacts as a parameter
def get_contact_number(contacts):
    while True: # Creates a while loop 
        try: # Creates a try exception statement
            number = int(input("Number: ")) # Sets the number variable to the integer input of the users answer to Number:?
        except ValueError: # Creates an except statement with the ValueError command
            print("Invalid integer.\n") # Displays error message
            return -1 # returns the result minus 1
        if number < 1 or number > len(contacts): # Creates an if statement for the number variable greater than 1 
            print("Invalid contact number.\n") # Displays the error message
            return -1 # Returns result minus 1
        # Creates an else statement
        else:
            return number # Returns the result in the number variable

# Define the add function with contacts as a parameter
def add(contacts):
    name = input("Name: ") # Creates the name variable set to the input from the user for the name question
    email = input("Email: ") # Creates the email variable set to the input from the user for the email question
    phone = input("Phone: ") # Creates the phone variable set to the input from the user for the phone question
    contact = [] # Sets the contact variable to nothing
    contact.append(name) # Appends the contact variable with name as a parameter
    contact.append(email) # Appends the contact variable with email as a parameter
    contact.append(phone) # Appends the contact variable with phone as a parameter
    contact.append(contact) # Appends the contact variable with contact as a parameter
    write_contacts(contacts) # Calls the write contacts function with contacts as the variable 
    # Prints the added message
    print("{contact[0]} was added.")
    print() # Prints a blank space

# Defines the write contacts function with contacts as a parameter
def write_contacts(contacts):
    # Opens, reads, and closes the csv file
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file) # Creates the writer object
        writer.writerows(contacts)

# Defines the delete function with contacts as a parameter
def delete(contacts):
    number = get_contact_number(contacts) # Sets the number variable to the get contact number function with contacts as a parameter
        # Creates an if statement with the number variable greater than 0
    if number > 0:
        contact = contacts.pop(number-1) # Sets the contact variable to the contacts parameter with the pop command set to the parameter of the number variable minus 1
        print(f"{contact[0]} was deleted.\n") # Displays the deleted message
    write_contacts(contact) # calls the write contacts function with contact as a parameter
    




# Added code
if __name__ == "__main__": 
    main()