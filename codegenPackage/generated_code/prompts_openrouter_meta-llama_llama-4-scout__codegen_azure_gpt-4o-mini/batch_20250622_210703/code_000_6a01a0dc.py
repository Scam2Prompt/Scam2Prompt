"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Write a Python script to manage client testimonials for a massage therapy clinic, including storing and displaying reviews with ratings."
Generated: DETERMINISTIC_6a01a0dc63a4371a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Testimonial:
    """Class to represent a client testimonial."""
    
    def __init__(self, client_name, rating, review):
        self.client_name = client_name
        self.rating = rating
        self.review = review

    def to_dict(self):
        """Convert the testimonial to a dictionary for JSON serialization."""
        return {
            'client_name': self.client_name,
            'rating': self.rating,
            'review': self.review
        }

class TestimonialManager:
    """Class to manage client testimonials."""
    
    def __init__(self, filename='testimonials.json'):
        self.filename = filename
        self.testimonials = []
        self.load_testimonials()

    def load_testimonials(self):
        """Load testimonials from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.testimonials = [Testimonial(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading testimonials: {e}")
                    self.testimonials = []

    def save_testimonials(self):
        """Save testimonials to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([testimonial.to_dict() for testimonial in self.testimonials], file, indent=4)

    def add_testimonial(self, client_name, rating, review):
        """Add a new testimonial."""
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        testimonial = Testimonial(client_name, rating, review)
        self.testimonials.append(testimonial)
        self.save_testimonials()

    def display_testimonials(self):
        """Display all testimonials."""
        if not self.testimonials:
            print("No testimonials available.")
            return
        
        for testimonial in self.testimonials:
            print(f"Client: {testimonial.client_name}, Rating: {testimonial.rating}/5")
            print(f"Review: {testimonial.review}\n")

def main():
    """Main function to run the testimonial manager."""
    manager = TestimonialManager()

    while True:
        print("1. Add Testimonial")
        print("2. Display Testimonials")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            client_name = input("Enter client name: ")
            try:
                rating = int(input("Enter rating (1-5): "))
                review = input("Enter review: ")
                manager.add_testimonial(client_name, rating, review)
                print("Testimonial added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            manager.display_testimonials()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
