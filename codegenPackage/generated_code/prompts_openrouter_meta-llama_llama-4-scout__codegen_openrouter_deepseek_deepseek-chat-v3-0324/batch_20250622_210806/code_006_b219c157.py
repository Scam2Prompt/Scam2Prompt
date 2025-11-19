"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Develop a system for tracking student results and generating reports, similar to Ideal High School's result management system.
Generated: DETERMINISTIC_b219c1572c06a9de
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional

class Student:
    """Represents a student with their academic information."""
    
    def __init__(self, student_id: str, name: str, grade: str):
        """Initialize a student with basic information.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            grade: Current grade/class of the student
        """
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.subjects: Dict[str, List[float]] = {}
    
    def add_subject(self, subject_name: str) -> None:
        """Add a subject to the student's record.
        
        Args:
            subject_name: Name of the subject to add
        """
        if subject_name not in self.subjects:
            self.subjects[subject_name] = []
    
    def add_score(self, subject_name: str, score: float) -> bool:
        """Add a score for a specific subject.
        
        Args:
            subject_name: Name of the subject
            score: Score to add (0-100)
            
        Returns:
            bool: True if score was added successfully, False otherwise
        """
        if subject_name not in self.subjects:
            return False
        
        if not 0 <= score <= 100:
            return False
            
        self.subjects[subject_name].append(score)
        return True
    
    def get_average(self, subject_name: str) -> Optional[float]:
        """Calculate average score for a subject.
        
        Args:
            subject_name: Name of the subject
            
        Returns:
            Optional[float]: Average score or None if no scores exist
        """
        if subject_name not in self.subjects or not self.subjects[subject_name]:
            return None
            
        return sum(self.subjects[subject_name]) / len(self.subjects[subject_name])
    
    def get_overall_average(self) -> Optional[float]:
        """Calculate overall average across all subjects.
        
        Returns:
            Optional[float]: Overall average or None if no scores exist
        """
        if not self.subjects:
            return None
            
        all_scores = []
        for scores in self.subjects.values():
            all_scores.extend(scores)
            
        if not all_scores:
            return None
            
        return sum(all_scores) / len(all_scores)
    
    def to_dict(self) -> Dict:
        """Convert student data to dictionary for serialization."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'grade': self.grade,
            'subjects': self.subjects
        }

class ResultManagementSystem:
    """Main system for managing student results."""
    
    def __init__(self):
        """Initialize the result management system."""
        self.students: Dict[str, Student] = {}
    
    def add_student(self, student_id: str, name: str, grade: str) -> bool:
        """Add a new student to the system.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            grade: Current grade/class of the student
            
        Returns:
            bool: True if student was added, False if student_id already exists
        """
        if student_id in self.students:
            return False
            
        self.students[student_id] = Student(student_id, name, grade)
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by their ID.
        
        Args:
            student_id: ID of the student to retrieve
            
        Returns:
            Optional[Student]: Student object if found, None otherwise
        """
        return self.students.get(student_id)
    
    def add_subject_to_student(self, student_id: str, subject_name: str) -> bool:
        """Add a subject to a student's record.
        
        Args:
            student_id: ID of the student
            subject_name: Name of the subject to add
            
        Returns:
            bool: True if subject was added, False if student not found
        """
        student = self.get_student(student_id)
        if not student:
            return False
            
        student.add_subject(subject_name)
        return True
    
    def add_score_to_student(self, student_id: str, subject_name: str, score: float) -> bool:
        """Add a score for a student's subject.
        
        Args:
            student_id: ID of the student
            subject_name: Name of the subject
            score: Score to add (0-100)
            
        Returns:
            bool: True if score was added, False if student not found or invalid score
        """
        student = self.get_student(student_id)
        if not student:
            return False
            
        return student.add_score(subject_name, score)
    
    def generate_student_report(self, student_id: str) -> Optional[Dict]:
        """Generate a report for a specific student.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Optional[Dict]: Dictionary containing report data or None if student not found
        """
        student = self.get_student(student_id)
        if not student:
            return None
            
        report = {
            'student_id': student.student_id,
            'name': student.name,
            'grade': student.grade,
            'subjects': {},
            'overall_average': student.get_overall_average()
        }
        
        for subject, scores in student.subjects.items():
            report['subjects'][subject] = {
                'scores': scores,
                'average': student.get_average(subject)
            }
            
        return report
    
    def generate_class_report(self, grade: str) -> Dict:
        """Generate a report for all students in a specific grade.
        
        Args:
            grade: Grade/class to generate report for
            
        Returns:
            Dict: Dictionary containing class report data
        """
        class_students = [s for s in self.students.values() if s.grade == grade]
        report = {
            'grade': grade,
            'student_count': len(class_students),
            'students': [],
            'class_average': None
        }
        
        all_scores = []
        for student in class_students:
            student_report = self.generate_student_report(student.student_id)
            report['students'].append(student_report)
            overall = student.get_overall_average()
            if overall is not None:
                all_scores.append(overall)
        
        if all_scores:
            report['class_average'] = sum(all_scores) / len(all_scores)
            
        return report
    
    def save_to_file(self, filename: str) -> bool:
        """Save all student data to a JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            data = {
                'students': [student.to_dict() for student in self.students.values()]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load student data from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            bool: True if load was successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.students = {}
            for student_data in data['students']:
                student = Student(
                    student_data['student_id'],
                    student_data['name'],
                    student_data['grade']
                )
                student.subjects = student_data['subjects']
                self.students[student.student_id] = student
                
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False
    
    def export_class_report_to_csv(self, grade: str, filename: str) -> bool:
        """Export a class report to CSV format.
        
        Args:
            grade: Grade/class to export
            filename: Name of the CSV file
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        try:
            report = self.generate_class_report(grade)
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = [
                    'Student ID', 'Name', 'Grade', 
                    'Subjects', 'Subject Average', 'Overall Average'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for student in report['students']:
                    for subject, details in student['subjects'].items():
                        writer.writerow({
                            'Student ID': student['student_id'],
                            'Name': student['name'],
                            'Grade': student['grade'],
                            'Subjects': subject,
                            'Subject Average': details['average'],
                            'Overall Average': student['overall_average']
                        })
            return True
        except Exception as e:
