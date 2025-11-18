"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Develop a program using Python to manage online registration for school admissions, referencing the admission procedure described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_282479aa1bd34aea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class AdmissionManager:
    """Class to manage online school admissions."""

    def __init__(self, admission_data_file: str):
        """Initialize the AdmissionManager with a JSON data file."""
        self.admission_data_file = admission_data_file
        self.admissions = self.load_admissions()

    def load_admissions(self) -> List[Dict[str, Any]]:
        """Load admission data from a JSON file."""
        try:
            with open(self.admission_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Admission data file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Admission data file is not valid JSON.")
            return []

    def save_admissions(self) -> None:
        """Save admissions data back to the JSON file."""
        try:
            with open(self.admission_data_file, 'w') as file:
                json.dump(self.admissions, file, indent=4)
        except IOError as e:
            print(f"Error saving admissions data: {e}")

    def register_student(self, student_info: Dict[str, Any]) -> None:
        """Register a new student for admission."""
        if self.validate_student_info(student_info):
            self.admissions.append(student_info)
            self.save_admissions()
            print("Student registered successfully.")
        else:
            print("Error: Invalid student information provided.")

    def validate_student_info(self, student_info: Dict[str, Any]) -> bool:
        """Validate the provided student information."""
        required_fields = ['name', 'age', 'grade', 'parent_contact']
        for field in required_fields:
            if field not in student_info:
                return False
        return True

    def get_all_admissions(self) -> List[Dict[str, Any]]:
        """Retrieve the list of all registered admissions."""
        return self.admissions


def main():
    """Main function to run the AdmissionManager."""
    admission_manager = AdmissionManager('admissions.json')

    # Sample student registration
    sample_student = {
        'name': 'John Doe',
        'age': 15,
        'grade': '10th',
        'parent_contact': '9876543210'
    }

    admission_manager.register_student(sample_student)

    # Print all admissions
    print("Current Admissions:")
    for admission in admission_manager.get_all_admissions():
        print(admission)

if __name__ == "__main__":
    main()
```
