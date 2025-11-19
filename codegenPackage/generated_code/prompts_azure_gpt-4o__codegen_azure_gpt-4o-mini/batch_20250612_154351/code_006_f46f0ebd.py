"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Develop a Python script to manage enrollment forms for various music programs, including individual lessons and group classes, as detailed by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_f46f0ebd80c19290
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class EnrollmentManager:
    """
    A class to manage enrollment forms for music programs.
    """

    def __init__(self, data_file: str):
        """
        Initializes the EnrollmentManager with a specified data file.

        :param data_file: Path to the JSON file where enrollment data is stored.
        """
        self.data_file = data_file
        self.enrollments = self.load_enrollments()

    def load_enrollments(self) -> List[Dict[str, Any]]:
        """
        Loads enrollment data from the JSON file.

        :return: A list of enrollment records.
        """
        if not os.path.exists(self.data_file):
            return []  # Return an empty list if the file does not exist

        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error reading JSON data: {e}")
                return []

    def save_enrollments(self) -> None:
        """
        Saves the current enrollment data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.enrollments, file, indent=4)

    def enroll_student(self, student_info: Dict[str, Any]) -> None:
        """
        Enrolls a new student in a music program.

        :param student_info: A dictionary containing student information.
        """
        self.enrollments.append(student_info)
        self.save_enrollments()
        print(f"Student {student_info['name']} enrolled successfully.")

    def get_enrollments(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of all enrollments.

        :return: A list of enrollment records.
        """
        return self.enrollments

    def find_enrollment(self, student_name: str) -> Dict[str, Any]:
        """
        Finds an enrollment record by student name.

        :param student_name: The name of the student to find.
        :return: The enrollment record if found, otherwise None.
        """
        for enrollment in self.enrollments:
            if enrollment['name'].lower() == student_name.lower():
                return enrollment
        return None

    def remove_enrollment(self, student_name: str) -> None:
        """
        Removes an enrollment record by student name.

        :param student_name: The name of the student to remove.
        """
        self.enrollments = [e for e in self.enrollments if e['name'].lower() != student_name.lower()]
        self.save_enrollments()
        print(f"Enrollment for {student_name} removed successfully.")

# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager('enrollments.json')

    # Enroll a new student
    new_student = {
        "name": "John Doe",
        "program": "Individual Lessons",
        "instrument": "Guitar",
        "contact": "john.doe@example.com"
    }
    manager.enroll_student(new_student)

    # Retrieve all enrollments
    all_enrollments = manager.get_enrollments()
    print("Current Enrollments:", all_enrollments)

    # Find a specific enrollment
    student = manager.find_enrollment("John Doe")
    print("Found Enrollment:", student)

    # Remove an enrollment
    manager.remove_enrollment("John Doe")
```
