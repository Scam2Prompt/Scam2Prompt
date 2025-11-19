"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Write a Python script to manage registrations for multiple Endeavor Plus programs across different schools, including fields for student information, program selection, and school location."
Generated: DETERMINISTIC_683bdef5f171ed5f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class RegistrationManager:
    """
    A class to manage registrations for Endeavor Plus programs across different schools.
    """

    def __init__(self):
        """
        Initializes the RegistrationManager with an empty list of registrations.
        """
        self.registrations = []

    def register_student(self, student_name, student_age, program_name, school_location):
        """
        Registers a student for a program at a specific school location.

        Args:
            student_name (str): Name of the student.
            student_age (int): Age of the student.
            program_name (str): Name of the program the student is registering for.
            school_location (str): Location of the school.

        Returns:
            dict: The registration details if successful.
        """
        try:
            # Validate inputs
            if not student_name or not isinstance(student_name, str):
                raise ValueError("Invalid student name.")
            if not isinstance(student_age, int) or student_age <= 0:
                raise ValueError("Invalid student age.")
            if not program_name or not isinstance(program_name, str):
                raise ValueError("Invalid program name.")
            if not school_location or not isinstance(school_location, str):
                raise ValueError("Invalid school location.")

            # Create registration record
            registration = {
                "student_name": student_name,
                "student_age": student_age,
                "program_name": program_name,
                "school_location": school_location
            }

            # Add to registrations list
            self.registrations.append(registration)
            return registration

        except ValueError as ve:
            print(f"Error: {ve}")
            return None

    def list_registrations(self):
        """
        Lists all registrations.

        Returns:
            list: A list of all registration records.
        """
        return self.registrations

    def save_to_file(self, file_name):
        """
        Saves all registrations to a JSON file.

        Args:
            file_name (str): Name of the file to save the registrations to.

        Returns:
            bool: True if the file was saved successfully, False otherwise.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.registrations, file, indent=4)
            print(f"Registrations saved to {file_name}.")
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, file_name):
        """
        Loads registrations from a JSON file.

        Args:
            file_name (str): Name of the file to load the registrations from.

        Returns:
            bool: True if the file was loaded successfully, False otherwise.
        """
        try:
            with open(file_name, 'r') as file:
                self.registrations = json.load(file)
            print(f"Registrations loaded from {file_name}.")
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


# Example usage
if __name__ == "__main__":
    manager = RegistrationManager()

    # Register students
    manager.register_student("Alice Johnson", 15, "Robotics", "Greenwood High")
    manager.register_student("Bob Smith", 16, "AI Fundamentals", "Springfield Academy")

    # List registrations
    print("Current Registrations:")
    print(manager.list_registrations())

    # Save registrations to file
    manager.save_to_file("registrations.json")

    # Load registrations from file
    manager.load_from_file("registrations.json")
    print("Registrations after loading from file:")
    print(manager.list_registrations())
```
