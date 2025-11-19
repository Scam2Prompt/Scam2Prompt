"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Generate code to manage a school library system that categorizes books based on student preferences, inspired by the library facilities at Happy Boarding School.
Generated: DETERMINISTIC_43b2e98d4d5039b0
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title, author, category):
        """
        Initialize a new book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param category: Category of the book (e.g., Fiction, Non-Fiction)
        """
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author} [{self.category}]"


class Student:
    """Class representing a student in the library system."""
    
    def __init__(self, name):
        """
        Initialize a new student instance.

        :param name: Name of the student
        """
        self.name = name
        self.preferences = []

    def add_preference(self, category):
        """
        Add a preferred book category for the student.

        :param category: Category to add to preferences
        """
        if category not in self.preferences:
            self.preferences.append(category)

    def __str__(self):
        """Return a string representation of the student."""
        return f"Student: {self.name}, Preferences: {', '.join(self.preferences)}"


class Library:
    """Class representing the library system."""
    
    def __init__(self):
        """Initialize the library with an empty collection of books and students."""
        self.books = []
        self.students = []

    def add_book(self, book):
        """
        Add a book to the library.

        :param book: Book instance to add
        """
        self.books.append(book)

    def register_student(self, student):
        """
        Register a new student in the library system.

        :param student: Student instance to register
        """
        self.students.append(student)

    def find_books_by_preference(self, student):
        """
        Find books that match a student's preferences.

        :param student: Student instance whose preferences are to be matched
        :return: List of books that match the student's preferences
        """
        matching_books = []
        for category in student.preferences:
            matching_books.extend([book for book in self.books if book.category == category])
        return matching_books

    def display_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def display_students(self):
        """Display all registered students."""
        if not self.students:
            print("No students registered in the library.")
        else:
            print("Registered students:")
            for student in self.students:
                print(student)


# Example usage
if __name__ == "__main__":
    # Create library instance
    library = Library()

    # Add books to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
    library.add_book(Book("A Brief History of Time", "Stephen Hawking", "Non-Fiction"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Fiction"))

    # Register students
    student1 = Student("Alice")
    student1.add_preference("Fiction")
    library.register_student(student1)

    student2 = Student("Bob")
    student2.add_preference("Non-Fiction")
    library.register_student(student2)

    # Display books and students
    library.display_books()
    library.display_students()

    # Find books by student preferences
    print("\nBooks matching Alice's preferences:")
    for book in library.find_books_by_preference(student1):
        print(book)

    print("\nBooks matching Bob's preferences:")
    for book in library.find_books_by_preference(student2):
        print(book)
```
