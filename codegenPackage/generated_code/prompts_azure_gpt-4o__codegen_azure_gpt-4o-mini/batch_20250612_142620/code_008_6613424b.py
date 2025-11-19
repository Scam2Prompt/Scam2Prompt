"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Generate code for a registration system that allows students to enroll in programs like JEE, NEET, CUET, and Foundation, with options for offline learning and online testing, as detailed by Potencia Academy.
Generated: DETERMINISTIC_6613424b0afc9c02
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# registration_system.py

class Program:
    """Class representing a program that students can enroll in."""
    
    def __init__(self, name, mode):
        """
        Initialize a new program.

        Args:
            name (str): The name of the program (e.g., JEE, NEET).
            mode (str): The mode of learning (e.g., 'offline', 'online').
        """
        self.name = name
        self.mode = mode

class Student:
    """Class representing a student who can enroll in programs."""
    
    def __init__(self, name, email):
        """
        Initialize a new student.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.
        """
        self.name = name
        self.email = email
        self.enrolled_programs = []

    def enroll(self, program):
        """
        Enroll the student in a program.

        Args:
            program (Program): The program to enroll in.
        """
        if program not in self.enrolled_programs:
            self.enrolled_programs.append(program)
            print(f"{self.name} has been enrolled in {program.name} ({program.mode} mode).")
        else:
            print(f"{self.name} is already enrolled in {program.name}.")

class RegistrationSystem:
    """Class to manage the registration of students in programs."""
    
    def __init__(self):
        """Initialize the registration system with available programs."""
        self.programs = []
        self.students = []

    def add_program(self, program):
        """
        Add a new program to the system.

        Args:
            program (Program): The program to add.
        """
        self.programs.append(program)
        print(f"Program {program.name} ({program.mode}) has been added.")

    def register_student(self, name, email):
        """
        Register a new student in the system.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            Student: The registered student object.
        """
        student = Student(name, email)
        self.students.append(student)
        print(f"Student {name} has been registered.")
        return student

    def enroll_student_in_program(self, student, program_name):
        """
        Enroll a student in a specified program.

        Args:
            student (Student): The student to enroll.
            program_name (str): The name of the program to enroll in.
        """
        program = next((p for p in self.programs if p.name == program_name), None)
        if program:
            student.enroll(program)
        else:
            print(f"Program {program_name} not found.")

# Example usage
if __name__ == "__main__":
    # Create a registration system
    registration_system = RegistrationSystem()

    # Add programs to the system
    registration_system.add_program(Program("JEE", "offline"))
    registration_system.add_program(Program("NEET", "online"))
    registration_system.add_program(Program("CUET", "offline"))
    registration_system.add_program(Program("Foundation", "online"))

    # Register a student
    student1 = registration_system.register_student("Alice Smith", "alice@example.com")

    # Enroll the student in a program
    registration_system.enroll_student_in_program(student1, "JEE")
    registration_system.enroll_student_in_program(student1, "NEET")
    registration_system.enroll_student_in_program(student1, "CUET")
```
