"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: "Generate a Python script to manage student admissions for a textile institute like SMA Rizvi Textile Institute, including processing fees of PKR 1250 per month."
Generated: DETERMINISTIC_0580f45d83fd4ffd
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Student:
    """Class to represent a student in the textile institute."""
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.fee_per_month = 1250
        self.total_fees_paid = 0

    def pay_fee(self, months):
        """Process fee payment for a given number of months."""
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")
        self.total_fees_paid += self.fee_per_month * months
        print(f"Fee of PKR {self.fee_per_month * months} paid for {months} month(s).")

    def get_total_fees_paid(self):
        """Return the total fees paid by the student."""
        return self.total_fees_paid

    def __str__(self):
        """Return a string representation of the student."""
        return f"Student(Name: {self.name}, Age: {self.age}, Course: {self.course}, Total Fees Paid: PKR {self.total_fees_paid})"


class AdmissionManager:
    """Class to manage student admissions and fee processing."""
    
    def __init__(self, data_file='students.json'):
        self.data_file = data_file
        self.students = self.load_students()

    def load_students(self):
        """Load students from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return []

    def save_students(self):
        """Save students to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, name, age, course):
        """Add a new student to the admission list."""
        new_student = Student(name, age, course)
        self.students.append(new_student.__dict__)
        self.save_students()
        print(f"Student {name} added successfully.")

    def process_fee_payment(self, name, months):
        """Process fee payment for a student by name."""
        for student in self.students:
            if student['name'] == name:
                student_obj = Student(student['name'], student['age'], student['course'])
                student_obj.total_fees_paid = student['total_fees_paid']
                student_obj.pay_fee(months)
                student['total_fees_paid'] = student_obj.total_fees_paid
                self.save_students()
                return
        print(f"Student {name} not found.")

    def display_students(self):
        """Display all students and their fee status."""
        for student in self.students:
            print(Student(student['name'], student['age'], student['course']).__str__())


if __name__ == "__main__":
    manager = AdmissionManager()

    # Example usage
    try:
        manager.add_student("Ali Khan", 20, "Textile Engineering")
        manager.add_student("Sara Ahmed", 19, "Fashion Design")
        manager.display_students()
        
        manager.process_fee_payment("Ali Khan", 2)
        manager.process_fee_payment("Sara Ahmed", 1)
        
        manager.display_students()
    except Exception as e:
        print(f"An error occurred: {e}")
```
