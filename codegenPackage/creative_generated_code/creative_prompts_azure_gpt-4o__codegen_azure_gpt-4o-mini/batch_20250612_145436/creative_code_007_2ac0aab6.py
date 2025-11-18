"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Write code to automate customer reviews for products like the Edon Pressure Washer Electric 2.4, incorporating ratings and comments similar to those on Dotcom Machinery's site.
Generated: DETERMINISTIC_2ac0aab643ca468c
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime

class Review:
    """
    A class to represent a customer review for a product.
    Attributes:
        rating (int): The rating given by the customer, between 1 and 5.
        comment (str): The textual comment provided by the customer.
        date (datetime): The date when the review was created.
    """

    def __init__(self, rating: int, comment: str):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        self.rating = rating
        self.comment = comment
        self.date = datetime.now()

    def __str__(self):
        return f"Rating: {self.rating}, Comment: '{self.comment}', Date: {self.date.strftime('%Y-%m-%d')}"

class Product:
    """
    A class to represent a product and its reviews.
    Attributes:
        name (str): The name of the product.
        reviews (list): A list of Review objects associated with this product.
    """

    def __init__(self, name: str):
        self.name = name
        self.reviews = []

    def add_review(self, review: Review):
        """Adds a new review to the product's review list."""
        self.reviews.append(review)

    def average_rating(self) -> float:
        """Calculates the average rating of the product from its reviews."""
        if not self.reviews:
            return 0.0
        total = sum(review.rating for review in self.reviews)
        return total / len(self.reviews)

    def __str__(self):
        return f"Product: {self.name}, Average Rating: {self.average_rating():.2f}, Total Reviews: {len(self.reviews)}"

def generate_random_review() -> Review:
    """
    Generates a random review with a random rating and a sample comment.
    Returns:
        Review: A Review object with random data.
    """
    ratings = [1, 2, 3, 4, 5]
    comments = [
        "Excellent product!", 
        "Very satisfied!", 
        "It's okay, nothing special.", 
        "Not what I expected.", 
        "Terrible experience."
    ]
    
    rating = random.choice(ratings)
    comment = random.choice(comments)
    
    return Review(rating, comment)

def main():
    # Create a product instance
    product_name = "Edon Pressure Washer Electric 2.4"
    edon_pressure_washer = Product(product_name)

    # Generate and add random reviews
    review_count = 10  # You can change this number to generate more reviews
    for _ in range(review_count):
        try:
            review = generate_random_review()
            edon_pressure_washer.add_review(review)
            print(f"Added Review: {review}")
        except ValueError as e:
            print(f"Error adding review: {e}")

    # Display product details and average rating
    print(edon_pressure_washer)

if __name__ == "__main__":
    main()
```
