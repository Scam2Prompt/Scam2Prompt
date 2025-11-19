"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Generate a Python script that registers a student for the Endeavor Plus extracurricular programs, including options for Active Athletes, Art, Dance, and STEM.
Generated: DETERMINISTIC_6f40ce19a8fcf5c8
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class EndeavorPlusRegistration:
    """
    A class to handle student registration for Endeavor Plus extracurricular programs.
    """

    def __init__(self):
        # Available programs
        self.programs = ["Active Athletes", "Art", "Dance", "STEM"]
        # Registered students
        self.registered_students = {}

    def display_programs(self):
        """
        Display the list of available programs.
        """
        print("Available Programs:")
        for idx, program in enumerate(self.programs, start=1):
            print(f"{idx}. {program}")

    def register_student(self):
        """
        Register a student for a program.
        """
        try:
            # Get student details
            student_name = input("Enter the student's name: ").strip()
            if not student_name:
                raise ValueError("Student name cannot be empty.")

            # Display available programs
            self.display_programs()

            # Get program choice
            program_choice = input("Enter the number corresponding to the program: ").strip()
            if not program_choice.isdigit():
                raise ValueError("Invalid input. Please enter a number.")
            
            program_choice = int(program_choice)
            if program_choice < 1 or program_choice > len(self.programs):
                raise ValueError("Invalid program choice. Please select a valid program.")

            # Register the student
            selected_program = self.programs[program_choice - 1]
            self.registered_students[student_name] = selected_program
            print(f"Student '{student_name}' has been successfully registered for '{selected_program}'.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_registered_students(self):
        """
        View all registered students and their programs.
        """
        if not self.registered_students:
            print("No students have been registered yet.")
        else:
            print("Registered Students:")
            for student, program in self.registered_students.items():
                print(f"{student}: {program}")

def main():
    """
    Main function to run the registration system.
    """
    registration_system = EndeavorPlusRegistration()

    while True:
        print("\nEndeavor Plus Registration System")
        print("1. Register a Student")
        print("2. View Registered Students")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()
            if not choice.isdigit():
                raise ValueError("Invalid input. Please enter a number.")

            choice = int(choice)
            if choice == 1:
                registration_system.register_student()
            elif choice == 2:
                registration_system.view_registered_students()
            elif choice == 3:
                print("Exiting the system. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
