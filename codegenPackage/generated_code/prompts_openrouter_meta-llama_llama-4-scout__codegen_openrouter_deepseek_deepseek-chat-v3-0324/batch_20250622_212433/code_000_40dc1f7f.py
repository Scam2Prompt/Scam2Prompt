"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Generate a Python script to manage student enrollment for a dental hygiene program with a duration of 2 years, similar to the Técnico Superior Universitario en Higienista Dental offered by INESO."
Generated: DETERMINISTIC_40dc1f7fc2250cfd
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime
from typing import List, Dict, Optional

class Student:
    """Represents a student enrolled in the dental hygiene program."""
    
    def __init__(self, student_id: str, first_name: str, last_name: str, email: str, 
                 enrollment_date: str, graduation_date: str):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student.
            first_name: Student's first name.
            last_name: Student's last name.
            email: Student's email address.
            enrollment_date: Date when student enrolled (YYYY-MM-DD).
            graduation_date: Expected graduation date (YYYY-MM-DD).
        """
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.graduation_date = graduation_date
        self.courses = []
    
    def add_course(self, course_code: str, course_name: str) -> None:
        """Add a course to the student's record."""
        self.courses.append({
            'code': course_code,
            'name': course_name
        })
    
    def get_courses(self) -> List[Dict[str, str]]:
        """Return list of courses the student is enrolled in."""
        return self.courses
    
    def __str__(self) -> str:
        """Return string representation of the student."""
        return (f"Student ID: {self.student_id}\n"
                f"Name: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\n"
                f"Enrollment Date: {self.enrollment_date}\n"
                f"Graduation Date: {self.graduation_date}\n"
                f"Courses Enrolled: {len(self.courses)}")

class EnrollmentSystem:
    """Manages student enrollment for the dental hygiene program."""
    
    def __init__(self):
        """Initialize the enrollment system with empty student list."""
        self.students = {}
        self.program_duration_years = 2
    
    def enroll_student(self, first_name: str, last_name: str, email: str) -> Optional[Student]:
        """
        Enroll a new student in the program.
        
        Args:
            first_name: Student's first name.
            last_name: Student's last name.
            email: Student's email address.
            
        Returns:
            Student object if enrollment successful, None otherwise.
        """
        try:
            if not self._validate_email(email):
                raise ValueError("Invalid email format")
            
            student_id = self._generate_student_id()
            today = datetime.now().strftime("%Y-%m-%d")
            graduation_date = self._calculate_graduation_date(today)
            
            student = Student(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                enrollment_date=today,
                graduation_date=graduation_date
            )
            
            self.students[student_id] = student
            return student
            
        except ValueError as e:
            print(f"Error enrolling student: {e}")
            return None
    
    def _generate_student_id(self) -> str:
        """Generate a unique student ID."""
        return f"DH{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def _calculate_graduation_date(self, enrollment_date: str) -> str:
        """
        Calculate graduation date based on enrollment date and program duration.
        
        Args:
            enrollment_date: Date in YYYY-MM-DD format.
            
        Returns:
            Graduation date in YYYY-MM-DD format.
        """
        try:
            enroll_date = datetime.strptime(enrollment_date, "%Y-%m-%d")
            grad_date = enroll_date.replace(year=enroll_date.year + self.program_duration_years)
            return grad_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format."""
        return '@' in email and '.' in email.split('@')[-1]
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by ID."""
        return self.students.get(student_id)
    
    def enroll_in_course(self, student_id: str, course_code: str, course_name: str) -> bool:
        """
        Enroll a student in a course.
        
        Args:
            student_id: ID of the student to enroll.
            course_code: Code of the course.
            course_name: Name of the course.
            
        Returns:
            True if enrollment successful, False otherwise.
        """
        student = self.get_student(student_id)
        if student:
            student.add_course(course_code, course_name)
            return True
        return False
    
    def export_students_to_csv(self, filename: str) -> bool:
        """
        Export student data to a CSV file.
        
        Args:
            filename: Name of the CSV file to create.
            
        Returns:
            True if export successful, False otherwise.
        """
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'Student ID',
                    'First Name',
                    'Last Name',
                    'Email',
                    'Enrollment Date',
                    'Graduation Date',
                    'Courses Count'
                ])
                
                for student in self.students.values():
                    writer.writerow([
                        student.student_id,
                        student.first_name,
                        student.last_name,
                        student.email,
                        student.enrollment_date,
                        student.graduation_date,
                        len(student.courses)
                    ])
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def import_students_from_csv(self, filename: str) -> bool:
        """
        Import student data from a CSV file.
        
        Args:
            filename: Name of the CSV file to import.
            
        Returns:
            True if import successful, False otherwise.
        """
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        student_id=row['Student ID'],
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        email=row['Email'],
                        enrollment_date=row['Enrollment Date'],
                        graduation_date=row['Graduation Date']
                    )
                    self.students[row['Student ID']] = student
            return True
        except Exception as e:
            print(f"Error importing from CSV: {e}")
            return False

def main():
    """Demonstrate the enrollment system functionality."""
    system = EnrollmentSystem()
    
    # Enroll new students
    student1 = system.enroll_student("Maria", "Garcia", "maria.garcia@example.com")
    student2 = system.enroll_student("Juan", "Lopez", "juan.lopez@example.com")
    
    if student1 and student2:
        # Enroll students in courses
        system.enroll_in_course(student1.student_id, "DH101", "Introduction to Dental Hygiene")
        system.enroll_in_course(student1.student_id, "DH102", "Oral Anatomy")
        system.enroll_in_course(student2.student_id, "DH101", "Introduction to Dental Hygiene")
        
        # Export data
        system.export_students_to_csv("dental_hygiene_students.csv")
        
        # Display student information
        print(student1)
        print("\n")
        print(student2)

if __name__ == "__main__":
    main()
```
