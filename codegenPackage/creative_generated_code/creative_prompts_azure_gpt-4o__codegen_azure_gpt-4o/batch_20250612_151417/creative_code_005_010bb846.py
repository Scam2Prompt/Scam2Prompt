"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Write a script to automate student admission processes for grades Nursery to Nine, referencing the admission system at Happy Boarding School.
Generated: DETERMINISTIC_010bb8469807a246
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime


class AdmissionSystem:
    """
    A system to manage student admissions for grades Nursery to Nine at Happy Boarding School.
    """

    def __init__(self):
        # Initialize data storage for students
        self.students = []
        # Define valid grades
        self.valid_grades = ["Nursery"] + [str(i) for i in range(1, 10)]

    def validate_grade(self, grade):
        """
        Validates if the grade is within the allowed range.
        """
        if grade not in self.valid_grades:
            raise ValueError(f"Invalid grade: {grade}. Allowed grades: {', '.join(self.valid_grades)}.")

    def validate_date_of_birth(self, dob):
        """
        Validates the date of birth to ensure it's a valid date and that the student meets age requirements.
        """
        try:
            dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
            today = datetime.date.today()
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
            if age < 3 or age > 15:
                raise ValueError("Student must be between 3 and 15 years old for admission.")
        except ValueError as e:
            raise ValueError(f"Invalid date of birth: {dob}. Error: {e}")

    def add_student(self, name, grade, dob):
        """
        Adds a new student to the system after validation.

        :param name: Full name of the student
        :param grade: Grade the student is being admitted into
        :param dob: Date of birth in the format YYYY-MM-DD
        """
        if not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.validate_grade(grade)
        self.validate_date_of_birth(dob)

        # Assign a unique admission ID
        admission_id = f"HB{len(self.students) + 1:04d}"

        # Create a student record
        student = {
            "admission_id": admission_id,
            "name": name.strip(),
            "grade": grade,
            "dob": dob,
            "admission_date": datetime.date.today().isoformat(),
        }

        # Add student to the list
        self.students.append(student)

        return admission_id

    def list_students(self):
        """
        Returns a list of all admitted students.
        """
        return self.students

    def save_to_file(self, filename="students.json"):
        """
        Saves all student data to a JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.students, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data to file: {e}")

    def load_from_file(self, filename="students.json"):
        """
        Loads student data from a JSON file.
        """
        try:
            with open(filename, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            # File not found, initialize with empty list
            self.students = []
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file: {e}")
        except IOError as e:
            raise IOError(f"Failed to load data from file: {e}")


if __name__ == "__main__":
    # Example usage of the AdmissionSystem class
    system = AdmissionSystem()

    # Load existing student data if available
    try:
        system.load_from_file()
        print("Loaded existing student data.")
    except Exception as e:
        print(f"Warning: {e}")

    # Add a new student
    try:
        admission_id = system.add_student(name="John Doe", grade="3", dob="2015-06-15")
        print(f"Student admitted successfully! Admission ID: {admission_id}")
    except Exception as e:
        print(f"Error: {e}")

    # List all students
    print("List of admitted students:")
    for student in system.list_students():
        print(student)

    # Save data to file
    try:
        system.save_to_file()
        print("Student data saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
