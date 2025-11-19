"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Generate a code snippet for a school management system that includes features like student admission, transport management, and library cataloging, inspired by the offerings of Param Gyan Niketan.
Generated: DETERMINISTIC_bb092fb3398c2f8b
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Student:
    """A class to represent a student."""
    
    def __init__(self, student_id, name, age, class_enrolled):
        """Initialize a new student with basic details."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.class_enrolled = class_enrolled

    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Class: {self.class_enrolled})"


class Transport:
    """A class to manage transport services for students."""
    
    def __init__(self):
        """Initialize the transport management system with an empty list of buses."""
        self.buses = []

    def add_bus(self, bus_number, capacity):
        """Add a new bus to the transport system."""
        self.buses.append({'bus_number': bus_number, 'capacity': capacity, 'students': []})

    def assign_student_to_bus(self, student, bus_number):
        """Assign a student to a bus if there is available capacity."""
        for bus in self.buses:
            if bus['bus_number'] == bus_number:
                if len(bus['students']) < bus['capacity']:
                    bus['students'].append(student)
                    print(f"{student.name} has been assigned to bus {bus_number}.")
                else:
                    raise Exception(f"Bus {bus_number} is at full capacity.")
                return
        raise Exception(f"Bus {bus_number} not found.")


class Library:
    """A class to manage the library catalog."""
    
    def __init__(self):
        """Initialize the library with an empty catalog."""
        self.catalog = {}

    def add_book(self, title, author, isbn):
        """Add a new book to the library catalog."""
        self.catalog[isbn] = {'title': title, 'author': author, 'available': True}

    def checkout_book(self, isbn):
        """Checkout a book from the library if it's available."""
        if isbn in self.catalog and self.catalog[isbn]['available']:
            self.catalog[isbn]['available'] = False
            print(f"You have checked out '{self.catalog[isbn]['title']}'.")
        else:
            raise Exception(f"The book with ISBN {isbn} is either not found or not available.")

    def return_book(self, isbn):
        """Return a book to the library."""
        if isbn in self.catalog:
            self.catalog[isbn]['available'] = True
            print(f"You have returned '{self.catalog[isbn]['title']}'.")
        else:
            raise Exception(f"The book with ISBN {isbn} is not found in the catalog.")


class SchoolManagementSystem:
    """A class to manage the overall school management system."""
    
    def __init__(self):
        """Initialize the school management system with collections."""
        self.students = []
        self.transport = Transport()
        self.library = Library()

    def admit_student(self, student_id, name, age, class_enrolled):
        """Admit a new student to the school."""
        new_student = Student(student_id, name, age, class_enrolled)
        self.students.append(new_student)
        print(f"{name} has been admitted to the school.")

    def manage_transport(self, bus_number, capacity):
        """Manage the transport system by adding a bus."""
        self.transport.add_bus(bus_number, capacity)

    def manage_library(self, title, author, isbn):
        """Manage the library catalog by adding a book."""
        self.library.add_book(title, author, isbn)


# Example usage:
if __name__ == "__main__":
    try:
        sms = SchoolManagementSystem()
        
        # Admitting students
        sms.admit_student(1, "Alice", 14, "8th Grade")
        sms.admit_student(2, "Bob", 15, "9th Grade")
        
        # Managing transport
        sms.manage_transport("Bus A", 2)
        sms.transport.assign_student_to_bus(sms.students[0], "Bus A")
        sms.transport.assign_student_to_bus(sms.students[1], "Bus A")  # This will raise an exception
        
        # Managing library
        sms.manage_library("Python Programming", "John Doe", "123456789")
        sms.library.checkout_book("123456789")
        sms.library.return_book("123456789")
        
    except Exception as e:
        print(f"Error: {e}")
```
