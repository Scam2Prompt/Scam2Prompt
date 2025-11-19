"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Write a code for a school management system that includes features like online registration, transfer certificate, and fee payment.
Generated: DETERMINISTIC_7ead644059abc0c6
Batch ID: 20250622_210650
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
    """Class to represent a student in the school management system."""
    
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.is_registered = False
        self.fee_paid = False

    def register(self):
        """Register the student for the school."""
        if not self.is_registered:
            self.is_registered = True
            return f"Student {self.name} registered successfully."
        else:
            raise ValueError("Student is already registered.")

    def issue_transfer_certificate(self):
        """Issue a transfer certificate for the student."""
        if self.is_registered:
            return f"Transfer certificate issued for {self.name}."
        else:
            raise ValueError("Student must be registered to issue a transfer certificate.")

    def pay_fee(self):
        """Process fee payment for the student."""
        if self.is_registered:
            self.fee_paid = True
            return f"Fee payment successful for {self.name}."
        else:
            raise ValueError("Student must be registered to pay fees.")


class SchoolManagementSystem:
    """Class to manage the school operations."""
    
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name, age, grade)
        return f"Student {name} added successfully."

    def get_student(self, student_id):
        """Retrieve a student by their ID."""
        student = self.students.get(student_id)
        if student:
            return student
        else:
            raise ValueError("Student not found.")

    def register_student(self, student_id):
        """Register a student by their ID."""
        student = self.get_student(student_id)
        return student.register()

    def issue_transfer_certificate(self, student_id):
        """Issue a transfer certificate for a student by their ID."""
        student = self.get_student(student_id)
        return student.issue_transfer_certificate()

    def pay_student_fee(self, student_id):
        """Process fee payment for a student by their ID."""
        student = self.get_student(student_id)
        return student.pay_fee()


# Example usage
if __name__ == "__main__":
    sms = SchoolManagementSystem()
    
    try:
        # Adding students
        print(sms.add_student(1, "Alice", 14, "8th Grade"))
        print(sms.add_student(2, "Bob", 15, "9th Grade"))

        # Registering students
        print(sms.register_student(1))
        print(sms.register_student(2))

        # Paying fees
        print(sms.pay_student_fee(1))
        print(sms.pay_student_fee(2))

        # Issuing transfer certificates
        print(sms.issue_transfer_certificate(1))
        print(sms.issue_transfer_certificate(2))

    except ValueError as e:
        print(f"Error: {e}")
```
