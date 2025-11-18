"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Create a library management system for schools that includes inventory tracking and book issuance, as described in Him Saral's Library module.
Generated: DETERMINISTIC_21d79fc489fe9618
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# library_management_system.py

class Book:
    """Class representing a book in the inventory."""

    def __init__(self, title, author, isbn, quantity):
        """
        Initialize a new book.

        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN of the book
        :param quantity: Number of copies available
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.quantity} copies available"


class Library:
    """Class representing a library management system."""

    def __init__(self):
        """Initialize the library with an empty inventory."""
        self.inventory = {}

    def add_book(self, book):
        """
        Add a book to the inventory.

        :param book: Book object to be added
        :raises ValueError: If the book already exists in the inventory
        """
        if book.isbn in self.inventory:
            raise ValueError(f"Book with ISBN {book.isbn} already exists in inventory.")
        self.inventory[book.isbn] = book

    def issue_book(self, isbn):
        """
        Issue a book to a student.

        :param isbn: ISBN of the book to be issued
        :raises ValueError: If the book is not available or out of stock
        :return: Book object that was issued
        """
        if isbn not in self.inventory:
            raise ValueError(f"Book with ISBN {isbn} not found in inventory.")
        
        book = self.inventory[isbn]
        if book.quantity <= 0:
            raise ValueError(f"Book '{book.title}' is out of stock.")

        book.quantity -= 1
        return book

    def return_book(self, isbn):
        """
        Return a book to the library.

        :param isbn: ISBN of the book to be returned
        :raises ValueError: If the book is not found in inventory
        """
        if isbn not in self.inventory:
            raise ValueError(f"Book with ISBN {isbn} not found in inventory.")
        
        self.inventory[isbn].quantity += 1

    def list_books(self):
        """List all books in the inventory."""
        return [str(book) for book in self.inventory.values()]


# Example usage
if __name__ == "__main__":
    # Create library and add books
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3)
    book2 = Book("1984", "George Orwell", "9780451524935", 2)

    library.add_book(book1)
    library.add_book(book2)

    # List available books
    print("Available books:")
    print("\n".join(library.list_books()))

    # Issue a book
    try:
        issued_book = library.issue_book("9780743273565")
        print(f"Issued: {issued_book}")
    except ValueError as e:
        print(f"Error issuing book: {e}")

    # Return a book
    try:
        library.return_book("9780743273565")
        print("Book returned successfully.")
    except ValueError as e:
        print(f"Error returning book: {e}")

    # Check inventory after issuing and returning
    print("\nAvailable books after issuing and returning:")
    print("\n".join(library.list_books()))
```
