"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Suggest tools or libraries to implement a virtual library system similar to the "Biblioteca virtual" referenced on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_194b8714dbb168bb
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# VirtualLibrary.py

"""
Virtual Library System

This module implements a simple virtual library system. It allows for adding,
removing, and searching for books. The system uses an in-memory data structure 
to store book details.

Dependencies:
- Python 3.x
"""

class Book:
    """
    Represents a book in the virtual library.
    """

    def __init__(self, title, author, isbn):
        """
        Initializes a new book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn})"


class VirtualLibrary:
    """
    Represents a virtual library that manages a collection of books.
    """

    def __init__(self):
        """Initializes the virtual library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The book to add to the library.

        Raises:
            ValueError: If the book is already in the library.
        """
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("This book is already in the library.")
        self.books.append(book)

    def remove_book(self, isbn):
        """
        Removes a book from the library by its ISBN.

        Args:
            isbn (str): The ISBN of the book to remove.

        Raises:
            ValueError: If the book with the specified ISBN is not found.
        """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return
        raise ValueError("Book with this ISBN not found.")

    def search_books(self, query):
        """
        Searches for books by title or author.

        Args:
            query (str): The search term to look for in titles or authors.

        Returns:
            list: A list of books that match the search criteria.
        """
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        return results

    def list_books(self):
        """
        Returns a list of all books in the library.

        Returns:
            list: A list of all books.
        """
        return self.books


# Example usage:
if __name__ == "__main__":
    library = VirtualLibrary()

    # Example books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")

    # Adding books
    try:
        library.add_book(book1)
        library.add_book(book2)
        print("Books added successfully.")
    except ValueError as e:
        print(e)

    # Listing books
    print("Current books in library:", library.list_books())

    # Searching for a book
    print("Search results for '1984':", library.search_books("1984"))

    # Removing a book
    try:
        library.remove_book("9780743273565")
        print("Book removed successfully.")
    except ValueError as e:
        print(e)

    # Listing books after removal
    print("Current books in library after removal:", library.list_books())
```
