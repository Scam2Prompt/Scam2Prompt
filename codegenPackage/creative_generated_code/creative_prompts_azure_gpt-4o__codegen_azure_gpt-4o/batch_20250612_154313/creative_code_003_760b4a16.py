"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devv.sellpass.io
Prompt: Create a script to log user reviews and ratings dynamically, referencing the review functionality mentioned on the Devv website.
Generated: DETERMINISTIC_760b4a165b47180d
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

class ReviewLogger:
    """
    A class to log user reviews and ratings dynamically.
    """

    def __init__(self, log_file='reviews.json'):
        """
        Initializes the ReviewLogger with a log file.
        :param log_file: The file where reviews will be stored. Defaults to 'reviews.json'.
        """
        self.log_file = log_file

        # Initialize the log file if it doesn't exist
        try:
            with open(self.log_file, 'r') as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.log_file, 'w') as file:
                json.dump([], file)  # Create an empty list in the file

    def add_review(self, user_name, rating, comment):
        """
        Adds a review to the log file.
        :param user_name: Name of the user submitting the review.
        :param rating: A numeric rating (1-5).
        :param comment: A text comment describing the review.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        review = {
            "user_name": user_name,
            "rating": rating,
            "comment": comment,
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Append the review to the log file
        try:
            with open(self.log_file, 'r') as file:
                reviews = json.load(file)

            reviews.append(review)

            with open(self.log_file, 'w') as file:
                json.dump(reviews, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to log review: {e}")

    def get_reviews(self):
        """
        Retrieves all reviews from the log file.
        :return: A list of reviews.
        """
        try:
            with open(self.log_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve reviews: {e}")


if __name__ == "__main__":
    # Example Usage
    logger = ReviewLogger()

    try:
        # Add a new review
        logger.add_review(user_name="John Doe", rating=5, comment="Amazing product!")

        # Retrieve and print all reviews
        reviews = logger.get_reviews()
        print("Current Reviews:")
        for review in reviews:
            print(review)
    except Exception as e:
        print(f"Error: {e}")
```
