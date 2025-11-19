"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Write a program to manage student information for a school like Ace Higher Secondary School.
Generated: DETERMINISTIC_a3390649284555f1
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
import os
from typing import Dict, List, Optional

class Student:
    """Represents a student with personal and academic information."""
    
    def __init__(self, student_id: str, name: str, age: int, grade: str, subjects: List[str], address: str, contact_number: str):
        """
        Initialize a Student object.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            age: Age of the student
            grade: Current grade/class of the student
            subjects: List of subjects the student is enrolled in
            address: Residential address of the student
            contact_number: Contact number of the student or guardian
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
        self.address = address
        self.contact_number = contact_number
    
    def to_dict(self) -> Dict:
        """Convert Student object to dictionary for serialization."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'subjects': self.subjects,
            'address': self.address,
            'contact_number': self.contact_number
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Create Student object from dictionary."""
        return cls(
            student_id=data['student_id'],
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
            subjects=data['subjects'],
            address=data['address'],
            contact_number=data['contact_number']
        )

class StudentManagementSystem:
    """Manages student records for a school."""
    
    def __init__(self, data_file: str = 'students.json'):
        """
        Initialize the student management system.
        
        Args:
            data_file: Path to JSON file storing student data
        """
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.load_students()
    
    def add_student(self, student: Student) -> bool:
        """
        Add a new student to the system.
        
        Args:
            student: Student object to add
            
        Returns:
            bool: True if successful, False if student ID already exists
        """
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        self.save_students()
        return True
    
    def update_student(self, student_id: str, updated_info: Dict) -> bool:
        """
        Update existing student information.
        
        Args:
            student_id: ID of student to update
            updated_info: Dictionary with fields to update
            
        Returns:
            bool: True if successful, False if student not found
        """
        if student_id not in self.students:
            return False
        
        student = self.students[student_id]
        for key, value in updated_info.items():
            if hasattr(student, key):
                setattr(student, key, value)
        
        self.save_students()
        return True
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student from the system.
        
        Args:
            student_id: ID of student to delete
            
        Returns:
            bool: True if successful, False if student not found
        """
        if student_id not in self.students:
            return False
        
        del self.students[student_id]
        self.save_students()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieve a student by ID.
        
        Args:
            student_id: ID of student to retrieve
            
        Returns:
            Student: Student object if found, None otherwise
        """
        return self.students.get(student_id)
    
    def get_all_students(self) -> List[Student]:
        """Return list of all students in the system."""
        return list(self.students.values())
    
    def search_students(self, search_term: str, search_field: str = 'name') -> List[Student]:
        """
        Search students by field.
        
        Args:
            search_term: Term to search for
            search_field: Field to search in ('name', 'grade', etc.)
            
        Returns:
            List[Student]: Matching students
        """
        results = []
        for student in self.students.values():
            field_value = getattr(student, search_field, None)
            if field_value and search_term.lower() in str(field_value).lower():
                results.append(student)
        return results
    
    def save_students(self) -> bool:
        """
        Save student data to file.
        
        Returns:
            bool: True if successful, False if error occurs
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(
                    {sid: student.to_dict() for sid, student in self.students.items()},
                    f,
                    indent=4
                )
            return True
        except Exception as e:
            print(f"Error saving student data: {e}")
            return False
    
    def load_students(self) -> bool:
        """
        Load student data from file.
        
        Returns:
            bool: True if successful, False if error occurs
        """
        if not os.path.exists(self.data_file):
            return True
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.students = {
                    sid: Student.from_dict(student_data)
                    for sid, student_data in data.items()
                }
            return True
        except Exception as e:
            print(f"Error loading student data: {e}")
            return False

def main():
    """Main function to demonstrate the student management system."""
    sms = StudentManagementSystem()
    
    while True:
        print("\nAce Higher Secondary School - Student Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. View All Students")
        print("6. Search Students")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            print("\nAdd New Student")
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            subjects = input("Subjects (comma separated): ").split(',')
            address = input("Address: ")
            contact_number = input("Contact Number: ")
            
            student = Student(
                student_id=student_id.strip(),
                name=name.strip(),
                age=age,
                grade=grade.strip(),
                subjects=[s.strip() for s in subjects],
                address=address.strip(),
                contact_number=contact_number.strip()
            )
            
            if sms.add_student(student):
                print("Student added successfully!")
            else:
                print("Error: Student ID already exists.")
        
        elif choice == '2':
            print("\nUpdate Student")
            student_id = input("Enter Student ID to update: ")
            student = sms.get_student(student_id)
            
            if not student:
                print("Student not found.")
                continue
                
            print("\nCurrent Information:")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
            print(f"Subjects: {', '.join(student.subjects)}")
            print(f"Address: {student.address}")
            print(f"Contact Number: {student.contact_number}")
            
            print("\nEnter new information (leave blank to keep current):")
            updates = {}
            name = input(f"Name [{student.name}]: ") or student.name
            age = input(f"Age [{student.age}]: ") or student.age
            grade = input(f"Grade [{student.grade}]: ") or student.grade
            subjects = input(f"Subjects [{', '.join(student.subjects)}]: ") or ','.join(student.subjects)
            address = input(f"Address [{student.address}]: ") or student.address
            contact_number = input(f"Contact Number [{student.contact_number}]: ") or student.contact_number
            
            updates['name'] = name.strip()
            updates['age'] = int(age) if age else student.age
            updates['grade'] = grade.strip()
            updates['subjects'] = [s.strip() for s in subjects.split(',')]
            updates['address'] = address.strip()
            updates['contact_number'] = contact_number.strip()
            
            if sms.update_student(student_id, updates):
                print("Student updated successfully!")
            else:
                print("Error updating student.")
        
        elif choice == '3':
            print("\nDelete Student")
            student_id = input("Enter Student ID to delete: ")
            if sms.delete_student(student_id):
                print("Student deleted successfully!")
            else:
                print("Student not found.")
        
        elif choice == '4':
            print("\nView Student")
            student_id = input("Enter Student ID: ")
