"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Develop a script that compiles a list of published works by an author, using Rade Milosavljevic's books as a reference for formatting and content organization.
Generated: DETERMINISTIC_5b38c788f8f33d90
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to compile a list of published works by an author.
This script uses Rade Milosavljevic's books as a reference for formatting and content organization.
"""

import json

# Define a class to represent a published work
class PublishedWork:
    def __init__(self, title, year, genre, publisher):
        """
        Initialize a PublishedWork instance.

        :param title: Title of the work
        :param year: Year of publication
        :param genre: Genre of the work
        :param publisher: Publisher of the work
        """
        self.title = title
        self.year = year
        self.genre = genre
        self.publisher = publisher

    def to_dict(self):
        """
        Convert the PublishedWork instance to a dictionary.

        :return: Dictionary representation of the work
        """
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "publisher": self.publisher,
        }


# Function to compile a list of works
def compile_published_works():
    """
    Compile a list of published works by an author.

    :return: List of PublishedWork instances
    """
    try:
        # Example list of works (using Rade Milosavljevic's books as a reference)
        works = [
            PublishedWork("Book Title 1", 2001, "Fiction", "Publisher A"),
            PublishedWork("Book Title 2", 2005, "Non-Fiction", "Publisher B"),
            PublishedWork("Book Title 3", 2010, "Poetry", "Publisher C"),
            PublishedWork("Book Title 4", 2015, "Drama", "Publisher D"),
        ]
        return works
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while compiling works: {e}")
        return []


# Function to save the compiled works to a JSON file
def save_works_to_file(works, filename="published_works.json"):
    """
    Save the list of works to a JSON file.

    :param works: List of PublishedWork instances
    :param filename: Name of the file to save the works
    """
    try:
        # Convert works to a list of dictionaries
        works_dict = [work.to_dict() for work in works]

        # Write to a JSON file
        with open(filename, "w") as file:
            json.dump(works_dict, file, indent=4)
        print(f"Works successfully saved to {filename}")
    except Exception as e:
        # Handle file I/O errors
        print(f"An error occurred while saving works to file: {e}")


# Main function to execute the script
def main():
    """
    Main function to compile and save the list of published works.
    """
    print("Compiling published works...")
    works = compile_published_works()

    if works:
        print("Saving works to file...")
        save_works_to_file(works)
    else:
        print("No works to save.")


# Entry point of the script
if __name__ == "__main__":
    main()
```
