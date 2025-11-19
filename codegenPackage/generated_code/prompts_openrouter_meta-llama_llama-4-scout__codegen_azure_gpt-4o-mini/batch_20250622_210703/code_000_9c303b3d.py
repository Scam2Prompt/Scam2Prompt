"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Write a Python script to manage a simple preschool database, including information about teachers, students, and daily activities.
Generated: DETERMINISTIC_9c303b3d454188b1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class PreschoolDatabase:
    def __init__(self, db_file: str):
        """
        Initializes the PreschoolDatabase with a specified JSON file.
        
        :param db_file: Path to the JSON file that stores the database.
        """
        self.db_file = db_file
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        """
        Loads the database from a JSON file.
        
        :return: A dictionary containing the database data.
        """
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"teachers": [], "students": [], "activities": []}
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted or invalid.")
            return {"teachers": [], "students": [], "activities": []}

    def save_data(self) -> None:
        """
        Saves the current database to the JSON file.
        """
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_teacher(self, teacher: Dict[str, Any]) -> None:
        """
        Adds a new teacher to the database.
        
        :param teacher: A dictionary containing teacher information.
        """
        self.data['teachers'].append(teacher)
        self.save_data()

    def add_student(self, student: Dict[str, Any]) -> None:
        """
        Adds a new student to the database.
        
        :param student: A dictionary containing student information.
        """
        self.data['students'].append(student)
        self.save_data()

    def add_activity(self, activity: Dict[str, Any]) -> None:
        """
        Adds a new activity to the database.
        
        :param activity: A dictionary containing activity information.
        """
        self.data['activities'].append(activity)
        self.save_data()

    def get_teachers(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of teachers.
        
        :return: A list of dictionaries containing teacher information.
        """
        return self.data['teachers']

    def get_students(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of students.
        
        :return: A list of dictionaries containing student information.
        """
        return self.data['students']

    def get_activities(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of activities.
        
        :return: A list of dictionaries containing activity information.
        """
        return self.data['activities']

if __name__ == "__main__":
    # Example usage of the PreschoolDatabase
    db = PreschoolDatabase('preschool_db.json')

    # Adding a teacher
    db.add_teacher({"name": "Alice Smith", "subject": "Art", "experience": 5})

    # Adding a student
    db.add_student({"name": "John Doe", "age": 4, "parent_contact": "555-1234"})

    # Adding an activity
    db.add_activity({"name": "Painting", "date": "2023-10-01", "participants": ["John Doe", "Jane Doe"]})

    # Retrieving and printing all teachers, students, and activities
    print("Teachers:", db.get_teachers())
    print("Students:", db.get_students())
    print("Activities:", db.get_activities())
```
