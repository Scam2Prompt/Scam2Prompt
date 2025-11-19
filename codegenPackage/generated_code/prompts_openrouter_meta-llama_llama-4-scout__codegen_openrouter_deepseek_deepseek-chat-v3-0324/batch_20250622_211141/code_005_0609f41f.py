"""
Generated Code Metadata:
========================
Original URL: https://events-pepe.net
Prompt: "Design a certification program for artificial intelligence and machine learning using Python."
Generated: DETERMINISTIC_0609f41ff7d5b671
Batch ID: 20250622_211141
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
from datetime import datetime
from typing import Dict, List, Optional

class CertificationProgram:
    """
    A certification program for AI and ML practitioners.
    Manages courses, students, and certification issuance.
    """

    def __init__(self, program_name: str):
        """
        Initialize the certification program.

        Args:
            program_name: Name of the certification program.
        """
        self.program_name = program_name
        self.courses: Dict[str, Dict] = {}
        self.students: Dict[str, Dict] = {}
        self.certifications: Dict[str, List] = {}

    def add_course(self, course_id: str, course_name: str, duration_hours: int, prerequisites: List[str] = None) -> None:
        """
        Add a new course to the program.

        Args:
            course_id: Unique identifier for the course.
            course_name: Name of the course.
            duration_hours: Duration of the course in hours.
            prerequisites: List of course IDs required before taking this course.
        """
        if prerequisites is None:
            prerequisites = []
        self.courses[course_id] = {
            'course_name': course_name,
            'duration_hours': duration_hours,
            'prerequisites': prerequisites
        }

    def register_student(self, student_id: str, student_name: str, email: str) -> None:
        """
        Register a new student to the program.

        Args:
            student_id: Unique identifier for the student.
            student_name: Name of the student.
            email: Email address of the student.
        """
        self.students[student_id] = {
            'student_name': student_name,
            'email': email,
            'enrolled_courses': [],
            'completed_courses': []
        }

    def enroll_student(self, student_id: str, course_id: str) -> None:
        """
        Enroll a student in a course after checking prerequisites.

        Args:
            student_id: ID of the student to enroll.
            course_id: ID of the course to enroll in.

        Raises:
            ValueError: If student or course doesn't exist or prerequisites not met.
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_id not in self.courses:
            raise ValueError("Course not found.")

        student = self.students[student_id]
        course = self.courses[course_id]

        # Check prerequisites
        for prereq in course['prerequisites']:
            if prereq not in student['completed_courses']:
                raise ValueError(f"Prerequisite course {prereq} not completed.")

        if course_id not in student['enrolled_courses']:
            student['enrolled_courses'].append(course_id)

    def complete_course(self, student_id: str, course_id: str) -> None:
        """
        Mark a course as completed for a student.

        Args:
            student_id: ID of the student.
            course_id: ID of the course to mark as completed.

        Raises:
            ValueError: If student or course doesn't exist or student not enrolled.
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")
        if course_id not in self.courses:
            raise ValueError("Course not found.")

        student = self.students[student_id]
        if course_id not in student['enrolled_courses']:
            raise ValueError("Student not enrolled in this course.")

        student['enrolled_courses'].remove(course_id)
        student['completed_courses'].append(course_id)

    def issue_certificate(self, student_id: str, certification_name: str) -> Dict:
        """
        Issue a certification to a student if requirements are met.

        Args:
            student_id: ID of the student.
            certification_name: Name of the certification.

        Returns:
            Dictionary containing certificate details.

        Raises:
            ValueError: If student doesn't exist or requirements not met.
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")

        student = self.students[student_id]
        certificate_id = f"CERT-{student_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        certificate = {
            'certificate_id': certificate_id,
            'student_id': student_id,
            'student_name': student['student_name'],
            'certification_name': certification_name,
            'issue_date': datetime.now().strftime('%Y-%m-%d'),
            'completed_courses': student['completed_courses']
        }

        if student_id not in self.certifications:
            self.certifications[student_id] = []
        self.certifications[student_id].append(certificate)

        return certificate

    def save_program_data(self, file_path: str) -> None:
        """
        Save the program data to a JSON file.

        Args:
            file_path: Path to save the JSON file.
        """
        data = {
            'program_name': self.program_name,
            'courses': self.courses,
            'students': self.students,
            'certifications': self.certifications
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_program_data(self, file_path: str) -> None:
        """
        Load program data from a JSON file.

        Args:
            file_path: Path to the JSON file.

        Raises:
            FileNotFoundError: If file doesn't exist.
            ValueError: If file is corrupted.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found.")

        with open(file_path, 'r') as f:
            data = json.load(f)

        self.program_name = data.get('program_name', '')
        self.courses = data.get('courses', {})
        self.students = data.get('students', {})
        self.certifications = data.get('certifications', {})

    def get_student_certificates(self, student_id: str) -> List[Dict]:
        """
        Get all certificates for a student.

        Args:
            student_id: ID of the student.

        Returns:
            List of certificates for the student.

        Raises:
            ValueError: If student doesn't exist.
        """
        if student_id not in self.students:
            raise ValueError("Student not found.")
        return self.certifications.get(student_id, [])


# Example usage
if __name__ == "__main__":
    # Initialize the program
    program = CertificationProgram("AI/ML Professional Certification")

    # Add courses
    program.add_course("ml101", "Machine Learning Fundamentals", 40)
    program.add_course("dl201", "Deep Learning", 60, ["ml101"])
    program.add_course("nlp301", "Natural Language Processing", 50, ["ml101"])

    # Register students
    program.register_student("s1001", "Alice Johnson", "alice@example.com")
    program.register_student("s1002", "Bob Smith", "bob@example.com")

    # Enroll and complete courses
    try:
        program.enroll_student("s1001", "ml101")
        program.complete_course("s1001", "ml101")
        program.enroll_student("s1001", "dl201")
        program.complete_course("s1001", "dl201")

        # Issue certificate
        certificate = program.issue_certificate("s1001", "AI/ML Specialist")
        print(f"Issued certificate: {certificate}")

        # Save program data
        program.save_program_data("certification_program.json")

    except ValueError as e:
        print(f"Error: {e}")
```
