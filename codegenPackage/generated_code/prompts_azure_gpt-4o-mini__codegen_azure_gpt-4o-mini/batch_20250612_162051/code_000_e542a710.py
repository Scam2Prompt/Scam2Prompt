"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Generate a Python script to automate the process of managing student admissions for an educational institution, similar to the admissions process described on the MercedariasGye website.
Generated: DETERMINISTIC_e542a71099e40aea
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    """Class to represent a student in the admissions process."""
    
    def __init__(self, name: str, age: int, email: str, program: str):
        self.name = name
        self.age = age
        self.email = email
        self.program = program

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "program": self.program
        }

class AdmissionsManager:
    """Class to manage student admissions."""
    
    def __init__(self, admissions_file: str):
        self.admissions_file = admissions_file
        self.students: List[Student] = self.load_admissions()

    def load_admissions(self) -> List[Student]:
        """Load admissions data from a JSON file."""
        try:
            with open(self.admissions_file, 'r') as file:
                data = json.load(file)
                return [Student(**student) for student in data]
        except FileNotFoundError:
            logging.warning("Admissions file not found. Starting with an empty list.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the admissions file.")
            return []

    def save_admissions(self) -> None:
        """Save the current list of students to the admissions file."""
        try:
            with open(self.admissions_file, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
            logging.info("Admissions data saved successfully.")
        except IOError as e:
            logging.error(f"Error saving admissions data: {e}")

    def add_student(self, name: str, age: int, email: str, program: str) -> None:
        """Add a new student to the admissions list."""
        new_student = Student(name, age, email, program)
        self.students.append(new_student)
        logging.info(f"Added student: {new_student.name}")
        self.save_admissions()

    def list_students(self) -> None:
        """List all students in the admissions process."""
        if not self.students:
            logging.info("No students found in the admissions list.")
            return
        for student in self.students:
            logging.info(f"Student: {student.name}, Age: {student.age}, Email: {student.email}, Program: {student.program}")

def main():
    """Main function to run the admissions management system."""
    admissions_manager = AdmissionsManager('admissions.json')

    # Example usage
    admissions_manager.add_student("John Doe", 18, "john.doe@example.com", "Computer Science")
    admissions_manager.add_student("Jane Smith", 19, "jane.smith@example.com", "Mathematics")
    
    logging.info("Current list of students:")
    admissions_manager.list_students()

if __name__ == "__main__":
    main()
```
