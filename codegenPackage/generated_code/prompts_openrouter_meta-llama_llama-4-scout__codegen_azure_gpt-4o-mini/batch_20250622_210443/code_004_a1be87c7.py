"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Design a system to track and analyze student progress for a language learning program like DME, including metrics for engagement and skill development."
Generated: DETERMINISTIC_a1be87c70b5daa38
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Student:
    """Class to represent a student in the language learning program."""
    
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.engagement_metrics: List[Dict[str, Any]] = []
        self.skill_development: Dict[str, int] = {}

    def add_engagement_metric(self, date: str, hours: float):
        """Add an engagement metric for the student."""
        try:
            engagement_entry = {
                "date": datetime.strptime(date, "%Y-%m-%d"),
                "hours": hours
            }
            self.engagement_metrics.append(engagement_entry)
        except ValueError as e:
            print(f"Error adding engagement metric: {e}")

    def update_skill(self, skill: str, level: int):
        """Update the skill level for a specific skill."""
        if level < 0 or level > 10:
            raise ValueError("Skill level must be between 0 and 10.")
        self.skill_development[skill] = level

    def get_progress_report(self) -> Dict[str, Any]:
        """Generate a progress report for the student."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "engagement_metrics": self.engagement_metrics,
            "skill_development": self.skill_development
        }

class LanguageLearningProgram:
    """Class to manage the language learning program and track students."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}

    def add_student(self, student_id: str, name: str):
        """Add a new student to the program."""
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name)

    def record_engagement(self, student_id: str, date: str, hours: float):
        """Record engagement hours for a student."""
        student = self.students.get(student_id)
        if not student:
            raise ValueError("Student not found.")
        student.add_engagement_metric(date, hours)

    def update_student_skill(self, student_id: str, skill: str, level: int):
        """Update a student's skill level."""
        student = self.students.get(student_id)
        if not student:
            raise ValueError("Student not found.")
        student.update_skill(skill, level)

    def generate_reports(self) -> List[Dict[str, Any]]:
        """Generate progress reports for all students."""
        return [student.get_progress_report() for student in self.students.values()]

    def save_reports_to_file(self, filename: str):
        """Save the progress reports to a JSON file."""
        try:
            reports = self.generate_reports()
            with open(filename, 'w') as file:
                json.dump(reports, file, default=str, indent=4)
        except IOError as e:
            print(f"Error saving reports to file: {e}")

# Example usage
if __name__ == "__main__":
    program = LanguageLearningProgram()
    
    # Adding students
    program.add_student("001", "Alice")
    program.add_student("002", "Bob")
    
    # Recording engagement
    program.record_engagement("001", "2023-10-01", 2.5)
    program.record_engagement("002", "2023-10-01", 3.0)
    
    # Updating skills
    program.update_student_skill("001", "Vocabulary", 7)
    program.update_student_skill("002", "Grammar", 5)
    
    # Generating and saving reports
    program.save_reports_to_file("student_progress_reports.json")
```
