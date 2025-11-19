"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python program to track student progress across multiple subjects, incorporating features like simulated exam scores and revision schedules, as used in the Maratona do ENEM course.
Generated: DETERMINISTIC_b6aa045d4a7d15be
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Student:
    """Class to represent a student and their progress in multiple subjects."""
    
    def __init__(self, name):
        self.name = name
        self.subjects = {}
    
    def add_subject(self, subject_name):
        """Add a new subject to the student's record."""
        if subject_name not in self.subjects:
            self.subjects[subject_name] = {'scores': [], 'revision_schedule': []}
        else:
            raise ValueError(f"Subject '{subject_name}' already exists.")
    
    def add_score(self, subject_name, score):
        """Add an exam score for a specific subject."""
        if subject_name in self.subjects:
            if 0 <= score <= 100:
                self.subjects[subject_name]['scores'].append(score)
            else:
                raise ValueError("Score must be between 0 and 100.")
        else:
            raise ValueError(f"Subject '{subject_name}' not found.")
    
    def schedule_revision(self, subject_name, date):
        """Schedule a revision session for a specific subject."""
        if subject_name in self.subjects:
            self.subjects[subject_name]['revision_schedule'].append(date)
        else:
            raise ValueError(f"Subject '{subject_name}' not found.")
    
    def get_average_score(self, subject_name):
        """Calculate the average score for a specific subject."""
        if subject_name in self.subjects:
            scores = self.subjects[subject_name]['scores']
            if scores:
                return sum(scores) / len(scores)
            else:
                return 0
        else:
            raise ValueError(f"Subject '{subject_name}' not found.")
    
    def get_revision_schedule(self, subject_name):
        """Get the revision schedule for a specific subject."""
        if subject_name in self.subjects:
            return self.subjects[subject_name]['revision_schedule']
        else:
            raise ValueError(f"Subject '{subject_name}' not found.")

    def to_json(self):
        """Convert the student's data to JSON format."""
        return json.dumps(self.__dict__, default=str)

def main():
    """Main function to demonstrate the Student class functionality."""
    try:
        # Create a new student
        student = Student("John Doe")
        
        # Add subjects
        student.add_subject("Mathematics")
        student.add_subject("Science")
        
        # Add scores
        student.add_score("Mathematics", 85)
        student.add_score("Mathematics", 90)
        student.add_score("Science", 78)
        
        # Schedule revisions
        revision_date = datetime.now() + timedelta(days=7)
        student.schedule_revision("Mathematics", revision_date)
        
        # Get average scores
        math_avg = student.get_average_score("Mathematics")
        science_avg = student.get_average_score("Science")
        
        # Print results
        print(f"Average score in Mathematics: {math_avg:.2f}")
        print(f"Average score in Science: {science_avg:.2f}")
        
        # Print revision schedule
        print("Revision schedule for Mathematics:", student.get_revision_schedule("Mathematics"))
        
        # Save student data to JSON
        with open("student_data.json", "w") as json_file:
            json_file.write(student.to_json())
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
