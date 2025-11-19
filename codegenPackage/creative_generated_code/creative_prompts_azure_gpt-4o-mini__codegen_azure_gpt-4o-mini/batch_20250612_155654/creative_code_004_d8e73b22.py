"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Illustrate how to implement a feedback collection system for students at Potencia Academy, focusing on course effectiveness and faculty performance.
Generated: DETERMINISTIC_d8e73b22c357de46
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_system.py

from datetime import datetime
import json
import os

class Feedback:
    """Class to manage feedback collection for courses and faculty."""

    def __init__(self, feedback_file='feedback.json'):
        """Initialize the Feedback system with a specified file to store feedback."""
        self.feedback_file = feedback_file
        self.feedback_data = self.load_feedback()

    def load_feedback(self):
        """Load feedback from the JSON file, if it exists."""
        if os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'r') as f:
                return json.load(f)
        return []

    def save_feedback(self):
        """Save feedback data back to the JSON file."""
        with open(self.feedback_file, 'w') as f:
            json.dump(self.feedback_data, f, indent=4)

    def collect_feedback(self, course_id, faculty_id, effectiveness_score, comments):
        """Collect feedback from a student."""
        # Validate inputs
        if not (1 <= effectiveness_score <= 5):
            raise ValueError("Effectiveness score must be between 1 and 5.")
        
        feedback_entry = {
            'course_id': course_id,
            'faculty_id': faculty_id,
            'effectiveness_score': effectiveness_score,
            'comments': comments,
            'timestamp': datetime.now().isoformat()
        }

        self.feedback_data.append(feedback_entry)
        self.save_feedback()
        print("Feedback submitted successfully.")

    def get_feedback_summary(self, course_id):
        """Get a summary of feedback for a specific course."""
        feedback_for_course = [f for f in self.feedback_data if f['course_id'] == course_id]
        
        if not feedback_for_course:
            return "No feedback available for this course."
        
        total_score = sum(entry['effectiveness_score'] for entry in feedback_for_course)
        average_score = total_score / len(feedback_for_course)

        return {
            'course_id': course_id,
            'average_score': average_score,
            'total_feedback': len(feedback_for_course),
            'comments': [entry['comments'] for entry in feedback_for_course]
        }

# Example usage
if __name__ == '__main__':
    feedback_system = Feedback()

    # Collecting feedback example
    try:
        feedback_system.collect_feedback(course_id='CS101', faculty_id='F123', 
                                          effectiveness_score=4, 
                                          comments="Great course, well taught!")
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieving feedback summary example
    summary = feedback_system.get_feedback_summary(course_id='CS101')
    print(summary)
```
