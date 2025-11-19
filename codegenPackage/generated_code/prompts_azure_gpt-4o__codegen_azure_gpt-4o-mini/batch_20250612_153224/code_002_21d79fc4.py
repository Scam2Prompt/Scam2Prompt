"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a library management system for schools that includes inventory tracking and book issuance, as described in Him Saral's Library module.
Generated: DETERMINISTIC_21d79fc489fe9618
Batch ID: 20250612_153224
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
    
    def __init__(self, title, author, isbn, quantity):
        """
        Initialize a new book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN number of the book
        :param quantity: Number of copies available
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Copies: {self.quantity}"


class Library:
    """Class representing a library management system."""
    
    def __init__(self):
        """Initialize the library with an empty inventory."""
        self.inventory = {}

    def add_book(self, book):
        """
        Add a book to the library inventory.

        :param book: Book instance to be added
        """
        if book.isbn in self.inventory:
            self.inventory[book.isbn].quantity += book.quantity
        else:
            self.inventory[book.isbn] = book

    def issue_book(self, isbn):
        """
        Issue a book from the library.

        :param isbn: ISBN number of the book to be issued
        :return: Success message or error message
        """
        if isbn in self.inventory:
            book = self.inventory[isbn]
            if book.quantity > 0:
                book.quantity -= 1
                return f"Book '{book.title}' issued successfully."
            else:
                return "Error: Book is currently unavailable."
        else:
            return "Error: Book not found in inventory."

    def return_book(self, isbn):
        """
        Return a book to the library.

        :param isbn: ISBN number of the book to be returned
        :return: Success message or error message
        """
        if isbn in self.inventory:
            self.inventory[isbn].quantity += 1
            return f"Book '{self.inventory[isbn].title}' returned successfully."
        else:
            return "Error: Book not found in inventory."

    def display_inventory(self):
        """Display the current inventory of the library."""
        if not self.inventory:
            print("No books in inventory.")
        else:
            for book in self.inventory.values():
                print(book)


# Example usage
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3))
    library.add_book(Book("1984", "George Orwell", "9780451524935", 2))

    # Displaying inventory
    print("Current Library Inventory:")
    library.display_inventory()

    # Issuing a book
    print(library.issue_book("9780743273565"))
    print(library.issue_book("9780451524935"))
    print(library.issue_book("9780451524935"))
    print(library.issue_book("9780451524935"))  # Should show error

    # Returning a book
    print(library.return_book("9780451524935"))

    # Displaying inventory after issuing and returning books
    print("\nUpdated Library Inventory:")
    library.display_inventory()
```
