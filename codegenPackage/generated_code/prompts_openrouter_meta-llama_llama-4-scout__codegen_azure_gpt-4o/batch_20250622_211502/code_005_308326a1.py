"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: "Create a Python script to manage client testimonials for a wedding photography business, allowing for easy addition, removal, and display of testimonials on a website."
Generated: DETERMINISTIC_308326a19b90c34a
Batch ID: 20250622_211502
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

class TestimonialManager:
    """
    A class to manage client testimonials for a wedding photography business.
    Testimonials are stored in a JSON file for persistence.
    """

    def __init__(self, storage_file="testimonials.json"):
        """
        Initialize the TestimonialManager with a storage file.
        :param storage_file: Path to the JSON file where testimonials are stored.
        """
        self.storage_file = storage_file
        # Load existing testimonials or initialize an empty list
        self.testimonials = self._load_testimonials()

    def _load_testimonials(self):
        """
        Load testimonials from the storage file.
        :return: A list of testimonials.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error: Could not load testimonials. Starting with an empty list.")
                return []
        return []

    def _save_testimonials(self):
        """
        Save the current testimonials to the storage file.
        """
        try:
            with open(self.storage_file, "w") as file:
                json.dump(self.testimonials, file, indent=4)
        except IOError as e:
            print(f"Error: Could not save testimonials. {e}")

    def add_testimonial(self, client_name, testimonial_text):
        """
        Add a new testimonial.
        :param client_name: Name of the client.
        :param testimonial_text: The testimonial text provided by the client.
        """
        if not client_name or not testimonial_text:
            print("Error: Client name and testimonial text cannot be empty.")
            return

        new_testimonial = {
            "client_name": client_name,
            "testimonial_text": testimonial_text
        }
        self.testimonials.append(new_testimonial)
        self._save_testimonials()
        print("Testimonial added successfully.")

    def remove_testimonial(self, index):
        """
        Remove a testimonial by its index.
        :param index: The index of the testimonial to remove.
        """
        if 0 <= index < len(self.testimonials):
            removed = self.testimonials.pop(index)
            self._save_testimonials()
            print(f"Testimonial from '{removed['client_name']}' removed successfully.")
        else:
            print("Error: Invalid index. No testimonial removed.")

    def display_testimonials(self):
        """
        Display all testimonials in a user-friendly format.
        """
        if not self.testimonials:
            print("No testimonials available.")
            return

        print("\nClient Testimonials:")
        print("-" * 40)
        for i, testimonial in enumerate(self.testimonials):
            print(f"{i + 1}. {testimonial['client_name']}:")
            print(f"   \"{testimonial['testimonial_text']}\"")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    manager = TestimonialManager()

    while True:
        print("\nWedding Photography Testimonial Manager")
        print("1. Add Testimonial")
        print("2. Remove Testimonial")
        print("3. Display Testimonials")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter client name: ")
            text = input("Enter testimonial text: ")
            manager.add_testimonial(name, text)
        elif choice == "2":
            manager.display_testimonials()
            try:
                index = int(input("Enter the index of the testimonial to remove: ")) - 1
                manager.remove_testimonial(index)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "3":
            manager.display_testimonials()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")
```
