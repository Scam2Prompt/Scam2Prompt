"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Generate a Python script to automate the registration process for new students at Sekolah Quran Indonesia, incorporating their unique programs like Sekolah Qur'an for various age groups.
Generated: DETERMINISTIC_c024906e38633e1c
Batch ID: 20250612_160703
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
    def __init__(self, name, age, program):
        """
        Initialize a Student object.

        Args:
            name (str): Student's name
            age (int): Student's age
            program (str): Student's program
        """
        self.name = name
        self.age = age
        self.program = program

class Program:
    def __init__(self, name, min_age, max_age):
        """
        Initialize a Program object.

        Args:
            name (str): Program's name
            min_age (int): Program's minimum age
            max_age (int): Program's maximum age
        """
        self.name = name
        self.min_age = min_age
        self.max_age = max_age

class SekolahQuran:
    def __init__(self):
        """
        Initialize a SekolahQuran object.
        """
        self.programs = {
            "Tahfidz": Program("Tahfidz", 6, 12),
            "Tafsir": Program("Tafsir", 13, 18),
            "Quranic Arabic": Program("Quranic Arabic", 7, 15),
        }
        self.students = []

    def register_student(self, name, age, program_name):
        """
        Register a new student.

        Args:
            name (str): Student's name
            age (int): Student's age
            program_name (str): Student's program name

        Returns:
            bool: True if registration is successful, False otherwise
        """
        if program_name not in self.programs:
            print(f"Program '{program_name}' not found.")
            return False

        program = self.programs[program_name]
        if age < program.min_age or age > program.max_age:
            print(f"Age {age} is not eligible for program '{program_name}'.")
            return False

        student = Student(name, age, program_name)
        self.students.append(student)
        print(f"Student '{name}' registered successfully in program '{program_name}'.")
        return True

    def display_students(self):
        """
        Display all registered students.
        """
        print("Registered Students:")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. Name: {student.name}, Age: {student.age}, Program: {student.program}")

def main():
    sekolah_quran = SekolahQuran()

    while True:
        print("\nSekolah Quran Indonesia Registration")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            print("Available programs:")
            for i, program_name in enumerate(sekolah_quran.programs.keys(), start=1):
                print(f"{i}. {program_name}")
            program_choice = int(input("Enter program number: "))
            program_name = list(sekolah_quran.programs.keys())[program_choice - 1]
            sekolah_quran.register_student(name, age, program_name)
        elif choice == "2":
            sekolah_quran.display_students()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
