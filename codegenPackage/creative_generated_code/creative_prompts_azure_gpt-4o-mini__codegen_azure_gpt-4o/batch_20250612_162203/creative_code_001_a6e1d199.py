"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: How can I implement a library management system for an educational institution that provides resources for admission exam preparation, similar to the "Biblioteca de estudio en casa" mentioned on Educar Comitán?
Generated: DETERMINISTIC_a6e1d199418e6da6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Library Management System for Educational Institution
# Language: Python
# This system allows managing books, users, and borrowed resources.

import datetime

class Book:
    """
    Represents a book/resource in the library.
    """
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies  # Number of available copies

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Copies: {self.copies}"


class User:
    """
    Represents a user of the library system (e.g., student or staff).
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  # List of borrowed books

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"


class Library:
    """
    Represents the library management system.
    """
    def __init__(self):
        self.books = {}  # Key: ISBN, Value: Book object
        self.users = {}  # Key: User ID, Value: User object

    # Add a new book to the library
    def add_book(self, book):
        if book.isbn in self.books:
            self.books[book.isbn].copies += book.copies  # Increase the number of copies
        else:
            self.books[book.isbn] = book

    # Register a new user
    def add_user(self, user):
        if user.user_id not in self.users:
            self.users[user.user_id] = user
        else:
            print(f"User {user.user_id} already exists.")

    # Borrow a book
    def borrow_book(self, user_id, isbn):
        if user_id not in self.users:
            print("Error: User not found.")
            return
        if isbn not in self.books:
            print("Error: Book not found.")
            return
        book = self.books[isbn]
        user = self.users[user_id]

        if book.copies > 0:
            book.copies -= 1
            user.borrowed_books.append(book)
            print(f"{user.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    # Return a borrowed book
    def return_book(self, user_id, isbn):
        if user_id not in self.users:
            print("Error: User not found.")
            return
        if isbn not in self.books:
            print("Error: Book not found.")
            return
        user = self.users[user_id]
        book = self.books[isbn]

        if book in user.borrowed_books:
            user.borrowed_books.remove(book)
            book.copies += 1
            print(f"{user.name} returned '{book.title}'.")
        else:
            print(f"Error: {user.name} did not borrow '{book.title}'.")

    # Display all books
    def display_books(self):
        print("Books in the Library:")
        for book in self.books.values():
            print(book)

    # Display all users
    def display_users(self):
        print("Registered Users:")
        for user in self.users.values():
            print(user)


# Example Usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book(Book("Introduction to Algorithms", "Thomas H. Cormen", "9780262033848", 3))
    library.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884", 2))

    # Registering users
    library.add_user(User(1, "Alice"))
    library.add_user(User(2, "Bob"))

    # Display books and users
    library.display_books()
    library.display_users()

    # Borrow and return books
    library.borrow_book(1, "9780262033848")  # Alice borrows "Introduction to Algorithms"
    library.borrow_book(2, "9780132350884")  # Bob borrows "Clean Code"
    library.return_book(1, "9780262033848")  # Alice returns "Introduction to Algorithms"

    # Display books after transactions
    library.display_books()
```
