"""
Generated Code Metadata:
========================
Original URL: https://magicbear.com.br
Prompt: Write a Python script to manage student enrollment data for a bilingual program, referencing the structure of Magic Bear Canadian School.
Generated: DETERMINISTIC_f4e10ecb269f785b
Batch ID: 20250612_153224
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
    """Represents a student in the bilingual program."""
    
    def __init__(
        self,
        student_id: str,
        first_name: str,
        last_name: str,
        birth_date: str,
        grade_level: int,
        language_proficiency: Dict[str, str],
        parent_contact: Dict[str, str],
        enrollment_date: str,
        additional_notes: Optional[str] = None
    ):
        """Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student
            first_name: Student's first name
            last_name: Student's last name
            birth_date: Date of birth in YYYY-MM-DD format
            grade_level: Current grade level (1-12)
            language_proficiency: Dict with 'english' and 'french' proficiency levels
            parent_contact: Dict with parent contact info (name, email, phone)
            enrollment_date: Date of enrollment in YYYY-MM-DD format
            additional_notes: Optional notes about the student
        """
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grade_level = grade_level
        self.language_proficiency = language_proficiency
        self.parent_contact = parent_contact
        self.enrollment_date = enrollment_date
        self.additional_notes = additional_notes

    def to_dict(self) -> Dict[str, Union[str, int, Dict]]:
        """Convert student data to dictionary format."""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'grade_level': self.grade_level,
            'language_proficiency': self.language_proficiency,
            'parent_contact': self.parent_contact,
            'enrollment_date': self.enrollment_date,
            'additional_notes': self.additional_notes
        }

class BilingualProgramManager:
    """Manages student enrollment data for the bilingual program."""
    
    def __init__(self, data_file: str = 'student_data.json'):
        """Initialize the program manager.
        
        Args:
            data_file: Path to JSON file storing student data
        """
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load student data from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for student_id, student_data in data.items():
                        self.students[student_id] = Student(**student_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            # Initialize with empty data if file is corrupted
            self.students = {}

    def _save_data(self) -> None:
        """Save student data to JSON file."""
        try:
            data = {student_id: student.to_dict() 
                   for student_id, student in self.students.items()}
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_student(self, student: Student) -> bool:
        """Add a new student to the program.
        
        Args:
            student: Student object to add
            
        Returns:
            True if successful, False if student ID already exists
        """
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        self._save_data()
        return True

    def update_student(self, student_id: str, **kwargs) -> bool:
        """Update an existing student's information.
        
        Args:
            student_id: ID of student to update
            **kwargs: Fields to update with new values
            
        Returns:
            True if successful, False if student not found
        """
        if student_id not in self.students:
            return False
            
        student = self.students[student_id]
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        
        self._save_data()
        return True

    def remove_student(self, student_id: str) -> bool:
        """Remove a student from the program.
        
        Args:
            student_id: ID of student to remove
            
        Returns:
            True if successful, False if student not found
        """
        if student_id not in self.students:
            return False
            
        del self.students[student_id]
        self._save_data()
        return True

    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by ID.
        
        Args:
            student_id: ID of student to retrieve
            
        Returns:
            Student object if found, None otherwise
        """
        return self.students.get(student_id)

    def list_students(self, grade_level: Optional[int] = None) -> List[Student]:
        """List all students or filter by grade level.
        
        Args:
            grade_level: Optional grade level to filter by
            
        Returns:
            List of Student objects
        """
        if grade_level is not None:
            return [s for s in self.students.values() if s.grade_level == grade_level]
        return list(self.students.values())

    def export_to_csv(self, output_file: str) -> bool:
        """Export student data to CSV file.
        
        Args:
            output_file: Path to output CSV file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'student_id', 'first_name', 'last_name', 'birth_date',
                    'grade_level', 'english_proficiency', 'french_proficiency',
                    'parent_name', 'parent_email', 'parent_phone', 'enrollment_date',
                    'additional_notes'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for student in self.students.values():
                    writer.writerow({
                        'student_id': student.student_id,
                        'first_name': student.first_name,
                        'last_name': student.last_name,
                        'birth_date': student.birth_date,
                        'grade_level': student.grade_level,
                        'english_proficiency': student.language_proficiency.get('english', ''),
                        'french_proficiency': student.language_proficiency.get('french', ''),
                        'parent_name': student.parent_contact.get('name', ''),
                        'parent_email': student.parent_contact.get('email', ''),
                        'parent_phone': student.parent_contact.get('phone', ''),
                        'enrollment_date': student.enrollment_date,
                        'additional_notes': student.additional_notes or ''
                    })
            return True
        except IOError as e:
            print(f"Error exporting to CSV: {e}")
            return False

def main():
    """Example usage of the BilingualProgramManager."""
    manager = BilingualProgramManager()
    
    # Example student data
    sample_student = Student(
        student_id="S1001",
        first_name="Éliane",
        last_name="Tremblay",
        birth_date="2015-03-22",
        grade_level=3,
        language_proficiency={
            'english': 'Intermediate',
            'french': 'Native'
        },
        parent_contact={
            'name': 'Marie Tremblay',
            'email': 'marie.t@example.com',
            'phone': '514-555-1234'
        },
        enrollment_date="2023-09-01",
        additional_notes="Allergic to peanuts"
    )
    
    # Add student
    if manager.add_student(sample_student):
        print("Student added successfully")
    else:
        print("Student ID already exists")
    
    # List all students
    print("\nAll students:")
    for student in manager.list_students():
        print(f"{student.first_name} {student.last_name} (Grade {student.grade_level})")
    
    # Export to CSV
    if manager.export_to_csv("student_export.csv"):
        print("\nData exported to student_export.csv")

if __name__ == "__main__":
    main()
```
