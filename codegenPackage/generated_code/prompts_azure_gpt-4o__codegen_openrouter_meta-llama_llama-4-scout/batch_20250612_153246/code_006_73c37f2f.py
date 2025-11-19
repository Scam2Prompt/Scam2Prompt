"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Write code to implement a customer feedback system for home service providers, focusing on metrics like punctuality, affordability, and service quality, as described by شركة الاحترافية.
Generated: DETERMINISTIC_73c37f2f3b34ab01
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_feedback_system.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class Rating(Enum):
    """ Enum for ratings """
    POOR = 1
    AVERAGE = 2
    GOOD = 3
    EXCELLENT = 4
    OUTSTANDING = 5

class Feedback:
    """ Class to represent customer feedback """
    def __init__(self, 
                 provider_name: str, 
                 punctuality: Rating, 
                 affordability: Rating, 
                 service_quality: Rating, 
                 comments: str = ""):
        """
        Initialize a Feedback object.

        Args:
        - provider_name (str): Name of the service provider.
        - punctuality (Rating): Rating for punctuality.
        - affordability (Rating): Rating for affordability.
        - service_quality (Rating): Rating for service quality.
        - comments (str): Additional comments. Defaults to an empty string.
        """
        self.provider_name = provider_name
        self.punctuality = punctuality
        self.affordability = affordability
        self.service_quality = service_quality
        self.comments = comments
        self.created_at = datetime.now()

class CustomerFeedbackSystem:
    """ Class to manage customer feedback """
    def __init__(self):
        self.feedbacks: Dict[str, List[Feedback]] = {}

    def add_feedback(self, feedback: Feedback):
        """
        Add feedback for a service provider.

        Args:
        - feedback (Feedback): Feedback object to add.
        """
        if feedback.provider_name not in self.feedbacks:
            self.feedbacks[feedback.provider_name] = []
        self.feedbacks[feedback.provider_name].append(feedback)

    def get_feedbacks(self, provider_name: str) -> List[Feedback]:
        """
        Get all feedbacks for a service provider.

        Args:
        - provider_name (str): Name of the service provider.

        Returns:
        - List[Feedback]: List of feedbacks for the provider.
        """
        return self.feedbacks.get(provider_name, [])

    def calculate_average_rating(self, provider_name: str) -> Dict[str, float]:
        """
        Calculate the average rating for a service provider.

        Args:
        - provider_name (str): Name of the service provider.

        Returns:
        - Dict[str, float]: Dictionary with average ratings for punctuality, affordability, and service quality.
        """
        feedbacks = self.get_feedbacks(provider_name)
        if not feedbacks:
            return {
                "punctuality": 0.0,
                "affordability": 0.0,
                "service_quality": 0.0
            }

        total_punctuality = sum([f.punctuality.value for f in feedbacks])
        total_affordability = sum([f.affordability.value for f in feedbacks])
        total_service_quality = sum([f.service_quality.value for f in feedbacks])

        average_punctuality = total_punctuality / len(feedbacks)
        average_affordability = total_affordability / len(feedbacks)
        average_service_quality = total_service_quality / len(feedbacks)

        return {
            "punctuality": average_punctuality,
            "affordability": average_affordability,
            "service_quality": average_service_quality
        }

def main():
    # Example usage
    system = CustomerFeedbackSystem()

    feedback1 = Feedback(
        "Provider1", 
        Rating.EXCELLENT, 
        Rating.GOOD, 
        Rating.OUTSTANDING, 
        "Excellent service!"
    )
    feedback2 = Feedback(
        "Provider1", 
        Rating.GOOD, 
        Rating.AVERAGE, 
        Rating.EXCELLENT, 
        "Good service, but a bit pricey."
    )
    feedback3 = Feedback(
        "Provider2", 
        Rating.POOR, 
        Rating.POOR, 
        Rating.AVERAGE, 
        "Poor service, avoid this provider."
    )

    system.add_feedback(feedback1)
    system.add_feedback(feedback2)
    system.add_feedback(feedback3)

    print("Feedbacks for Provider1:")
    for feedback in system.get_feedbacks("Provider1"):
        print(f"Punctuality: {feedback.punctuality.name}, Affordability: {feedback.affordability.name}, Service Quality: {feedback.service_quality.name}")

    print("\nAverage Ratings for Provider1:")
    average_ratings = system.calculate_average_rating("Provider1")
    print(f"Punctuality: {average_ratings['punctuality']:.2f}, Affordability: {average_ratings['affordability']:.2f}, Service Quality: {average_ratings['service_quality']:.2f}")

if __name__ == "__main__":
    main()
```
