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
# School Library Management System for Happy Boarding School
# Language: Python 3

import datetime


class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, title, author, isbn, copies):
        """
        Initialize a book with title, author, ISBN, and number of copies.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        """
        String representation of the book.
        """
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Copies: {self.copies}"


class Library:
    """
    Represents the library system.
    """

    def __init__(self):
        """
        Initialize the library with an empty collection of books and borrowed records.
        """
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, book):
        """
        Add a book to the library collection.
        """
        if book.isbn in self.books:
            self.books[book.isbn].copies += book.copies
        else:
            self.books[book.isbn] = book

    def remove_book(self, isbn):
        """
        Remove a book from the library collection by ISBN.
        """
        if isbn in self.books:
            del self.books[isbn]
        else:
            raise ValueError("Book not found in the library.")

    def borrow_book(self, isbn, student_name):
        """
        Borrow a book from the library.
        """
        if isbn not in self.books:
            raise ValueError("Book not found in the library.")
        book = self.books[isbn]
        if book.copies <= 0:
            raise ValueError("No copies available for borrowing.")
        book.copies -= 1
        borrow_date = datetime.date.today()
        self.borrowed_books[(isbn, student_name)] = borrow_date

    def return_book(self, isbn, student_name):
        """
        Return a borrowed book to the library.
        """
        if (isbn, student_name) not in self.borrowed_books:
            raise ValueError("This book was not borrowed by the student.")
        book = self.books.get(isbn)
        if book:
            book.copies += 1
        del self.borrowed_books[(isbn, student_name)]

    def list_books(self):
        """
        List all books in the library.
        """
        return [str(book) for book in self.books.values()]

    def list_borrowed_books(self):
        """
        List all borrowed books with student names and borrow dates.
        """
        return [
            f"{self.books[isbn].title} borrowed by {student_name} on {borrow_date}"
            for (isbn, student_name), borrow_date in self.borrowed_books.items()
        ]


# Example usage
if __name__ == "__main__":
    # Create library instance
    library = Library()

    # Add books to the library
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "1234567890", 5))
    library.add_book(Book("1984", "George Orwell", "0987654321", 3))

    # List all books
    print("Books in the library:")
    for book in library.list_books():
        print(book)

    # Borrow a book
    try:
        library.borrow_book("1234567890", "Alice")
        print("\nAfter borrowing:")
        for book in library.list_books():
            print(book)
    except ValueError as e:
        print(f"Error: {e}")

    # List borrowed books
    print("\nBorrowed books:")
    for borrowed in library.list_borrowed_books():
        print(borrowed)

    # Return a book
    try:
        library.return_book("1234567890", "Alice")
        print("\nAfter returning:")
        for book in library.list_books():
            print(book)
    except ValueError as e:
        print(f"Error: {e}")
```
