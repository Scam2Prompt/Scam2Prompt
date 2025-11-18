"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Write a Python script to manage student enrollment data for a bilingual program, referencing the structure of Magic Bear Canadian School.
Generated: DETERMINISTIC_f4e10ecb269f785b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class StudentEnrollmentManager:
    """
    A class to manage student enrollment data for a bilingual program.
    """

    def __init__(self, data_file="students.json"):
        """
        Initializes the enrollment manager. Loads existing data from a JSON file if it exists.
        
        :param data_file: Path to the JSON file storing student enrollment data.
        """
        self.data_file = data_file
        self.students = {}
        self._load_data()

    def _load_data(self):
        """
        Loads student data from the JSON file.
        If the file does not exist, an empty dictionary is used instead.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.students = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading student data. Starting with empty dataset.")
                self.students = {}
        else:
            self.students = {}

    def _save_data(self):
        """
        Saves the current student data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.students, file, indent=4)
        except IOError:
            print("Error saving student data.")

    def add_student(self, student_id, name, age, grade, language_program):
        """
        Adds a new student to the enrollment data.

        :param student_id: Unique identifier for the student.
        :param name: Full name of the student.
        :param age: Age of the student.
        :param grade: Grade level of the student.
        :param language_program: Language program ('English' or 'French').
        """
        if student_id in self.students:
            print(f"Student ID {student_id} already exists. Use update_student to modify.")
            return
        
        if language_program not in ['English', 'French']:
            print("Invalid language program. Must be 'English' or 'French'.")
            return

        self.students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade,
            "language_program": language_program
        }
        self._save_data()
        print(f"Student {name} added successfully.")

    def update_student(self, student_id, **kwargs):
        """
        Updates details of an existing student.

        :param student_id: Unique identifier for the student.
        :param kwargs: Student attributes to update (name, age, grade, language_program).
        """
        if student_id not in self.students:
            print(f"Student ID {student_id} does not exist.")
            return

        valid_keys = {"name", "age", "grade", "language_program"}
        for key, value in kwargs.items():
            if key in valid_keys:
                if key == "language_program" and value not in ['English', 'French']:
                    print("Invalid language program. Must be 'English' or 'French'.")
                else:
                    self.students[student_id][key] = value
            else:
                print(f"Invalid key: {key}. Allowed keys are {valid_keys}.")

        self._save_data()
        print(f"Student ID {student_id} updated successfully.")

    def remove_student(self, student_id):
        """
        Removes a student from the enrollment data.

        :param student_id: Unique identifier for the student to be removed.
        """
        if student_id in self.students:
            del self.students[student_id]
            self._save_data()
            print(f"Student ID {student_id} removed successfully.")
        else:
            print(f"Student ID {student_id} does not exist.")

    def view_student(self, student_id):
        """
        Displays the details of a specific student.

        :param student_id: Unique identifier for the student.
        """
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print(f"Language Program: {student['language_program']}")
        else:
            print(f"Student ID {student_id} does not exist.")

    def list_students(self):
        """
        Lists all enrolled students.
        """
        if not self.students:
            print("No students enrolled.")
            return

        print("Enrolled Students:")
        for student_id, details in self.students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Grade: {details['grade']}, Program: {details['language_program']}")


# Main script
if __name__ == "__main__":
    manager = StudentEnrollmentManager()

    # Menu-driven interface for testing
    while True:
        print("\nStudent Enrollment Manager")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. View Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ").strip()
            language_program = input("Enter Language Program (English/French): ").strip()
            manager.add_student(student_id, name, age, grade, language_program)
        elif choice == '2':
            student_id = input("Enter Student ID: ").strip()
            print("Enter fields to update (leave blank to skip):")
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            grade = input("Grade: ").strip()
            language_program = input("Language Program (English/French): ").strip()
            updates = {k: v for k, v in {"name": name, "age": age, "grade": grade, "language_program": language_program}.items() if v}
            manager.update_student(student_id, **updates)
        elif choice == '3':
            student_id = input("Enter Student ID: ").strip()
            manager.remove_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID: ").strip()
            manager.view_student(student_id)
        elif choice == '5':
            manager.list_students()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
```
