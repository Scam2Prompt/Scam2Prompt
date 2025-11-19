"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Develop a script to manage customer testimonials and ratings for carpet repair services, inspired by the testimonial section of Perfect Melbourne Carpet.
Generated: DETERMINISTIC_be31eb8d05544924
Batch ID: 20250612_154740
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

class Testimonial:
    """Class to represent a customer testimonial."""
    
    def __init__(self, customer_name: str, rating: int, message: str):
        """
        Initialize a new Testimonial instance.

        :param customer_name: Name of the customer providing the testimonial.
        :param rating: Rating given by the customer (1 to 5).
        :param message: The testimonial message from the customer.
        """
        self.customer_name = customer_name
        self.rating = self.validate_rating(rating)
        self.message = message

    @staticmethod
    def validate_rating(rating: int) -> int:
        """Validate the rating to ensure it is between 1 and 5."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def to_dict(self) -> Dict[str, Any]:
        """Convert the testimonial to a dictionary format."""
        return {
            "customer_name": self.customer_name,
            "rating": self.rating,
            "message": self.message
        }

class TestimonialManager:
    """Class to manage a collection of testimonials."""
    
    def __init__(self, filename: str):
        """
        Initialize the TestimonialManager with a file to store testimonials.

        :param filename: The filename where testimonials will be saved.
        """
        self.filename = filename
        self.testimonials: List[Testimonial] = self.load_testimonials()

    def load_testimonials(self) -> List[Testimonial]:
        """Load testimonials from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Testimonial(**item) for item in data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file.")
            return []

    def save_testimonials(self) -> None:
        """Save testimonials to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([testimonial.to_dict() for testimonial in self.testimonials], file, indent=4)

    def add_testimonial(self, customer_name: str, rating: int, message: str) -> None:
        """Add a new testimonial to the collection and save it."""
        try:
            new_testimonial = Testimonial(customer_name, rating, message)
            self.testimonials.append(new_testimonial)
            self.save_testimonials()
        except ValueError as e:
            print(f"Error adding testimonial: {e}")

    def get_all_testimonials(self) -> List[Testimonial]:
        """Retrieve all testimonials."""
        return self.testimonials

# Example usage
if __name__ == "__main__":
    manager = TestimonialManager("testimonials.json")
    
    # Adding a new testimonial
    manager.add_testimonial("John Doe", 5, "Excellent carpet repair service!")
    
    # Retrieving all testimonials
    for testimonial in manager.get_all_testimonials():
        print(f"{testimonial.customer_name} rated {testimonial.rating}: {testimonial.message}")
```
