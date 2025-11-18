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
# testimonials_manager.py

import json
import os


class TestimonialManager:
    """
    A class to manage and display testimonials for a hearing care solutions website.
    """

    def __init__(self, storage_file="testimonials.json"):
        """
        Initialize the TestimonialManager with a storage file.

        :param storage_file: Path to the JSON file where testimonials will be stored.
        """
        self.storage_file = storage_file
        self.testimonials = []

        # Load existing testimonials from the file if it exists
        self._load_testimonials()

    def _load_testimonials(self):
        """
        Load testimonials from the storage file.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as file:
                    self.testimonials = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading testimonials: {e}")
                self.testimonials = []

    def _save_testimonials(self):
        """
        Save testimonials to the storage file.
        """
        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.testimonials, file, indent=4)
        except IOError as e:
            print(f"Error saving testimonials: {e}")

    def add_testimonial(self, name, message, rating):
        """
        Add a new testimonial.

        :param name: Name of the person giving the testimonial.
        :param message: Testimonial message.
        :param rating: Rating out of 5.
        :return: None
        """
        # Validate inputs
        if not name or not message or not isinstance(rating, (int, float)) or rating < 0 or rating > 5:
            print("Invalid testimonial data. Ensure all fields are filled and the rating is between 0 and 5.")
            return

        testimonial = {
            "name": name,
            "message": message,
            "rating": rating
        }

        self.testimonials.append(testimonial)
        self._save_testimonials()
        print("Testimonial added successfully.")

    def display_testimonials(self):
        """
        Display all testimonials.
        """
        if not self.testimonials:
            print("No testimonials available.")
            return

        print("\n--- Testimonials ---")
        for idx, testimonial in enumerate(self.testimonials, start=1):
            print(f"{idx}. {testimonial['name']} (Rating: {testimonial['rating']}/5)")
            print(f"   \"{testimonial['message']}\"\n")

    def delete_testimonial(self, index):
        """
        Delete a testimonial by index.

        :param index: Index of the testimonial to delete (1-based).
        :return: None
        """
        try:
            index = int(index) - 1
            if index < 0 or index >= len(self.testimonials):
                print("Invalid index. Please try again.")
                return

            deleted_testimonial = self.testimonials.pop(index)
            self._save_testimonials()
            print(f"Deleted testimonial from {deleted_testimonial['name']} successfully.")
        except ValueError:
            print("Invalid index. Please provide a numeric value.")
        except Exception as e:
            print(f"Error deleting testimonial: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the manager with default storage file
    manager = TestimonialManager()

    while True:
        print("\nOptions:")
        print("1. Add Testimonial")
        print("2. Display Testimonials")
        print("3. Delete Testimonial")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            message = input("Enter testimonial message: ")
            try:
                rating = float(input("Enter rating (0-5): "))
            except ValueError:
                print("Invalid rating. Please try again.")
                continue
            manager.add_testimonial(name, message, rating)
        elif choice == "2":
            manager.display_testimonials()
        elif choice == "3":
            index = input("Enter the index of the testimonial to delete: ")
            manager.delete_testimonial(index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
```
