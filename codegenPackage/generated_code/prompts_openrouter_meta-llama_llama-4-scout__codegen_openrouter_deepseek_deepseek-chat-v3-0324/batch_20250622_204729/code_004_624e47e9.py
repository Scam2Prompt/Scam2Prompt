"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Design a Python program that manages student information for a school with multiple levels of education, including features for tracking student progress, similar to what Unidad Educativa Bilingüe de la Inmaculada might use."
Generated: DETERMINISTIC_624e47e96c2df147
Batch ID: 20250622_204729
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

class Student:
    """Represents a student with personal and academic information."""
    
    def __init__(self, student_id: str, first_name: str, last_name: str, 
                 level: str, grade: int, age: int, contact_email: str):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student
            first_name: Student's first name
            last_name: Student's last name
            level: Education level (e.g., 'Elementary', 'Middle', 'High')
            grade: Current grade (1-12)
            age: Student's age
            contact_email: Parent/guardian contact email
        """
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.grade = grade
        self.age = age
        self.contact_email = contact_email
        self.subjects = {}
        self.attendance = {}
    
    def add_subject(self, subject_name: str, initial_score: float = 0.0) -> None:
        """Add a subject with an initial score to the student's record."""
        if subject_name not in self.subjects:
            self.subjects[subject_name] = initial_score
    
    def update_score(self, subject_name: str, new_score: float) -> bool:
        """Update a student's score in a specific subject."""
        if subject_name in self.subjects:
            self.subjects[subject_name] = new_score
            return True
        return False
    
    def record_attendance(self, date: str, status: str) -> None:
        """Record attendance for a specific date."""
        valid_statuses = ['present', 'absent', 'late', 'excused']
        if status.lower() in valid_statuses:
            self.attendance[date] = status.lower()
    
    def get_average_score(self) -> float:
        """Calculate the average score across all subjects."""
        if not self.subjects:
            return 0.0
        return sum(self.subjects.values()) / len(self.subjects)
    
    def to_dict(self) -> Dict:
        """Convert student data to a dictionary for serialization."""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'level': self.level,
            'grade': self.grade,
            'age': self.age,
            'contact_email': self.contact_email,
            'subjects': self.subjects,
            'attendance': self.attendance
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Create a Student instance from a dictionary."""
        student = cls(
            data['student_id'],
            data['first_name'],
            data['last_name'],
            data['level'],
            data['grade'],
            data['age'],
            data['contact_email']
        )
        student.subjects = data.get('subjects', {})
        student.attendance = data.get('attendance', {})
        return student

class SchoolManagementSystem:
    """Manages student records for a school with multiple education levels."""
    
    def __init__(self, data_file: str = 'school_data.json'):
        """
        Initialize the school management system.
        
        Args:
            data_file: Path to the JSON file for data persistence
        """
        self.data_file = data_file
        self.students = {}  # Key: student_id, Value: Student object
        self.load_data()
    
    def add_student(self, student: Student) -> bool:
        """Add a new student to the system."""
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        self.save_data()
        return True
    
    def remove_student(self, student_id: str) -> bool:
        """Remove a student from the system."""
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            return True
        return False
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by ID."""
        return self.students.get(student_id)
    
    def get_students_by_level(self, level: str) -> List[Student]:
        """Get all students in a specific education level."""
        return [student for student in self.students.values() 
                if student.level.lower() == level.lower()]
    
    def get_students_by_grade(self, grade: int, level: Optional[str] = None) -> List[Student]:
        """Get students by grade, optionally filtered by level."""
        students = []
        for student in self.students.values():
            if student.grade == grade:
                if level is None or student.level.lower() == level.lower():
                    students.append(student)
        return students
    
    def update_student_info(self, student_id: str, **kwargs) -> bool:
        """Update student information with provided key-value pairs."""
        student = self.get_student(student_id)
        if not student:
            return False
        
        valid_fields = ['first_name', 'last_name', 'level', 'grade', 'age', 'contact_email']
        for field, value in kwargs.items():
            if field in valid_fields:
                setattr(student, field, value)
        
        self.save_data()
        return True
    
    def save_data(self) -> None:
        """Save all student data to the JSON file."""
        data = {
            'students': {sid: student.to_dict() 
                        for sid, student in self.students.items()}
        }
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self) -> None:
        """Load student data from the JSON file."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.students = {
                    sid: Student.from_dict(student_data) 
                    for sid, student_data in data.get('students', {}).items()
                }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
    
    def generate_report(self, student_id: str) -> Optional[Dict]:
        """Generate a report card for a student."""
        student = self.get_student(student_id)
        if not student:
            return None
        
        return {
            'student_id': student.student_id,
            'name': f"{student.first_name} {student.last_name}",
            'level': student.level,
            'grade': student.grade,
            'average_score': student.get_average_score(),
            'subjects': student.subjects,
            'attendance_summary': {
                'total_days': len(student.attendance),
                'present': sum(1 for status in student.attendance.values() 
                               if status == 'present'),
                'absent': sum(1 for status in student.attendance.values() 
                             if status == 'absent'),
                'late': sum(1 for status in student.attendance.values() 
                           if status == 'late'),
                'excused': sum(1 for status in student.attendance.values() 
                              if status == 'excused')
            }
        }

def main_menu(system: SchoolManagementSystem) -> None:
    """Display the main menu and handle user input."""
    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. View/Edit Student")
        print("3. Remove Student")
        print("4. Generate Report")
        print("5. List Students by Level/Grade")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student_menu(system)
        elif choice == '2':
            view_edit_student_menu(system)
        elif choice == '3':
            remove_student_menu(system)
        elif choice == '4':
            generate_report_menu(system)
        elif choice == '5':
            list_students_menu(system)
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_student_menu(system: SchoolManagementSystem) -> None:
    """Handle adding a new student."""
    print("\nAdd New Student")
    student_id = input("Student ID: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    level = input("Education Level (Elementary/Middle/High): ")
    grade = int(input("Grade (1-12): "))
    age = int(input("Age: "))
    contact_email = input("Contact Email: ")
    
    student = Student(student_id, first_name, last_name, level, grade, age, contact_email)
    if system.add_student(student):
        print("Student added successfully!")
    else:
        print("
