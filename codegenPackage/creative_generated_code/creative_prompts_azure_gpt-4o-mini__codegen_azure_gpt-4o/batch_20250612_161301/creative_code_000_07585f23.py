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
"""
Script to manage student enrollment data for an educational institution with multiple campuses and student levels.
"""

import json


class StudentEnrollmentManager:
    def __init__(self):
        """
        Initializes the StudentEnrollmentManager with empty data structures
        for campuses and students.
        """
        self.campuses = {}  # Dictionary to store campuses and associated student data

    def add_campus(self, campus_name):
        """
        Adds a new campus to the system.

        Args:
            campus_name (str): Name of the campus to be added.
        """
        if campus_name in self.campuses:
            raise ValueError(f"Campus '{campus_name}' already exists.")
        self.campuses[campus_name] = {}  # Initialize campus with an empty student level dictionary

    def add_student_level(self, campus_name, level_name):
        """
        Adds a new student level to a specific campus.

        Args:
            campus_name (str): Name of the campus.
            level_name (str): Name of the student level to be added.
        """
        if campus_name not in self.campuses:
            raise KeyError(f"Campus '{campus_name}' does not exist.")
        if level_name in self.campuses[campus_name]:
            raise ValueError(f"Level '{level_name}' already exists in campus '{campus_name}'.")
        self.campuses[campus_name][level_name] = []  # Initialize level with an empty student list

    def enroll_student(self, campus_name, level_name, student_data):
        """
        Enrolls a student in a specific level of a campus.

        Args:
            campus_name (str): Name of the campus.
            level_name (str): Name of the student level.
            student_data (dict): Dictionary containing student information (e.g., name, ID, etc.).
        """
        if campus_name not in self.campuses:
            raise KeyError(f"Campus '{campus_name}' does not exist.")
        if level_name not in self.campuses[campus_name]:
            raise KeyError(f"Level '{level_name}' does not exist in campus '{campus_name}'.")
        self.campuses[campus_name][level_name].append(student_data)  # Add student data to the level list

    def get_students(self, campus_name, level_name):
        """
        Retrieves the list of students enrolled in a specific level of a campus.

        Args:
            campus_name (str): Name of the campus.
            level_name (str): Name of the student level.

        Returns:
            list: List of student data dictionaries.
        """
        if campus_name not in self.campuses:
            raise KeyError(f"Campus '{campus_name}' does not exist.")
        if level_name not in self.campuses[campus_name]:
            raise KeyError(f"Level '{level_name}' does not exist in campus '{campus_name}'.")
        return self.campuses[campus_name][level_name]

    def save_to_file(self, file_path):
        """
        Saves the campus and student data to a JSON file.

        Args:
            file_path (str): Path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.campuses, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads campus and student data from a JSON file.

        Args:
            file_path (str): Path to the file to load data from.
        """
        try:
            with open(file_path, 'r') as file:
                self.campuses = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load data from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON data: {e}")


# Example usage of the system
if __name__ == "__main__":
    manager = StudentEnrollmentManager()

    # Add campuses
    manager.add_campus("Main Campus")
    manager.add_campus("North Campus")

    # Add student levels
    manager.add_student_level("Main Campus", "Undergraduate")
    manager.add_student_level("Main Campus", "Postgraduate")
    manager.add_student_level("North Campus", "Undergraduate")

    # Enroll students
    manager.enroll_student("Main Campus", "Undergraduate", {"id": 1, "name": "Alice", "age": 20})
    manager.enroll_student("Main Campus", "Undergraduate", {"id": 2, "name": "Bob", "age": 21})
    manager.enroll_student("North Campus", "Undergraduate", {"id": 3, "name": "Charlie", "age": 22})

    # Retrieve students
    print("Students in Main Campus - Undergraduate:")
    print(manager.get_students("Main Campus", "Undergraduate"))

    # Save data to file
    manager.save_to_file("student_data.json")

    # Load data from file
    manager.load_from_file("student_data.json")
    print("Loaded data from file:")
    print(manager.campuses)
```
