"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a Python code snippet to manage student information for a technical school in Iran, including fields for student name, ID, and رشته تحصیلی (field of study).
Generated: DETERMINISTIC_b9bf8768d2f18bad
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Student Information Management System for Iranian Technical Schools
"""

import json
import os
from typing import Dict, List, Optional

class Student:
    """Represents a student with their personal and academic information."""
    
    def __init__(self, name: str, student_id: str, field_of_study: str):
        """
        Initialize a Student object.
        
        Args:
            name: Full name of the student
            student_id: Unique identifier for the student
            field_of_study: رشته تحصیلی (major/field of study)
        """
        self.name = name
        self.student_id = student_id
        self.field_of_study = field_of_study
    
    def to_dict(self) -> Dict:
        """Convert student object to dictionary for serialization."""
        return {
            'name': self.name,
            'student_id': self.student_id,
            'field_of_study': self.field_of_study
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Create Student object from dictionary."""
        return cls(
            name=data['name'],
            student_id=data['student_id'],
            field_of_study=data['field_of_study']
        )

class StudentManager:
    """Manages student records with CRUD operations."""
    
    def __init__(self, file_path: str = 'students.json'):
        """
        Initialize StudentManager with storage file.
        
        Args:
            file_path: Path to JSON file for storing student data
        """
        self.file_path = file_path
        self.students: Dict[str, Student] = {}
        self._load_students()
    
    def _load_students(self) -> None:
        """Load student data from JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = {
                        student_id: Student.from_dict(student_data)
                        for student_id, student_data in data.items()
                    }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading student data: {e}")
            self.students = {}
    
    def _save_students(self) -> None:
        """Save student data to JSON file."""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(
                    {sid: student.to_dict() for sid, student in self.students.items()},
                    f,
                    ensure_ascii=False,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving student data: {e}")
    
    def add_student(self, name: str, student_id: str, field_of_study: str) -> bool:
        """
        Add a new student to the system.
        
        Args:
            name: Student's full name
            student_id: Unique student ID
            field_of_study: رشته تحصیلی
            
        Returns:
            bool: True if student was added successfully, False if student ID already exists
        """
        if student_id in self.students:
            return False
        
        self.students[student_id] = Student(name, student_id, field_of_study)
        self._save_students()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieve a student by ID.
        
        Args:
            student_id: ID of the student to retrieve
            
        Returns:
            Optional[Student]: Student object if found, None otherwise
        """
        return self.students.get(student_id)
    
    def update_student(self, student_id: str, name: str = None, field_of_study: str = None) -> bool:
        """
        Update student information.
        
        Args:
            student_id: ID of the student to update
            name: New name (optional)
            field_of_study: New field of study (optional)
            
        Returns:
            bool: True if student was updated, False if student not found
        """
        if student_id not in self.students:
            return False
        
        student = self.students[student_id]
        if name:
            student.name = name
        if field_of_study:
            student.field_of_study = field_of_study
        
        self._save_students()
        return True
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student from the system.
        
        Args:
            student_id: ID of the student to delete
            
        Returns:
            bool: True if student was deleted, False if student not found
        """
        if student_id not in self.students:
            return False
        
        del self.students[student_id]
        self._save_students()
        return True
    
    def list_students(self) -> List[Dict]:
        """
        Get list of all students.
        
        Returns:
            List[Dict]: List of student dictionaries
        """
        return [student.to_dict() for student in self.students.values()]
    
    def search_students(self, name: str = None, field_of_study: str = None) -> List[Dict]:
        """
        Search for students by name and/or field of study.
        
        Args:
            name: Name to search for (partial match)
            field_of_study: Field of study to search for (exact match)
            
        Returns:
            List[Dict]: List of matching student dictionaries
        """
        results = []
        for student in self.students.values():
            match = True
            if name and name.lower() not in student.name.lower():
                match = False
            if field_of_study and field_of_study != student.field_of_study:
                match = False
            if match:
                results.append(student.to_dict())
        return results

# Example usage
if __name__ == "__main__":
    manager = StudentManager()
    
    # Add sample students
    manager.add_student("علی محمدی", "98012345", "کامپیوتر")
    manager.add_student("فاطمه احمدی", "98012346", "برق")
    manager.add_student("رضا حسینی", "98012347", "مکانیک")
    
    # List all students
    print("All Students:")
    for student in manager.list_students():
        print(student)
    
    # Search students
    print("\nComputer Students:")
    for student in manager.search_students(field_of_study="کامپیوتر"):
        print(student)
```
