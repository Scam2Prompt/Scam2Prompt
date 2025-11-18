"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Develop a script to manage customer testimonials and ratings for carpet repair services, inspired by the testimonial section of Perfect Melbourne Carpet.
Generated: DETERMINISTIC_be31eb8d05544924
Batch ID: 20250612_154740
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

class Testimonial:
    """Class to represent a customer testimonial."""

    def __init__(self, customer_name: str, rating: int, message: str) -> None:
        """
        Initialize a new testimonial.

        :param customer_name: Name of the customer
        :param rating: Rating given by the customer (1 to 5)
        :param message: Testimonial message
        """
        self.customer_name = customer_name
        self.rating = rating
        self.message = message

        # Validate rating
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the testimonial to a dictionary format."""
        return {
            "customer_name": self.customer_name,
            "rating": self.rating,
            "message": self.message
        }

class TestimonialManager:
    """Class to manage customer testimonials."""

    def __init__(self, file_path: str) -> None:
        """
        Initialize the testimonial manager.

        :param file_path: Path to the JSON file storing testimonials
        """
        self.file_path = file_path
        self.testimonials: List[Testimonial] = self.load_testimonials()

    def load_testimonials(self) -> List[Testimonial]:
        """Load testimonials from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Testimonial(**item) for item in data]
        except FileNotFoundError:
            return []  # Return empty list if file does not exist
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the testimonials file.")

    def save_testimonials(self) -> None:
        """Save testimonials to a JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump([testimonial.to_dict() for testimonial in self.testimonials], file, indent=4)

    def add_testimonial(self, customer_name: str, rating: int, message: str) -> None:
        """Add a new testimonial."""
        new_testimonial = Testimonial(customer_name, rating, message)
        self.testimonials.append(new_testimonial)
        self.save_testimonials()

    def get_all_testimonials(self) -> List[Testimonial]:
        """Retrieve all testimonials."""
        return self.testimonials

    def get_average_rating(self) -> float:
        """Calculate the average rating of all testimonials."""
        if not self.testimonials:
            return 0.0
        total_rating = sum(testimonial.rating for testimonial in self.testimonials)
        return total_rating / len(self.testimonials)

if __name__ == "__main__":
    # Example usage
    manager = TestimonialManager("testimonials.json")

    # Adding a new testimonial
    try:
        manager.add_testimonial("John Doe", 5, "Excellent carpet repair service!")
    except ValueError as e:
        print(f"Error adding testimonial: {e}")

    # Retrieving all testimonials
    for testimonial in manager.get_all_testimonials():
        print(f"{testimonial.customer_name}: {testimonial.rating} - {testimonial.message}")

    # Getting average rating
    average_rating = manager.get_average_rating()
    print(f"Average Rating: {average_rating:.2f}")
```
