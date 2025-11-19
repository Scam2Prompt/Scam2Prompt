"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Write a Python program to manage a library network like the "අහස පුස්තකාල ජාලය" described on smplanka.lk, including features for book distribution and volunteer management.
Generated: DETERMINISTIC_a5ffc42106b8ea29
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime


class Book:
    """
    Represents a book in the library network.
    """
    def __init__(self, title, author, isbn):
        self.id = str(uuid.uuid4())  # Unique identifier for the book
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Availability status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Volunteer:
    """
    Represents a volunteer in the library network.
    """
    def __init__(self, name, contact):
        self.id = str(uuid.uuid4())  # Unique identifier for the volunteer
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.name} (Contact: {self.contact})"


class LibraryNetwork:
    """
    Manages the library network, including books and volunteers.
    """
    def __init__(self):
        self.books = {}  # Dictionary to store books by their ID
        self.volunteers = {}  # Dictionary to store volunteers by their ID
        self.distribution_log = []  # Log of book distributions

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library network.
        """
        book = Book(title, author, isbn)
        self.books[book.id] = book
        print(f"Book added: {book}")

    def add_volunteer(self, name, contact):
        """
        Adds a new volunteer to the library network.
        """
        volunteer = Volunteer(name, contact)
        self.volunteers[volunteer.id] = volunteer
        print(f"Volunteer added: {volunteer}")

    def distribute_book(self, book_id, volunteer_id):
        """
        Distributes a book to a volunteer.
        """
        try:
            book = self.books[book_id]
            volunteer = self.volunteers[volunteer_id]

            if not book.is_available:
                print(f"Book '{book.title}' is not available for distribution.")
                return

            book.is_available = False
            distribution_entry = {
                "book_id": book_id,
                "volunteer_id": volunteer_id,
                "timestamp": datetime.now()
            }
            self.distribution_log.append(distribution_entry)
            print(f"Book '{book.title}' distributed to volunteer '{volunteer.name}'.")
        except KeyError as e:
            print(f"Error: {e}. Invalid book or volunteer ID.")

    def return_book(self, book_id):
        """
        Marks a book as returned and available for distribution.
        """
        try:
            book = self.books[book_id]
            if book.is_available:
                print(f"Book '{book.title}' is already available.")
                return

            book.is_available = True
            print(f"Book '{book.title}' has been returned and is now available.")
        except KeyError:
            print(f"Error: Invalid book ID.")

    def list_books(self):
        """
        Lists all books in the library network.
        """
        print("Books in the library network:")
        for book in self.books.values():
            status = "Available" if book.is_available else "Not Available"
            print(f"{book} - {status}")

    def list_volunteers(self):
        """
        Lists all volunteers in the library network.
        """
        print("Volunteers in the library network:")
        for volunteer in self.volunteers.values():
            print(volunteer)

    def view_distribution_log(self):
        """
        Displays the log of book distributions.
        """
        print("Book Distribution Log:")
        for entry in self.distribution_log:
            book = self.books[entry["book_id"]]
            volunteer = self.volunteers[entry["volunteer_id"]]
            timestamp = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"Book '{book.title}' distributed to '{volunteer.name}' on {timestamp}.")


# Example usage
if __name__ == "__main__":
    library_network = LibraryNetwork()

    # Adding books
    library_network.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    library_network.add_book("1984", "George Orwell", "9780451524935")

    # Adding volunteers
    library_network.add_volunteer("Alice", "alice@example.com")
    library_network.add_volunteer("Bob", "bob@example.com")

    # Distributing books
    book_id = list(library_network.books.keys())[0]
    volunteer_id = list(library_network.volunteers.keys())[0]
    library_network.distribute_book(book_id, volunteer_id)

    # Returning books
    library_network.return_book(book_id)

    # Listing books and volunteers
    library_network.list_books()
    library_network.list_volunteers()

    # Viewing distribution log
    library_network.view_distribution_log()
```
