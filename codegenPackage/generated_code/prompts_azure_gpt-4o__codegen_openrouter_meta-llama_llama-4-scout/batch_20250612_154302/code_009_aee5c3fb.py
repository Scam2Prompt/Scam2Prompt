"""
Generated Code Metadata:
========================
Original URL: https://vagopros.com
Prompt: Write code to implement a user feedback system for virtual assistance services, inspired by Vagopros' customer-centric approach.
Generated: DETERMINISTIC_aee5c3fb7372f3d8
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_feedback_system.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class FeedbackRating(Enum):
    """Enum for feedback ratings"""
    POOR = 1
    AVERAGE = 2
    GOOD = 3
    EXCELLENT = 4

class UserFeedback:
    """Class to represent user feedback"""
    def __init__(self, user_id: int, service_id: int, rating: FeedbackRating, comment: str):
        """
        Initialize user feedback

        Args:
        - user_id (int): ID of the user
        - service_id (int): ID of the virtual assistance service
        - rating (FeedbackRating): Rating given by the user
        - comment (str): Comment provided by the user
        """
        self.user_id = user_id
        self.service_id = service_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()

class FeedbackRepository:
    """Class to manage user feedback repository"""
    def __init__(self):
        self.feedbacks: List[UserFeedback] = []

    def add_feedback(self, feedback: UserFeedback):
        """Add user feedback to the repository"""
        self.feedbacks.append(feedback)

    def get_feedbacks(self, service_id: int = None) -> List[UserFeedback]:
        """
        Get user feedbacks

        Args:
        - service_id (int): ID of the virtual assistance service (optional)

        Returns:
        - List[UserFeedback]: List of user feedbacks
        """
        if service_id:
            return [f for f in self.feedbacks if f.service_id == service_id]
        return self.feedbacks

    def get_average_rating(self, service_id: int) -> float:
        """
        Get average rating for a virtual assistance service

        Args:
        - service_id (int): ID of the virtual assistance service

        Returns:
        - float: Average rating
        """
        feedbacks = self.get_feedbacks(service_id)
        if not feedbacks:
            return 0.0
        ratings = [f.rating.value for f in feedbacks]
        return sum(ratings) / len(ratings)

class UserFeedbackSystem:
    """Class to manage user feedback system"""
    def __init__(self):
        self.repository = FeedbackRepository()

    def submit_feedback(self, user_id: int, service_id: int, rating: int, comment: str):
        """
        Submit user feedback

        Args:
        - user_id (int): ID of the user
        - service_id (int): ID of the virtual assistance service
        - rating (int): Rating given by the user
        - comment (str): Comment provided by the user

        Raises:
        - ValueError: If rating is invalid
        """
        try:
            rating_enum = FeedbackRating(rating)
        except ValueError:
            raise ValueError("Invalid rating")

        feedback = UserFeedback(user_id, service_id, rating_enum, comment)
        self.repository.add_feedback(feedback)

    def get_feedbacks(self, service_id: int = None) -> List[UserFeedback]:
        """
        Get user feedbacks

        Args:
        - service_id (int): ID of the virtual assistance service (optional)

        Returns:
        - List[UserFeedback]: List of user feedbacks
        """
        return self.repository.get_feedbacks(service_id)

    def get_average_rating(self, service_id: int) -> float:
        """
        Get average rating for a virtual assistance service

        Args:
        - service_id (int): ID of the virtual assistance service

        Returns:
        - float: Average rating
        """
        return self.repository.get_average_rating(service_id)

def main():
    # Example usage
    system = UserFeedbackSystem()

    system.submit_feedback(1, 1, 4, "Excellent service!")
    system.submit_feedback(2, 1, 3, "Good service.")
    system.submit_feedback(3, 2, 2, "Average service.")

    feedbacks = system.get_feedbacks(1)
    for feedback in feedbacks:
        print(f"User {feedback.user_id}: {feedback.rating.name} - {feedback.comment}")

    average_rating = system.get_average_rating(1)
    print(f"Average rating for service 1: {average_rating:.2f}")

if __name__ == "__main__":
    main()
```
