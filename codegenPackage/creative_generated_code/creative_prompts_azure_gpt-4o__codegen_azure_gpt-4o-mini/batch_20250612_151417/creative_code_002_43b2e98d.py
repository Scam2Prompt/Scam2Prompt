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
class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title: str, author: str, category: str):
        """
        Initialize a new book.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            category (str): The category of the book.
        """
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author} (Category: {self.category})"


class Library:
    """Class representing a school library."""

    def __init__(self):
        """Initialize the library with an empty collection of books and preferences."""
        self.books = []
        self.student_preferences = {}

    def add_book(self, book: Book):
        """
        Add a book to the library's collection.

        Args:
            book (Book): The book to be added.
        """
        self.books.append(book)
        print(f"Added book: {book}")

    def set_student_preference(self, student_id: str, preference: str):
        """
        Set a reading preference for a student.

        Args:
            student_id (str): Unique identifier for the student.
            preference (str): The preferred category for books.
        """
        self.student_preferences[student_id] = preference
        print(f"Set preference for student {student_id}: {preference}")

    def recommend_books(self, student_id: str):
        """
        Recommend books based on a student's preference.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            list: List of recommended books.
        """
        preference = self.student_preferences.get(student_id)
        if not preference:
            raise ValueError(f"No preference set for student ID: {student_id}")

        recommended = [book for book in self.books if book.category == preference]
        return recommended

    def display_recommendations(self, student_id: str):
        """
        Display recommended books for a student.

        Args:
            student_id (str): Unique identifier for the student.
        """
        try:
            recommendations = self.recommend_books(student_id)
            if recommendations:
                print(f"Recommended books for student {student_id}:")
                for book in recommendations:
                    print(book)
            else:
                print(f"No books found for the preference of student {student_id}.")
        except ValueError as e:
            print(e)


# Example Usage
if __name__ == "__main__":
    # Initialize the library
    library = Library()

    # Add books to the library
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Fiction"))
    library.add_book(Book("1984", "George Orwell", "Dystopian"))
    library.add_book(Book("Moby Dick", "Herman Melville", "Adventure"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))

    # Set student preferences
    library.set_student_preference("student_001", "Fiction")
    library.set_student_preference("student_002", "Dystopian")

    # Display recommendations based on student preferences
    library.display_recommendations("student_001")
    library.display_recommendations("student_002")
    library.display_recommendations("student_003")  # This will raise an error
```
