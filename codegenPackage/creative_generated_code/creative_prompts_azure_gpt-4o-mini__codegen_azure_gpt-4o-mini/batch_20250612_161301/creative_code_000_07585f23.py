"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Generate a Python script to manage student enrollment data for an educational institution like I.E Politécnico Municipal Cali, focusing on handling multiple campuses and student levels.
Generated: DETERMINISTIC_07585f23b5f809c4
Batch ID: 20250612_161301
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


class StudentEnrollmentManager:
    def __init__(self, data_file: str) -> None:
        """
        Initializes the StudentEnrollmentManager with the specified data file.

        :param data_file: The path to the JSON file storing enrollment data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        """
        Loads enrollment data from a JSON file. If the file does not exist, initializes an empty structure.

        :return: A dictionary representing the enrollment data.
        """
        if os.path.isfile(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {"campuses": {}}

    def save_data(self) -> None:
        """
        Saves the current enrollment data to the JSON file.
        """
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_campus(self, campus_name: str) -> None:
        """
        Adds a new campus to the enrollment data.

        :param campus_name: The name of the campus to add.
        """
        if campus_name not in self.data['campuses']:
            self.data['campuses'][campus_name] = {"students": {}}
            self.save_data()
        else:
            raise ValueError(f"Campus '{campus_name}' already exists.")

    def add_student(self, campus_name: str, student_id: str, student_level: str) -> None:
        """
        Adds a student to a specific campus.

        :param campus_name: The name of the campus where the student is enrolled.
        :param student_id: The unique identifier for the student.
        :param student_level: The level of the student (e.g., 'Undergraduate', 'Graduate').
        """
        if campus_name in self.data['campuses']:
            if student_id not in self.data['campuses'][campus_name]['students']:
                self.data['campuses'][campus_name]['students'][student_id] = {
                    "level": student_level
                }
                self.save_data()
            else:
                raise ValueError(f"Student with ID '{student_id}' already enrolled in '{campus_name}'.")
        else:
            raise ValueError(f"Campus '{campus_name}' does not exist.")

    def get_students(self, campus_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves a list of students enrolled at a specified campus.

        :param campus_name: The name of the campus to retrieve students from.
        :return: A list of dictionaries containing student information.
        """
        if campus_name in self.data['campuses']:
            return [
                {"student_id": student_id, "level": student_info["level"]}
                for student_id, student_info in self.data['campuses'][campus_name]['students'].items()
            ]
        else:
            raise ValueError(f"Campus '{campus_name}' does not exist.")

    def remove_student(self, campus_name: str, student_id: str) -> None:
        """
        Removes a student from a specific campus.

        :param campus_name: The name of the campus from which to remove the student.
        :param student_id: The unique identifier for the student to remove.
        """
        if campus_name in self.data['campuses']:
            if student_id in self.data['campuses'][campus_name]['students']:
                del self.data['campuses'][campus_name]['students'][student_id]
                self.save_data()
            else:
                raise ValueError(f"Student with ID '{student_id}' not found in '{campus_name}'.")
        else:
            raise ValueError(f"Campus '{campus_name}' does not exist.")


if __name__ == "__main__":
    # Example usage of the StudentEnrollmentManager
    manager = StudentEnrollmentManager(data_file='enrollment_data.json')

    try:
        manager.add_campus("Campus A")
        manager.add_student("Campus A", "S12345", "Undergraduate")
        students = manager.get_students("Campus A")
        print("Students enrolled in Campus A:", students)

        manager.remove_student("Campus A", "S12345")
        print("Students after removal:", manager.get_students("Campus A"))
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
