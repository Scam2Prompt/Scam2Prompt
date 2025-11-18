"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Develop a Python script to manage a school transportation system, inspired by the transportation service offered by Del Sol Montessori.
Generated: DETERMINISTIC_be900be1f7fbbb95
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Student:
    """Represents a student with a name and assigned pickup location."""

    def __init__(self, name: str, pickup_location: str):
        self.name = name
        self.pickup_location = pickup_location

    def to_dict(self) -> Dict[str, str]:
        """Convert the Student object to a dictionary."""
        return {
            "name": self.name,
            "pickup_location": self.pickup_location
        }


class TransportationService:
    """Manages transportation for students."""

    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, name: str, pickup_location: str) -> None:
        """Add a new student to the transportation service."""
        if not name or not pickup_location:
            raise ValueError("Both name and pickup location must be provided.")
        student = Student(name, pickup_location)
        self.students.append(student)
        print(f"Added student: {student.to_dict()}")

    def remove_student(self, name: str) -> None:
        """Remove a student from the transportation service by name."""
        before_count = len(self.students)
        self.students = [student for student in self.students if student.name != name]
        if len(self.students) == before_count:
            raise ValueError(f"No student found with name: {name}")
        print(f"Removed student: {name}")

    def list_students(self) -> List[Dict[str, str]]:
        """Return a list of all students in the transportation service."""
        return [student.to_dict() for student in self.students]

    def save_to_file(self, filename: str) -> None:
        """Save the list of students to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_students(), file)
            print(f"Saved students to {filename}")
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load students from a JSON file."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                self.students = [Student(**data) for data in students_data]
            print(f"Loaded students from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading the file: {e}")

def main():
    """Main function to run the transportation service."""
    service = TransportationService()

    # Example usage
    try:
        service.add_student("Alice Smith", "123 Elm St")
        service.add_student("Bob Johnson", "456 Oak St")
        
        print("Current students:")
        print(service.list_students())
        
        service.save_to_file("students.json")
        
        service.remove_student("Alice Smith")
        
        print("Current students after removal:")
        print(service.list_students())
        
        service.load_from_file("students.json")
        
        print("Students after reloading:")
        print(service.list_students())
        
    except ValueError as ve:
        print(f"ValueError: {ve}")

if __name__ == "__main__":
    main()
```
