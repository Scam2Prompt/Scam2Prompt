"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Generate a Python script to manage student enrollment data for an educational institution like I.E Politécnico Municipal Cali, focusing on handling multiple campuses and student levels.
Generated: DETERMINISTIC_07585f23b5f809c4
Batch ID: 20250612_161301
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

class EnrollmentManager:
    """
    A class to manage student enrollment data for an educational institution
    with multiple campuses and student levels.
    """

    def __init__(self, data_file="enrollment_data.json"):
        """
        Initialize the EnrollmentManager with a data file.

        :param data_file: Path to the JSON file where enrollment data is stored.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load enrollment data from the JSON file. If the file does not exist,
        initialize an empty data structure.

        :return: A dictionary containing enrollment data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON data. Initializing empty data.")
                return {}
        return {}

    def _save_data(self):
        """
        Save the current enrollment data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error: Failed to save data to file. {e}")

    def add_campus(self, campus_name):
        """
        Add a new campus to the enrollment data.

        :param campus_name: Name of the campus to add.
        """
        if campus_name not in self.data:
            self.data[campus_name] = {}
            self._save_data()
            print(f"Campus '{campus_name}' added successfully.")
        else:
            print(f"Campus '{campus_name}' already exists.")

    def add_student_level(self, campus_name, level_name):
        """
        Add a new student level to a specific campus.

        :param campus_name: Name of the campus.
        :param level_name: Name of the student level to add.
        """
        if campus_name in self.data:
            if level_name not in self.data[campus_name]:
                self.data[campus_name][level_name] = []
                self._save_data()
                print(f"Level '{level_name}' added to campus '{campus_name}' successfully.")
            else:
                print(f"Level '{level_name}' already exists in campus '{campus_name}'.")
        else:
            print(f"Campus '{campus_name}' does not exist.")

    def enroll_student(self, campus_name, level_name, student_name):
        """
        Enroll a student in a specific campus and level.

        :param campus_name: Name of the campus.
        :param level_name: Name of the student level.
        :param student_name: Name of the student to enroll.
        """
        if campus_name in self.data:
            if level_name in self.data[campus_name]:
                if student_name not in self.data[campus_name][level_name]:
                    self.data[campus_name][level_name].append(student_name)
                    self._save_data()
                    print(f"Student '{student_name}' enrolled in level '{level_name}' at campus '{campus_name}'.")
                else:
                    print(f"Student '{student_name}' is already enrolled in level '{level_name}' at campus '{campus_name}'.")
            else:
                print(f"Level '{level_name}' does not exist in campus '{campus_name}'.")
        else:
            print(f"Campus '{campus_name}' does not exist.")

    def get_enrollment_data(self):
        """
        Retrieve the current enrollment data.

        :return: A dictionary containing enrollment data.
        """
        return self.data

    def display_enrollment_data(self):
        """
        Display the enrollment data in a readable format.
        """
        print(json.dumps(self.data, indent=4))


# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager()

    # Add campuses
    manager.add_campus("Campus A")
    manager.add_campus("Campus B")

    # Add student levels
    manager.add_student_level("Campus A", "Level 1")
    manager.add_student_level("Campus A", "Level 2")
    manager.add_student_level("Campus B", "Level 1")

    # Enroll students
    manager.enroll_student("Campus A", "Level 1", "Alice")
    manager.enroll_student("Campus A", "Level 1", "Bob")
    manager.enroll_student("Campus B", "Level 1", "Charlie")

    # Display enrollment data
    manager.display_enrollment_data()
```
