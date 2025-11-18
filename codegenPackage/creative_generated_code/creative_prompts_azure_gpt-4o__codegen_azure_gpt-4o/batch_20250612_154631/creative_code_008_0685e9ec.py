"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Write code to implement a client feedback system for an investment platform, inspired by the testimonials section on Finance Investment Limited's website.
Generated: DETERMINISTIC_0685e9ec2d6545b3
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class FeedbackSystem:
    """
    A class to implement a client feedback system for an investment platform.
    Handles storage, retrieval, and validation of user testimonials.
    """

    def __init__(self, storage_file='feedback.json'):
        """
        Initialize the FeedbackSystem.
        
        :param storage_file: File to store feedback data (default: 'feedback.json').
        """
        self.storage_file = storage_file
        self.feedback_data = []

        # Load existing feedback data from storage
        self._load_feedback()

    def _load_feedback(self):
        """
        Private method to load feedback data from the storage file.
        Creates the file if it does not exist.
        """
        try:
            with open(self.storage_file, 'r') as file:
                self.feedback_data = json.load(file)
        except FileNotFoundError:
            # Create a new file if it doesn't exist
            self.feedback_data = []
            self._save_feedback()
        except json.JSONDecodeError:
            # Handle corrupted files gracefully
            print("Error: Feedback file is corrupted. Starting with empty feedback list.")
            self.feedback_data = []

    def _save_feedback(self):
        """
        Private method to save feedback data to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.feedback_data, file, indent=4)
        except Exception as e:
            print(f"Error saving feedback data: {e}")

    def add_feedback(self, name, message, rating):
        """
        Add new feedback to the system.

        :param name: Client's name (string).
        :param message: Client's feedback message (string).
        :param rating: Client's rating (integer, 1-5).
        :return: Confirmation message.
        """
        # Validate inputs
        if not name or not message or not isinstance(rating, int) or not (1 <= rating <= 5):
            return "Error: Invalid feedback data. Ensure name, message, and a rating between 1-5 are provided."

        # Create feedback entry
        feedback_entry = {
            "name": name,
            "message": message,
            "rating": rating,
            "timestamp": datetime.now().isoformat()
        }

        # Add entry to feedback list and save to storage
        self.feedback_data.append(feedback_entry)
        self._save_feedback()
        return "Feedback submitted successfully."

    def get_feedback(self):
        """
        Retrieve all feedback from the system.

        :return: List of feedback entries.
        """
        return self.feedback_data

    def get_average_rating(self):
        """
        Calculate and return the average rating from all feedback.

        :return: Average rating (float) or None if no feedback exists.
        """
        if not self.feedback_data:
            return None

        total_rating = sum(entry['rating'] for entry in self.feedback_data)
        return round(total_rating / len(self.feedback_data), 2)


# Example usage of the FeedbackSystem class
if __name__ == "__main__":
    # Initialize the feedback system
    feedback_system = FeedbackSystem()

    # Add feedback entries
    print(feedback_system.add_feedback("Alice", "Great Investment Platform!", 5))
    print(feedback_system.add_feedback("Bob", "Helpful customer service.", 4))
    print(feedback_system.add_feedback("Charlie", "Needs improvement in mobile app experience.", 3))

    # Retrieve and display all feedback
    print("All Feedback:")
    for feedback in feedback_system.get_feedback():
        print(feedback)

    # Display average rating
    print(f"Average Rating: {feedback_system.get_average_rating()}")
```
