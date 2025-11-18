"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Generate code to manage a school library system that categorizes books based on student preferences, inspired by the library facilities at Happy Boarding School.
Generated: DETERMINISTIC_43b2e98d4d5039b0
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class LibrarySystem:
    """
    A class to manage a school library system, categorizing books based on student preferences.
    Inspired by Happy Boarding School's library facilities.
    """

    def __init__(self):
        """
        Initialize the library system with empty book categories and student preferences.
        """
        self.book_categories = {}  # Dictionary to hold books categorized by genre
        self.student_preferences = {}  # Dictionary to hold students and their preferred genres

    def add_book(self, title, genre):
        """
        Add a book to the library under the specified genre.

        Parameters:
            title (str): The title of the book.
            genre (str): The genre/category of the book.
        """
        if genre not in self.book_categories:
            self.book_categories[genre] = []
        self.book_categories[genre].append(title)

    def register_student_preference(self, student_name, preferred_genre):
        """
        Register a student's preferred genre.

        Parameters:
            student_name (str): The name of the student.
            preferred_genre (str): The genre the student prefers.
        """
        self.student_preferences[student_name] = preferred_genre

    def recommend_books(self, student_name):
        """
        Recommend books to a student based on their preferred genre.

        Parameters:
            student_name (str): The name of the student.

        Returns:
            list: A list of book titles recommended for the student.
        """
        preferred_genre = self.student_preferences.get(student_name)
        if not preferred_genre:
            raise ValueError("Student preference not found. Please register the student first.")
        return self.book_categories.get(preferred_genre, [])

    def save_data_to_file(self, file_path):
        """
        Save the library data (books and student preferences) to a file in JSON format.

        Parameters:
            file_path (str): The path to the file where data should be saved.
        """
        data = {
            "book_categories": self.book_categories,
            "student_preferences": self.student_preferences,
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, file_path):
        """
        Load library data (books and student preferences) from a file in JSON format.

        Parameters:
            file_path (str): The path to the file from where data should be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.book_categories = data.get("book_categories", {})
                self.student_preferences = data.get("student_preferences", {})
        except Exception as e:
            print(f"Error loading data from file: {e}")


# Example usage:
if __name__ == "__main__":
    # Create library system instance
    library = LibrarySystem()

    # Add books
    library.add_book("Harry Potter and the Sorcerer's Stone", "Fantasy")
    library.add_book("Percy Jackson & The Olympians", "Fantasy")
    library.add_book("To Kill a Mockingbird", "Classic")

    # Register student preferences
    library.register_student_preference("Alice", "Fantasy")
    library.register_student_preference("Bob", "Classic")

    # Recommend books
    try:
        print("Alice's recommendations:", library.recommend_books("Alice"))
        print("Bob's recommendations:", library.recommend_books("Bob"))
    except ValueError as e:
        print(e)

    # Save data to file
    library.save_data_to_file("library_data.json")

    # Load data from file
    new_library = LibrarySystem()
    new_library.load_data_from_file("library_data.json")
    print("\nLoaded Data:")
    print("Book Categories:", new_library.book_categories)
    print("Student Preferences:", new_library.student_preferences)
```
