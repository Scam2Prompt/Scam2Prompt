"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Describe how to implement a customer feedback system for a travel agency that specializes in luxury safaris, ensuring exceptional service is highlighted.
Generated: DETERMINISTIC_c27fc978d5a5b59f
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Feedback:
    """Class to handle customer feedback for a luxury safari travel agency."""
    
    def __init__(self, customer_name: str, rating: int, comments: str):
        """
        Initialize the Feedback object.
        
        :param customer_name: Name of the customer providing feedback
        :param rating: Rating given by the customer (1 to 5)
        :param comments: Feedback comments provided by the customer
        """
        self.customer_name = customer_name
        self.rating = self.validate_rating(rating)
        self.comments = comments

    @staticmethod
    def validate_rating(rating: int) -> int:
        """Validate that the rating is within the acceptable range (1 to 5)."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

class FeedbackSystem:
    """Class to manage feedback submissions and retrieval."""
    
    def __init__(self):
        """Initialize the feedback system with an empty feedback list."""
        self.feedback_list: List[Feedback] = []

    def submit_feedback(self, feedback: Feedback) -> None:
        """
        Submit feedback to the system.
        
        :param feedback: An instance of Feedback to store
        """
        self.feedback_list.append(feedback)
    
    def get_feedback_summary(self) -> Dict[str, Any]:
        """
        Generate a summary of all feedback received.
        
        :return: A summary including average rating and comments
        """
        if not self.feedback_list:
            return {'average_rating': 0, 'comments': []}
        
        total_rating = sum(f.rating for f in self.feedback_list)
        average_rating = total_rating / len(self.feedback_list)
        comments = [f.comments for f in self.feedback_list]
        
        return {
            'average_rating': round(average_rating, 2),
            'comments': comments
        }

    def save_feedback_to_file(self, filename: str) -> None:
        """
        Save feedback to a JSON file.
        
        :param filename: The name of the file to save feedback to
        """
        try:
            with open(filename, 'w') as file:
                json.dump([feedback.__dict__ for feedback in self.feedback_list], file)
        except IOError as e:
            print(f"Error saving feedback to file: {e}")

    def load_feedback_from_file(self, filename: str) -> None:
        """
        Load feedback from a JSON file.
        
        :param filename: The name of the file to load feedback from
        """
        try:
            with open(filename, 'r') as file:
                feedback_data = json.load(file)
                for entry in feedback_data:
                    feedback = Feedback(entry['customer_name'], entry['rating'], entry['comments'])
                    self.submit_feedback(feedback)
        except (IOError, ValueError) as e:
            print(f"Error loading feedback from file: {e}")

# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem()
    
    # Submit some feedback
    try:
        feedback1 = Feedback("Alice Smith", 5, "The safari experience was unforgettable!")
        feedback2 = Feedback("John Doe", 4, "Great service, but the accommodations could be improved.")
        feedback_system.submit_feedback(feedback1)
        feedback_system.submit_feedback(feedback2)
        
        # Save feedback to file
        feedback_system.save_feedback_to_file("feedback.json")
        
        # Load feedback from file
        feedback_system.load_feedback_from_file("feedback.json")
        
        # Get feedback summary
        summary = feedback_system.get_feedback_summary()
        print(f"Average Rating: {summary['average_rating']}")
        print("Comments:")
        for comment in summary['comments']:
            print(f"- {comment}")
    except ValueError as e:
        print(f"Invalid input: {e}")
```
