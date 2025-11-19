"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Write a Python script to automate the registration process for new students in Sekolah Quran Indonesia's programs, including fields for name, age, program selection, and contact information.
Generated: DETERMINISTIC_be9137dc8b744faa
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_registration.py

class Student:
    """Represents a student with their details."""

    def __init__(self, name, age, program, phone_number, email):
        """
        Initializes a Student object.

        Args:
            name (str): Student's name.
            age (int): Student's age.
            program (str): Student's program selection.
            phone_number (str): Student's phone number.
            email (str): Student's email address.
        """
        self.name = name
        self.age = age
        self.program = program
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nProgram: {self.program}\nPhone Number: {self.phone_number}\nEmail: {self.email}"


class StudentRegistry:
    """Manages student registrations."""

    def __init__(self):
        self.students = []
        self.programs = ["Tahfidz", "Tafsir", "Aqidah", "Fikih"]

    def display_programs(self):
        """Displays available programs."""
        print("Available Programs:")
        for i, program in enumerate(self.programs, start=1):
            print(f"{i}. {program}")

    def register_student(self):
        """Registers a new student."""
        name = input("Enter student's name: ")
        while True:
            try:
                age = int(input("Enter student's age: "))
                if age <= 0:
                    print("Age must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid age. Please enter a positive integer.")

        self.display_programs()
        while True:
            try:
                program_choice = int(input("Enter the number of the program: "))
                if 1 <= program_choice <= len(self.programs):
                    program = self.programs[program_choice - 1]
                    break
                else:
                    print("Invalid program choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        phone_number = input("Enter student's phone number: ")
        email = input("Enter student's email address: ")

        student = Student(name, age, program, phone_number, email)
        self.students.append(student)
        print("\nStudent registered successfully!")
        print(student)

    def display_students(self):
        """Displays all registered students."""
        if not self.students:
            print("No students registered yet.")
        else:
            for i, student in enumerate(self.students, start=1):
                print(f"\nStudent {i}:")
                print(student)


def main():
    registry = StudentRegistry()

    while True:
        print("\nSekolah Quran Indonesia Student Registration")
        print("1. Register a new student")
        print("2. Display all registered students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                registry.register_student()
            elif choice == 2:
                registry.display_students()
            elif choice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
```
