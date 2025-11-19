"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Generate a Python script that demonstrates how to manage student enrollment for the Graduate Diploma of Management (Learning) at Global Healthcare Management College.
Generated: DETERMINISTIC_3706fc22b7e63889
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Student Enrollment Management System for Graduate Diploma of Management (Learning)
at Global Healthcare Management College.

This script allows the user to:
1. Add new students to the enrollment list.
2. Remove students from the enrollment list.
3. View all enrolled students.
4. Save and load student data to/from a file.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json
import os

# File to store student enrollment data
DATA_FILE = "student_enrollment.json"

class EnrollmentManager:
    def __init__(self):
        """Initialize the EnrollmentManager and load existing data if available."""
        self.enrolled_students = []
        self.load_data()

    def add_student(self, student_name):
        """
        Add a new student to the enrollment list.

        Args:
            student_name (str): Name of the student to enroll.
        """
        if student_name.strip() == "":
            print("Error: Student name cannot be empty.")
            return

        if student_name in self.enrolled_students:
            print(f"Error: {student_name} is already enrolled.")
            return

        self.enrolled_students.append(student_name)
        print(f"Success: {student_name} has been enrolled.")
        self.save_data()

    def remove_student(self, student_name):
        """
        Remove a student from the enrollment list.

        Args:
            student_name (str): Name of the student to remove.
        """
        if student_name in self.enrolled_students:
            self.enrolled_students.remove(student_name)
            print(f"Success: {student_name} has been removed from the enrollment list.")
            self.save_data()
        else:
            print(f"Error: {student_name} is not enrolled.")

    def view_students(self):
        """Print the list of all enrolled students."""
        if not self.enrolled_students:
            print("No students are currently enrolled.")
        else:
            print("Enrolled Students:")
            for i, student in enumerate(self.enrolled_students, start=1):
                print(f"{i}. {student}")

    def save_data(self):
        """Save enrollment data to a file."""
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.enrolled_students, f)
        except IOError as e:
            print(f"Error: Failed to save data to {DATA_FILE}. Details: {e}")

    def load_data(self):
        """Load enrollment data from a file, if it exists."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    self.enrolled_students = json.load(f)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error: Failed to load data from {DATA_FILE}. Details: {e}")


def main():
    """Main function to interact with the enrollment system."""
    manager = EnrollmentManager()

    while True:
        print("\n--- Student Enrollment Management ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Enrolled Students")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            student_name = input("Enter the name of the student to add: ")
            manager.add_student(student_name)
        elif choice == "2":
            student_name = input("Enter the name of the student to remove: ")
            manager.remove_student(student_name)
        elif choice == "3":
            manager.view_students()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
