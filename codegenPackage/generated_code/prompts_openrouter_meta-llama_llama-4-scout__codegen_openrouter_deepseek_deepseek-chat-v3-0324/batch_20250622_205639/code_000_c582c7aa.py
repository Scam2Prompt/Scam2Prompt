"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a Python script to manage student enrollments for IELTS and PTE courses at Red & White International, including student details and course assignments.
Generated: DETERMINISTIC_c582c7aa1502dfa4
Batch ID: 20250622_205639
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
    """Represents a student with personal details and course enrollment information."""
    
    def __init__(self, student_id: str, name: str, email: str, phone: str):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student.
            name: Full name of the student.
            email: Email address of the student.
            phone: Phone number of the student.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.courses: List[str] = []
    
    def enroll_in_course(self, course_name: str) -> bool:
        """
        Enroll the student in a course if not already enrolled.
        
        Args:
            course_name: Name of the course to enroll in (IELTS or PTE).
            
        Returns:
            bool: True if enrollment was successful, False otherwise.
        """
        if course_name not in ["IELTS", "PTE"]:
            return False
        if course_name not in self.courses:
            self.courses.append(course_name)
            return True
        return False
    
    def unenroll_from_course(self, course_name: str) -> bool:
        """
        Unenroll the student from a course if enrolled.
        
        Args:
            course_name: Name of the course to unenroll from.
            
        Returns:
            bool: True if unenrollment was successful, False otherwise.
        """
        if course_name in self.courses:
            self.courses.remove(course_name)
            return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert the Student object to a dictionary for serialization."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "courses": self.courses.copy()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Create a Student object from a dictionary."""
        student = cls(
            student_id=data["student_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"]
        )
        student.courses = data.get("courses", [])
        return student

class EnrollmentManager:
    """Manages student enrollments and persistence."""
    
    def __init__(self, data_file: str = "enrollments.json"):
        """
        Initialize the EnrollmentManager.
        
        Args:
            data_file: Path to the JSON file for storing enrollment data.
        """
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.load_data()
    
    def add_student(self, student_id: str, name: str, email: str, phone: str) -> bool:
        """
        Add a new student to the system.
        
        Args:
            student_id: Unique identifier for the student.
            name: Full name of the student.
            email: Email address of the student.
            phone: Phone number of the student.
            
        Returns:
            bool: True if student was added successfully, False if student_id already exists.
        """
        if student_id in self.students:
            return False
        self.students[student_id] = Student(student_id, name, email, phone)
        self.save_data()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Retrieve a student by ID.
        
        Args:
            student_id: ID of the student to retrieve.
            
        Returns:
            Optional[Student]: The Student object if found, None otherwise.
        """
        return self.students.get(student_id)
    
    def enroll_student(self, student_id: str, course_name: str) -> bool:
        """
        Enroll a student in a course.
        
        Args:
            student_id: ID of the student to enroll.
            course_name: Name of the course to enroll in.
            
        Returns:
            bool: True if enrollment was successful, False otherwise.
        """
        student = self.get_student(student_id)
        if not student:
            return False
        success = student.enroll_in_course(course_name)
        if success:
            self.save_data()
        return success
    
    def unenroll_student(self, student_id: str, course_name: str) -> bool:
        """
        Unenroll a student from a course.
        
        Args:
            student_id: ID of the student to unenroll.
            course_name: Name of the course to unenroll from.
            
        Returns:
            bool: True if unenrollment was successful, False otherwise.
        """
        student = self.get_student(student_id)
        if not student:
            return False
        success = student.unenroll_from_course(course_name)
        if success:
            self.save_data()
        return success
    
    def delete_student(self, student_id: str) -> bool:
        """
        Delete a student from the system.
        
        Args:
            student_id: ID of the student to delete.
            
        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            return True
        return False
    
    def load_data(self) -> None:
        """Load student data from the JSON file."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for student_data in data.get("students", []):
                    student = Student.from_dict(student_data)
                    self.students[student.student_id] = student
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
    
    def save_data(self) -> None:
        """Save student data to the JSON file."""
        data = {
            "students": [student.to_dict() for student in self.students.values()]
        }
        try:
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

def main():
    """Command-line interface for managing student enrollments."""
    manager = EnrollmentManager()
    
    while True:
        print("\nRed & White International Enrollment System")
        print("1. Add Student")
        print("2. Enroll Student in Course")
        print("3. Unenroll Student from Course")
        print("4. View Student Details")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            phone = input("Enter student phone: ")
            if manager.add_student(student_id, name, email, phone):
                print("Student added successfully.")
            else:
                print("Error: Student ID already exists.")
        
        elif choice == "2":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name (IELTS/PTE): ").upper()
            if manager.enroll_student(student_id, course_name):
                print("Enrollment successful.")
            else:
                print("Error: Invalid student ID or course name.")
        
        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name (IELTS/PTE): ").upper()
            if manager.unenroll_student(student_id, course_name):
                print("Unenrollment successful.")
            else:
                print("Error: Invalid student ID or course name.")
        
        elif choice == "4":
            student_id = input("Enter student ID: ")
            student = manager.get_student(student_id)
            if student:
                print("\nStudent Details:")
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Email: {student.email}")
                print(f"Phone: {student.phone}")
                print(f"Courses: {', '.join(student.courses) if student.courses else 'None'}")
            else:
                print("Error: Student not found.")
        
        elif choice == "5":
            student_id = input("Enter student ID: ")
            if manager.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Error: Student not found.")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
