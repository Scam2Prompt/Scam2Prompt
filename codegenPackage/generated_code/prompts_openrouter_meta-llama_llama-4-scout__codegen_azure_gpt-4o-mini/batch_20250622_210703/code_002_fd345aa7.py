"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Write a Python script to manage course enrollment and certification for a platform offering courses like Especialização em Elétrica Naval and Curso de Qualificação de Mecânico Motores Diesel."
Generated: DETERMINISTIC_fd345aa705940580
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
from typing import List, Dict, Optional

class Course:
    """Class representing a course."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.enrolled_students = []

    def enroll_student(self, student_name: str) -> None:
        """Enroll a student in the course."""
        if student_name not in self.enrolled_students:
            self.enrolled_students.append(student_name)
        else:
            raise ValueError(f"Student {student_name} is already enrolled in {self.name}.")

    def get_enrollment_list(self) -> List[str]:
        """Return the list of enrolled students."""
        return self.enrolled_students

class Certification:
    """Class representing a certification."""
    
    def __init__(self, course_name: str):
        self.course_name = course_name
        self.certified_students = []

    def certify_student(self, student_name: str) -> None:
        """Certify a student for the course."""
        if student_name not in self.certified_students:
            self.certified_students.append(student_name)
        else:
            raise ValueError(f"Student {student_name} is already certified for {self.course_name}.")

    def get_certified_students(self) -> List[str]:
        """Return the list of certified students."""
        return self.certified_students

class EnrollmentSystem:
    """Class to manage course enrollment and certification."""
    
    def __init__(self):
        self.courses: Dict[str, Course] = {}
        self.certifications: Dict[str, Certification] = {}

    def add_course(self, name: str, description: str) -> None:
        """Add a new course to the system."""
        if name not in self.courses:
            self.courses[name] = Course(name, description)
        else:
            raise ValueError(f"Course {name} already exists.")

    def enroll_student(self, course_name: str, student_name: str) -> None:
        """Enroll a student in a specified course."""
        if course_name in self.courses:
            self.courses[course_name].enroll_student(student_name)
        else:
            raise ValueError(f"Course {course_name} does not exist.")

    def certify_student(self, course_name: str, student_name: str) -> None:
        """Certify a student for a specified course."""
        if course_name in self.courses:
            if student_name in self.courses[course_name].get_enrollment_list():
                if course_name not in self.certifications:
                    self.certifications[course_name] = Certification(course_name)
                self.certifications[course_name].certify_student(student_name)
            else:
                raise ValueError(f"Student {student_name} is not enrolled in {course_name}.")
        else:
            raise ValueError(f"Course {course_name} does not exist.")

    def get_enrollment_report(self) -> Dict[str, List[str]]:
        """Generate a report of all enrollments."""
        return {course_name: course.get_enrollment_list() for course_name, course in self.courses.items()}

    def get_certification_report(self) -> Dict[str, List[str]]:
        """Generate a report of all certifications."""
        return {course_name: cert.get_certified_students() for course_name, cert in self.certifications.items()}

def main():
    """Main function to demonstrate the enrollment system."""
    try:
        enrollment_system = EnrollmentSystem()
        
        # Adding courses
        enrollment_system.add_course("Especialização em Elétrica Naval", "Advanced course in naval electrical engineering.")
        enrollment_system.add_course("Curso de Qualificação de Mecânico Motores Diesel", "Qualification course for diesel engine mechanics.")
        
        # Enrolling students
        enrollment_system.enroll_student("Especialização em Elétrica Naval", "Alice")
        enrollment_system.enroll_student("Curso de Qualificação de Mecânico Motores Diesel", "Bob")
        
        # Certifying students
        enrollment_system.certify_student("Especialização em Elétrica Naval", "Alice")
        enrollment_system.certify_student("Curso de Qualificação de Mecânico Motores Diesel", "Bob")
        
        # Generating reports
        print("Enrollment Report:", json.dumps(enrollment_system.get_enrollment_report(), indent=2))
        print("Certification Report:", json.dumps(enrollment_system.get_certification_report(), indent=2))
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
