"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Illustrate how to implement a customer feedback system in a tech store setting, referencing the customer trust highlighted by Akash Infotech.
Generated: DETERMINISTIC_a91ed2a9c2ff8afe
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: customer_feedback_system.py

import json

# Define a class to represent a feedback system
class CustomerFeedbackSystem:
    """
    A class to manage customer feedback for a tech store, inspired by Akash Infotech's customer trust principles.
    """

    def __init__(self, feedback_file='feedback_data.json'):
        """
        Initializes the feedback system.

        :param feedback_file: Path to the JSON file where feedback data will be stored.
        """
        self.feedback_file = feedback_file
        self.feedback_data = self._load_feedback()

    def _load_feedback(self):
        """
        Loads feedback data from the JSON file.

        :return: A list of feedback records if file exists; otherwise, an empty list.
        """
        try:
            with open(self.feedback_file, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            # Return an empty list if the file doesn't exist
            return []
        except json.JSONDecodeError:
            # Handle case where the JSON file is corrupted
            print("Error: Feedback file is corrupted, starting fresh.")
            return []

    def add_feedback(self, customer_name, rating, comments):
        """
        Adds new feedback to the system.

        :param customer_name: Name of the customer providing feedback.
        :param rating: Rating score given by the customer (1-5).
        :param comments: Additional comments provided by the customer.
        """
        if not (1 <= rating <= 5):
            print("Error: Rating must be between 1 and 5.")
            return

        new_feedback = {
            "customer_name": customer_name,
            "rating": rating,
            "comments": comments
        }
        self.feedback_data.append(new_feedback)
        self._save_feedback()

    def _save_feedback(self):
        """
        Saves the current feedback data to the JSON file.
        """
        try:
            with open(self.feedback_file, 'w') as file:
                json.dump(self.feedback_data, file, indent=4)
        except IOError:
            print("Error: Unable to save feedback data.")

    def display_feedback(self):
        """
        Displays all feedback records in a readable format.
        """
        if not self.feedback_data:
            print("No feedback available yet.")
            return

        print("\nCustomer Feedback:")
        print("-" * 30)
        for feedback in self.feedback_data:
            print(f"Customer Name: {feedback['customer_name']}")
            print(f"Rating: {feedback['rating']}/5")
            print(f"Comments: {feedback['comments']}")
            print("-" * 30)

    def average_rating(self):
        """
        Calculates and displays the average rating.

        :return: The average rating score as a float, or None if no feedback exists.
        """
        if not self.feedback_data:
            print("No feedback available to calculate average rating.")
            return None

        total_rating = sum(feedback['rating'] for feedback in self.feedback_data)
        avg_rating = total_rating / len(self.feedback_data)
        print(f"Average Rating: {avg_rating:.2f}/5")
        return avg_rating


# Main function to demonstrate the feedback system
def main():
    """
    Main function to run the customer feedback system.
    """
    feedback_system = CustomerFeedbackSystem()

    print("Welcome to the Tech Store Customer Feedback System")
    while True:
        print("\nOptions:")
        print("1. Add Feedback")
        print("2. Display Feedback")
        print("3. Show Average Rating")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            customer_name = input("Enter customer name: ").strip()
            try:
                rating = int(input("Enter rating (1-5): "))
            except ValueError:
                print("Error: Rating must be a number between 1 and 5.")
                continue
            comments = input("Enter comments: ").strip()
            feedback_system.add_feedback(customer_name, rating, comments)
        elif choice == 2:
            feedback_system.display_feedback()
        elif choice == 3:
            feedback_system.average_rating()
        elif choice == 4:
            print("Thank you for using the feedback system. Goodbye!")
            break
        else:
            print("Error: Invalid choice, please select again.")


# Entry point for the script
if __name__ == "__main__":
    main()
```
