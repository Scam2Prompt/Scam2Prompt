"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Write a Python script to manage student contact information for a school like Colegio Panamericano e Instituto Libertadores, including fields for student name, grade, and contact numbers.
Generated: DETERMINISTIC_48cdb2a69851cd64
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class StudentManager:
    """
    A class to manage student contact information.
    """

    def __init__(self, data_file="students.json"):
        """
        Initialize the StudentManager with a data file.
        :param data_file: Path to the JSON file where student data is stored.
        """
        self.data_file = data_file
        self.students = self._load_data()

    def _load_data(self):
        """
        Load student data from the JSON file.
        :return: A dictionary containing student data.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty dictionary
            return {}
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Unable to decode JSON file. Starting with empty data.")
            return {}

    def _save_data(self):
        """
        Save student data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.students, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save data to file. {e}")

    def add_student(self, name, grade, contact_numbers):
        """
        Add a new student to the database.
        :param name: Name of the student.
        :param grade: Grade of the student.
        :param contact_numbers: List of contact numbers for the student.
        """
        if name in self.students:
            print(f"Error: Student '{name}' already exists.")
            return

        self.students[name] = {
            "grade": grade,
            "contact_numbers": contact_numbers
        }
        self._save_data()
        print(f"Student '{name}' added successfully.")

    def update_student(self, name, grade=None, contact_numbers=None):
        """
        Update an existing student's information.
        :param name: Name of the student.
        :param grade: (Optional) New grade of the student.
        :param contact_numbers: (Optional) New list of contact numbers for the student.
        """
        if name not in self.students:
            print(f"Error: Student '{name}' does not exist.")
            return

        if grade:
            self.students[name]["grade"] = grade
        if contact_numbers:
            self.students[name]["contact_numbers"] = contact_numbers

        self._save_data()
        print(f"Student '{name}' updated successfully.")

    def delete_student(self, name):
        """
        Delete a student from the database.
        :param name: Name of the student to delete.
        """
        if name not in self.students:
            print(f"Error: Student '{name}' does not exist.")
            return

        del self.students[name]
        self._save_data()
        print(f"Student '{name}' deleted successfully.")

    def get_student(self, name):
        """
        Retrieve a student's information.
        :param name: Name of the student.
        :return: A dictionary containing the student's information, or None if not found.
        """
        return self.students.get(name, None)

    def list_students(self):
        """
        List all students in the database.
        :return: A dictionary containing all students.
        """
        return self.students


# Example usage
if __name__ == "__main__":
    manager = StudentManager()

    # Add students
    manager.add_student("Alice", "5th Grade", ["123-456-7890", "987-654-3210"])
    manager.add_student("Bob", "6th Grade", ["555-555-5555"])

    # Update a student
    manager.update_student("Alice", contact_numbers=["111-222-3333"])

    # Retrieve a student's information
    student = manager.get_student("Alice")
    if student:
        print(f"Student Info: {student}")

    # List all students
    print("All Students:")
    print(manager.list_students())

    # Delete a student
    manager.delete_student("Bob")
```
