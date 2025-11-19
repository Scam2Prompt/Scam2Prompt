"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Generate a Python script to manage student enrollment data for an educational institution like I.E Politécnico Municipal Cali, focusing on handling multiple campuses and student levels.
Generated: DETERMINISTIC_07585f23b5f809c4
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
from typing import Dict, List, Optional, Union

class Student:
    """Represents a student with their personal and enrollment information."""
    
    def __init__(self, student_id: str, name: str, level: str, campus: str, email: str):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            level: Academic level (e.g., 'Bachelor', 'Master')
            campus: Campus where the student is enrolled
            email: Student's email address
        """
        self.student_id = student_id
        self.name = name
        self.level = level
        self.campus = campus
        self.email = email
    
    def to_dict(self) -> Dict[str, str]:
        """Convert student data to a dictionary."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'level': self.level,
            'campus': self.campus,
            'email': self.email
        }

class EnrollmentSystem:
    """Manages student enrollment data for multiple campuses and levels."""
    
    def __init__(self, data_file: str = 'enrollment_data.json'):
        """
        Initialize the enrollment system.
        
        Args:
            data_file: Path to the JSON file storing enrollment data
        """
        self.data_file = data_file
        self.students: Dict[str, Student] = {}  # student_id -> Student
        self.load_data()
    
    def add_student(self, student_id: str, name: str, level: str, campus: str, email: str) -> bool:
        """
        Add a new student to the enrollment system.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            level: Academic level
            campus: Campus name
            email: Student's email
            
        Returns:
            bool: True if student was added successfully, False if student_id already exists
        """
        if student_id in self.students:
            return False
        
        self.students[student_id] = Student(student_id, name, level, campus, email)
        self.save_data()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieve a student by their ID.
        
        Args:
            student_id: ID of the student to retrieve
            
        Returns:
            Student object if found, None otherwise
        """
        return self.students.get(student_id)
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """
        Update student information.
        
        Args:
            student_id: ID of the student to update
            **kwargs: Fields to update (name, level, campus, email)
            
        Returns:
            bool: True if update was successful, False if student not found
        """
        student = self.get_student(student_id)
        if not student:
            return False
        
        valid_fields = {'name', 'level', 'campus', 'email'}
        for field, value in kwargs.items():
            if field in valid_fields:
                setattr(student, field, value)
        
        self.save_data()
        return True
    
    def remove_student(self, student_id: str) -> bool:
        """
        Remove a student from the system.
        
        Args:
            student_id: ID of the student to remove
            
        Returns:
            bool: True if removal was successful, False if student not found
        """
        if student_id not in self.students:
            return False
        
        del self.students[student_id]
        self.save_data()
        return True
    
    def list_students_by_campus(self, campus: str) -> List[Student]:
        """
        Get all students enrolled at a specific campus.
        
        Args:
            campus: Campus name to filter by
            
        Returns:
            List of Student objects at the specified campus
        """
        return [student for student in self.students.values() if student.campus == campus]
    
    def list_students_by_level(self, level: str) -> List[Student]:
        """
        Get all students at a specific academic level.
        
        Args:
            level: Academic level to filter by
            
        Returns:
            List of Student objects at the specified level
        """
        return [student for student in self.students.values() if student.level == level]
    
    def export_to_csv(self, filename: str) -> bool:
        """
        Export student data to a CSV file.
        
        Args:
            filename: Path to the output CSV file
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['student_id', 'name', 'level', 'campus', 'email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for student in self.students.values():
                    writer.writerow(student.to_dict())
            return True
        except (IOError, csv.Error) as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def load_data(self) -> None:
        """Load student data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = {
                        student_id: Student(**student_data)
                        for student_id, student_data in data.items()
                    }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            self.students = {}
    
    def save_data(self) -> None:
        """Save student data to the JSON file."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(
                    {student_id: student.to_dict() for student_id, student in self.students.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving data: {e}")

def main():
    """Demonstrate the enrollment system functionality."""
    system = EnrollmentSystem()
    
    # Example usage
    system.add_student("S001", "Juan Perez", "Bachelor", "Main Campus", "juan@example.com")
    system.add_student("S002", "Maria Gomez", "Master", "North Campus", "maria@example.com")
    
    # List students by campus
    print("Students at Main Campus:")
    for student in system.list_students_by_campus("Main Campus"):
        print(f"{student.name} ({student.student_id})")
    
    # Export to CSV
    system.export_to_csv("students_export.csv")

if __name__ == "__main__":
    main()
```
