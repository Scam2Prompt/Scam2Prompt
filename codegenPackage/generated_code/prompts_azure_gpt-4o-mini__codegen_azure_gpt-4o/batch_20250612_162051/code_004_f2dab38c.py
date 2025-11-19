"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Illustrate how to implement a customer feedback system in a computer repair service application, taking cues from the customer satisfaction guarantees of Geeks on Repair.
Generated: DETERMINISTIC_f2dab38cab6366d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_feedback_system.py

import json
import datetime

class FeedbackSystem:
    """
    A class to manage customer feedback for a computer repair service application.
    """

    def __init__(self, feedback_file="feedback.json"):
        """
        Initializes the feedback system with a file to store feedback data.
        :param feedback_file: Path to the JSON file where feedback will be stored.
        """
        self.feedback_file = feedback_file
        self._initialize_feedback_file()

    def _initialize_feedback_file(self):
        """
        Ensures the feedback file exists and initializes it if necessary.
        """
        try:
            # Check if the feedback file exists and is valid
            with open(self.feedback_file, 'r') as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Create a new feedback file if it doesn't exist or is invalid
            with open(self.feedback_file, 'w') as file:
                json.dump([], file)

    def submit_feedback(self, customer_name, rating, comments):
        """
        Submits customer feedback to the system.
        :param customer_name: Name of the customer providing feedback.
        :param rating: Customer satisfaction rating (1-5).
        :param comments: Additional comments from the customer.
        :return: None
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        feedback_entry = {
            "customer_name": customer_name,
            "rating": rating,
            "comments": comments,
            "timestamp": datetime.datetime.now().isoformat()
        }

        try:
            # Load existing feedback
            with open(self.feedback_file, 'r') as file:
                feedback_data = json.load(file)

            # Append new feedback
            feedback_data.append(feedback_entry)

            # Save updated feedback
            with open(self.feedback_file, 'w') as file:
                json.dump(feedback_data, file, indent=4)

        except Exception as e:
            print(f"Error saving feedback: {e}")
            raise

    def view_feedback(self):
        """
        Retrieves all customer feedback from the system.
        :return: List of feedback entries.
        """
        try:
            with open(self.feedback_file, 'r') as file:
                feedback_data = json.load(file)
            return feedback_data
        except Exception as e:
            print(f"Error reading feedback: {e}")
            raise

    def average_rating(self):
        """
        Calculates the average customer satisfaction rating.
        :return: Average rating as a float.
        """
        try:
            with open(self.feedback_file, 'r') as file:
                feedback_data = json.load(file)

            if not feedback_data:
                return 0.0  # No feedback available

            total_rating = sum(entry["rating"] for entry in feedback_data)
            return total_rating / len(feedback_data)

        except Exception as e:
            print(f"Error calculating average rating: {e}")
            raise


# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem()

    # Submit feedback
    try:
        feedback_system.submit_feedback("John Doe", 5, "Excellent service!")
        feedback_system.submit_feedback("Jane Smith", 4, "Good service, but room for improvement.")
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # View feedback
    try:
        feedback = feedback_system.view_feedback()
        print("Customer Feedback:")
        for entry in feedback:
            print(entry)
    except Exception as e:
        print(f"Error viewing feedback: {e}")

    # Calculate average rating
    try:
        avg_rating = feedback_system.average_rating()
        print(f"Average Customer Rating: {avg_rating:.2f}")
    except Exception as e:
        print(f"Error calculating average rating: {e}")
```
