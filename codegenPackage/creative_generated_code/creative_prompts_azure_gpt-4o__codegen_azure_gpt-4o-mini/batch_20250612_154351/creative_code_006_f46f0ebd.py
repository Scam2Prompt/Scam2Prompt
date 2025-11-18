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
from typing import List, Dict, Any

class EnrollmentManager:
    def __init__(self, data_file: str):
        """
        Initializes the EnrollmentManager with the specified data file.
        :param data_file: Path to the JSON file storing enrollment data.
        """
        self.data_file = data_file
        self.enrollments = self.load_enrollments()

    def load_enrollments(self) -> List[Dict[str, Any]]:
        """
        Loads enrollments from the JSON data file. Creates the file if it does not exist.
        :return: A list of enrollment records.
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)  # Initialize with empty list
            return []

        with open(self.data_file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error loading data: {e}")
                return []

    def save_enrollments(self) -> None:
        """
        Saves the current list of enrollments to the JSON data file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.enrollments, f, indent=4)

    def enroll_student(self, student_name: str, program: str, lesson_type: str) -> None:
        """
        Enrolls a student in a specified program and lesson type.
        :param student_name: Name of the student.
        :param program: Name of the music program.
        :param lesson_type: Type of lesson (individual or group).
        """
        enrollment = {
            "student_name": student_name,
            "program": program,
            "lesson_type": lesson_type
        }
        self.enrollments.append(enrollment)
        self.save_enrollments()
        print(f"Successfully enrolled {student_name} in {program} ({lesson_type}).")

    def get_enrollments(self) -> List[Dict[str, Any]]:
        """
        Retrieves all current enrollments.
        :return: A list of enrollment records.
        """
        return self.enrollments

    def find_student_enrollments(self, student_name: str) -> List[Dict[str, Any]]:
        """
        Finds all enrollments for a specific student.
        :param student_name: Name of the student to search for.
        :return: A list of enrollment records for the specified student.
        """
        return [enrollment for enrollment in self.enrollments if enrollment['student_name'] == student_name]

if __name__ == "__main__":
    # Define the path for the enrollment data file
    enrollment_file = 'enrollments.json'

    # Create an instance of the EnrollmentManager
    manager = EnrollmentManager(enrollment_file)

    # Example usage
    try:
        # Enroll students in different programs
        manager.enroll_student("John Doe", "Guitar Basics", "Individual")
        manager.enroll_student("Jane Smith", "Piano Advance", "Group")
        
        # Retrieve and display all enrollments
        all_enrollments = manager.get_enrollments()
        print("Current enrollments:", all_enrollments)

        # Find specific student's enrollments
        john_enrollments = manager.find_student_enrollments("John Doe")
        print("John Doe's enrollments:", john_enrollments)

    except Exception as e:
        print(f"An error occurred: {e}")
```
