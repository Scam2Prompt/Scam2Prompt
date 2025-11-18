"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Write a program to simulate customer reviews for promotional products, incorporating feedback examples from the Merchandiso website.
Generated: DETERMINISTIC_051dd11994a1e2bc
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class CustomerReview:
    """Class to represent a customer review."""
    product_name: str
    rating: int  # Rating from 1 to 5
    review_text: str
    reviewer_name: str

    def to_dict(self):
        """Convert the review to a dictionary format."""
        return asdict(self)

class ReviewSimulator:
    """A class to simulate customer reviews for promotional products."""

    def __init__(self, products: List[str]):
        """
        Initialize the simulator with a list of products.

        :param products: List of product names to simulate reviews for.
        """
        self.products = products
        self.reviews = []

    def generate_review(self, product_name: str) -> CustomerReview:
        """
        Generate a random customer review for a given product.

        :param product_name: The name of the product to review.
        :return: A CustomerReview object.
        """
        # Define possible ratings and sample review texts
        ratings = [1, 2, 3, 4, 5]
        review_texts = [
            "Amazing product! Exceeded my expectations.",
            "Good quality but had some issues.",
            "It's okay, not what I expected.",
            "Pretty decent product for the price.",
            "Absolutely love it! Will buy again."
        ]
        
        # Generate random rating and review text
        rating = random.choice(ratings)
        review_text = random.choice(review_texts)
        reviewer_name = f"Customer{random.randint(1, 1000)}"

        return CustomerReview(product_name, rating, review_text, reviewer_name)

    def simulate_reviews(self, num_reviews: int):
        """
        Simulate a number of reviews for the products.

        :param num_reviews: The total number of reviews to generate.
        """
        try:
            if num_reviews < 1:
                raise ValueError("Number of reviews must be at least 1.")
            for _ in range(num_reviews):
                product_name = random.choice(self.products)
                review = self.generate_review(product_name)
                self.reviews.append(review)
        except Exception as e:
            print(f"Error during review simulation: {e}")

    def get_reviews(self) -> List[dict]:
        """
        Get the list of generated reviews in dictionary format.

        :return: A list of reviews as dictionaries.
        """
        return [review.to_dict() for review in self.reviews]


if __name__ == "__main__":
    # List of promotional products
    promotional_products = [
        "Wireless Headphones",
        "Smartwatch",
        "Portable Charger",
        "Bluetooth Speaker",
        "Fitness Tracker"
    ]

    # Create an instance of ReviewSimulator
    simulator = ReviewSimulator(promotional_products)

    # Simulate 10 customer reviews
    simulator.simulate_reviews(10)

    # Retrieve and print the simulated reviews
    reviews = simulator.get_reviews()
    for review in reviews:
        print(review)
```
