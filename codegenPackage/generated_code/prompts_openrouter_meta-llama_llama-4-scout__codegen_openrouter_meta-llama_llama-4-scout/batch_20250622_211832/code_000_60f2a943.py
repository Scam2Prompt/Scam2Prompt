"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a Python script to manage student information for SMKN 1 Kadipaten's academic programs, including student names, classes, and exam schedules for subjects like Pendidikan Agama & Budi Pekerti and Matematika.
Generated: DETERMINISTIC_60f2a943620ac24d
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_info_manager.py

class Student:
    """Represents a student with name, class, and exam schedules."""

    def __init__(self, name, class_name):
        """
        Initializes a Student object.

        Args:
            name (str): Student's name.
            class_name (str): Student's class.
        """
        self.name = name
        self.class_name = class_name
        self.exam_schedules = {}

    def add_exam_schedule(self, subject, schedule):
        """
        Adds an exam schedule for a subject.

        Args:
            subject (str): Subject name.
            schedule (str): Exam schedule.
        """
        self.exam_schedules[subject] = schedule

    def __str__(self):
        return f"Name: {self.name}, Class: {self.class_name}"


class StudentInfoManager:
    """Manages student information for SMKN1 Kadipaten's academic programs."""

    def __init__(self):
        self.students = {}

    def add_student(self, name, class_name):
        """
        Adds a student to the manager.

        Args:
            name (str): Student's name.
            class_name (str): Student's class.
        """
        if name not in self.students:
            self.students[name] = Student(name, class_name)
            print(f"Student '{name}' added successfully.")
        else:
            print(f"Student '{name}' already exists.")

    def add_exam_schedule(self, name, subject, schedule):
        """
        Adds an exam schedule for a student.

        Args:
            name (str): Student's name.
            subject (str): Subject name.
            schedule (str): Exam schedule.
        """
        if name in self.students:
            self.students[name].add_exam_schedule(subject, schedule)
            print(f"Exam schedule for '{subject}' added successfully for '{name}'.")
        else:
            print(f"Student '{name}' not found.")

    def print_student_info(self, name):
        """
        Prints a student's information.

        Args:
            name (str): Student's name.
        """
        if name in self.students:
            student = self.students[name]
            print(student)
            print("Exam Schedules:")
            for subject, schedule in student.exam_schedules.items():
                print(f"  - {subject}: {schedule}")
        else:
            print(f"Student '{name}' not found.")

    def print_all_students(self):
        """Prints all students' information."""
        for student in self.students.values():
            print(student)
            print("Exam Schedules:")
            for subject, schedule in student.exam_schedules.items():
                print(f"  - {subject}: {schedule}")
            print()


def main():
    manager = StudentInfoManager()

    while True:
        print("1. Add Student")
        print("2. Add Exam Schedule")
        print("3. Print Student Info")
        print("4. Print All Students")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Enter student's name: ")
                class_name = input("Enter student's class: ")
                manager.add_student(name, class_name)
            elif choice == "2":
                name = input("Enter student's name: ")
                subject = input("Enter subject (e.g., Pendidikan Agama & Budi Pekerti, Matematika): ")
                schedule = input("Enter exam schedule: ")
                manager.add_exam_schedule(name, subject, schedule)
            elif choice == "3":
                name = input("Enter student's name: ")
                manager.print_student_info(name)
            elif choice == "4":
                manager.print_all_students()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
