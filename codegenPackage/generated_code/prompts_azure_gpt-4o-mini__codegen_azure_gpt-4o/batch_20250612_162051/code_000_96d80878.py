"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Generate a Python script that utilizes the "Pomoćnici u nastavi" program features from Udruga Radost Ogulin to support educational initiatives.
Generated: DETERMINISTIC_96d80878df837cd3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python Script: Pomoćnici u nastavi Program Support
This script is designed to support educational initiatives inspired by the "Pomoćnici u nastavi" program 
from Udruga Radost Ogulin. It includes features for managing assistants, tracking student progress, 
and generating reports.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='program_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Assistant:
    """
    Represents a teaching assistant in the program.
    """
    def __init__(self, name, email, skills):
        """
        Initialize an Assistant object.

        :param name: Name of the assistant
        :param email: Email address of the assistant
        :param skills: List of skills the assistant possesses
        """
        self.name = name
        self.email = email
        self.skills = skills

    def to_dict(self):
        """
        Convert the Assistant object to a dictionary for serialization.

        :return: Dictionary representation of the Assistant
        """
        return {
            "name": self.name,
            "email": self.email,
            "skills": self.skills
        }


class Student:
    """
    Represents a student in the program.
    """
    def __init__(self, name, grade, needs):
        """
        Initialize a Student object.

        :param name: Name of the student
        :param grade: Grade level of the student
        :param needs: List of educational needs
        """
        self.name = name
        self.grade = grade
        self.needs = needs
        self.progress = []

    def add_progress(self, date, notes):
        """
        Add a progress entry for the student.

        :param date: Date of the progress update
        :param notes: Notes about the progress
        """
        self.progress.append({"date": date, "notes": notes})

    def to_dict(self):
        """
        Convert the Student object to a dictionary for serialization.

        :return: Dictionary representation of the Student
        """
        return {
            "name": self.name,
            "grade": self.grade,
            "needs": self.needs,
            "progress": self.progress
        }


class ProgramManager:
    """
    Manages the "Pomoćnici u nastavi" program.
    """
    def __init__(self):
        """
        Initialize the ProgramManager with empty lists for assistants and students.
        """
        self.assistants = []
        self.students = []

    def add_assistant(self, assistant):
        """
        Add a teaching assistant to the program.

        :param assistant: Assistant object to add
        """
        if not isinstance(assistant, Assistant):
            raise TypeError("Expected an Assistant object.")
        self.assistants.append(assistant)
        logging.info(f"Assistant added: {assistant.name}")

    def add_student(self, student):
        """
        Add a student to the program.

        :param student: Student object to add
        """
        if not isinstance(student, Student):
            raise TypeError("Expected a Student object.")
        self.students.append(student)
        logging.info(f"Student added: {student.name}")

    def generate_report(self, filename="program_report.json"):
        """
        Generate a report of the program's data and save it to a file.

        :param filename: Name of the file to save the report
        """
        try:
            data = {
                "assistants": [assistant.to_dict() for assistant in self.assistants],
                "students": [student.to_dict() for student in self.students]
            }
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Report generated: {filename}")
        except Exception as e:
            logging.error(f"Failed to generate report: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the program manager
        manager = ProgramManager()

        # Add assistants
        assistant1 = Assistant("Ana Horvat", "ana.horvat@example.com", ["Math", "Science"])
        assistant2 = Assistant("Ivan Novak", "ivan.novak@example.com", ["History", "Literature"])
        manager.add_assistant(assistant1)
        manager.add_assistant(assistant2)

        # Add students
        student1 = Student("Marko Perić", "5th Grade", ["Math Support"])
        student2 = Student("Lucija Kovač", "6th Grade", ["Literature Support"])
        student1.add_progress(datetime.now().strftime("%Y-%m-%d"), "Improved in multiplication.")
        student2.add_progress(datetime.now().strftime("%Y-%m-%d"), "Completed reading assignment.")
        manager.add_student(student1)
        manager.add_student(student2)

        # Generate report
        manager.generate_report()

        print("Program executed successfully. Check the log and report file for details.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
```
