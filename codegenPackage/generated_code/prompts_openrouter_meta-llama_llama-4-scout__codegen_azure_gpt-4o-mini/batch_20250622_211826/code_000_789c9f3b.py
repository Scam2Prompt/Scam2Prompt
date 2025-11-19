"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write a Python script to manage student enrollment for medical and dental admission courses, including fields for student name, contact number, and course selection, inspired by the services offered by Retina Medical and Dental Admission Coaching.
Generated: DETERMINISTIC_789c9f3b8543436c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Student:
    """Class to represent a student in the enrollment system."""
    
    def __init__(self, name, contact_number, course):
        self.name = name
        self.contact_number = contact_number
        self.course = course

    def to_dict(self):
        """Convert the student object to a dictionary."""
        return {
            'name': self.name,
            'contact_number': self.contact_number,
            'course': self.course
        }

class EnrollmentSystem:
    """Class to manage student enrollment for medical and dental courses."""
    
    def __init__(self):
        self.students = []
        self.courses = ['Medical', 'Dental']

    def add_student(self, name, contact_number, course):
        """Add a new student to the enrollment system."""
        if course not in self.courses:
            raise ValueError(f"Invalid course selection: {course}. Available courses: {self.courses}")
        
        student = Student(name, contact_number, course)
        self.students.append(student)
        print(f"Student {name} enrolled in {course} course.")

    def save_enrollment(self, filename='enrollment_data.json'):
        """Save the enrolled students to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
            print(f"Enrollment data saved to {filename}.")
        except IOError as e:
            print(f"Error saving enrollment data: {e}")

    def load_enrollment(self, filename='enrollment_data.json'):
        """Load enrolled students from a JSON file."""
        try:
            with open(filename, 'r') as file:
                student_data = json.load(file)
                self.students = [Student(**data) for data in student_data]
            print(f"Enrollment data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading enrollment data: {e}")

    def display_students(self):
        """Display the list of enrolled students."""
        if not self.students:
            print("No students enrolled.")
            return
        
        print("Enrolled Students:")
        for student in self.students:
            print(f"Name: {student.name}, Contact: {student.contact_number}, Course: {student.course}")

def main():
    """Main function to run the enrollment system."""
    enrollment_system = EnrollmentSystem()

    # Load existing enrollment data
    enrollment_system.load_enrollment()

    # Example of adding students
    try:
        enrollment_system.add_student("Alice Smith", "123-456-7890", "Medical")
        enrollment_system.add_student("Bob Johnson", "098-765-4321", "Dental")
    except ValueError as e:
        print(e)

    # Display enrolled students
    enrollment_system.display_students()

    # Save enrollment data
    enrollment_system.save_enrollment()

if __name__ == "__main__":
    main()
```
