"""
Generated Code Metadata:
========================
Original URL: https://finishdrop.com
Prompt: Generate code to implement a feature that tracks and displays user testimonials about e-commerce performance, as seen on FinishDrop's website.
Generated: DETERMINISTIC_cef8bd8c5212f2a9
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# testimonials.py

from datetime import datetime
from typing import List, Dict

class Testimonial:
    """Represents a user testimonial."""

    def __init__(self, id: int, user_name: str, rating: int, review: str, created_at: datetime):
        """
        Initializes a Testimonial object.

        Args:
        id (int): Unique identifier for the testimonial.
        user_name (str): Name of the user who wrote the testimonial.
        rating (int): Rating given by the user (1-5).
        review (str): The testimonial text.
        created_at (datetime): Timestamp when the testimonial was created.
        """
        self.id = id
        self.user_name = user_name
        self.rating = rating
        self.review = review
        self.created_at = created_at

class TestimonialService:
    """Manages user testimonials."""

    def __init__(self):
        # In-memory storage for simplicity; consider a database in production
        self.testimonials: List[Testimonial] = []

    def add_testimonial(self, testimonial: Testimonial):
        """Adds a new testimonial."""
        self.testimonials.append(testimonial)

    def get_testimonials(self) -> List[Testimonial]:
        """Retrieves all testimonials."""
        return self.testimonials

    def get_average_rating(self) -> float:
        """Calculates the average rating of all testimonials."""
        if not self.testimonials:
            return 0.0
        ratings = [t.rating for t in self.testimonials]
        return sum(ratings) / len(ratings)

class TestimonialRepository:
    """Handles data storage and retrieval for testimonials."""

    def __init__(self, db_name: str):
        # Initialize a simple in-memory data store
        self.db_name = db_name
        self.testimonials: Dict[int, Testimonial] = {}

    def save_testimonial(self, testimonial: Testimonial):
        """Saves a testimonial to the repository."""
        self.testimonials[testimonial.id] = testimonial

    def get_testimonial(self, id: int) -> Testimonial:
        """Retrieves a testimonial by ID."""
        return self.testimonials.get(id)

def main():
    # Create a testimonial service
    service = TestimonialService()

    # Create a testimonial repository
    repository = TestimonialRepository("testimonials.db")

    try:
        # Create testimonials
        testimonial1 = Testimonial(1, "John Doe", 5, "Excellent service!", datetime(2022, 1, 1))
        testimonial2 = Testimonial(2, "Jane Doe", 4, "Good experience.", datetime(2022, 1, 15))

        # Add testimonials to service and repository
        service.add_testimonial(testimonial1)
        service.add_testimonial(testimonial2)
        repository.save_testimonial(testimonial1)
        repository.save_testimonial(testimonial2)

        # Display testimonials
        print("Testimonials:")
        for testimonial in service.get_testimonials():
            print(f"ID: {testimonial.id}, User: {testimonial.user_name}, Rating: {testimonial.rating}, Review: {testimonial.review}")

        # Display average rating
        print(f"\nAverage Rating: {service.get_average_rating():.2f}")

        # Retrieve a testimonial from the repository
        retrieved_testimonial = repository.get_testimonial(1)
        if retrieved_testimonial:
            print(f"\nRetrieved Testimonial: {retrieved_testimonial.user_name}, Rating: {retrieved_testimonial.rating}, Review: {retrieved_testimonial.review}")
        else:
            print("\nTestimonial not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
