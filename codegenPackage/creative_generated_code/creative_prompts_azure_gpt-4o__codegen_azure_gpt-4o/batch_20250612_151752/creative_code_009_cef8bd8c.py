"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Generate code to implement a feature that tracks and displays user testimonials about e-commerce performance, as seen on FinishDrop's website.
Generated: DETERMINISTIC_cef8bd8c5212f2a9
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# testimonials.py

import json
import datetime
from typing import List, Dict


class Testimonial:
    """
    A class representing a single user testimonial.
    """

    def __init__(self, user_name: str, message: str, rating: int):
        """
        Initializes a Testimonial object.

        :param user_name: Name of the user providing the testimonial
        :param message: The testimonial message
        :param rating: The rating provided (scale of 1 to 5)
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")

        self.user_name = user_name
        self.message = message
        self.rating = rating
        self.timestamp = datetime.datetime.now()

    def to_dict(self) -> Dict:
        """
        Converts the Testimonial object into a dictionary.

        :return: Dictionary representation of the testimonial
        """
        return {
            "user_name": self.user_name,
            "message": self.message,
            "rating": self.rating,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }


class TestimonialManager:
    """
    A class to manage storing and displaying testimonials.
    """

    def __init__(self, storage_file: str = "testimonials.json"):
        """
        Initializes the TestimonialManager.

        :param storage_file: File to store testimonials persistently
        """
        self.storage_file = storage_file
        self.testimonials = self._load_testimonials()

    def _load_testimonials(self) -> List[Testimonial]:
        """
        Loads testimonials from the storage file.

        :return: List of Testimonial objects
        """
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                return [
                    Testimonial(
                        user_name=item["user_name"],
                        message=item["message"],
                        rating=item["rating"],
                    )
                    for item in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist or is malformed; start with empty list
            return []

    def add_testimonial(self, user_name: str, message: str, rating: int) -> None:
        """
        Adds a new testimonial and saves it to the storage file.

        :param user_name: Name of the user
        :param message: Testimonial message
        :param rating: Rating provided (scale of 1 to 5)
        """
        new_testimonial = Testimonial(user_name, message, rating)
        self.testimonials.append(new_testimonial)
        self._save_testimonials()

    def _save_testimonials(self) -> None:
        """
        Saves testimonials to the storage file.
        """
        try:
            with open(self.storage_file, "w") as f:
                json.dump(
                    [testimonial.to_dict() for testimonial in self.testimonials],
                    f,
                    indent=4,
                )
        except IOError as e:
            print(f"Error saving testimonials: {e}")

    def display_testimonials(self) -> None:
        """
        Displays all testimonials.
        """
        print("User Testimonials:\n")
        for testimonial in self.testimonials:
            print(f"User: {testimonial.user_name}")
            print(f"Message: {testimonial.message}")
            print(f"Rating: {testimonial.rating} / 5")
            print(f"Timestamp: {testimonial.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 40)


# Example usage (only for demonstration; remove in production)
if __name__ == "__main__":
    manager = TestimonialManager()

    # Add sample testimonials
    try:
        manager.add_testimonial("Alice", "Great service!", 5)
        manager.add_testimonial("Bob", "Fast shipping.", 4)
    except ValueError as e:
        print(f"Error adding testimonial: {e}")

    # Display testimonials
    manager.display_testimonials()
```
