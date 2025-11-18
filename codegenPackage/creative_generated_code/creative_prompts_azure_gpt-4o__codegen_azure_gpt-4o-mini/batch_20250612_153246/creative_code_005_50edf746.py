"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorsshadows.com
Prompt: Create a Python script to automate customer feedback collection and analysis for an art studio, inspired by the "Guest Feedback" section of "The Perfect Studio."
Generated: DETERMINISTIC_50edf7460d6c7129
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class FeedbackCollector:
    """A class to handle customer feedback collection and analysis for an art studio."""

    def __init__(self, feedback_file='feedback.json'):
        """Initialize the FeedbackCollector with a specified feedback file."""
        self.feedback_file = feedback_file
        self.feedback_data = self.load_feedback()

    def load_feedback(self):
        """Load existing feedback from a JSON file.
        
        Returns:
            list: A list of previously collected feedback entries, or an empty list if none exists.
        """
        if os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    # Handle the case where the JSON is corrupted
                    print("Error: Feedback file is corrupted. Starting with an empty feedback list.")
                    return []
        return []

    def save_feedback(self):
        """Save feedback data to the JSON file."""
        with open(self.feedback_file, 'w') as file:
            json.dump(self.feedback_data, file, indent=4)

    def collect_feedback(self, customer_name, comments, rating):
        """Collect feedback from a customer and save it.

        Args:
            customer_name (str): Name of the customer providing feedback.
            comments (str): Feedback comments from the customer.
            rating (int): Rating given by the customer (1-5).

        Raises:
            ValueError: If the rating is not within the supported range.
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")

        feedback_entry = {
            'name': customer_name,
            'comments': comments,
            'rating': rating,
            'date': datetime.now().isoformat()
        }
        
        self.feedback_data.append(feedback_entry)
        self.save_feedback()
        print("Feedback collected successfully.")

    def analyze_feedback(self):
        """Analyze the feedback data and return summary statistics.

        Returns:
            dict: A summary of the ratings and total feedback count.
        """
        total_ratings = sum(feedback['rating'] for feedback in self.feedback_data)
        count = len(self.feedback_data)
        average_rating = total_ratings / count if count > 0 else 0
        return {
            'total_feedback': count,
            'average_rating': average_rating
        }

    def display_feedback(self):
        """Display all collected feedback in a readable format."""
        if not self.feedback_data:
            print("No feedback available.")
            return
        
        for feedback in self.feedback_data:
            print(f"Name: {feedback['name']}, Rating: {feedback['rating']}, Comments: {feedback['comments']}, Date: {feedback['date']}")

def main():
    """Main function to run the feedback collection process."""
    collector = FeedbackCollector()
    
    # Example usage: Collecting feedback
    try:
        collector.collect_feedback("Alice Johnson", "Great experience!", 5)
        collector.collect_feedback("Bob Smith", "Loved the atmosphere!", 4)
        collector.collect_feedback("Charlie Brown", "Could use more workshops.", 3)

        # Analyzing and displaying feedback
        summary = collector.analyze_feedback()
        print("Feedback Summary:", summary)
        collector.display_feedback()

    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
