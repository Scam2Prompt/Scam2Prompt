"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Develop a script to analyze and manage modular certifications for students, similar to the "Certificaciones Modulares" system described on the Trentino website.
Generated: DETERMINISTIC_e65f89dedef7e2c3
Batch ID: 20250612_151445
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


class CertificationManager:
    """A class to analyze and manage modular certifications for students."""

    def __init__(self, data_file):
        """
        Initializes the CertificationManager.

        :param data_file: Path to the JSON file containing student certifications.
        """
        self.data_file = data_file
        self.certifications = {}
        self._load_certifications()

    def _load_certifications(self):
        """Loads certifications from the JSON file."""
        if not os.path.exists(self.data_file):
            # If file does not exist, initialize with an empty dictionary
            self.certifications = {}
            return

        try:
            with open(self.data_file, 'r') as file:
                self.certifications = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading certifications: {e}")
            self.certifications = {}

    def _save_certifications(self):
        """Saves the certifications to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.certifications, file, indent=4)
        except IOError as e:
            print(f"Error saving certifications: {e}")

    def add_certification(self, student_id, module_name, status):
        """
        Adds or updates a certification for a student.

        :param student_id: Unique ID of the student.
        :param module_name: Name of the certification module.
        :param status: Status of the certification (e.g., "Completed", "In Progress").
        """
        if student_id not in self.certifications:
            self.certifications[student_id] = {}

        self.certifications[student_id][module_name] = status
        self._save_certifications()

    def get_certifications(self, student_id):
        """
        Retrieves certifications for a specific student.

        :param student_id: Unique ID of the student.
        :return: Dictionary of module names and statuses for the student.
        """
        return self.certifications.get(student_id, {})

    def get_certified_students(self, module_name):
        """
        Retrieves a list of students who have completed a specific module.

        :param module_name: Name of the certification module.
        :return: List of student IDs who have completed the module.
        """
        certified_students = [
            student_id
            for student_id, modules in self.certifications.items()
            if modules.get(module_name) == "Completed"
        ]
        return certified_students

    def remove_certification(self, student_id, module_name):
        """
        Removes a specific certification for a student.

        :param student_id: Unique ID of the student.
        :param module_name: Name of the certification module to remove.
        """
        if student_id in self.certifications and module_name in self.certifications[student_id]:
            del self.certifications[student_id][module_name]
            # Remove the student entirely if they have no other certifications
            if not self.certifications[student_id]:
                del self.certifications[student_id]
            self._save_certifications()

    def display_certifications(self):
        """Prints all certifications in a formatted way."""
        print(json.dumps(self.certifications, indent=4))


if __name__ == "__main__":
    # Example usage
    manager = CertificationManager("certifications.json")

    # Adding certifications
    manager.add_certification("student_001", "Module A", "Completed")
    manager.add_certification("student_002", "Module B", "In Progress")
    manager.add_certification("student_001", "Module B", "Completed")

    # Displaying all certifications
    manager.display_certifications()

    # Fetching certifications for a specific student
    print(manager.get_certifications("student_001"))

    # Fetching students certified for a specific module
    print(manager.get_certified_students("Module B"))

    # Removing a certification
    manager.remove_certification("student_001", "Module A")
    manager.display_certifications()
```
