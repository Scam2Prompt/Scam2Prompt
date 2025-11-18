"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Create a function to generate a report summarizing customer reviews and success stories, similar to those highlighted on the Financial Recovery Solutions Ltd website.
Generated: DETERMINISTIC_2f4c7a640acd532a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict


class Review:
    """Class to represent a customer review."""

    def __init__(self, customer_name: str, review_text: str, rating: int):
        """
        Initialize a new Review instance.

        :param customer_name: Name of the customer giving the review
        :param review_text: The content of the review
        :param rating: Rating given by the customer (1-5 scale)
        """
        self.customer_name = customer_name
        self.review_text = review_text
        self.rating = rating

    def to_dict(self) -> Dict:
        """Convert Review instance to dictionary format."""
        return {
            "customer_name": self.customer_name,
            "review_text": self.review_text,
            "rating": self.rating
        }


def generate_review_report(reviews: List[Review]) -> str:
    """
    Generate a summary report for a list of customer reviews.

    :param reviews: List of Review instances
    :return: JSON-formatted string summarizing the reviews
    """
    if not reviews:
        raise ValueError("The reviews list cannot be empty.")

    report_summary = {
        "total_reviews": len(reviews),
        "average_rating": sum(review.rating for review in reviews) / len(reviews),
        "reviews": [review.to_dict() for review in reviews]
    }

    return json.dumps(report_summary, indent=4)


if __name__ == "__main__":
    # Example usage
    try:
        sample_reviews = [
            Review("Alice Smith", "Excellent service and results!", 5),
            Review("Bob Johnson", "Very helpful and supportive team.", 4),
            Review("Charlie Brown", "My situation improved significantly.", 5),
            Review("Daisy Miller", "I am very satisfied with the outcome.", 4),
            Review("Eva Green", "Not what I expected, but okay.", 3)
        ]

        # Generate the review report
        report = generate_review_report(sample_reviews)
        print("Customer Review Report:")
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
