"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Generate a course outline for a 30-hour basic safety course in electrical installations, including topics and quizzes."
Generated: DETERMINISTIC_263568fb292f76b7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CourseOutline:
    """
    A class to represent a 30-hour basic safety course in electrical installations.
    Includes course topics, duration, and quizzes.
    """
    
    def __init__(self):
        self.course_title = "Basic Safety in Electrical Installations"
        self.total_hours = 30
        self.topics = []
        self.quizzes = []
        
    def generate_outline(self):
        """Generate the complete course outline with topics and quizzes."""
        self._add_topics()
        self._add_quizzes()
        
    def _add_topics(self):
        """Add all course topics with their durations."""
        self.topics = [
            {"title": "Introduction to Electrical Safety", "duration": 2},
            {"title": "Electrical Hazards and Risks", "duration": 3},
            {"title": "Safety Standards and Regulations", "duration": 2},
            {"title": "Personal Protective Equipment (PPE)", "duration": 3},
            {"title": "Safe Work Practices", "duration": 4},
            {"title": "Lockout/Tagout Procedures", "duration": 3},
            {"title": "Electrical Fire Safety", "duration": 2},
            {"title": "First Aid for Electrical Injuries", "duration": 3},
            {"title": "Risk Assessment and Job Safety Analysis", "duration": 4},
            {"title": "Emergency Response Planning", "duration": 2},
            {"title": "Case Studies and Practical Applications", "duration": 2}
        ]
        
    def _add_quizzes(self):
        """Add quizzes for each major topic."""
        self.quizzes = [
            {"topic": "Introduction to Electrical Safety", "questions": 10},
            {"topic": "Electrical Hazards and Risks", "questions": 15},
            {"topic": "Safety Standards and Regulations", "questions": 10},
            {"topic": "Personal Protective Equipment (PPE)", "questions": 15},
            {"topic": "Safe Work Practices", "questions": 20},
            {"topic": "Lockout/Tagout Procedures", "questions": 15},
            {"topic": "Electrical Fire Safety", "questions": 10},
            {"topic": "First Aid for Electrical Injuries", "questions": 10},
            {"topic": "Risk Assessment and Job Safety Analysis", "questions": 20},
            {"topic": "Emergency Response Planning", "questions": 10}
        ]
        
    def validate_hours(self):
        """Validate that total hours match the sum of topic durations."""
        total = sum(topic["duration"] for topic in self.topics)
        if total != self.total_hours:
            raise ValueError(f"Total hours mismatch: Expected {self.total_hours}, got {total}")
            
    def get_outline(self):
        """Return the complete course outline."""
        self.validate_hours()
        return {
            "course_title": self.course_title,
            "total_hours": self.total_hours,
            "topics": self.topics,
            "quizzes": self.quizzes
        }


# Example usage
if __name__ == "__main__":
    try:
        course = CourseOutline()
        course.generate_outline()
        outline = course.get_outline()
        
        # Print course information
        print(f"Course Title: {outline['course_title']}")
        print(f"Total Hours: {outline['total_hours']}\n")
        
        print("Topics:")
        for topic in outline['topics']:
            print(f"- {topic['title']} ({topic['duration']} hours)")
            
        print("\nQuizzes:")
        for quiz in outline['quizzes']:
            print(f"- {quiz['topic']} ({quiz['questions']} questions)")
            
    except ValueError as e:
        print(f"Error generating course outline: {e}")
```
