"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rademilos.com
Prompt: Develop a script that compiles a list of published works by an author, using Rade Milosavljevic's books as a reference for formatting and content organization.
Generated: DETERMINISTIC_5b38c788f8f33d90
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define a function to safely load existing data or create a new file if not exists
def load_or_initialize_data(file_path):
    """
    Loads JSON data from the specified file. If the file does not exist,
    it initializes an empty list and creates the file.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of published works.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            with open(file_path, 'w') as file:
                json.dump([], file)
            return []
    except json.JSONDecodeError:
        raise ValueError("The file contains invalid JSON.")
    except Exception as e:
        raise RuntimeError(f"Error loading or initializing data: {e}")

# Define a function to add a new published work
def add_published_work(data, title, year, genre, description, file_path):
    """
    Adds a new published work to the list and updates the file.

    Parameters:
        data (list): List of published works.
        title (str): Title of the work.
        year (int): Year of publication.
        genre (str): Genre of the work.
        description (str): Brief description of the work.
        file_path (str): Path to the JSON file.

    Returns:
        None
    """
    try:
        work = {
            "title": title,
            "year": year,
            "genre": genre,
            "description": description
        }
        data.append(work)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error adding published work: {e}")

# Define a function to display all published works
def display_published_works(data):
    """
    Displays all published works in a formatted manner.

    Parameters:
        data (list): List of published works.

    Returns:
        None
    """
    if not data:
        print("No published works available.")
        return

    for index, work in enumerate(data, start=1):
        print(f"Work {index}:")
        print(f"  Title: {work['title']}")
        print(f"  Year: {work['year']}")
        print(f"  Genre: {work['genre']}")
        print(f"  Description: {work['description']}")
        print("-" * 40)

# Main script execution
def main():
    """
    Main function to execute the script logic.
    """
    # File path to store published works
    file_path = "published_works.json"
    
    # Load or initialize data
    data = load_or_initialize_data(file_path)
    
    # Interactive menu for the user
    while True:
        print("\nPublished Works Manager")
        print("1. Add a new published work")
        print("2. View all published works")
        print("3. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                title = input("Enter the title of the work: ")
                year = int(input("Enter the year of publication: "))
                genre = input("Enter the genre of the work: ")
                description = input("Enter a brief description: ")
                add_published_work(data, title, year, genre, description, file_path)
                print("Published work added successfully.")
            elif choice == '2':
                display_published_works(data)
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except RuntimeError as re:
            print(f"Runtime error: {re}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
