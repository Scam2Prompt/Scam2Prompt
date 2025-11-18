"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Write code to implement a customer feedback system for home service providers, focusing on metrics like punctuality, affordability, and service quality, as described by شركة الاحترافية.
Generated: DETERMINISTIC_73c37f2f3b34ab01
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# customer_feedback_system.py

import json
import datetime

class FeedbackSystem:
    """
    A class to manage customer feedback for home service providers.

    Metrics:
    - Punctuality: Rating of provider's timeliness.
    - Affordability: Rating of pricing fairness.
    - Service Quality: Rating of service quality.
    """

    def __init__(self):
        # Initialize feedback storage
        self.feedback_storage = []

    def add_feedback(self, provider_name, customer_name, punctuality, affordability, service_quality, comments):
        """
        Add customer feedback to the system.

        Args:
            provider_name (str): Name of the service provider.
            customer_name (str): Name of the customer.
            punctuality (int): Rating for punctuality (1-5).
            affordability (int): Rating for affordability (1-5).
            service_quality (int): Rating for service quality (1-5).
            comments (str): Additional comments from the customer.
        """
        try:
            # Validate input ratings
            if not (1 <= punctuality <= 5):
                raise ValueError("Punctuality rating must be between 1 and 5.")
            if not (1 <= affordability <= 5):
                raise ValueError("Affordability rating must be between 1 and 5.")
            if not (1 <= service_quality <= 5):
                raise ValueError("Service quality rating must be between 1 and 5.")

            # Create feedback entry
            feedback_entry = {
                "timestamp": datetime.datetime.now().isoformat(),
                "provider_name": provider_name,
                "customer_name": customer_name,
                "ratings": {
                    "punctuality": punctuality,
                    "affordability": affordability,
                    "service_quality": service_quality
                },
                "comments": comments
            }

            # Store feedback
            self.feedback_storage.append(feedback_entry)
            print("Feedback added successfully!")

        except Exception as e:
            print(f"Error while adding feedback: {e}")

    def get_feedback(self):
        """
        Retrieve all feedback entries.
        
        Returns:
            list: List of feedback entries.
        """
        return self.feedback_storage

    def save_feedback_to_file(self, file_path):
        """
        Save feedback data to a file in JSON format.

        Args:
            file_path (str): Path to the file where feedback data will be stored.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.feedback_storage, file, indent=4)
            print(f"Feedback saved to {file_path} successfully!")
        except Exception as e:
            print(f"Error while saving feedback to file: {e}")

    def load_feedback_from_file(self, file_path):
        """
        Load feedback data from a file in JSON format.

        Args:
            file_path (str): Path to the file from which feedback data will be loaded.
        """
        try:
            with open(file_path, "r") as file:
                self.feedback_storage = json.load(file)
            print(f"Feedback loaded from {file_path} successfully!")
        except Exception as e:
            print(f"Error while loading feedback from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create FeedbackSystem instance
    feedback_system = FeedbackSystem()

    # Add feedback entries
    feedback_system.add_feedback(
        provider_name="شركة الاحترافية",
        customer_name="John Doe",
        punctuality=5,
        affordability=4,
        service_quality=5,
        comments="Excellent service. Highly recommended!"
    )

    feedback_system.add_feedback(
        provider_name="شركة الاحترافية",
        customer_name="Jane Smith",
        punctuality=4,
        affordability=5,
        service_quality=4,
        comments="Good service overall but could improve punctuality."
    )

    # Retrieve feedback
    all_feedback = feedback_system.get_feedback()
    print("All Feedback:")
    print(json.dumps(all_feedback, indent=4))

    # Save feedback to a file
    feedback_system.save_feedback_to_file("feedback.json")

    # Load feedback from a file
    feedback_system.load_feedback_from_file("feedback.json")
```
