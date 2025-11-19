"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Create a library management system for a school like Deepti Convent Higher Secondary School, including features like book issuance, return, and fine management.
Generated: DETERMINISTIC_f83a60e48e4ad357
Batch ID: 20250622_210650
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
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Student:
    """Class representing a student in the library."""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.issued_books = {}

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"


class Library:
    """Class representing the library management system."""
    
    def __init__(self):
        self.books = {}
        self.students = {}
        self.fine_per_day = 1  # Fine amount per day for overdue books

    def add_book(self, book):
        """Add a book to the library."""
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book

    def register_student(self, student):
        """Register a new student in the library."""
        if student.student_id in self.students:
            raise ValueError("Student with this ID already exists.")
        self.students[student.student_id] = student

    def issue_book(self, student_id, isbn):
        """Issue a book to a student."""
        if student_id not in self.students:
            raise ValueError("Student not registered.")
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if book.is_issued:
            raise ValueError("Book is already issued.")
        
        book.is_issued = True
        self.students[student_id].issued_books[isbn] = 0  # Days issued

    def return_book(self, student_id, isbn):
        """Return a book from a student."""
        if student_id not in self.students:
            raise ValueError("Student not registered.")
        if isbn not in self.students[student_id].issued_books:
            raise ValueError("This book was not issued to the student.")
        
        book = self.books[isbn]
        days_issued = self.students[student_id].issued_books.pop(isbn)
        book.is_issued = False
        
        # Calculate fine if overdue
        if days_issued > 14:  # Assuming 14 days is the allowed period
            fine = (days_issued - 14) * self.fine_per_day
            return fine
        return 0

    def update_days_issued(self, student_id, isbn):
        """Update the number of days a book has been issued."""
        if student_id in self.students and isbn in self.students[student_id].issued_books:
            self.students[student_id].issued_books[isbn] += 1
        else:
            raise ValueError("Invalid student ID or ISBN.")


# Example usage
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"))
    library.add_book(Book("1984", "George Orwell", "9780451524935"))

    # Registering students
    library.register_student(Student("Alice", "S001"))
    library.register_student(Student("Bob", "S002"))

    # Issuing a book
    try:
        library.issue_book("S001", "9780743273565")
    except ValueError as e:
        print(e)

    # Simulating days passed
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")
    library.update_days_issued("S001", "9780743273565")

    # Returning a book and checking for fines
    try:
        fine = library.return_book("S001", "9780743273565")
        if fine > 0:
            print(f"Fine for overdue book: ${fine}")
        else:
            print("Book returned without any fine.")
    except ValueError as e:
        print(e)
```
