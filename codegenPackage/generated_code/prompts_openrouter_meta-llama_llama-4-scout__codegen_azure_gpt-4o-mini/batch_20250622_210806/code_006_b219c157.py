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
from typing import List, Dict, Any

class Student:
    """Class to represent a student with their name and results."""
    
    def __init__(self, name: str):
        self.name = name
        self.results: Dict[str, float] = {}  # Subject: Score

    def add_result(self, subject: str, score: float) -> None:
        """Add a result for a specific subject."""
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.results[subject] = score

    def get_average(self) -> float:
        """Calculate the average score of the student."""
        if not self.results:
            return 0.0
        return sum(self.results.values()) / len(self.results)

    def to_dict(self) -> Dict[str, Any]:
        """Convert student data to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "results": self.results,
            "average": self.get_average()
        }


class StudentResultsManager:
    """Class to manage student results and generate reports."""
    
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a new student to the results manager."""
        self.students.append(student)

    def generate_report(self) -> List[Dict[str, Any]]:
        """Generate a report of all students and their results."""
        return [student.to_dict() for student in self.students]

    def save_report_to_file(self, filename: str) -> None:
        """Save the report to a JSON file."""
        report = self.generate_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
        except IOError as e:
            print(f"Error saving report to file: {e}")

    def load_report_from_file(self, filename: str) -> None:
        """Load student results from a JSON file."""
        try:
            with open(filename, 'r') as file:
                report = json.load(file)
                for student_data in report:
                    student = Student(student_data['name'])
                    for subject, score in student_data['results'].items():
                        student.add_result(subject, score)
                    self.add_student(student)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading report from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = StudentResultsManager()

    # Adding students and their results
    student1 = Student("Alice")
    student1.add_result("Math", 95)
    student1.add_result("Science", 88)
    manager.add_student(student1)

    student2 = Student("Bob")
    student2.add_result("Math", 76)
    student2.add_result("Science", 82)
    manager.add_student(student2)

    # Generating and saving report
    manager.save_report_to_file("student_results.json")

    # Loading report from file
    new_manager = StudentResultsManager()
    new_manager.load_report_from_file("student_results.json")
    print(new_manager.generate_report())
```
