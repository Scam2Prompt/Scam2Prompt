"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Generate a sample enrollment application for Happy Scholars Academy, including required documents and information, such as the Universal Child Health Record form.
Generated: DETERMINISTIC_818322bfa2d21f63
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# enrollment_app.py

import json
from typing import List, Dict

class EnrollmentApplication:
    """
    A class to represent an enrollment application for Happy Scholars Academy.
    """

    def __init__(self, student_name: str, age: int, parent_name: str, contact_info: str, health_record: Dict):
        """
        Initializes the enrollment application with student and parent information.

        :param student_name: Name of the student
        :param age: Age of the student
        :param parent_name: Name of the parent or guardian
        :param contact_info: Contact information of the parent or guardian
        :param health_record: Universal Child Health Record form data
        """
        self.student_name = student_name
        self.age = age
        self.parent_name = parent_name
        self.contact_info = contact_info
        self.health_record = health_record

    def validate(self) -> List[str]:
        """
        Validates the enrollment application data.

        :return: A list of validation errors, if any
        """
        errors = []
        if not self.student_name:
            errors.append("Student name is required.")
        if not (5 <= self.age <= 18):
            errors.append("Age must be between 5 and 18.")
        if not self.parent_name:
            errors.append("Parent name is required.")
        if not self.contact_info:
            errors.append("Contact information is required.")
        if not self.health_record:
            errors.append("Health record is required.")
        return errors

    def to_dict(self) -> Dict:
        """
        Converts the enrollment application to a dictionary format.

        :return: A dictionary representation of the enrollment application
        """
        return {
            "student_name": self.student_name,
            "age": self.age,
            "parent_name": self.parent_name,
            "contact_info": self.contact_info,
            "health_record": self.health_record
        }

def save_application(application: EnrollmentApplication, filename: str) -> None:
    """
    Saves the enrollment application to a JSON file.

    :param application: The enrollment application to save
    :param filename: The name of the file to save the application to
    """
    try:
        with open(filename, 'w') as file:
            json.dump(application.to_dict(), file, indent=4)
        print(f"Application saved successfully to {filename}.")
    except IOError as e:
        print(f"Error saving application: {e}")

def main():
    """
    Main function to run the enrollment application process.
    """
    # Sample data for the enrollment application
    student_name = "John Doe"
    age = 10
    parent_name = "Jane Doe"
    contact_info = "jane.doe@example.com"
    health_record = {
        "immunizations": ["MMR", "DTP", "Polio"],
        "allergies": ["None"],
        "doctor_contact": "Dr. Smith, (555) 123-4567"
    }

    # Create an enrollment application instance
    application = EnrollmentApplication(student_name, age, parent_name, contact_info, health_record)

    # Validate the application
    validation_errors = application.validate()
    if validation_errors:
        print("Validation errors:")
        for error in validation_errors:
            print(f"- {error}")
    else:
        # Save the application if valid
        save_application(application, "enrollment_application.json")

if __name__ == "__main__":
    main()
```
