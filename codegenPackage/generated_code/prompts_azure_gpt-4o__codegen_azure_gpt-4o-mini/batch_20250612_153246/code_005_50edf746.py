"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Create a Python script to automate customer feedback collection and analysis for an art studio, inspired by the "Guest Feedback" section of "The Perfect Studio."
Generated: DETERMINISTIC_50edf7460d6c7129
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class FeedbackCollector:
    """Class to collect and analyze customer feedback for an art studio."""

    def __init__(self, feedback_file='feedback.json'):
        """
        Initializes the FeedbackCollector with a specified feedback file.

        Args:
            feedback_file (str): The path to the JSON file where feedback will be stored.
        """
        self.feedback_file = feedback_file
        self.feedback_data = self.load_feedback()

    def load_feedback(self):
        """Loads feedback data from the JSON file, if it exists."""
        if os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Feedback file is corrupted. Starting with an empty list.")
                    return []
        return []

    def save_feedback(self):
        """Saves the current feedback data to the JSON file."""
        with open(self.feedback_file, 'w') as file:
            json.dump(self.feedback_data, file, indent=4)

    def collect_feedback(self, customer_name, feedback_text, rating):
        """
        Collects feedback from a customer.

        Args:
            customer_name (str): The name of the customer providing feedback.
            feedback_text (str): The feedback text provided by the customer.
            rating (int): The rating given by the customer (1-5).

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        feedback_entry = {
            'customer_name': customer_name,
            'feedback_text': feedback_text,
            'rating': rating,
            'timestamp': datetime.now().isoformat()
        }
        self.feedback_data.append(feedback_entry)
        self.save_feedback()

    def analyze_feedback(self):
        """Analyzes the feedback and returns a summary of ratings."""
        if not self.feedback_data:
            return "No feedback available for analysis."

        total_ratings = sum(entry['rating'] for entry in self.feedback_data)
        average_rating = total_ratings / len(self.feedback_data)
        return {
            'total_feedback': len(self.feedback_data),
            'average_rating': average_rating,
            'feedback_details': self.feedback_data
        }

def main():
    """Main function to run the feedback collection process."""
    collector = FeedbackCollector()

    while True:
        print("\n--- Customer Feedback Collection ---")
        customer_name = input("Enter your name: ")
        feedback_text = input("Enter your feedback: ")
        try:
            rating = int(input("Rate your experience (1-5): "))
            collector.collect_feedback(customer_name, feedback_text, rating)
            print("Thank you for your feedback!")
        except ValueError as e:
            print(f"Error: {e}")

        another = input("Would you like to submit another feedback? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Analyze and display feedback summary
    summary = collector.analyze_feedback()
    print("\n--- Feedback Summary ---")
    print(json.dumps(summary, indent=4))

if __name__ == "__main__":
    main()
```
