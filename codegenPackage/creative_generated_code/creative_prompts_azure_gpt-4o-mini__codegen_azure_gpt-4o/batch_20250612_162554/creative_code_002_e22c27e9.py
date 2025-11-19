"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Can you provide a code snippet for integrating a feedback system for UMKM using the guidelines from leprettystellar.com?
Generated: DETERMINISTIC_e22c27e90b35ce2b
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_system.py
import json
import datetime

# Feedback Class to handle storing and retrieving feedback
class FeedbackSystem:
    def __init__(self, feedback_file="feedback.json"):
        """
        Initialize the feedback system with a JSON file to store feedback data.

        :param feedback_file: File path for storing feedback data.
        """
        self.feedback_file = feedback_file
        self._load_feedback()

    def _load_feedback(self):
        """
        Load feedback from the file. Create the file if it does not exist.
        """
        try:
            with open(self.feedback_file, "r") as file:
                self.feedback_data = json.load(file)
        except FileNotFoundError:
            self.feedback_data = []  # Initialize empty feedback list if file not found
        except json.JSONDecodeError:
            self.feedback_data = []  # Initialize empty feedback list if JSON is invalid

    def _save_feedback(self):
        """
        Save feedback data to the file.
        """
        try:
            with open(self.feedback_file, "w") as file:
                json.dump(self.feedback_data, file, indent=4)
        except IOError as e:
            print(f"Error saving feedback data: {e}")

    def add_feedback(self, user_name, feedback_text, rating):
        """
        Add a new feedback entry to the system.

        :param user_name: Name of the user providing feedback.
        :param feedback_text: Feedback content.
        :param rating: Rating provided by the user (integer between 1 and 5).
        :raises ValueError: If rating is not in the valid range.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")

        feedback_entry = {
            "user_name": user_name,
            "feedback_text": feedback_text,
            "rating": rating,
            "timestamp": datetime.datetime.now().isoformat(),
        }

        self.feedback_data.append(feedback_entry)
        self._save_feedback()

    def get_feedback(self):
        """
        Retrieve all feedback entries.

        :return: List of feedback entries.
        """
        return self.feedback_data

    def get_average_rating(self):
        """
        Calculate the average rating from all feedback entries.

        :return: Average rating (float), or None if no feedback exists.
        """
        if not self.feedback_data:
            return None  # No ratings available

        total_rating = sum(entry["rating"] for entry in self.feedback_data)
        return round(total_rating / len(self.feedback_data), 2)


# Example usage:
if __name__ == "__main__":
    feedback_system = FeedbackSystem()

    # Adding feedback
    try:
        feedback_system.add_feedback("Alice", "Great service!", 5)
        feedback_system.add_feedback("Bob", "Good selection of products.", 4)
        feedback_system.add_feedback("Charlie", "Needs improvement.", 2)
    except ValueError as e:
        print(f"Error adding feedback: {e}")

    # Retrieving feedback
    all_feedback = feedback_system.get_feedback()
    print("Feedback Entries:")
    for entry in all_feedback:
        print(entry)

    # Calculating average rating
    avg_rating = feedback_system.get_average_rating()
    print(f"Average Rating: {avg_rating if avg_rating else 'No ratings yet'}")
```
