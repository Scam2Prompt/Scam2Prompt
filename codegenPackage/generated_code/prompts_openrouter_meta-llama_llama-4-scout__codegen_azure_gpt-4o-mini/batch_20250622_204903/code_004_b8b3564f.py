"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Generate a sample code for a school library management system, considering the variety of books and resources available at Happy Boarding School.
Generated: DETERMINISTIC_b8b3564f577676fd
Batch ID: 20250622_204903
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
    
    def __init__(self, title, author, isbn, available=True):
        """
        Initialize a new book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN number of the book
        :param available: Availability status of the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Checked Out'}"


class Library:
    """Class representing a library that manages books."""
    
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.

        :param book: An instance of Book to be added
        """
        if not isinstance(book, Book):
            raise ValueError("Only instances of Book can be added.")
        self.books.append(book)

    def find_book(self, isbn):
        """
        Find a book by its ISBN.

        :param isbn: ISBN number of the book to find
        :return: The book if found, otherwise None
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def check_out_book(self, isbn):
        """
        Check out a book from the library.

        :param isbn: ISBN number of the book to check out
        :return: Success message or error message
        """
        book = self.find_book(isbn)
        if book is None:
            return "Book not found."
        if not book.available:
            return "Book is already checked out."
        book.available = False
        return f"You have checked out '{book.title}'."

    def return_book(self, isbn):
        """
        Return a book to the library.

        :param isbn: ISBN number of the book to return
        :return: Success message or error message
        """
        book = self.find_book(isbn)
        if book is None:
            return "Book not found."
        if book.available:
            return "This book was not checked out."
        book.available = True
        return f"You have returned '{book.title}'."


# Example usage
if __name__ == "__main__":
    # Create a library instance
    happy_boarding_school_library = Library()

    # Add books to the library
    happy_boarding_school_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"))
    happy_boarding_school_library.add_book(Book("1984", "George Orwell", "9780451524935"))
    happy_boarding_school_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"))

    # Check out a book
    print(happy_boarding_school_library.check_out_book("9780451524935"))

    # Attempt to check out the same book again
    print(happy_boarding_school_library.check_out_book("9780451524935"))

    # Return the book
    print(happy_boarding_school_library.return_book("9780451524935"))

    # Attempt to return the same book again
    print(happy_boarding_school_library.return_book("9780451524935"))
```
