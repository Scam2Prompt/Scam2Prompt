"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Generate a script to manage and display testimonials for a hearing care solutions website, inspired by the testimonials section on Otex.ae.
Generated: DETERMINISTIC_691341db503cbf13
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# testimonials_manager.py

import json
import os

class Testimonial:
    """Class to represent a single testimonial."""
    
    def __init__(self, name, message, rating):
        self.name = name
        self.message = message
        self.rating = rating

    def to_dict(self):
        """Convert the testimonial to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'message': self.message,
            'rating': self.rating
        }

class TestimonialManager:
    """Class to manage testimonials."""
    
    def __init__(self, file_path='testimonials.json'):
        self.file_path = file_path
        self.testimonials = []
        self.load_testimonials()

    def load_testimonials(self):
        """Load testimonials from a JSON file."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    testimonials_data = json.load(file)
                    self.testimonials = [Testimonial(**data) for data in testimonials_data]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading testimonials: {e}")
                self.testimonials = []

    def save_testimonials(self):
        """Save testimonials to a JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump([testimonial.to_dict() for testimonial in self.testimonials], file, indent=4)
        except IOError as e:
            print(f"Error saving testimonials: {e}")

    def add_testimonial(self, name, message, rating):
        """Add a new testimonial."""
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        new_testimonial = Testimonial(name, message, rating)
        self.testimonials.append(new_testimonial)
        self.save_testimonials()

    def display_testimonials(self):
        """Display all testimonials."""
        if not self.testimonials:
            print("No testimonials available.")
            return
        
        for testimonial in self.testimonials:
            print(f"Name: {testimonial.name}\nMessage: {testimonial.message}\nRating: {testimonial.rating}/5\n")

if __name__ == "__main__":
    # Example usage of the TestimonialManager
    manager = TestimonialManager()

    # Adding a new testimonial
    try:
        manager.add_testimonial("John Doe", "Great service and very helpful staff!", 5)
    except ValueError as e:
        print(e)

    # Displaying all testimonials
    manager.display_testimonials()
```
