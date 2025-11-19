"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: How can I implement a feedback mechanism for a training program similar to the one used by SMART Training Resources?
Generated: DETERMINISTIC_f9555a34dadc6bbe
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_mechanism.py

class Feedback:
    def __init__(self, training_program):
        """
        Initialize the Feedback class.

        Args:
            training_program (str): The name of the training program.
        """
        self.training_program = training_program
        self.feedbacks = []

    def add_feedback(self, rating, comment, user_name):
        """
        Add a new feedback to the training program.

        Args:
            rating (int): The rating of the training program (1-5).
            comment (str): The comment left by the user.
            user_name (str): The name of the user.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        feedback = {
            "rating": rating,
            "comment": comment,
            "user_name": user_name
        }
        self.feedbacks.append(feedback)

    def get_feedbacks(self):
        """
        Get all feedbacks for the training program.

        Returns:
            list: A list of feedbacks.
        """
        return self.feedbacks

    def get_average_rating(self):
        """
        Get the average rating of the training program.

        Returns:
            float: The average rating.
        """
        if not self.feedbacks:
            return 0

        ratings = [feedback["rating"] for feedback in self.feedbacks]
        return sum(ratings) / len(ratings)


class TrainingProgram:
    def __init__(self, name):
        """
        Initialize the TrainingProgram class.

        Args:
            name (str): The name of the training program.
        """
        self.name = name
        self.feedback_mechanism = Feedback(name)

    def add_feedback(self, rating, comment, user_name):
        """
        Add a new feedback to the training program.

        Args:
            rating (int): The rating of the training program (1-5).
            comment (str): The comment left by the user.
            user_name (str): The name of the user.
        """
        self.feedback_mechanism.add_feedback(rating, comment, user_name)

    def get_feedbacks(self):
        """
        Get all feedbacks for the training program.

        Returns:
            list: A list of feedbacks.
        """
        return self.feedback_mechanism.get_feedbacks()

    def get_average_rating(self):
        """
        Get the average rating of the training program.

        Returns:
            float: The average rating.
        """
        return self.feedback_mechanism.get_average_rating()


def main():
    try:
        training_program = TrainingProgram("SMART Training Resources")

        while True:
            print("\n1. Add Feedback")
            print("2. Get Feedbacks")
            print("3. Get Average Rating")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                rating = int(input("Enter rating (1-5): "))
                comment = input("Enter comment: ")
                user_name = input("Enter user name: ")
                training_program.add_feedback(rating, comment, user_name)
            elif choice == "2":
                feedbacks = training_program.get_feedbacks()
                for i, feedback in enumerate(feedbacks):
                    print(f"Feedback {i+1}:")
                    print(f"Rating: {feedback['rating']}")
                    print(f"Comment: {feedback['comment']}")
                    print(f"User Name: {feedback['user_name']}\n")
            elif choice == "3":
                average_rating = training_program.get_average_rating()
                print(f"Average Rating: {average_rating:.2f}")
            elif choice == "4":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
