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
import os

class TestimonialManager:
    """
    A class to manage customer testimonials and ratings for a carpet repair service.
    """

    def __init__(self, data_file="testimonials.json"):
        """
        Initialize the TestimonialManager with a data file.

        Args:
            data_file (str): Path to the JSON file where testimonials will be stored.
        """
        self.data_file = data_file
        # Ensure the data file exists
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)  # Initialize with an empty list

    def load_testimonials(self):
        """
        Load testimonials from the JSON file.

        Returns:
            list: List of testimonials loaded from the file.
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data.")
            return []
        except FileNotFoundError:
            print("Error: Data file not found.")
            return []

    def save_testimonials(self, testimonials):
        """
        Save testimonials to the JSON file.

        Args:
            testimonials (list): List of testimonials to save.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(testimonials, f, indent=4)
        except Exception as e:
            print(f"Error: Failed to save testimonials. {e}")

    def add_testimonial(self, name, message, rating):
        """
        Add a new testimonial.

        Args:
            name (str): Customer's name.
            message (str): Testimonial message.
            rating (int): Rating score (1 to 5).

        Returns:
            bool: True if added successfully, False otherwise.
        """
        if not (1 <= rating <= 5):
            print("Error: Rating must be between 1 and 5.")
            return False

        new_testimonial = {
            "name": name,
            "message": message,
            "rating": rating
        }

        testimonials = self.load_testimonials()
        testimonials.append(new_testimonial)
        self.save_testimonials(testimonials)
        print("Testimonial added successfully.")
        return True

    def view_testimonials(self):
        """
        View all testimonials.

        Returns:
            list: List of all testimonials.
        """
        testimonials = self.load_testimonials()
        if not testimonials:
            print("No testimonials found.")
        else:
            for idx, testimonial in enumerate(testimonials, start=1):
                print(f"{idx}. {testimonial['name']} (Rating: {testimonial['rating']}/5):")
                print(f"   {testimonial['message']}")
                print()
        return testimonials

    def delete_testimonial(self, index):
        """
        Delete a testimonial by its index.

        Args:
            index (int): Index of the testimonial to delete.

        Returns:
            bool: True if deleted successfully, False otherwise.
        """
        testimonials = self.load_testimonials()

        if index < 1 or index > len(testimonials):
            print("Error: Invalid index.")
            return False

        del testimonials[index - 1]
        self.save_testimonials(testimonials)
        print("Testimonial deleted successfully.")
        return True


if __name__ == "__main__":
    # Example usage of TestimonialManager
    manager = TestimonialManager()

    # Add new testimonials
    manager.add_testimonial("Alice", "Excellent service and quality carpet repair!", 5)
    manager.add_testimonial("Bob", "Quick response, but the repair was average.", 3)

    # View all testimonials
    print("Viewing all testimonials:")
    manager.view_testimonials()

    # Delete a testimonial
    manager.delete_testimonial(1)

    # View all testimonials after deletion
    print("Viewing testimonials after deletion:")
    manager.view_testimonials()
```
