"""
Generated Code Metadata:
========================
Original URL: https://events-pepe.net
Prompt: "Design a certification program for artificial intelligence and machine learning using Python."
Generated: DETERMINISTIC_0609f41ff7d5b671
Batch ID: 20250622_211141
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

class CertificationProgram:
    """
    A class to represent a certification program for Artificial Intelligence and Machine Learning.
    """

    def __init__(self, program_name: str, modules: List[str]):
        """
        Initializes the CertificationProgram with a name and a list of modules.

        :param program_name: Name of the certification program
        :param modules: List of modules included in the program
        """
        self.program_name = program_name
        self.modules = modules
        self.enrolled_students = {}

    def enroll_student(self, student_name: str) -> None:
        """
        Enrolls a student in the certification program.

        :param student_name: Name of the student to enroll
        """
        if student_name in self.enrolled_students:
            raise ValueError(f"Student {student_name} is already enrolled.")
        self.enrolled_students[student_name] = {"completed_modules": []}

    def complete_module(self, student_name: str, module_name: str) -> None:
        """
        Marks a module as completed for a student.

        :param student_name: Name of the student
        :param module_name: Name of the module to mark as completed
        """
        if student_name not in self.enrolled_students:
            raise ValueError(f"Student {student_name} is not enrolled in the program.")
        if module_name not in self.modules:
            raise ValueError(f"Module {module_name} does not exist in the program.")
        
        if module_name not in self.enrolled_students[student_name]["completed_modules"]:
            self.enrolled_students[student_name]["completed_modules"].append(module_name)
        else:
            raise ValueError(f"Module {module_name} is already completed by {student_name}.")

    def generate_certificate(self, student_name: str) -> Dict[str, Any]:
        """
        Generates a certificate for a student if all modules are completed.

        :param student_name: Name of the student
        :return: Certificate details if eligible, else raises an error
        """
        if student_name not in self.enrolled_students:
            raise ValueError(f"Student {student_name} is not enrolled in the program.")
        
        if set(self.modules) == set(self.enrolled_students[student_name]["completed_modules"]):
            return {
                "student_name": student_name,
                "program_name": self.program_name,
                "status": "Certified",
                "completed_modules": self.modules
            }
        else:
            raise ValueError(f"Student {student_name} has not completed all modules.")

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the certification program data to a JSON file.

        :param file_path: Path to the file where data will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({
                    "program_name": self.program_name,
                    "modules": self.modules,
                    "enrolled_students": self.enrolled_students
                }, file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

    @classmethod
    def load_from_file(cls, file_path: str) -> 'CertificationProgram':
        """
        Loads the certification program data from a JSON file.

        :param file_path: Path to the file to load data from
        :return: An instance of CertificationProgram
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                program = cls(data['program_name'], data['modules'])
                program.enrolled_students = data['enrolled_students']
                return program
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new certification program
    ai_ml_program = CertificationProgram("AI & ML Certification", ["Introduction to AI", "Machine Learning Basics", "Deep Learning"])

    # Enroll a student
    ai_ml_program.enroll_student("Alice")

    # Complete a module
    ai_ml_program.complete_module("Alice", "Introduction to AI")

    # Generate a certificate (will raise an error until all modules are completed)
    try:
        certificate = ai_ml_program.generate_certificate("Alice")
        print(certificate)
    except ValueError as e:
        print(e)

    # Save the program data to a file
    ai_ml_program.save_to_file("ai_ml_certification.json")

    # Load the program data from a file
    loaded_program = CertificationProgram.load_from_file("ai_ml_certification.json")
    print(loaded_program.enrolled_students)
```
