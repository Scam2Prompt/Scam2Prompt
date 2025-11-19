"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Write a Python script to manage a TV aerial installation company's client reviews and ratings, including storing customer feedback and calculating overall ratings.
Generated: DETERMINISTIC_62c83f7ae358acbc
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Review:
    """Class to represent a customer review."""
    
    def __init__(self, customer_name: str, rating: int, feedback: str):
        """
        Initialize a new review.

        :param customer_name: Name of the customer
        :param rating: Rating given by the customer (1 to 5)
        :param feedback: Feedback provided by the customer
        """
        self.customer_name = customer_name
        self.rating = rating
        self.feedback = feedback

    def to_dict(self) -> Dict[str, Any]:
        """Convert the review to a dictionary for easy storage."""
        return {
            "customer_name": self.customer_name,
            "rating": self.rating,
            "feedback": self.feedback
        }

class ReviewManager:
    """Class to manage customer reviews."""
    
    def __init__(self, filename: str):
        """
        Initialize the ReviewManager with a file to store reviews.

        :param filename: The filename where reviews will be stored
        """
        self.filename = filename
        self.reviews: List[Review] = []
        self.load_reviews()

    def load_reviews(self):
        """Load reviews from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                reviews_data = json.load(file)
                self.reviews = [Review(**review) for review in reviews_data]
        except FileNotFoundError:
            # If the file does not exist, we start with an empty review list
            self.reviews = []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file. Starting with an empty review list.")
            self.reviews = []

    def save_reviews(self):
        """Save the current reviews to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([review.to_dict() for review in self.reviews], file, indent=4)

    def add_review(self, customer_name: str, rating: int, feedback: str):
        """
        Add a new review to the list and save it.

        :param customer_name: Name of the customer
        :param rating: Rating given by the customer (1 to 5)
        :param feedback: Feedback provided by the customer
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        
        new_review = Review(customer_name, rating, feedback)
        self.reviews.append(new_review)
        self.save_reviews()

    def calculate_average_rating(self) -> float:
        """Calculate the average rating from all reviews."""
        if not self.reviews:
            return 0.0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

    def get_reviews(self) -> List[Dict[str, Any]]:
        """Get a list of all reviews as dictionaries."""
        return [review.to_dict() for review in self.reviews]

if __name__ == "__main__":
    # Example usage of the ReviewManager
    review_manager = ReviewManager('reviews.json')

    # Adding a new review
    try:
        review_manager.add_review("John Doe", 5, "Excellent service!")
        review_manager.add_review("Jane Smith", 4, "Very good, but could improve on timing.")
    except ValueError as e:
        print(f"Error adding review: {e}")

    # Calculating average rating
    average_rating = review_manager.calculate_average_rating()
    print(f"Average Rating: {average_rating:.2f}")

    # Displaying all reviews
    all_reviews = review_manager.get_reviews()
    print("All Reviews:")
    for review in all_reviews:
        print(review)
```
