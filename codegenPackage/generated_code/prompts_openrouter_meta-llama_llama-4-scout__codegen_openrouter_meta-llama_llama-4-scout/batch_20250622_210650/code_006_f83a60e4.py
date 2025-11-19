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
# library_management_system.py

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author, publication_year, isbn):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The year the book was published.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.is_issued = False

    def issue(self):
        """Marks the book as issued."""
        if not self.is_issued:
            self.is_issued = True
            return f"'{self.title}' has been issued."
        else:
            return f"'{self.title}' is already issued."

    def return_book(self):
        """Marks the book as returned."""
        if self.is_issued:
            self.is_issued = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' is not issued."


class Student:
    """Represents a student in the school."""
    
    def __init__(self, student_id, name):
        """
        Initializes a Student object.

        Args:
            student_id (str): The ID of the student.
            name (str): The name of the student.
        """
        self.student_id = student_id
        self.name = name
        self.issued_books = []

    def issue_book(self, book):
        """Issues a book to the student."""
        if book.is_issued:
            return f"'{book.title}' is already issued to another student."
        else:
            result = book.issue()
            if "has been issued" in result:
                self.issued_books.append(book)
            return result

    def return_book(self, book):
        """Returns a book from the student."""
        if book in self.issued_books:
            result = book.return_book()
            self.issued_books.remove(book)
            return result
        else:
            return f"'{book.title}' is not issued to {self.name}."


class Library:
    """Represents the library management system."""
    
    def __init__(self):
        """Initializes the library management system."""
        self.books = {}
        self.students = {}

    def add_book(self, book):
        """Adds a book to the library."""
        self.books[book.isbn] = book
        return f"'{book.title}' has been added to the library."

    def remove_book(self, isbn):
        """Removes a book from the library."""
        if isbn in self.books:
            del self.books[isbn]
            return f"The book with ISBN {isbn} has been removed."
        else:
            return f"No book found with ISBN {isbn}."

    def add_student(self, student):
        """Adds a student to the library."""
        self.students[student.student_id] = student
        return f"{student.name} has been added to the library."

    def remove_student(self, student_id):
        """Removes a student from the library."""
        if student_id in self.students:
            del self.students[student_id]
            return f"The student with ID {student_id} has been removed."
        else:
            return f"No student found with ID {student_id}."

    def issue_book_to_student(self, student_id, isbn):
        """Issues a book to a student."""
        if student_id in self.students and isbn in self.books:
            student = self.students[student_id]
            book = self.books[isbn]
            return student.issue_book(book)
        else:
            return "Invalid student or book."

    def return_book_from_student(self, student_id, isbn):
        """Returns a book from a student."""
        if student_id in self.students and isbn in self.books:
            student = self.students[student_id]
            book = self.books[isbn]
            return student.return_book(book)
        else:
            return "Invalid student or book."

    def calculate_fine(self, student_id):
        """Calculates the fine for a student."""
        if student_id in self.students:
            student = self.students[student_id]
            fine = 0
            for book in student.issued_books:
                # Assuming a fine of 1 rupee per day
                fine += 1
            return fine
        else:
            return "Invalid student."


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Remove book")
        print("3. Add student")
        print("4. Remove student")
        print("5. Issue book to student")
        print("6. Return book from student")
        print("7. Calculate fine")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = int(input("Enter book publication year: "))
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, publication_year, isbn)
            print(library.add_book(book))
        elif choice == "2":
            isbn = input("Enter book ISBN: ")
            print(library.remove_book(isbn))
        elif choice == "3":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            student = Student(student_id, name)
            print(library.add_student(student))
        elif choice == "4":
            student_id = input("Enter student ID: ")
            print(library.remove_student(student_id))
        elif choice == "5":
            student_id = input("Enter student ID: ")
            isbn = input("Enter book ISBN: ")
            print(library.issue_book_to_student(student_id, isbn))
        elif choice == "6":
            student_id = input("Enter student ID: ")
            isbn = input("Enter book ISBN: ")
            print(library.return_book_from_student(student_id, isbn))
        elif choice == "7":
            student_id = input("Enter student ID: ")
            print(library.calculate_fine(student_id))
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
