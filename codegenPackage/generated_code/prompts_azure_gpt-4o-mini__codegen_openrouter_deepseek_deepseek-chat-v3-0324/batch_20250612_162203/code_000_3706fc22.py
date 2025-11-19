"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a Python script that demonstrates how to manage student enrollment for the Graduate Diploma of Management (Learning) at Global Healthcare Management College.
Generated: DETERMINISTIC_3706fc22b7e63889
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto
from datetime import datetime
import os


class EnrollmentStatus(Enum):
    """Enum representing possible enrollment statuses."""
    APPLIED = auto()
    ENROLLED = auto()
    WITHDRAWN = auto()
    COMPLETED = auto()


@dataclass
class Student:
    """Data class representing a student."""
    student_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    enrollment_date: str
    status: EnrollmentStatus


class EnrollmentManager:
    """Manages student enrollments for the Graduate Diploma of Management (Learning)."""
    
    def __init__(self, data_file: str = "enrollments.csv"):
        """Initialize the enrollment manager with a data file."""
        self.data_file = data_file
        self.students: List[Student] = []
        self._load_enrollments()
    
    def _load_enrollments(self) -> None:
        """Load existing enrollments from the data file."""
        if not os.path.exists(self.data_file):
            return
            
        with open(self.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    self.students.append(Student(
                        student_id=row['student_id'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email=row['email'],
                        phone=row['phone'],
                        enrollment_date=row['enrollment_date'],
                        status=EnrollmentStatus[row['status']]
                    ))
                except KeyError as e:
                    print(f"Error loading student data: {e}. Skipping row.")
    
    def _save_enrollments(self) -> None:
        """Save current enrollments to the data file."""
        with open(self.data_file, mode='w', newline='') as file:
            fieldnames = [
                'student_id', 'first_name', 'last_name', 
                'email', 'phone', 'enrollment_date', 'status'
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in self.students:
                writer.writerow({
                    'student_id': student.student_id,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'email': student.email,
                    'phone': student.phone,
                    'enrollment_date': student.enrollment_date,
                    'status': student.status.name
                })
    
    def enroll_student(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        enrollment_date: Optional[str] = None
    ) -> Student:
        """Enroll a new student in the program."""
        if not all([first_name, last_name, email, phone]):
            raise ValueError("All student details must be provided")
        
        if not enrollment_date:
            enrollment_date = datetime.now().strftime("%Y-%m-%d")
        
        student_id = f"GHC{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        student = Student(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            enrollment_date=enrollment_date,
            status=EnrollmentStatus.APPLIED
        )
        
        self.students.append(student)
        self._save_enrollments()
        return student
    
    def update_enrollment_status(
        self, 
        student_id: str, 
        new_status: EnrollmentStatus
    ) -> Optional[Student]:
        """Update a student's enrollment status."""
        for student in self.students:
            if student.student_id == student_id:
                student.status = new_status
                self._save_enrollments()
                return student
        return None
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def list_students(self, status: Optional[EnrollmentStatus] = None) -> List[Student]:
        """List all students, optionally filtered by status."""
        if status:
            return [s for s in self.students if s.status == status]
        return self.students
    
    def withdraw_student(self, student_id: str) -> Optional[Student]:
        """Withdraw a student from the program."""
        return self.update_enrollment_status(student_id, EnrollmentStatus.WITHDRAWN)


# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager()
    
    # Enroll a new student
    new_student = manager.enroll_student(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="+1234567890"
    )
    print(f"Enrolled new student: {new_student}")
    
    # Update student status
    updated_student = manager.update_enrollment_status(
        new_student.student_id,
        EnrollmentStatus.ENROLLED
    )
    print(f"Updated student status: {updated_student}")
    
    # List all enrolled students
    enrolled_students = manager.list_students(EnrollmentStatus.ENROLLED)
    print(f"Enrolled students: {enrolled_students}")
```
