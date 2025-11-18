"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Write a script to manage customer reviews and satisfaction ratings for cleaning services. Include functionality to store feedback and calculate overall satisfaction scores.
Generated: DETERMINISTIC_c4f92a7425aab3f0
Batch ID: 20250612_153224
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

class ReviewManager:
    """A class to manage customer reviews and calculate satisfaction scores."""

    def __init__(self, filename: str):
        """
        Initializes the ReviewManager with a specified file to store reviews.

        :param filename: The name of the file where reviews will be stored.
        """
        self.filename = filename
        self.reviews = self.load_reviews()

    def load_reviews(self) -> List[Dict[str, Any]]:
        """Loads reviews from the specified file. Returns an empty list if the file does not exist."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: File is not a valid JSON.")
            return []

    def save_reviews(self):
        """Saves the current list of reviews back to the specified file."""
        with open(self.filename, 'w') as file:
            json.dump(self.reviews, file, indent=4)

    def add_review(self, customer_name: str, rating: int, feedback: str):
        """
        Adds a new review to the review list.

        :param customer_name: The name of the customer providing the review.
        :param rating: The rating given by the customer (1-5).
        :param feedback: The feedback text provided by the customer.
        :raises ValueError: If the rating is not between 1 and 5.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        
        review = {
            'customer_name': customer_name,
            'rating': rating,
            'feedback': feedback
        }
        self.reviews.append(review)
        self.save_reviews()

    def calculate_overall_satisfaction(self) -> float:
        """
        Calculates the overall satisfaction score based on the average rating.

        :return: The average rating as a float, or 0 if no reviews exist.
        """
        if not self.reviews:
            return 0.0
        
        total_rating = sum(review['rating'] for review in self.reviews)
        average_rating = total_rating / len(self.reviews)
        return round(average_rating, 2)

    def get_reviews(self) -> List[Dict[str, Any]]:
        """Returns the list of all reviews."""
        return self.reviews

# Example usage
if __name__ == "__main__":
    review_manager = ReviewManager('reviews.json')

    # Adding a sample review
    try:
        review_manager.add_review("Alice Smith", 5, "Excellent cleaning service!")
    except ValueError as e:
        print(f"Error adding review: {e}")

    # Calculating overall satisfaction
    overall_satisfaction = review_manager.calculate_overall_satisfaction()
    print(f"Overall Satisfaction Score: {overall_satisfaction}")

    # Retrieving all reviews
    all_reviews = review_manager.get_reviews()
    print("All Reviews:", all_reviews)
```
