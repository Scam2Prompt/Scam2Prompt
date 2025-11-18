"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otex.ae
Prompt: Generate a script to manage and display testimonials for a hearing care solutions website, inspired by the testimonials section on Otex.ae.
Generated: DETERMINISTIC_691341db503cbf13
Batch ID: 20250612_153517
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

class Testimonial:
    """A class to represent a testimonial."""

    def __init__(self, name: str, message: str, rating: int):
        """
        Initializes a new Testimonial instance.

        Args:
            name (str): The name of the person giving the testimonial.
            message (str): The testimonial message.
            rating (int): A rating from 1 to 5.
        """
        self.name = name
        self.message = message
        self.rating = rating

    def to_dict(self) -> Dict:
        """Convert the testimonial to a dictionary."""
        return {
            'name': self.name,
            'message': self.message,
            'rating': self.rating
        }


class TestimonialManager:
    """A class to manage testimonials."""

    def __init__(self, file_path: str):
        """
        Initializes the TestimonialManager.

        Args:
            file_path (str): The file path to store testimonials.
        """
        self.file_path = file_path
        self.testimonials: List[Testimonial] = []
        self.load_testimonials()

    def load_testimonials(self):
        """Load testimonials from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for entry in data:
                    testimonial = Testimonial(
                        name=entry['name'],
                        message=entry['message'],
                        rating=entry['rating']
                    )
                    self.testimonials.append(testimonial)
        except FileNotFoundError:
            print("No testimonials found, starting fresh.")
        except json.JSONDecodeError:
            print("Error reading testimonials file, please check the format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_testimonials(self):
        """Save testimonials to a JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump([t.to_dict() for t in self.testimonials], file, indent=4)
        except Exception as e:
            print(f"Failed to save testimonials: {e}")

    def add_testimonial(self, name: str, message: str, rating: int):
        """
        Add a new testimonial.

        Args:
            name (str): The name of the person giving the testimonial.
            message (str): The testimonial message.
            rating (int): A rating from 1 to 5.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")

        new_testimonial = Testimonial(name, message, rating)
        self.testimonials.append(new_testimonial)
        self.save_testimonials()

    def display_testimonials(self):
        """Display all testimonials."""
        for testimonial in self.testimonials:
            print(f"{testimonial.name} (Rating: {testimonial.rating}): {testimonial.message}")


# Example usage:
if __name__ == "__main__":
    testimonial_manager = TestimonialManager("testimonials.json")

    # Add a new testimonial
    try:
        testimonial_manager.add_testimonial("John Doe", "Great service and support!", 5)
    except ValueError as e:
        print(e)

    # Display all testimonials
    testimonial_manager.display_testimonials()
```
