"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Write Python code to create a basic educational platform similar to the "Notebook" platform mentioned on the Del Sol Montessori website, allowing students and parents to track academic progress and communicate with teachers.
Generated: DETERMINISTIC_2224d19c172ae1f2
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# educational_platform.py

from datetime import datetime
from typing import List, Dict

class User:
    """Base class for users"""
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class Student(User):
    """Student class"""
    def __init__(self, id: int, name: str, email: str, grade: str):
        super().__init__(id, name, email)
        self.grade = grade
        self.progress: List[Dict] = []

    def add_progress(self, subject: str, score: float):
        """Add academic progress"""
        self.progress.append({
            "subject": subject,
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

class Parent(User):
    """Parent class"""
    def __init__(self, id: int, name: str, email: str, student_id: int):
        super().__init__(id, name, email)
        self.student_id = student_id

class Teacher(User):
    """Teacher class"""
    def __init__(self, id: int, name: str, email: str):
        super().__init__(id, name, email)

class EducationalPlatform:
    """Educational platform class"""
    def __init__(self):
        self.students: Dict[int, Student] = {}
        self.parents: Dict[int, Parent] = {}
        self.teachers: Dict[int, Teacher] = {}

    def add_student(self, student: Student):
        """Add student to platform"""
        self.students[student.id] = student

    def add_parent(self, parent: Parent):
        """Add parent to platform"""
        self.parents[parent.id] = parent

    def add_teacher(self, teacher: Teacher):
        """Add teacher to platform"""
        self.teachers[teacher.id] = teacher

    def get_student_progress(self, student_id: int):
        """Get student's academic progress"""
        if student_id in self.students:
            return self.students[student_id].progress
        else:
            raise ValueError("Student not found")

    def send_message(self, sender_id: int, recipient_id: int, message: str):
        """Send message between users"""
        if sender_id in self.students:
            sender = self.students[sender_id]
        elif sender_id in self.parents:
            sender = self.parents[sender_id]
        elif sender_id in self.teachers:
            sender = self.teachers[sender_id]
        else:
            raise ValueError("Sender not found")

        if recipient_id in self.students:
            recipient = self.students[recipient_id]
        elif recipient_id in self.parents:
            recipient = self.parents[recipient_id]
        elif recipient_id in self.teachers:
            recipient = self.teachers[recipient_id]
        else:
            raise ValueError("Recipient not found")

        print(f"Message from {sender.name} to {recipient.name}: {message}")

def main():
    platform = EducationalPlatform()

    # Create users
    student1 = Student(1, "John Doe", "john@example.com", "A")
    parent1 = Parent(2, "Jane Doe", "jane@example.com", 1)
    teacher1 = Teacher(3, "Ms. Smith", "smith@example.com")

    # Add users to platform
    platform.add_student(student1)
    platform.add_parent(parent1)
    platform.add_teacher(teacher1)

    # Add academic progress
    student1.add_progress("Math", 90.0)
    student1.add_progress("English", 85.0)

    # Get student's academic progress
    progress = platform.get_student_progress(1)
    print("Student's Progress:")
    for item in progress:
        print(f"Subject: {item['subject']}, Score: {item['score']}, Date: {item['date']}")

    # Send message
    platform.send_message(2, 3, "Hello, Ms. Smith! How is John doing?")

if __name__ == "__main__":
    main()
```
