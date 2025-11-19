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

from enum import Enum
from typing import Dict, List

class ProgramType(str, Enum):
    """Enum for program types"""
    JEE = "JEE"
    NEET = "NEET"
    CUET = "CUET"
    FOUNDATION = "Foundation"

class LearningMode(str, Enum):
    """Enum for learning modes"""
    OFFLINE = "Offline"
    ONLINE = "Online"

class Program:
    """Class representing a program"""
    def __init__(self, name: ProgramType, learning_mode: LearningMode):
        self.name = name
        self.learning_mode = learning_mode

class Student:
    """Class representing a student"""
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.programs = []

    def enroll_program(self, program: Program):
        """Enroll a student in a program"""
        self.programs.append(program)

class RegistrationSystem:
    """Class representing a registration system"""
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.programs: Dict[ProgramType, List[LearningMode]] = {
            ProgramType.JEE: [LearningMode.OFFLINE, LearningMode.ONLINE],
            ProgramType.NEET: [LearningMode.OFFLINE, LearningMode.ONLINE],
            ProgramType.CUET: [LearningMode.OFFLINE, LearningMode.ONLINE],
            ProgramType.FOUNDATION: [LearningMode.OFFLINE]
        }

    def register_student(self, name: str, email: str, phone: str):
        """Register a new student"""
        if email in self.students:
            raise ValueError("Student already exists")
        self.students[email] = Student(name, email, phone)

    def enroll_student_in_program(self, email: str, program_name: ProgramType, learning_mode: LearningMode):
        """Enroll a student in a program"""
        if email not in self.students:
            raise ValueError("Student not found")
        if program_name not in self.programs:
            raise ValueError("Program not available")
        if learning_mode not in self.programs[program_name]:
            raise ValueError("Learning mode not available for this program")

        student = self.students[email]
        program = Program(program_name, learning_mode)
        student.enroll_program(program)

    def get_student_info(self, email: str):
        """Get student information"""
        if email not in self.students:
            raise ValueError("Student not found")
        return self.students[email]

def main():
    registration_system = RegistrationSystem()

    while True:
        print("1. Register Student")
        print("2. Enroll Student in Program")
        print("3. Get Student Info")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            try:
                registration_system.register_student(name, email, phone)
                print("Student registered successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            email = input("Enter email: ")
            print("Available programs:")
            for i, program in enumerate(registration_system.programs.keys()):
                print(f"{i+1}. {program}")
            program_choice = int(input("Enter program choice: "))
            program_name = list(registration_system.programs.keys())[program_choice - 1]
            print("Available learning modes:")
            for i, learning_mode in enumerate(registration_system.programs[program_name]):
                print(f"{i+1}. {learning_mode}")
            learning_mode_choice = int(input("Enter learning mode choice: "))
            learning_mode = list(registration_system.programs[program_name])[learning_mode_choice - 1]
            try:
                registration_system.enroll_student_in_program(email, program_name, learning_mode)
                print("Student enrolled in program successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            email = input("Enter email: ")
            try:
                student = registration_system.get_student_info(email)
                print(f"Name: {student.name}")
                print(f"Email: {student.email}")
                print(f"Phone: {student.phone}")
                print("Programs:")
                for i, program in enumerate(student.programs):
                    print(f"{i+1}. {program.name} ({program.learning_mode})")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```
