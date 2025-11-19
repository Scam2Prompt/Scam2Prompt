"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: Write Python code to design an e-learning platform for vocational education, incorporating blended virtual learning features like live lectures, online tutoring, self-paced learning, and assessment modules, as described on the AVEA website.
Generated: DETERMINISTIC_99a48a7bb524626b
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_learning_platform.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class UserRole(Enum):
    """User roles for the e-learning platform"""
    STUDENT = 1
    INSTRUCTOR = 2
    ADMIN = 3

class User:
    """Represents a user on the e-learning platform"""
    def __init__(self, id: int, name: str, email: str, role: UserRole):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

class Course:
    """Represents a course on the e-learning platform"""
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

class Module:
    """Represents a module within a course"""
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

class LiveLecture:
    """Represents a live lecture"""
    def __init__(self, id: int, title: str, start_time: datetime, end_time: datetime):
        self.id = id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

class OnlineTutoring:
    """Represents online tutoring session"""
    def __init__(self, id: int, title: str, start_time: datetime, end_time: datetime):
        self.id = id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

class SelfPacedLearning:
    """Represents self-paced learning module"""
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

class Assessment:
    """Represents an assessment"""
    def __init__(self, id: int, title: str, questions: List[Dict]):
        self.id = id
        self.title = title
        self.questions = questions

class ELearningPlatform:
    """E-learning platform for vocational education"""
    def __init__(self):
        self.users = []
        self.courses = []
        self.live_lectures = []
        self.online_tutoring_sessions = []
        self.self_paced_learning_modules = []
        self.assessments = []

    def register_user(self, user: User):
        """Registers a new user"""
        self.users.append(user)

    def create_course(self, course: Course):
        """Creates a new course"""
        self.courses.append(course)

    def schedule_live_lecture(self, live_lecture: LiveLecture):
        """Schedules a live lecture"""
        self.live_lectures.append(live_lecture)

    def schedule_online_tutoring(self, online_tutoring: OnlineTutoring):
        """Schedules online tutoring session"""
        self.online_tutoring_sessions.append(online_tutoring)

    def add_self_paced_learning_module(self, self_paced_learning: SelfPacedLearning):
        """Adds self-paced learning module"""
        self.self_paced_learning_modules.append(self_paced_learning)

    def create_assessment(self, assessment: Assessment):
        """Creates an assessment"""
        self.assessments.append(assessment)

def main():
    platform = ELearningPlatform()

    # Create users
    student = User(1, "John Doe", "john@example.com", UserRole.STUDENT)
    instructor = User(2, "Jane Doe", "jane@example.com", UserRole.INSTRUCTOR)
    platform.register_user(student)
    platform.register_user(instructor)

    # Create course
    course = Course(1, "Vocational Education", "Course description")
    platform.create_course(course)

    # Create live lecture
    live_lecture = LiveLecture(1, "Live Lecture 1", datetime(2024, 9, 16, 10, 0), datetime(2024, 9, 16, 11, 0))
    platform.schedule_live_lecture(live_lecture)

    # Create online tutoring session
    online_tutoring = OnlineTutoring(1, "Online Tutoring 1", datetime(2024, 9, 17, 10, 0), datetime(2024, 9, 17, 11, 0))
    platform.schedule_online_tutoring(online_tutoring)

    # Create self-paced learning module
    self_paced_learning = SelfPacedLearning(1, "Self-Paced Learning 1", "Module content")
    platform.add_self_paced_learning_module(self_paced_learning)

    # Create assessment
    assessment = Assessment(1, "Assessment 1", [{"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin"], "correct_answer": "Paris"}])
    platform.create_assessment(assessment)

if __name__ == "__main__":
    main()
```
