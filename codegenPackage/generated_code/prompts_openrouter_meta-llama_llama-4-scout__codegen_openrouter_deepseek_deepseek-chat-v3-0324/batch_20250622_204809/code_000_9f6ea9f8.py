"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Generate a Python script to manage course enrollment for a training program in public management and law, similar to those offered by Escuela de Ciencias Politicas."
Generated: DETERMINISTIC_9f6ea9f8dc07ca5d
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from typing import List, Dict, Optional

class CourseEnrollmentSystem:
    """A system to manage course enrollment for public management and law training programs."""
    
    def __init__(self, data_file: str = "enrollments.csv"):
        """Initialize the enrollment system with a data file.
        
        Args:
            data_file: Path to the CSV file storing enrollment data.
        """
        self.data_file = data_file
        self.enrollments: List[Dict] = []
        self._load_data()
    
    def _load_data(self) -> None:
        """Load enrollment data from the CSV file."""
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self._get_fieldnames())
                writer.writeheader()
            return
        
        with open(self.data_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            self.enrollments = list(reader)
    
    def _save_data(self) -> None:
        """Save enrollment data to the CSV file."""
        with open(self.data_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self._get_fieldnames())
            writer.writeheader()
            writer.writerows(self.enrollments)
    
    def _get_fieldnames(self) -> List[str]:
        """Return the fieldnames for the CSV file."""
        return [
            'student_id',
            'first_name',
            'last_name',
            'email',
            'course_code',
            'course_name',
            'enrollment_date',
            'status'
        ]
    
    def enroll_student(
        self,
        student_id: str,
        first_name: str,
        last_name: str,
        email: str,
        course_code: str,
        course_name: str,
        enrollment_date: str
    ) -> bool:
        """Enroll a student in a course.
        
        Args:
            student_id: Unique identifier for the student.
            first_name: Student's first name.
            last_name: Student's last name.
            email: Student's email address.
            course_code: Code identifying the course.
            course_name: Name of the course.
            enrollment_date: Date of enrollment (YYYY-MM-DD).
            
        Returns:
            bool: True if enrollment was successful, False otherwise.
        """
        if any(
            e['student_id'] == student_id and e['course_code'] == course_code
            for e in self.enrollments
        ):
            return False
        
        new_enrollment = {
            'student_id': student_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'course_code': course_code,
            'course_name': course_name,
            'enrollment_date': enrollment_date,
            'status': 'active'
        }
        
        self.enrollments.append(new_enrollment)
        self._save_data()
        return True
    
    def update_enrollment_status(
        self,
        student_id: str,
        course_code: str,
        new_status: str
    ) -> bool:
        """Update the status of a student's enrollment.
        
        Args:
            student_id: ID of the student to update.
            course_code: Code of the course to update.
            new_status: New status ('active', 'completed', 'withdrawn').
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        for enrollment in self.enrollments:
            if (
                enrollment['student_id'] == student_id
                and enrollment['course_code'] == course_code
            ):
                enrollment['status'] = new_status
                self._save_data()
                return True
        return False
    
    def get_student_enrollments(self, student_id: str) -> List[Dict]:
        """Get all enrollments for a specific student.
        
        Args:
            student_id: ID of the student to query.
            
        Returns:
            List of enrollment dictionaries for the student.
        """
        return [
            e for e in self.enrollments
            if e['student_id'] == student_id
        ]
    
    def get_course_enrollments(self, course_code: str) -> List[Dict]:
        """Get all enrollments for a specific course.
        
        Args:
            course_code: Code of the course to query.
            
        Returns:
            List of enrollment dictionaries for the course.
        """
        return [
            e for e in self.enrollments
            if e['course_code'] == course_code
        ]
    
    def search_enrollments(
        self,
        student_id: Optional[str] = None,
        course_code: Optional[str] = None,
        status: Optional[str] = None
    ) -> List[Dict]:
        """Search enrollments based on criteria.
        
        Args:
            student_id: Optional student ID filter.
            course_code: Optional course code filter.
            status: Optional status filter.
            
        Returns:
            List of enrollment dictionaries matching the criteria.
        """
        results = self.enrollments
        
        if student_id:
            results = [e for e in results if e['student_id'] == student_id]
        if course_code:
            results = [e for e in results if e['course_code'] == course_code]
        if status:
            results = [e for e in results if e['status'] == status]
            
        return results
    
    def remove_enrollment(self, student_id: str, course_code: str) -> bool:
        """Remove a student's enrollment from a course.
        
        Args:
            student_id: ID of the student to remove.
            course_code: Code of the course to remove from.
            
        Returns:
            bool: True if removal was successful, False otherwise.
        """
        initial_count = len(self.enrollments)
        self.enrollments = [
            e for e in self.enrollments
            if not (e['student_id'] == student_id and e['course_code'] == course_code)
        ]
        
        if len(self.enrollments) < initial_count:
            self._save_data()
            return True
        return False


def main():
    """Demonstrate the CourseEnrollmentSystem functionality."""
    enrollment_system = CourseEnrollmentSystem()
    
    # Example usage
    enrollment_system.enroll_student(
        "S001",
        "Maria",
        "Garcia",
        "maria.garcia@example.com",
        "PM101",
        "Introduction to Public Management",
        "2023-10-15"
    )
    
    enrollments = enrollment_system.get_student_enrollments("S001")
    print("Maria's enrollments:", enrollments)


if __name__ == "__main__":
    main()
```
