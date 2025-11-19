"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Generate a Python script that registers a student for the Endeavor Plus extracurricular programs, including options for Active Athletes, Art, Dance, and STEM.
Generated: DETERMINISTIC_6f40ce19a8fcf5c8
Batch ID: 20250612_162325
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
    def __init__(self, name, age, email):
        """Initialize a new student with name, age, and email."""
        self.name = name
        self.age = age
        self.email = email
        self.programs = []

    def register_program(self, program):
        """Register the student for a specified program."""
        if program not in self.programs:
            self.programs.append(program)
            print(f"{self.name} successfully registered for {program}.")
        else:
            print(f"{self.name} is already registered for {program}.")

    def get_registered_programs(self):
        """Return a list of registered programs."""
        return self.programs


class ProgramRegistration:
    def __init__(self):
        """Initialize the program registration system."""
        self.registered_students = []

    def add_student(self, student):
        """Add a new student to the registration system."""
        self.registered_students.append(student)
        print(f"Student {student.name} added to the system.")

    def register_student_for_program(self, student_email, program):
        """Register a student for a program based on their email."""
        for student in self.registered_students:
            if student.email == student_email:
                student.register_program(program)
                return
        print(f"No student found with email: {student_email}")

    def save_registration_data(self, filename='registrations.json'):
        """Save registered students' data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([vars(student) for student in self.registered_students], file, indent=2)
            print(f"Registration data saved to {filename}.")
        except IOError as e:
            print(f"Error saving registration data: {e}")


def main():
    """Main function to run the program."""
    registration_system = ProgramRegistration()

    # Sample students
    student1 = Student("Alice Smith", 15, "alice.smith@example.com")
    student2 = Student("Bob Johnson", 16, "bob.johnson@example.com")

    # Add students to the registration system
    registration_system.add_student(student1)
    registration_system.add_student(student2)

    # Register students for programs
    registration_system.register_student_for_program("alice.smith@example.com", "Active Athletes")
    registration_system.register_student_for_program("bob.johnson@example.com", "Art")
    registration_system.register_student_for_program("alice.smith@example.com", "STEM")

    # Save registration data
    registration_system.save_registration_data()


if __name__ == "__main__":
    main()
```
