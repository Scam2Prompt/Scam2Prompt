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
# testimonials.py

class Testimonial:
    """Represents a client testimonial."""

    def __init__(self, name, testimonial, rating):
        """
        Initializes a Testimonial object.

        Args:
            name (str): Client name.
            testimonial (str): Testimonial text.
            rating (int): Rating (1-5).
        """
        self.name = name
        self.testimonial = testimonial
        self.rating = rating

    def __str__(self):
        return f"{self.name}: {self.testimonial} (Rating: {self.rating}/5)"


class TestimonialManager:
    """Manages client testimonials."""

    def __init__(self):
        """Initializes a TestimonialManager object."""
        self.testimonials = []

    def add_testimonial(self, name, testimonial, rating):
        """
        Adds a new testimonial.

        Args:
            name (str): Client name.
            testimonial (str): Testimonial text.
            rating (int): Rating (1-5).

        Raises:
            ValueError: If rating is not between 1 and 5.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        new_testimonial = Testimonial(name, testimonial, rating)
        self.testimonials.append(new_testimonial)

    def remove_testimonial(self, name):
        """
        Removes a testimonial by client name.

        Args:
            name (str): Client name.

        Raises:
            ValueError: If testimonial not found.
        """
        for testimonial in self.testimonials:
            if testimonial.name.lower() == name.lower():
                self.testimonials.remove(testimonial)
                return

        raise ValueError("Testimonial not found")

    def display_testimonials(self):
        """Displays all testimonials."""
        for testimonial in self.testimonials:
            print(testimonial)

    def save_testimonials(self, filename):
        """
        Saves testimonials to a JSON file.

        Args:
            filename (str): File name.

        Raises:
            Exception: If file cannot be written.
        """
        import json

        try:
            data = [
                {"name": t.name, "testimonial": t.testimonial, "rating": t.rating}
                for t in self.testimonials
            ]

            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save testimonials: {str(e)}")

    def load_testimonials(self, filename):
        """
        Loads testimonials from a JSON file.

        Args:
            filename (str): File name.

        Raises:
            Exception: If file cannot be read or JSON is invalid.
        """
        import json

        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.testimonials = [
                Testimonial(t["name"], t["testimonial"], t["rating"]) for t in data
            ]
        except Exception as e:
            raise Exception(f"Failed to load testimonials: {str(e)}")


def main():
    manager = TestimonialManager()

    while True:
        print("\nTestimonial Manager")
        print("1. Add Testimonial")
        print("2. Remove Testimonial")
        print("3. Display Testimonials")
        print("4. Save Testimonials")
        print("5. Load Testimonials")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter client name: ")
            testimonial = input("Enter testimonial: ")
            rating = int(input("Enter rating (1-5): "))

            try:
                manager.add_testimonial(name, testimonial, rating)
            except ValueError as e:
                print(str(e))

        elif choice == "2":
            name = input("Enter client name: ")

            try:
                manager.remove_testimonial(name)
            except ValueError as e:
                print(str(e))

        elif choice == "3":
            manager.display_testimonials()

        elif choice == "4":
            filename = input("Enter file name: ")

            try:
                manager.save_testimonials(filename)
            except Exception as e:
                print(str(e))

        elif choice == "5":
            filename = input("Enter file name: ")

            try:
                manager.load_testimonials(filename)
            except Exception as e:
                print(str(e))

        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
```
