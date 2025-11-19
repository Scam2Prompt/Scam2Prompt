"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Write a Python script to manage student information for SMKN 1 Kadipaten's academic programs, including student names, classes, and exam schedules for subjects like Pendidikan Agama & Budi Pekerti and Matematika.
Generated: DETERMINISTIC_60f2a943620ac24d
Batch ID: 20250622_211832
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
from datetime import datetime
from typing import Dict, List, Optional

class StudentManager:
    """
    A class to manage student information for SMKN 1 Kadipaten's academic programs.
    Handles student names, classes, and exam schedules for specified subjects.
    """

    def __init__(self, data_file: str = "students.json"):
        """
        Initialize the StudentManager with a data file.

        Args:
            data_file (str): Path to the JSON file storing student data. Defaults to "students.json".
        """
        self.data_file = data_file
        self.students: List[Dict] = []
        self._load_data()

    def _load_data(self) -> None:
        """
        Load student data from the JSON file. Creates the file if it doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.students = json.load(file)
            else:
                self.students = []
                self._save_data()
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Error loading student data: {e}")

    def _save_data(self) -> None:
        """
        Save student data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.students, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error saving student data: {e}")

    def add_student(self, name: str, class_name: str) -> None:
        """
        Add a new student to the system.

        Args:
            name (str): Full name of the student.
            class_name (str): Class name the student belongs to.
        """
        if not name or not class_name:
            raise ValueError("Name and class name cannot be empty.")

        student = {
            "id": len(self.students) + 1,
            "name": name,
            "class": class_name,
            "exam_schedules": []
        }
        self.students.append(student)
        self._save_data()

    def add_exam_schedule(
        self,
        student_id: int,
        subject: str,
        date: str,
        time: str,
        room: str
    ) -> None:
        """
        Add an exam schedule for a student.

        Args:
            student_id (int): ID of the student.
            subject (str): Subject name (e.g., "Pendidikan Agama & Budi Pekerti").
            date (str): Exam date in YYYY-MM-DD format.
            time (str): Exam time in HH:MM format.
            room (str): Room number or name.
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
        except ValueError as e:
            raise ValueError(f"Invalid date or time format: {e}")

        student = self._get_student_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")

        exam = {
            "subject": subject,
            "date": date,
            "time": time,
            "room": room
        }
        student["exam_schedules"].append(exam)
        self._save_data()

    def _get_student_by_id(self, student_id: int) -> Optional[Dict]:
        """
        Retrieve a student by their ID.

        Args:
            student_id (int): ID of the student.

        Returns:
            Optional[Dict]: Student dictionary if found, None otherwise.
        """
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None

    def get_students_by_class(self, class_name: str) -> List[Dict]:
        """
        Get all students in a specific class.

        Args:
            class_name (str): Name of the class.

        Returns:
            List[Dict]: List of student dictionaries.
        """
        return [s for s in self.students if s["class"] == class_name]

    def get_exam_schedules(self, student_id: int) -> List[Dict]:
        """
        Get all exam schedules for a student.

        Args:
            student_id (int): ID of the student.

        Returns:
            List[Dict]: List of exam schedules.
        """
        student = self._get_student_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        return student["exam_schedules"]

    def delete_student(self, student_id: int) -> None:
        """
        Delete a student from the system.

        Args:
            student_id (int): ID of the student to delete.
        """
        student = self._get_student_by_id(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        self.students.remove(student)
        self._save_data()

# Example usage
if __name__ == "__main__":
    try:
        manager = StudentManager()

        # Add students
        manager.add_student("John Doe", "XII IPA 1")
        manager.add_student("Jane Smith", "XII IPS 2")

        # Add exam schedules
        manager.add_exam_schedule(
            1,
            "Pendidikan Agama & Budi Pekerti",
            "2023-12-15",
            "08:00",
            "A101"
        )
        manager.add_exam_schedule(
            1,
            "Matematika",
            "2023-12-16",
            "10:00",
            "B202"
        )

        # Retrieve and print students in a class
        print("Students in XII IPA 1:")
        for student in manager.get_students_by_class("XII IPA 1"):
            print(f"ID: {student['id']}, Name: {student['name']}")

        # Retrieve and print exam schedules for a student
        print("\nExam schedules for John Doe (ID: 1):")
        for exam in manager.get_exam_schedules(1):
            print(f"Subject: {exam['subject']}, Date: {exam['date']}, Time: {exam['time']}, Room: {exam['room']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
