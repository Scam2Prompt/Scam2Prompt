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
import json
from typing import List, Dict, Optional

class Book:
    """Class to represent a book in the library."""
    
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', is_available={self.is_available})"


class Volunteer:
    """Class to represent a volunteer in the library."""
    
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"Volunteer(name='{self.name}', contact='{self.contact}')"


class Library:
    """Class to manage the library network."""
    
    def __init__(self):
        self.books: List[Book] = []
        self.volunteers: List[Volunteer] = []

    def add_book(self, title: str, author: str, isbn: str) -> None:
        """Add a new book to the library."""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Added book: {new_book}")

    def remove_book(self, isbn: str) -> None:
        """Remove a book from the library by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book: {book}")
                return
        print(f"Book with ISBN {isbn} not found.")

    def distribute_book(self, isbn: str) -> Optional[Book]:
        """Distribute a book to a volunteer."""
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                print(f"Distributed book: {book}")
                return book
        print(f"Book with ISBN {isbn} is not available for distribution.")
        return None

    def return_book(self, isbn: str) -> None:
        """Return a book to the library."""
        for book in self.books:
            if book.isbn == isbn:
                book.is_available = True
                print(f"Returned book: {book}")
                return
        print(f"Book with ISBN {isbn} not found.")

    def add_volunteer(self, name: str, contact: str) -> None:
        """Add a new volunteer to the library."""
        new_volunteer = Volunteer(name, contact)
        self.volunteers.append(new_volunteer)
        print(f"Added volunteer: {new_volunteer}")

    def remove_volunteer(self, name: str) -> None:
        """Remove a volunteer from the library."""
        for volunteer in self.volunteers:
            if volunteer.name == name:
                self.volunteers.remove(volunteer)
                print(f"Removed volunteer: {volunteer}")
                return
        print(f"Volunteer with name {name} not found.")

    def save_data(self, filename: str) -> None:
        """Save library data to a JSON file."""
        data = {
            'books': [vars(book) for book in self.books],
            'volunteers': [vars(volunteer) for volunteer in self.volunteers]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename: str) -> None:
        """Load library data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.books = [Book(**book) for book in data['books']]
                self.volunteers = [Volunteer(**volunteer) for volunteer in data['volunteers']]
            print(f"Data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")


# Example usage
if __name__ == "__main__":
    library = Library()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    library.add_volunteer("John Doe", "john@example.com")
    library.distribute_book("9780743273565")
    library.return_book("9780743273565")
    library.save_data("library_data.json")
    library.load_data("library_data.json")
```
