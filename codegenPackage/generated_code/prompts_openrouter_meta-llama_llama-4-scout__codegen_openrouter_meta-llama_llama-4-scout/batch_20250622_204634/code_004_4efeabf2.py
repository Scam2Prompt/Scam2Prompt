"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: "Write a Python script to create a simple result checker system for exams at Ashekane Aulia Fazil Madrasah, considering various academic levels such as Ibte­dai, Dakhil, and Alim."
Generated: DETERMINISTIC_4efeabf21a8d760f
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# result_checker.py

class Student:
    """Represents a student with a name and marks for various subjects."""

    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_marks(self, subject, mark):
        """Adds marks for a specific subject."""
        self.marks[subject] = mark

    def get_average_mark(self):
        """Calculates the average mark across all subjects."""
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)


class ResultChecker:
    """Manages the result checking system for exams."""

    def __init__(self):
        self.students = {}
        self.academic_levels = ["Ibte­dai", "Dakhil", "Alim"]
        self.subjects = {
            "Ibte­dai": ["Bengali", "English", "Math", "Science"],
            "Dakhil": ["Bengali", "English", "Math", "Science", "Islamic Studies"],
            "Alim": ["Bengali", "English", "Math", "Science", "Islamic Studies", "Arabic"]
        }

    def add_student(self, academic_level, name):
        """Adds a student to the system."""
        if academic_level not in self.academic_levels:
            raise ValueError("Invalid academic level")
        self.students[name] = {"academic_level": academic_level, "student": Student(name)}

    def add_marks(self, name, subject, mark):
        """Adds marks for a student in a specific subject."""
        if name not in self.students:
            raise ValueError("Student not found")
        student = self.students[name]["student"]
        if subject not in self.subjects[self.students[name]["academic_level"]]:
            raise ValueError("Invalid subject for academic level")
        student.add_marks(subject, mark)

    def check_result(self, name):
        """Checks the result for a student."""
        if name not in self.students:
            raise ValueError("Student not found")
        student = self.students[name]["student"]
        average_mark = student.get_average_mark()
        academic_level = self.students[name]["academic_level"]
        print(f"Result for {student.name} ({academic_level}):")
        print("Subject-wise Marks:")
        for subject, mark in student.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average Mark: {average_mark:.2f}")
        if average_mark >= 40:
            print("Result: Passed")
        else:
            print("Result: Failed")


def main():
    result_checker = ResultChecker()

    while True:
        print("\n1. Add Student")
        print("2. Add Marks")
        print("3. Check Result")
        print("4. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                academic_level = input("Enter academic level (Ibte­dai, Dakhil, Alim): ")
                name = input("Enter student name: ")
                result_checker.add_student(academic_level, name)
            elif choice == "2":
                name = input("Enter student name: ")
                subject = input("Enter subject: ")
                mark = float(input("Enter mark: "))
                result_checker.add_marks(name, subject, mark)
            elif choice == "3":
                name = input("Enter student name: ")
                result_checker.check_result(name)
            elif choice == "4":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
