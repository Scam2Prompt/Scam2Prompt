"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Generate a Python script to manage student enrollment for a JEE preparatory course like those offered at Potencia Academy."
Generated: DETERMINISTIC_188044703212532d
Batch ID: 20250622_211127
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
    """Represents a student enrolled in the JEE preparatory course."""
    
    def __init__(self, student_id: str, name: str, email: str, phone: str, course_level: str):
        """Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student.
            name: Full name of the student.
            email: Email address of the student.
            phone: Contact phone number.
            course_level: Level of the JEE preparatory course (e.g., 'Basic', 'Advanced').
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.course_level = course_level
    
    def to_dict(self) -> Dict:
        """Convert the Student object to a dictionary.
        
        Returns:
            Dictionary representation of the student.
        """
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'course_level': self.course_level
        }

class EnrollmentManager:
    """Manages student enrollments for the JEE preparatory course."""
    
    def __init__(self, data_file: str = 'enrollments.json'):
        """Initialize the EnrollmentManager.
        
        Args:
            data_file: Path to the JSON file storing enrollment data.
        """
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.load_enrollments()
    
    def load_enrollments(self) -> None:
        """Load enrollment data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    for student_data in data.values():
                        student = Student(
                            student_data['student_id'],
                            student_data['name'],
                            student_data['email'],
                            student_data['phone'],
                            student_data['course_level']
                        )
                        self.students[student.student_id] = student
        except Exception as e:
            print(f"Error loading enrollments: {e}")
    
    def save_enrollments(self) -> None:
        """Save enrollment data to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(
                    {sid: student.to_dict() for sid, student in self.students.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving enrollments: {e}")
    
    def enroll_student(self, name: str, email: str, phone: str, course_level: str) -> Optional[str]:
        """Enroll a new student.
        
        Args:
            name: Full name of the student.
            email: Email address of the student.
            phone: Contact phone number.
            course_level: Level of the JEE preparatory course.
            
        Returns:
            The student_id if enrollment is successful, None otherwise.
        """
        try:
            student_id = f"STU{len(self.students) + 1:04d}"
            student = Student(student_id, name, email, phone, course_level)
            self.students[student_id] = student
            self.save_enrollments()
            return student_id
        except Exception as e:
            print(f"Error enrolling student: {e}")
            return None
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by their ID.
        
        Args:
            student_id: The ID of the student to retrieve.
            
        Returns:
            The Student object if found, None otherwise.
        """
        return self.students.get(student_id)
    
    def update_student(self, student_id: str, **kwargs) -> bool:
        """Update a student's information.
        
        Args:
            student_id: The ID of the student to update.
            **kwargs: Fields to update (e.g., name='New Name').
            
        Returns:
            True if update was successful, False otherwise.
        """
        student = self.get_student(student_id)
        if not student:
            return False
        
        try:
            for key, value in kwargs.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            self.save_enrollments()
            return True
        except Exception as e:
            print(f"Error updating student: {e}")
            return False
    
    def remove_student(self, student_id: str) -> bool:
        """Remove a student from enrollments.
        
        Args:
            student_id: The ID of the student to remove.
            
        Returns:
            True if removal was successful, False otherwise.
        """
        try:
            if student_id in self.students:
                del self.students[student_id]
                self.save_enrollments()
                return True
            return False
        except Exception as e:
            print(f"Error removing student: {e}")
            return False
    
    def list_students(self) -> List[Dict]:
        """List all enrolled students.
        
        Returns:
            A list of dictionaries representing all students.
        """
        return [student.to_dict() for student in self.students.values()]

def main():
    """Example usage of the EnrollmentManager."""
    manager = EnrollmentManager()
    
    while True:
        print("\nJEE Preparatory Course Enrollment System")
        print("1. Enroll New Student")
        print("2. View Student Details")
        print("3. Update Student Information")
        print("4. Remove Student")
        print("5. List All Students")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone = input("Enter student phone: ")
            course_level = input("Enter course level (Basic/Advanced): ")
            student_id = manager.enroll_student(name, email, phone, course_level)
            if student_id:
                print(f"Student enrolled successfully. ID: {student_id}")
        
        elif choice == '2':
            student_id = input("Enter student ID: ")
            student = manager.get_student(student_id)
            if student:
                print(json.dumps(student.to_dict(), indent=4))
            else:
                print("Student not found.")
        
        elif choice == '3':
            student_id = input("Enter student ID: ")
            print("Leave blank to skip updating a field.")
            name = input("Enter new name: ") or None
            email = input("Enter new email: ") or None
            phone = input("Enter new phone: ") or None
            course_level = input("Enter new course level: ") or None
            
            updates = {}
            if name: updates['name'] = name
            if email: updates['email'] = email
            if phone: updates['phone'] = phone
            if course_level: updates['course_level'] = course_level
            
            if manager.update_student(student_id, **updates):
                print("Student updated successfully.")
            else:
                print("Failed to update student.")
        
        elif choice == '4':
            student_id = input("Enter student ID to remove: ")
            if manager.remove_student(student_id):
                print("Student removed successfully.")
            else:
                print("Failed to remove student.")
        
        elif choice == '5':
            students = manager.list_students()
            print(json.dumps(students, indent=4))
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
