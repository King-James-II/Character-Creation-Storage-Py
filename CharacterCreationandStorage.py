# Video Game Character Management

"""
This Python program manages character data for a video game using strings, lists, and file operations.
It allows the user to add new characters, display existing characters, and save character data to a file.
"""

# Function to add a new character to the character list
def add_character(characters, name, level, health):
    characters.append((name, level, health))

# Function to display all characters in the character list
def display_characters(characters):
    print("Characters in the game:")
    for character in characters:
        print("Name:", character[0], ", Level:", character[1], ", Health:", character[2])

# Function to save character data to a file
def save_to_file(characters, filename):
    with open(filename, 'w') as file:
        for character in characters:
            file.write(f"{character[0]},{character[1]},{character[2]}\n")
    print("Character data saved to file.")

# Function to load character data from a file
def load_from_file(filename):
    characters = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, level, health = line.strip().split(',')
                characters.append((name, int(level), int(health)))
    except FileNotFoundError:
        print("File not found. No character data loaded.")
    return characters

def main():
    # Initialize an empty list to store characters
    characters = []
    # Load character data from a file if available
    filename = "characters.txt"
    characters = load_from_file(filename)

    # Display menu options
    print("1. Add Character")
    print("2. Display Characters")
    print("3. Save Characters to File")
    print("4. Quit")

    # Process user input
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            name = input("Enter character name: ")
            level = int(input("Enter character level: "))
            health = int(input("Enter character health: "))
            add_character(characters, name, level, health)
        elif choice == '2':
            display_characters(characters)
        elif choice == '3':
            save_to_file(characters, filename)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
