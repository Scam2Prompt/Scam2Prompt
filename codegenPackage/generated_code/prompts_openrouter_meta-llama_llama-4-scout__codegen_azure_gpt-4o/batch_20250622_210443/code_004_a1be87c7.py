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
# student_progress_tracker.py

import json
from datetime import datetime

class Student:
    """
    Represents a student in the language learning program.
    Tracks personal details, engagement metrics, and skill development progress.
    """
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.engagement_metrics = {
            "sessions_completed": 0,
            "time_spent_minutes": 0,
            "active_days": set()
        }
        self.skill_development = {
            "vocabulary_mastery": 0,  # Percentage (0-100)
            "grammar_mastery": 0,     # Percentage (0-100)
            "listening_comprehension": 0,  # Percentage (0-100)
            "speaking_proficiency": 0      # Percentage (0-100)
        }
        self.activity_log = []  # Logs of activities with timestamps

    def log_activity(self, activity_type, time_spent_minutes):
        """
        Logs an activity and updates engagement metrics.
        :param activity_type: Type of activity (e.g., "lesson", "quiz", "practice").
        :param time_spent_minutes: Time spent on the activity in minutes.
        """
        self.engagement_metrics["sessions_completed"] += 1
        self.engagement_metrics["time_spent_minutes"] += time_spent_minutes
        self.engagement_metrics["active_days"].add(datetime.now().date())
        self.activity_log.append({
            "activity_type": activity_type,
            "time_spent_minutes": time_spent_minutes,
            "timestamp": datetime.now().isoformat()
        })

    def update_skill_progress(self, skill, progress_percentage):
        """
        Updates the skill development progress for a specific skill.
        :param skill: Skill name (e.g., "vocabulary_mastery").
        :param progress_percentage: Progress percentage (0-100).
        """
        if skill in self.skill_development:
            self.skill_development[skill] = max(0, min(100, progress_percentage))  # Ensure valid range
        else:
            raise ValueError(f"Invalid skill name: {skill}")

    def get_summary(self):
        """
        Returns a summary of the student's progress and engagement.
        :return: Dictionary containing engagement metrics and skill development.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "engagement_metrics": self.engagement_metrics,
            "skill_development": self.skill_development,
            "activity_log": self.activity_log
        }


class LanguageLearningProgram:
    """
    Represents the language learning program.
    Manages students and provides analytics on their progress.
    """
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, email):
        """
        Adds a new student to the program.
        :param student_id: Unique identifier for the student.
        :param name: Name of the student.
        :param email: Email address of the student.
        """
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name, email)

    def get_student(self, student_id):
        """
        Retrieves a student by their ID.
        :param student_id: Unique identifier for the student.
        :return: Student object.
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        return self.students[student_id]

    def generate_program_report(self):
        """
        Generates a report summarizing the progress of all students.
        :return: JSON string containing the report.
        """
        report = {
            "total_students": len(self.students),
            "students": [student.get_summary() for student in self.students.values()]
        }
        return json.dumps(report, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the program
        program = LanguageLearningProgram()

        # Add students
        program.add_student("S001", "Alice Johnson", "alice@example.com")
        program.add_student("S002", "Bob Smith", "bob@example.com")

        # Log activities and update progress for Alice
        alice = program.get_student("S001")
        alice.log_activity("lesson", 45)
        alice.log_activity("quiz", 30)
        alice.update_skill_progress("vocabulary_mastery", 80)
        alice.update_skill_progress("grammar_mastery", 70)

        # Log activities and update progress for Bob
        bob = program.get_student("S002")
        bob.log_activity("practice", 60)
        bob.update_skill_progress("listening_comprehension", 85)
        bob.update_skill_progress("speaking_proficiency", 90)

        # Generate and print program report
        print(program.generate_program_report())

    except Exception as e:
        print(f"Error: {e}")
```
