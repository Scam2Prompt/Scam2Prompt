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
# customer_feedback.py

class Feedback:
    """
    A class to represent customer feedback for a computer repair service.
    """

    def __init__(self, customer_name, service_rating, comments):
        """
        Initializes the Feedback object with customer details.

        :param customer_name: str - Name of the customer providing feedback
        :param service_rating: int - Rating given by the customer (1 to 5)
        :param comments: str - Additional comments from the customer
        """
        self.customer_name = customer_name
        self.service_rating = service_rating
        self.comments = comments

        # Validate the service rating
        if not (1 <= self.service_rating <= 5):
            raise ValueError("Service rating must be between 1 and 5.")

    def __str__(self):
        """
        Returns a string representation of the feedback.
        """
        return f"Feedback from {self.customer_name}: Rating {self.service_rating}/5 - {self.comments}"


class FeedbackSystem:
    """
    A class to manage customer feedback for the repair service.
    """

    def __init__(self):
        """
        Initializes the FeedbackSystem with an empty feedback list.
        """
        self.feedback_list = []

    def add_feedback(self, feedback):
        """
        Adds feedback to the feedback list.

        :param feedback: Feedback - An instance of the Feedback class
        """
        if not isinstance(feedback, Feedback):
            raise TypeError("Expected an instance of Feedback.")
        self.feedback_list.append(feedback)

    def get_average_rating(self):
        """
        Calculates the average rating from the feedback list.

        :return: float - The average rating, or 0 if no feedback is present
        """
        if not self.feedback_list:
            return 0.0
        total_rating = sum(f.service_rating for f in self.feedback_list)
        return total_rating / len(self.feedback_list)

    def display_feedback(self):
        """
        Displays all feedback in the system.
        """
        if not self.feedback_list:
            print("No feedback available.")
            return
        for feedback in self.feedback_list:
            print(feedback)


# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem()

    # Sample feedback entries
    try:
        feedback1 = Feedback("Alice", 5, "Excellent service, very satisfied!")
        feedback2 = Feedback("Bob", 4, "Good service, but could be faster.")
        feedback3 = Feedback("Charlie", 2, "Service was okay, but not what I expected.")

        feedback_system.add_feedback(feedback1)
        feedback_system.add_feedback(feedback2)
        feedback_system.add_feedback(feedback3)

        # Display all feedback
        feedback_system.display_feedback()

        # Calculate and display average rating
        average_rating = feedback_system.get_average_rating()
        print(f"Average Rating: {average_rating:.2f}/5")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
