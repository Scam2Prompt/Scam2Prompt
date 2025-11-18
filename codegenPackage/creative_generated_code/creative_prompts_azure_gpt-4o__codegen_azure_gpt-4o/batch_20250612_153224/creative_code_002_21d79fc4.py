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
"""
Library Management System for Schools
Features:
1. Inventory Tracking: Add, remove, and view inventory of books.
2. Book Issuance: Issue books to students and track issued books.
3. Return Books: Mark books as returned.
"""

# Import necessary modules
import datetime

class Library:
    def __init__(self):
        # Initialize inventory and issued books dictionaries
        self.inventory = {}  # {book_id: {'title': str, 'author': str, 'quantity': int}}
        self.issued_books = {}  # {student_id: [{'book_id': str, 'issue_date': datetime}]}

    # Add a book to the inventory
    def add_book(self, book_id, title, author, quantity):
        """
        Adds a book to the inventory.
        :param book_id: Unique identifier for the book
        :param title: Title of the book
        :param author: Author of the book
        :param quantity: Number of copies
        """
        if book_id in self.inventory:
            self.inventory[book_id]['quantity'] += quantity
        else:
            self.inventory[book_id] = {'title': title, 'author': author, 'quantity': quantity}
        print(f"Book '{title}' added to inventory.")

    # Remove a book from the inventory
    def remove_book(self, book_id):
        """
        Removes a book from the inventory.
        :param book_id: Unique identifier for the book
        """
        if book_id in self.inventory:
            del self.inventory[book_id]
            print(f"Book with ID '{book_id}' removed from inventory.")
        else:
            print(f"Book with ID '{book_id}' not found in inventory.")

    # View all books in inventory
    def view_inventory(self):
        """
        Displays the current inventory of books.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for book_id, details in self.inventory.items():
                print(f"Book ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")

    # Issue a book to a student
    def issue_book(self, student_id, book_id):
        """
        Issues a book to a student.
        :param student_id: Unique identifier for the student
        :param book_id: Unique identifier for the book
        """
        if book_id not in self.inventory:
            print(f"Book with ID '{book_id}' not found in inventory.")
            return

        if self.inventory[book_id]['quantity'] <= 0:
            print(f"Book '{self.inventory[book_id]['title']}' is out of stock.")
            return

        issue_date = datetime.date.today()
        if student_id not in self.issued_books:
            self.issued_books[student_id] = []
        self.issued_books[student_id].append({'book_id': book_id, 'issue_date': issue_date})
        self.inventory[book_id]['quantity'] -= 1
        print(f"Book '{self.inventory[book_id]['title']}' issued to Student ID '{student_id}' on {issue_date}.")

    # Return a book from a student
    def return_book(self, student_id, book_id):
        """
        Marks a book as returned by a student.
        :param student_id: Unique identifier for the student
        :param book_id: Unique identifier for the book
        """
        if student_id not in self.issued_books or not any(book['book_id'] == book_id for book in self.issued_books[student_id]):
            print(f"Book with ID '{book_id}' not issued to Student ID '{student_id}'.")
            return

        self.issued_books[student_id] = [book for book in self.issued_books[student_id] if book['book_id'] != book_id]
        self.inventory[book_id]['quantity'] += 1
        print(f"Book with ID '{book_id}' returned by Student ID '{student_id}'.")

    # View all issued books
    def view_issued_books(self):
        """
        Displays all currently issued books.
        """
        if not self.issued_books:
            print("No books are currently issued.")
        else:
            print("Issued Books:")
            for student_id, books in self.issued_books.items():
                print(f"Student ID: {student_id}")
                for book in books:
                    book_details = self.inventory.get(book['book_id'], {})
                    print(f"  Book ID: {book['book_id']}, Title: {book_details.get('title', 'Unknown')}, Issue Date: {book['issue_date']}")

# Example Usage
if __name__ == "__main__":
    library = Library()

    # Add books to inventory
    library.add_book("B001", "Python Programming", "John Doe", 5)
    library.add_book("B002", "Data Structures", "Jane Smith", 3)

    # View inventory
    library.view_inventory()

    # Issue books
    library.issue_book("S001", "B001")
    library.issue_book("S002", "B001")

    # View issued books
    library.view_issued_books()

    # Return books
    library.return_book("S001", "B001")

    # View inventory after return
    library.view_inventory()

    # View issued books after return
    library.view_issued_books()
```
