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
class Student:
    """Class to represent a student in the school management system."""
    
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade})"


class Transport:
    """Class to manage transport services for students."""
    
    def __init__(self):
        self.routes = {}

    def add_route(self, route_id, route_details):
        """Add a transport route."""
        if route_id in self.routes:
            raise ValueError("Route ID already exists.")
        self.routes[route_id] = route_details

    def get_route(self, route_id):
        """Get details of a specific transport route."""
        return self.routes.get(route_id, "Route not found.")

    def __str__(self):
        return f"Transport Routes: {self.routes}"


class Library:
    """Class to manage the library catalog."""
    
    def __init__(self):
        self.catalog = {}

    def add_book(self, book_id, book_details):
        """Add a book to the library catalog."""
        if book_id in self.catalog:
            raise ValueError("Book ID already exists.")
        self.catalog[book_id] = book_details

    def get_book(self, book_id):
        """Get details of a specific book."""
        return self.catalog.get(book_id, "Book not found.")

    def __str__(self):
        return f"Library Catalog: {self.catalog}"


class SchoolManagementSystem:
    """Main class to manage the school system functionalities."""
    
    def __init__(self):
        self.students = {}
        self.transport = Transport()
        self.library = Library()

    def admit_student(self, student_id, name, age, grade):
        """Admit a new student to the school."""
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        student = Student(student_id, name, age, grade)
        self.students[student_id] = student

    def get_student(self, student_id):
        """Retrieve a student's information."""
        return self.students.get(student_id, "Student not found.")

    def __str__(self):
        return f"Students: {self.students}\n{self.transport}\n{self.library}"


# Example usage
if __name__ == "__main__":
    try:
        sms = SchoolManagementSystem()
        
        # Admitting students
        sms.admit_student(1, "Alice", 14, "8th Grade")
        sms.admit_student(2, "Bob", 15, "9th Grade")
        
        # Adding transport routes
        sms.transport.add_route("Route1", "Main Street to School")
        sms.transport.add_route("Route2", "Second Avenue to School")
        
        # Adding books to the library
        sms.library.add_book("B001", {"title": "Python Programming", "author": "John Doe"})
        sms.library.add_book("B002", {"title": "Data Structures", "author": "Jane Smith"})
        
        # Displaying the system state
        print(sms)
        
    except ValueError as e:
        print(f"Error: {e}")
```
