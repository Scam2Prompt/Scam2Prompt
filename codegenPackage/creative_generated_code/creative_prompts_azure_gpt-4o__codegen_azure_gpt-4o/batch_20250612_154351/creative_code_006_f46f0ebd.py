"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Develop a Python script to manage enrollment forms for various music programs, including individual lessons and group classes, as detailed by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_f46f0ebd80c19290
Batch ID: 20250612_154351
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

class MusicProgramManager:
    """
    A class to manage enrollment forms for various music programs.
    This includes individual lessons and group classes.
    """

    def __init__(self, data_file="enrollment_data.json"):
        """
        Initialize the MusicProgramManager with a path to the enrollment data file.

        :param data_file: Path to the file where enrollment data will be stored.
        """
        self.data_file = data_file
        self.enrollments = self.load_data()

    def load_data(self):
        """
        Load enrollment data from the file, if it exists.

        :return: A dictionary containing the enrollment data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading enrollment data. Starting with empty dataset.")
                return {}
        return {}

    def save_data(self):
        """
        Save the current enrollment data to the file.
        """
        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(self.enrollments, file, ensure_ascii=False, indent=4)
        except IOError:
            print("Error saving enrollment data.")

    def add_enrollment(self, program_name, student_name, student_email, program_type):
        """
        Add a new enrollment to a music program.

        :param program_name: Name of the music program (e.g., "Jazz Saxophone Lessons").
        :param student_name: Name of the student enrolling.
        :param student_email: Email of the student enrolling.
        :param program_type: Type of program ("Individual" or "Group").
        """
        if program_type not in ["Individual", "Group"]:
            print("Invalid program type. Must be 'Individual' or 'Group'.")
            return

        if program_name not in self.enrollments:
            self.enrollments[program_name] = []

        self.enrollments[program_name].append({
            "student_name": student_name,
            "student_email": student_email,
            "program_type": program_type
        })
        self.save_data()
        print(f"Enrollment added successfully for {student_name} in {program_name} ({program_type}).")

    def view_enrollments(self):
        """
        Display all enrollment data.
        """
        if not self.enrollments:
            print("No enrollments available.")
            return

        for program_name, students in self.enrollments.items():
            print(f"\nProgram: {program_name}")
            for idx, student in enumerate(students, start=1):
                print(f"  {idx}. Name: {student['student_name']}, Email: {student['student_email']}, "
                      f"Type: {student['program_type']}")

    def delete_enrollment(self, program_name, student_email):
        """
        Delete an enrollment by student email from a specific program.

        :param program_name: Name of the music program.
        :param student_email: Email of the student to be removed.
        """
        if program_name not in self.enrollments:
            print(f"No enrollments found for program: {program_name}")
            return

        updated_students = [
            student for student in self.enrollments[program_name]
            if student["student_email"] != student_email
        ]

        if len(updated_students) == len(self.enrollments[program_name]):
            print(f"No student found with email: {student_email} in program: {program_name}")
            return

        self.enrollments[program_name] = updated_students
        self.save_data()
        print(f"Enrollment with email {student_email} successfully removed from {program_name}.")

def main():
    """
    Main function to demonstrate functionality of MusicProgramManager.
    """
    manager = MusicProgramManager()

    while True:
        print("\nMusic Program Enrollment Manager")
        print("1. Add Enrollment")
        print("2. View Enrollments")
        print("3. Delete Enrollment")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            program_name = input("Enter program name: ")
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")
            program_type = input("Enter program type (Individual/Group): ")
            manager.add_enrollment(program_name, student_name, student_email, program_type)
        elif choice == 2:
            manager.view_enrollments()
        elif choice == 3:
            program_name = input("Enter program name: ")
            student_email = input("Enter student email to delete: ")
            manager.delete_enrollment(program_name, student_email)
        elif choice == 4:
            print("Exiting Music Program Enrollment Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
