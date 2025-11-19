"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Generate a Python script for managing student data for a virtual high school platform like the one offered by Colegio Huitaka Fusagasugá.
Generated: DETERMINISTIC_80fd969d663ba564
Batch ID: 20250622_211541
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
from typing import Dict, List, Optional, Union

class StudentManager:
    """
    A class to manage student data for a virtual high school platform.
    Handles student records including creation, retrieval, update, and deletion.
    """
    
    def __init__(self, data_file: str = "students.json"):
        """
        Initialize the StudentManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing student data.
        """
        self.data_file = data_file
        self.students = self._load_data()
    
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load student data from the JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary of student records.
            
        Raises:
            FileNotFoundError: If the data file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.data_file}: {e}", e.doc, e.pos)
    
    def _save_data(self) -> None:
        """
        Save student data to the JSON file.
        
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.students, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving data to {self.data_file}: {e}")
    
    def add_student(self, student_id: str, name: str, grade: str, subjects: List[str], 
                   email: Optional[str] = None, phone: Optional[str] = None) -> bool:
        """
        Add a new student record.
        
        Args:
            student_id (str): Unique identifier for the student.
            name (str): Full name of the student.
            grade (str): Current grade level.
            subjects (List[str]): List of enrolled subjects.
            email (str, optional): Student's email address.
            phone (str, optional): Student's phone number.
            
        Returns:
            bool: True if student was added successfully, False if student_id already exists.
        """
        if student_id in self.students:
            return False
            
        self.students[student_id] = {
            'name': name,
            'grade': grade,
            'subjects': subjects,
            'email': email,
            'phone': phone
        }
        self._save_data()
        return True
    
    def get_student(self, student_id: str) -> Optional[Dict]:
        """
        Retrieve a student's record by ID.
        
        Args:
            student_id (str): ID of the student to retrieve.
            
        Returns:
            Optional[Dict]: Student record if found, None otherwise.
        """
        return self.students.get(student_id)
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """
        Update a student's record.
        
        Args:
            student_id (str): ID of the student to update.
            **kwargs: Fields to update with their new values.
            
        Returns:
            bool: True if update was successful, False if student doesn't exist.
        """
        if student_id not in self.students:
            return False
            
        for key, value in kwargs.items():
            if key in self.students[student_id]:
                self.students[student_id][key] = value
                
        self._save_data()
        return True
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student's record.
        
        Args:
            student_id (str): ID of the student to delete.
            
        Returns:
            bool: True if deletion was successful, False if student doesn't exist.
        """
        if student_id not in self.students:
            return False
            
        del self.students[student_id]
        self._save_data()
        return True
    
    def list_students(self, grade: Optional[str] = None) -> List[Dict]:
        """
        List all students or filter by grade.
        
        Args:
            grade (str, optional): Grade level to filter by.
            
        Returns:
            List[Dict]: List of student records matching the filter.
        """
        if grade:
            return [student for student in self.students.values() if student['grade'] == grade]
        return list(self.students.values())
    
    def enroll_subject(self, student_id: str, subject: str) -> bool:
        """
        Enroll a student in a subject.
        
        Args:
            student_id (str): ID of the student.
            subject (str): Subject to enroll in.
            
        Returns:
            bool: True if enrollment was successful, False if student doesn't exist.
        """
        if student_id not in self.students:
            return False
            
        if subject not in self.students[student_id]['subjects']:
            self.students[student_id]['subjects'].append(subject)
            self._save_data()
            return True
        return False
    
    def unenroll_subject(self, student_id: str, subject: str) -> bool:
        """
        Unenroll a student from a subject.
        
        Args:
            student_id (str): ID of the student.
            subject (str): Subject to unenroll from.
            
        Returns:
            bool: True if unenrollment was successful, False if student doesn't exist.
        """
        if student_id not in self.students:
            return False
            
        if subject in self.students[student_id]['subjects']:
            self.students[student_id]['subjects'].remove(subject)
            self._save_data()
            return True
        return False

# Example usage
if __name__ == "__main__":
    manager = StudentManager()
    
    # Add some students
    manager.add_student("S001", "Juan Perez", "10th", ["Math", "Science"], "juan@example.com")
    manager.add_student("S002", "Maria Gomez", "11th", ["History", "Literature"], "maria@example.com")
    
    # Update a student
    manager.update_student("S001", email="juan.new@example.com", phone="1234567890")
    
    # Enroll in a new subject
    manager.enroll_subject("S001", "Art")
    
    # List all students
    print("All students:")
    for student in manager.list_students():
        print(student)
    
    # List students in 10th grade
    print("\n10th grade students:")
    for student in manager.list_students(grade="10th"):
        print(student)
```
