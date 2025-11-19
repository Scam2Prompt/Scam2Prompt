"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Generate a code snippet for a school management system that includes features like student admission, transport management, and library cataloging, inspired by the offerings of Param Gyan Niketan.
Generated: DETERMINISTIC_bb092fb3398c2f8b
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py

class Student:
    """Represents a student in the school management system."""

    def __init__(self, student_id, name, grade, admission_date):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Student's name.
            grade (int): Student's current grade.
            admission_date (str): Date of admission (YYYY-MM-DD).
        """
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.admission_date = admission_date

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Admission Date: {self.admission_date}"


class Transport:
    """Represents a transport vehicle in the school management system."""

    def __init__(self, vehicle_id, vehicle_type, capacity):
        """
        Initializes a Transport object.

        Args:
            vehicle_id (int): Unique identifier for the vehicle.
            vehicle_type (str): Type of vehicle (e.g., bus, van).
            capacity (int): Seating capacity of the vehicle.
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        """
        Adds a student to the vehicle.

        Args:
            student (Student): Student to be added.

        Raises:
            ValueError: If the vehicle is full.
        """
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            raise ValueError("Vehicle is full")

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}, Type: {self.vehicle_type}, Capacity: {self.capacity}, Students: {len(self.students)}"


class Book:
    """Represents a book in the library catalog."""

    def __init__(self, book_id, title, author, publication_date):
        """
        Initializes a Book object.

        Args:
            book_id (int): Unique identifier for the book.
            title (str): Book title.
            author (str): Book author.
            publication_date (str): Date of publication (YYYY-MM-DD).
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.borrowed = False

    def borrow(self):
        """
        Marks the book as borrowed.

        Raises:
            ValueError: If the book is already borrowed.
        """
        if not self.borrowed:
            self.borrowed = True
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self):
        """
        Marks the book as returned.

        Raises:
            ValueError: If the book is not borrowed.
        """
        if self.borrowed:
            self.borrowed = False
        else:
            raise ValueError("Book is not borrowed")

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_date}, Borrowed: {self.borrowed}"


class SchoolManagementSystem:
    """Represents the school management system."""

    def __init__(self):
        self.students = []
        self.transports = []
        self.books = []

    def admit_student(self, student):
        """
        Admits a student to the school.

        Args:
            student (Student): Student to be admitted.
        """
        self.students.append(student)

    def add_transport(self, transport):
        """
        Adds a transport vehicle to the school.

        Args:
            transport (Transport): Transport vehicle to be added.
        """
        self.transports.append(transport)

    def add_book(self, book):
        """
        Adds a book to the library catalog.

        Args:
            book (Book): Book to be added.
        """
        self.books.append(book)

    def display_students(self):
        """Displays all students in the school."""
        for student in self.students:
            print(student)

    def display_transports(self):
        """Displays all transport vehicles in the school."""
        for transport in self.transports:
            print(transport)
            for student in transport.students:
                print(f"  - {student.name}")

    def display_books(self):
        """Displays all books in the library catalog."""
        for book in self.books:
            print(book)


def main():
    school = SchoolManagementSystem()

    while True:
        print("\nSchool Management System")
        print("1. Admit Student")
        print("2. Add Transport")
        print("3. Add Book")
        print("4. Display Students")
        print("5. Display Transports")
        print("6. Display Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            admission_date = input("Enter admission date (YYYY-MM-DD): ")
            student = Student(student_id, name, grade, admission_date)
            school.admit_student(student)
        elif choice == "2":
            vehicle_id = int(input("Enter vehicle ID: "))
            vehicle_type = input("Enter vehicle type: ")
            capacity = int(input("Enter vehicle capacity: "))
            transport = Transport(vehicle_id, vehicle_type, capacity)
            school.add_transport(transport)

            num_students = int(input("Enter number of students to add: "))
            for _ in range(num_students):
                student_id = int(input("Enter student ID: "))
                student_name = input("Enter student name: ")
                student_grade = int(input("Enter student grade: "))
                student_admission_date = input("Enter student admission date (YYYY-MM-DD): ")
                student = Student(student_id, student_name, student_grade, student_admission_date)
                try:
                    transport.add_student(student)
                except ValueError as e:
                    print(e)
        elif choice == "3":
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(book_id, title, author, publication_date)
            school.add_book(book)
        elif choice == "4":
            school.display_students()
        elif choice == "5":
            school.display_transports()
        elif choice == "6":
            school.display_books()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
