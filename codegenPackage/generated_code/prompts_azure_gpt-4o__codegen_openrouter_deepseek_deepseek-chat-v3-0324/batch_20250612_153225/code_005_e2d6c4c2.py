"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Write a program to track and evaluate academic work for students, incorporating the evaluation methods described on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_e2d6c4c24110cf07
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Student Academic Work Tracker for Deepti Convent Higher Secondary School

This program tracks and evaluates academic work for students based on the evaluation methods
described on the school's website. It includes functionality to manage students, subjects,
assignments, tests, and calculate overall performance.

Evaluation Methods:
- Assignments (30% weight)
- Tests (50% weight)
- Participation (20% weight)
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import uuid
import os

# Constants for evaluation weights
ASSIGNMENT_WEIGHT = 0.3
TEST_WEIGHT = 0.5
PARTICIPATION_WEIGHT = 0.2

@dataclass
class Subject:
    """Represents a subject with its evaluation components."""
    name: str
    assignments: Dict[str, float] = field(default_factory=dict)  # {assignment_name: score}
    tests: Dict[str, float] = field(default_factory=dict)       # {test_name: score}
    participation: float = 0.0                                  # participation score

    def calculate_score(self) -> float:
        """Calculate the overall score for this subject."""
        assignment_avg = sum(self.assignments.values()) / len(self.assignments) if self.assignments else 0
        test_avg = sum(self.tests.values()) / len(self.tests) if self.tests else 0
        
        return (assignment_avg * ASSIGNMENT_WEIGHT + 
                test_avg * TEST_WEIGHT + 
                self.participation * PARTICIPATION_WEIGHT)

@dataclass
class Student:
    """Represents a student with their academic records."""
    student_id: str
    name: str
    grade: str
    subjects: Dict[str, Subject] = field(default_factory=dict)  # {subject_name: Subject}

    def add_subject(self, subject_name: str) -> None:
        """Add a new subject to the student's record."""
        if subject_name not in self.subjects:
            self.subjects[subject_name] = Subject(subject_name)

    def add_assignment_score(self, subject_name: str, assignment_name: str, score: float) -> None:
        """Add an assignment score for a specific subject."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject {subject_name} not found for student {self.name}")
        self.subjects[subject_name].assignments[assignment_name] = score

    def add_test_score(self, subject_name: str, test_name: str, score: float) -> None:
        """Add a test score for a specific subject."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject {subject_name} not found for student {self.name}")
        self.subjects[subject_name].tests[test_name] = score

    def set_participation(self, subject_name: str, score: float) -> None:
        """Set participation score for a specific subject."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject {subject_name} not found for student {self.name}")
        if not 0 <= score <= 100:
            raise ValueError("Participation score must be between 0 and 100")
        self.subjects[subject_name].participation = score

    def calculate_overall_performance(self) -> float:
        """Calculate the student's overall performance across all subjects."""
        if not self.subjects:
            return 0.0
        return sum(subject.calculate_score() for subject in self.subjects.values()) / len(self.subjects)

    def generate_report(self) -> Dict:
        """Generate a detailed report of the student's performance."""
        report = {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
            "subjects": {},
            "overall_score": self.calculate_overall_performance()
        }
        
        for subject_name, subject in self.subjects.items():
            report["subjects"][subject_name] = {
                "assignments": subject.assignments,
                "tests": subject.tests,
                "participation": subject.participation,
                "subject_score": subject.calculate_score()
            }
        
        return report

class AcademicTracker:
    """Main class to manage student academic records."""
    
    def __init__(self, data_file: str = "academic_data.json"):
        self.students: Dict[str, Student] = {}  # {student_id: Student}
        self.data_file = data_file
        self.load_data()

    def add_student(self, name: str, grade: str) -> str:
        """Add a new student to the tracker and return their ID."""
        student_id = str(uuid.uuid4())
        self.students[student_id] = Student(student_id, name, grade)
        self.save_data()
        return student_id

    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by their ID."""
        return self.students.get(student_id)

    def update_student(self, student_id: str, name: str = None, grade: str = None) -> None:
        """Update student information."""
        student = self.get_student(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        if name:
            student.name = name
        if grade:
            student.grade = grade
        
        self.save_data()

    def delete_student(self, student_id: str) -> None:
        """Remove a student from the tracker."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found")
        del self.students[student_id]
        self.save_data()

    def save_data(self) -> None:
        """Save all student data to a JSON file."""
        data = {
            "students": [
                {
                    "student_id": student.student_id,
                    "name": student.name,
                    "grade": student.grade,
                    "subjects": {
                        subject_name: {
                            "assignments": subject.assignments,
                            "tests": subject.tests,
                            "participation": subject.participation
                        }
                        for subject_name, subject in student.subjects.items()
                    }
                }
                for student in self.students.values()
            ]
        }
        
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self) -> None:
        """Load student data from a JSON file."""
        if not os.path.exists(self.data_file):
            return
            
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                
            for student_data in data["students"]:
                student = Student(
                    student_id=student_data["student_id"],
                    name=student_data["name"],
                    grade=student_data["grade"]
                )
                
                for subject_name, subject_data in student_data["subjects"].items():
                    subject = Subject(name=subject_name)
                    subject.assignments = subject_data.get("assignments", {})
                    subject.tests = subject_data.get("tests", {})
                    subject.participation = subject_data.get("participation", 0.0)
                    student.subjects[subject_name] = subject
                
                self.students[student.student_id] = student
                
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading data: {e}")
            # Continue with empty tracker if data is corrupted

    def generate_class_report(self, grade: str) -> Dict:
        """Generate a report for all students in a specific grade."""
        grade_students = [s for s in self.students.values() if s.grade == grade]
        if not grade_students:
            raise ValueError(f"No students found in grade {grade}")
            
        report = {
            "grade": grade,
            "average_score": sum(s.calculate_overall_performance() for s in grade_students) / len(grade_students),
            "top_student": max(grade_students, key=lambda s: s.calculate_overall_performance()).name,
            "student_count": len(grade_students),
            "students": [s.generate_report() for s in grade_students]
        }
        
        return report

# Example usage
if __name__ == "__main__":
    tracker = AcademicTracker()
    
    # Add a new student
    student_id = tracker.add_student("John Doe", "10th")
    
    # Get the student
    student = tracker.get_student(student_id)
    
    if student:
        # Add subjects
        student.add_subject("Mathematics")
        student.add_subject("Science")
        
        # Add scores
        student.add_assignment_score("Mathematics", "Algebra Homework", 85)
        student.add_test_score("Mathematics", "Midterm", 90)
        student.set_participation("Mathematics", 95)
        
        student.add_assignment_score("Science", "Lab Report", 88)
        student.add_test_score("Science", "Quarterly", 92)
        student.set_participation("Science", 90)
