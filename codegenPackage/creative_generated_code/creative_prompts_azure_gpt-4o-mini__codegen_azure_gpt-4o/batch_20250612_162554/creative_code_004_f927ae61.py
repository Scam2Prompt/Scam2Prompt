"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevmtrustline.info
Prompt: Design a library in Python that helps manage student records for an elementary school, focusing on features like enrollment tracking and academic performance, similar to the academic focus of Excellence Elementary School.
Generated: DETERMINISTIC_f927ae61f27ce586
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Library for Managing Student Records - Enrollment Tracking and Academic Performance
Designed for use in an elementary school setting.
"""

import json
import os

class StudentRecordManager:
    """
    A library for managing student records at an elementary school.
    Features:
    - Enrollment tracking
    - Academic performance tracking
    """

    def __init__(self, data_file='students.json'):
        """
        Initialize the manager with an optional file for persistent storage.
        
        :param data_file: Path to the JSON file where student records will be saved.
        """
        self.data_file = data_file
        self.students = {}
        self._load_data()

    def _load_data(self):
        """
        Load student records from the JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.students = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Failed to load existing data. Starting with empty records.")
                self.students = {}

    def _save_data(self):
        """
        Save student records to the JSON file for persistent storage.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.students, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def enroll_student(self, student_id, name, grade):
        """
        Enroll a new student.
        
        :param student_id: Unique identifier for the student.
        :param name: Name of the student.
        :param grade: Grade the student is enrolled in.
        :raises ValueError: If the student ID is already in use.
        """
        if student_id in self.students:
            raise ValueError(f"A student with ID {student_id} is already enrolled.")
        
        self.students[student_id] = {
            'name': name,
            'grade': grade,
            'performance': {}
        }
        self._save_data()

    def update_performance(self, student_id, subject, score):
        """
        Update the academic performance for a student.
        
        :param student_id: Unique identifier for the student.
        :param subject: Subject name (e.g., "Math", "Science").
        :param score: Numeric score for the subject.
        :raises KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError(f"No student found with ID {student_id}.")
        
        self.students[student_id]['performance'][subject] = score
        self._save_data()

    def get_student_record(self, student_id):
        """
        Retrieve the record of a specific student.
        
        :param student_id: Unique identifier for the student.
        :return: Dictionary containing the student's details.
        :raises KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError(f"No student found with ID {student_id}.")
        
        return self.students[student_id]

    def remove_student(self, student_id):
        """
        Remove a student from the records.
        
        :param student_id: Unique identifier for the student.
        :raises KeyError: If the student ID does not exist.
        """
        if student_id not in self.students:
            raise KeyError(f"No student found with ID {student_id}.")
        
        del self.students[student_id]
        self._save_data()

    def list_students(self):
        """
        List all students currently enrolled.
        
        :return: A list of dictionaries containing basic details of all students.
        """
        return [{'id': student_id, 'name': info['name'], 'grade': info['grade']} 
                for student_id, info in self.students.items()]


# Example usage (not part of the library):
if __name__ == "__main__":
    manager = StudentRecordManager()
    
    # Enroll students
    try:
        manager.enroll_student("001", "Alice Smith", "Grade 4")
        manager.enroll_student("002", "Bob Johnson", "Grade 5")
    except ValueError as e:
        print(e)
    
    # Update performance
    try:
        manager.update_performance("001", "Math", 95)
        manager.update_performance("002", "Science", 88)
    except KeyError as e:
        print(e)
    
    # Retrieve student records
    try:
        print(manager.get_student_record("001"))
        print(manager.get_student_record("002"))
    except KeyError as e:
        print(e)
    
    # List all students
    print(manager.list_students())
    
    # Remove a student
    try:
        manager.remove_student("002")
    except KeyError as e:
        print(e)
    
    # List students after removal
    print(manager.list_students())
```
