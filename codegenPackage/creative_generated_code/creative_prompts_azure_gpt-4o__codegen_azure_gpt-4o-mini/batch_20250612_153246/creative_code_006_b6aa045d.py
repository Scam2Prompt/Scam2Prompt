"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python program to track student progress across multiple subjects, incorporating features like simulated exam scores and revision schedules, as used in the Maratona do ENEM course.
Generated: DETERMINISTIC_b6aa045d4a7d15be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class Student:
    """Class to represent a student and their subject progress."""

    def __init__(self, name):
        self.name = name
        self.subjects = {}
    
    def add_subject(self, subject):
        """Add a new subject to the student's tracking."""
        if subject not in self.subjects:
            self.subjects[subject] = {
                'scores': [],
                'revision_schedule': []
            }
        else:
            raise ValueError(f"Subject '{subject}' already exists.")

    def add_exam_score(self, subject, score):
        """Add an exam score for the specified subject."""
        if subject in self.subjects:
            self.subjects[subject]['scores'].append(score)
        else:
            raise ValueError(f"Subject '{subject}' not found.")

    def add_revision_schedule(self, subject, date):
        """Add a revision date for a specified subject."""
        if subject in self.subjects:
            self.subjects[subject]['revision_schedule'].append(date)
        else:
            raise ValueError(f"Subject '{subject}' not found.")

    def get_average_score(self, subject):
        """Calculate and return the average score for a subject."""
        if subject in self.subjects and self.subjects[subject]['scores']:
            return sum(self.subjects[subject]['scores']) / len(self.subjects[subject]['scores'])
        else:
            raise ValueError(f"No scores recorded for subject '{subject}' or subject does not exist.")

    def get_revision_schedule(self, subject):
        """Return the revision schedule for a specified subject."""
        if subject in self.subjects:
            return self.subjects[subject]['revision_schedule']
        else:
            raise ValueError(f"Subject '{subject}' not found.")

    def save_progress(self, filename):
        """Save the student's progress to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.subjects, f, default=str)

    def load_progress(self, filename):
        """Load the student's progress from a JSON file."""
        with open(filename, 'r') as f:
            self.subjects = json.load(f)

def main():
    """Main function to demonstrate the student progress tracking system."""
    # Create a new student
    student = Student("John Doe")

    # Add subjects
    try:
        student.add_subject("Mathematics")
        student.add_subject("Science")
    except ValueError as e:
        print(e)

    # Simulate adding exam scores
    try:
        student.add_exam_score("Mathematics", 85)
        student.add_exam_score("Mathematics", 90)
        student.add_exam_score("Science", 78)
    except ValueError as e:
        print(e)

    # Add revision schedules
    try:
        student.add_revision_schedule("Mathematics", datetime.now() + timedelta(days=7))
        student.add_revision_schedule("Science", datetime.now() + timedelta(days=5))
    except ValueError as e:
        print(e)

    # Calculate average scores
    try:
        math_avg = student.get_average_score("Mathematics")
        print(f"Average score in Mathematics: {math_avg:.2f}")
    except ValueError as e:
        print(e)
    
    # Get revision schedules
    try:
        science_revision = student.get_revision_schedule("Science")
        print(f"Science revision schedule: {science_revision}")
    except ValueError as e:
        print(e)

    # Save progress
    try:
        student.save_progress('student_progress.json')
        print("Progress saved successfully.")
    except Exception as e:
        print(f"Error saving progress: {e}")

    # Load progress (for demonstration)
    try:
        student.load_progress('student_progress.json')
        print("Progress loaded successfully.")
    except Exception as e:
        print(f"Error loading progress: {e}")

if __name__ == "__main__":
    main()
```
