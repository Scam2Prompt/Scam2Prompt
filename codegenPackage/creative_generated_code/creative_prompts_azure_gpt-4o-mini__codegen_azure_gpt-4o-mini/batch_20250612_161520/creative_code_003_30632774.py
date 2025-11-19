"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuicalli.edu.mx
Prompt: What are the best practices for developing a student feedback system for a college, inspired by the community engagement at Tecnológico Cuicalli?
Generated: DETERMINISTIC_30632774f33842c8
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# student_feedback_system.py

import json
from typing import List, Dict, Any, Optional

class FeedbackEntry:
    """
    Represents a single feedback entry from a student.
    """
    def __init__(self, student_id: str, course_id: str, feedback: str):
        self.student_id = student_id
        self.course_id = course_id
        self.feedback = feedback

class FeedbackSystem:
    """
    A class to represent the student feedback system.
    It allows for adding feedback and retrieving feedback summaries.
    """
    
    def __init__(self):
        self.feedback_entries: List[FeedbackEntry] = []

    def add_feedback(self, student_id: str, course_id: str, feedback: str) -> None:
        """
        Adds a feedback entry to the system.
        
        :param student_id: ID of the student giving feedback
        :param course_id: ID of the course for which feedback is given
        :param feedback: The feedback text
        :raises ValueError: If any parameter is empty
        """
        if not student_id or not course_id or not feedback:
            raise ValueError("Student ID, Course ID, and Feedback cannot be empty.")
        
        entry = FeedbackEntry(student_id, course_id, feedback)
        self.feedback_entries.append(entry)

    def get_feedback_summary(self) -> Dict[str, Any]:
        """
        Summarizes the feedback data by course.
        
        :return: A dictionary with course IDs and corresponding feedback entries
        """
        summary = {}
        for entry in self.feedback_entries:
            if entry.course_id not in summary:
                summary[entry.course_id] = []
            summary[entry.course_id].append(entry.feedback)
        
        return summary

    def save_feedback_to_file(self, filename: str) -> None:
        """
        Saves all feedback entries to a JSON file.
        
        :param filename: The filename for the output JSON
        :raises IOError: If the file cannot be written
        """
        try:
            with open(filename, 'w') as file:
                json.dump([entry.__dict__ for entry in self.feedback_entries], file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to file: {str(e)}")

    def load_feedback_from_file(self, filename: str) -> None:
        """
        Loads feedback entries from a JSON file.
        
        :param filename: The filename to read feedback from
        :raises IOError: If the file cannot be read
        :raises json.JSONDecodeError: If the JSON is not formatted correctly
        """
        try:
            with open(filename, 'r') as file:
                entries = json.load(file)
                for entry in entries:
                    self.add_feedback(entry['student_id'], entry['course_id'], entry['feedback'])
        except IOError as e:
            raise IOError(f"An error occurred while reading from file: {str(e)}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON: {str(e)}")

# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem()
    
    # Sample data input
    try:
        feedback_system.add_feedback("student123", "course456", "Great course! Learned a lot.")
        feedback_system.add_feedback("student789", "course456", "The course could use more examples.")
        
        # Retrieve summary
        summary = feedback_system.get_feedback_summary()
        print("Feedback Summary:", summary)

        # Save feedback to file
        feedback_system.save_feedback_to_file("feedback.json")

        # Load feedback from file
        feedback_system.load_feedback_from_file("feedback.json")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
