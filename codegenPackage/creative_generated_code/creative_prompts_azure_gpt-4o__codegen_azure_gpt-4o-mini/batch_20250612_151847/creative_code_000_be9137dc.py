"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Write a Python script to automate the registration process for new students in Sekolah Quran Indonesia's programs, including fields for name, age, program selection, and contact information.
Generated: DETERMINISTIC_be9137dc8b744faa
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Student:
    """Class to represent a student."""
    
    def __init__(self, name, age, program, contact_info):
        self.name = name
        self.age = age
        self.program = program
        self.contact_info = contact_info

    def to_dict(self):
        """Convert student object to dictionary for easy JSON serialization."""
        return {
            "name": self.name,
            "age": self.age,
            "program": self.program,
            "contact_info": self.contact_info
        }

class RegistrationSystem:
    """Class to handle student registration."""

    def __init__(self, filename='students.json'):
        self.filename = filename

    def register_student(self, student):
        """Register a new student by saving their information to a file."""
        try:
            # Load existing students
            students = self.load_students()
            # Add the new student
            students.append(student.to_dict())
            # Save the updated list back to the file
            self.save_students(students)
            print(f"Successfully registered: {student.name}")
        except Exception as e:
            print(f"An error occurred during registration: {e}")

    def load_students(self):
        """Load students from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if file not found or is empty

    def save_students(self, students):
        """Save the list of students to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(students, file, indent=4)

def main():
    """Main function to run the student registration process."""
    print("Welcome to the Sekolah Quran Indonesia Student Registration")
    
    # Gather student information
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    program = input("Enter program selection: ")
    contact_info = input("Enter contact information: ")
    
    try:
        # Validate age to be an integer
        age = int(age)
    except ValueError:
        print("Invalid age. Please enter a number.")
        return
    
    # Create a new student object
    new_student = Student(name, age, program, contact_info)
    
    # Create a registration system instance and register the student
    reg_system = RegistrationSystem()
    reg_system.register_student(new_student)

if __name__ == "__main__":
    main()
```
