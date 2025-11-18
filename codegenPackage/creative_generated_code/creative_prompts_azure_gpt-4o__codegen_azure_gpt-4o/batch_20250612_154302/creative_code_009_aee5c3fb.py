"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vagopros.com
Prompt: Write code to implement a user feedback system for virtual assistance services, inspired by Vagopros' customer-centric approach.
Generated: DETERMINISTIC_aee5c3fb7372f3d8
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Feedback System for Virtual Assistance Services
Inspired by Vagopros' customer-centric approach
"""

import json

class FeedbackSystem:
    def __init__(self, feedback_file="feedback.json"):
        """
        Initializes the FeedbackSystem with a file to store feedback.
        
        :param feedback_file: File path to store feedback data, default is 'feedback.json'.
        """
        self.feedback_file = feedback_file
        self.feedback_data = self._load_feedback()

    def _load_feedback(self):
        """
        Loads existing feedback from the specified file.
        
        :return: A dictionary containing feedback data.
        """
        try:
            with open(self.feedback_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty dictionary
            return {}
        except json.JSONDecodeError:
            # Handle corrupted JSON files
            print("Warning: Feedback file is corrupted. Starting fresh.")
            return {}

    def save_feedback(self):
        """
        Saves the current feedback data to the specified file.
        """
        try:
            with open(self.feedback_file, "w") as file:
                json.dump(self.feedback_data, file, indent=4)
        except Exception as e:
            print(f"Error saving feedback: {e}")

    def submit_feedback(self, user_id, feedback_text, rating):
        """
        Submits feedback for a user.
        
        :param user_id: Unique identifier for the user.
        :param feedback_text: Text of the feedback provided by the user.
        :param rating: Rating provided by the user (integer between 1 and 5).
        :return: None
        """
        if not (1 <= rating <= 5):
            print("Error: Rating must be between 1 and 5.")
            return

        if user_id not in self.feedback_data:
            self.feedback_data[user_id] = []

        self.feedback_data[user_id].append({
            "feedback_text": feedback_text,
            "rating": rating
        })
        
        self.save_feedback()
        print("Feedback submitted successfully!")

    def get_feedback_summary(self):
        """
        Provides a summary of feedback, including average rating and total feedback count.
        
        :return: A dictionary containing summary data.
        """
        total_feedback = 0
        total_rating = 0

        for feedbacks in self.feedback_data.values():
            total_feedback += len(feedbacks)
            total_rating += sum(feedback["rating"] for feedback in feedbacks)

        # Avoid division by zero
        average_rating = total_rating / total_feedback if total_feedback > 0 else 0

        return {
            "total_feedback_count": total_feedback,
            "average_rating": round(average_rating, 2)
        }

    def display_all_feedback(self):
        """
        Displays all feedback stored in the system.
        """
        if not self.feedback_data:
            print("No feedback available yet.")
            return

        print("All Feedback:")
        for user_id, feedbacks in self.feedback_data.items():
            print(f"User ID: {user_id}")
            for feedback in feedbacks:
                print(f"  - Feedback: {feedback['feedback_text']}")
                print(f"  - Rating: {feedback['rating']}")
            print()

# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem()

    # Submit feedback
    feedback_system.submit_feedback(user_id="user123", feedback_text="Great service!", rating=5)
    feedback_system.submit_feedback(user_id="user123", feedback_text="Very helpful.", rating=4)

    # Display feedback summary
    summary = feedback_system.get_feedback_summary()
    print(f"Feedback Summary: {summary}")

    # Display all feedback
    feedback_system.display_all_feedback()
```
