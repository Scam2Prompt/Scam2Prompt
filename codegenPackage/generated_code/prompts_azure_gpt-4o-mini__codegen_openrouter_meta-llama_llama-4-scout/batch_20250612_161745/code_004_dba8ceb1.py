"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Illustrate how to implement a feedback system for training sessions that captures participant satisfaction and ROI, as emphasized by Romain Rissoan in his consultancy work.
Generated: DETERMINISTIC_dba8ceb1bdda1809
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_system.py

from datetime import datetime
from typing import Dict, List

class TrainingSession:
    """Represents a training session with associated feedback."""

    def __init__(self, id: int, name: str, date: datetime):
        """
        Initializes a TrainingSession.

        Args:
        id (int): Unique identifier for the session.
        name (str): Name of the training session.
        date (datetime): Date the session took place.
        """
        self.id = id
        self.name = name
        self.date = date
        self.feedbacks = []

    def add_feedback(self, feedback: 'Feedback'):
        """Adds a feedback to the session."""
        self.feedbacks.append(feedback)


class Feedback:
    """Represents a participant's feedback for a training session."""

    def __init__(self, participant_name: str, satisfaction: int, roi: str, comments: str = ""):
        """
        Initializes a Feedback.

        Args:
        participant_name (str): Name of the participant.
        satisfaction (int): Satisfaction rating (1-5).
        roi (str): Perceived return on investment.
        comments (str): Additional comments. Defaults to "".
        """
        self.participant_name = participant_name
        self.satisfaction = satisfaction
        self.roi = roi
        self.comments = comments

    def __str__(self):
        return f"Participant: {self.participant_name}, Satisfaction: {self.satisfaction}, ROI: {self.roi}, Comments: {self.comments}"


class FeedbackSystem:
    """Manages training sessions and their associated feedback."""

    def __init__(self):
        self.sessions: Dict[int, TrainingSession] = {}

    def create_session(self, id: int, name: str, date: datetime):
        """
        Creates a new training session.

        Args:
        id (int): Unique identifier for the session.
        name (str): Name of the training session.
        date (datetime): Date the session took place.
        """
        if id in self.sessions:
            raise ValueError("Session ID already exists")

        self.sessions[id] = TrainingSession(id, name, date)

    def add_feedback(self, session_id: int, feedback: Feedback):
        """
        Adds a feedback to a training session.

        Args:
        session_id (int): ID of the session.
        feedback (Feedback): Feedback to add.

        Raises:
        ValueError: If the session ID does not exist.
        """
        if session_id not in self.sessions:
            raise ValueError("Session ID does not exist")

        self.sessions[session_id].add_feedback(feedback)

    def get_session_feedback(self, session_id: int) -> List[Feedback]:
        """
        Retrieves all feedback for a training session.

        Args:
        session_id (int): ID of the session.

        Returns:
        List[Feedback]: List of feedback for the session.

        Raises:
        ValueError: If the session ID does not exist.
        """
        if session_id not in self.sessions:
            raise ValueError("Session ID does not exist")

        return self.sessions[session_id].feedbacks


def main():
    # Example usage
    feedback_system = FeedbackSystem()

    # Create a training session
    session_date = datetime(2024, 9, 16)
    feedback_system.create_session(1, "Python Training", session_date)

    # Add feedback
    feedback1 = Feedback("John Doe", 4, "High", "Very informative")
    feedback2 = Feedback("Jane Doe", 5, "Excellent", "")
    feedback_system.add_feedback(1, feedback1)
    feedback_system.add_feedback(1, feedback2)

    # Retrieve and print session feedback
    try:
        feedbacks = feedback_system.get_session_feedback(1)
        for feedback in feedbacks:
            print(feedback)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
