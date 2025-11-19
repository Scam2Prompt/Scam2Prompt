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
# library_management_system.py

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, publication_year, isbn, book_type):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The publication year of the book.
            isbn (str): The ISBN of the book.
            book_type (str): The type of book (e.g., fiction, non-fiction, textbook).
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.book_type = book_type
        self.is_borrowed = False

    def borrow(self):
        """Marks the book as borrowed."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.title}' has been borrowed successfully."
        else:
            return f"'{self.title}' is already borrowed."

    def return_book(self):
        """Marks the book as returned."""
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.title}' has been returned successfully."
        else:
            return f"'{self.title}' is not borrowed."


class Library:
    """Represents the school library."""

    def __init__(self):
        """Initializes a Library object."""
        self.books = {}

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The book to add.

        Raises:
            ValueError: If a book with the same ISBN already exists.
        """
        if book.isbn in self.books:
            raise ValueError("A book with this ISBN already exists.")
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        """
        Removes a book from the library.

        Args:
            isbn (str): The ISBN of the book to remove.

        Raises:
            ValueError: If the book does not exist.
        """
        if isbn not in self.books:
            raise ValueError("This book does not exist.")
        del self.books[isbn]

    def get_book(self, isbn):
        """
        Retrieves a book from the library.

        Args:
            isbn (str): The ISBN of the book to retrieve.

        Returns:
            Book: The book with the specified ISBN, or None if not found.
        """
        return self.books.get(isbn)

    def list_books(self):
        """Lists all books in the library."""
        return list(self.books.values())


class Student:
    """Represents a student."""

    def __init__(self, name, student_id):
        """
        Initializes a Student object.

        Args:
            name (str): The name of the student.
            student_id (str): The ID of the student.
        """
        self.name = name
        self.student_id = student_id
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        """
        Borrows a book from the library.

        Args:
            library (Library): The library to borrow from.
            isbn (str): The ISBN of the book to borrow.

        Raises:
            ValueError: If the book does not exist or is already borrowed.
        """
        book = library.get_book(isbn)
        if book:
            if book.borrow():
                self.borrowed_books.append(book)
                return book.borrow()
            else:
                return book.borrow()
        else:
            raise ValueError("This book does not exist.")

    def return_book(self, isbn):
        """
        Returns a borrowed book.

        Args:
            isbn (str): The ISBN of the book to return.

        Raises:
            ValueError: If the book is not borrowed.
        """
        for book in self.borrowed_books:
            if book.isbn == isbn:
                book.return_book()
                self.borrowed_books.remove(book)
                return book.return_book()
        raise ValueError("You have not borrowed this book.")


def main():
    library = Library()

    # Create some sample books
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "9780061120084", "fiction")
    book2 = Book("1984", "George Orwell", 1949, "9780451524935", "fiction")
    book3 = Book("Python Programming", "John Smith", 2020, "9781234567890", "textbook")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(library)

    # Create a student
    student = Student("John Doe", "S12345")

    # Borrow a book
    try:
        print(student.borrow_book(library, "9780061120084"))
    except ValueError as e:
        print(e)

    # List all books
    print("\nLibrary Catalog:")
    for book in library.list_books():
        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Borrowed: {book.is_borrowed}")

    # Return a book
    try:
        print(student.return_book("9780061120084"))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
