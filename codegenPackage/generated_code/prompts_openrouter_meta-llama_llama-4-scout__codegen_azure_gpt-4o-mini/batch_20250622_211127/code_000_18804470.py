"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Generate a Python script to manage student enrollment for a JEE preparatory course like those offered at Potencia Academy."
Generated: DETERMINISTIC_188044703212532d
Batch ID: 20250622_211127
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
    """Class to represent a student in the enrollment system."""
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """Convert the student object to a dictionary."""
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

class EnrollmentManager:
    """Class to manage student enrollments for the JEE preparatory course."""
    
    def __init__(self, data_file='enrollment_data.json'):
        self.data_file = data_file
        self.students = self.load_enrollment_data()

    def load_enrollment_data(self):
        """Load enrollment data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return [Student(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading data: {e}")
                    return []
        return []

    def save_enrollment_data(self):
        """Save the current enrollment data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def enroll_student(self, name, email, phone):
        """Enroll a new student in the course."""
        if self.is_email_registered(email):
            print(f"Error: Email {email} is already registered.")
            return
        
        new_student = Student(name, email, phone)
        self.students.append(new_student)
        self.save_enrollment_data()
        print(f"Successfully enrolled {name}.")

    def is_email_registered(self, email):
        """Check if the email is already registered."""
        return any(student.email == email for student in self.students)

    def list_students(self):
        """List all enrolled students."""
        if not self.students:
            print("No students enrolled.")
            return
        
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student.name} ({student.email}, {student.phone})")

def main():
    """Main function to run the enrollment management system."""
    manager = EnrollmentManager()

    while True:
        print("\n--- JEE Preparatory Course Enrollment ---")
        print("1. Enroll Student")
        print("2. List Students")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            email = input("Enter student's email: ")
            phone = input("Enter student's phone number: ")
            manager.enroll_student(name, email, phone)
        elif choice == '2':
            manager.list_students()
        elif choice == '3':
            print("Exiting the enrollment system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
