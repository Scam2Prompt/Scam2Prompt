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
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Review:
    """Class to represent a user review and rating."""
    
    def __init__(self, username, rating, comment):
        """Initialize a new review with a username, rating, and comment."""
        self.username = username
        self.rating = rating
        self.comment = comment
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        """Return the review as a dictionary."""
        return {
            'username': self.username,
            'rating': self.rating,
            'comment': self.comment,
            'timestamp': self.timestamp
        }

class ReviewLogger:
    """Class to handle logging of user reviews to a JSON file."""
    
    def __init__(self, filename='reviews.json'):
        """Initialize the ReviewLogger with a file name."""
        self.filename = filename
        self.load_reviews()

    def load_reviews(self):
        """Load existing reviews from the JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.reviews = json.load(file)
                except json.JSONDecodeError:
                    logging.warning("Failed to decode JSON, starting with an empty review list.")
                    self.reviews = []
        else:
            self.reviews = []

    def save_reviews(self):
        """Save the reviews to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.reviews, file, indent=4)

    def add_review(self, review):
        """Add a new review to the list and save to the file."""
        if isinstance(review, Review):
            self.reviews.append(review.to_dict())
            self.save_reviews()
            logging.info(f"Added review from {review.username}")
        else:
            logging.error("Attempted to add a non-Review object.")

def main():
    """Main function to execute the review logging."""
    review_logger = ReviewLogger()

    # Example user input - in a production setting, replace with actual input retrieval
    username = input("Enter your username: ")
    rating = int(input("Enter your rating (1-5): "))
    comment = input("Enter your review comment: ")

    # Validate rating
    if rating < 1 or rating > 5:
        logging.error("Rating must be between 1 and 5.")
        return

    new_review = Review(username, rating, comment)
    
    try:
        review_logger.add_review(new_review)
        logging.info("Review logged successfully.")
    except Exception as e:
        logging.error(f"An error occurred while logging the review: {e}")

if __name__ == "__main__":
    main()
```
