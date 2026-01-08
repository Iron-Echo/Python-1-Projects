# Imports csv and sys modules
import csv
import sys

FILENAME = "movies1.csv"

# Defines the exit program function
def exit_program():
    print("Terminating program.") # Displays termination message
    sys.exit() # calls sys module with exit function

# Defines the read movies function
def read_movies():
    try: # Creates try statement
        movies = [] # Sets movies variable to blank
        # Opens, reads, and closes csv file
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file) # Creates reader object for csv file with file as a parameter
            for row in reader: # Creates for loop
                movies.append(row) # Appends movies variable to row parameter
        return movies # Returns results from movies variable
    # Creates except statement
    except FileNotFoundError as e:
      # print(f"Could not find {FILENAME} file.") # Print message with filename
      # exit_program() # Calls the exit program function
      return movies
    # Creates except statement
    except Exception as e:
        print(type(e), e)
        exit_program() # Calls the exit program function

# Defines the write movies function with movies as a parameter
def write_movies(movies):
    # Creates a try statement
    try:
        # Opens, reads, and closes the csv file
        with open(FILENAME, "w", newline="") as file:
            # Brings up a the Blockingioerrror, as a child process for the OS error
        #raise BlockingIOError("Test the OSError exception.")
            writer = csv.writer(file) # Creates writer object for the csv file with file as a parameter
            writer.writerows(movies)
    # Creates exception statement for OS errors
    except OSError as e:
        print(type(e), e)
        exit_program() # Calls the exit program function
    # Create except statement
    except Exception as e:
        print(type(e), e)
        exit_program() # Call the exit program function

# Defines list movies function with movies as a parameter
def list_movies(movies):
    # Creates a for loop
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print() # Prints blank space

# Defines add movie function with movies as a parameter
def add_movie(movies):
    name = input("Name: ")
    while True:
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid year. Please try again.")
            continue
        if year <=0:
            print("Year must be greater than zero. Pleaser try again")
            continue
        else:
            break
    # Creates movie list
    movie = [name, year]
    movies.append(movie) # Appends movies to the movie parameter
    write_movies(movies) # Calls write movies function with movies as a parameter
    print(f"{name} was added.\n")

# Defines the delete movie function with movies as a parameter
def delete_movie(movies):
    # Create while loop
    while True:
        # Create try statement
        try:
            number = int(input("Number: ")) # Creates number variable set to an integer input from the user
        # Create except statement
        except ValueError:
            print("Invalid integer. Please try again.") # Display error message
            continue # contiunes the try statement
        if number < 1 or number > len(movies):
            # Display error message
            print("There is no movie with that number. Please try again.")
        else: # Else statement
            break # Breaks while loop
    movie = movies.pop(number - 1) 
    write_movies(movies) # Calls write movies function with movies as a parameter
    print(f"{movie[0]} was deleted.\n")

# Defines the display menu function
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

# Defines main function
def main():
    display_menu() # Calls display menu function
    movies = read_movies() # Sets movies variable to read_movies function
    # Creates while loop with commands
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break # Breaks while loop
        else:
            # Display error message
            print("Not a valid command. Please try again.\n")
    print("Bye!") # Displays exit message

if __name__ == "__main__":
    main()
