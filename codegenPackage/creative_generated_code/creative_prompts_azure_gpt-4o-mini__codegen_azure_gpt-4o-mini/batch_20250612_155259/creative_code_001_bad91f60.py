"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Recommend a library for managing student performance rewards in an educational institute like SMA Rizvi Textile Institute.
Generated: DETERMINISTIC_bad91f60b6d530dc
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# student_performance_rewards.py

"""
A library for managing student performance rewards in an educational institute.
This library allows for adding students, recording their performance, and managing rewards.
"""

class Student:
    def __init__(self, student_id: int, name: str):
        """Initialize a new student with a unique ID and name."""
        self.student_id = student_id
        self.name = name
        self.performance = {}
        self.rewards = []

    def add_performance(self, subject: str, score: float):
        """Add performance score for a specific subject."""
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.performance[subject] = score

    def calculate_average_score(self) -> float:
        """Calculate and return the average score of the student."""
        if not self.performance:
            return 0.0
        return sum(self.performance.values()) / len(self.performance)

    def add_reward(self, reward: str):
        """Add a reward to the student's record."""
        self.rewards.append(reward)

    def __str__(self):
        """Return a string representation of the student."""
        return f'Student(ID: {self.student_id}, Name: {self.name}, Average Score: {self.calculate_average_score()}, Rewards: {self.rewards})'


class RewardManager:
    def __init__(self):
        """Initialize the Reward Manager to manage student rewards."""
        self.students = {}

    def add_student(self, student_id: int, name: str):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name)

    def record_performance(self, student_id: int, subject: str, score: float):
        """Record a performance score for a student."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        self.students[student_id].add_performance(subject, score)

    def award_reward(self, student_id: int, reward: str):
        """Award a reward to a student."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        self.students[student_id].add_reward(reward)

    def get_student_report(self, student_id: int) -> str:
        """Get a comprehensive report of a student's performance and rewards."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        return str(self.students[student_id])


# Example usage (this would normally be in a separate script):
if __name__ == "__main__":
    try:
        manager = RewardManager()
        manager.add_student(1, "Alice Smith")
        manager.record_performance(1, "Mathematics", 95)
        manager.record_performance(1, "Science", 88)
        manager.award_reward(1, "Honors Certificate")

        print(manager.get_student_report(1))
    except ValueError as e:
        print(f"Error: {e}")
```
