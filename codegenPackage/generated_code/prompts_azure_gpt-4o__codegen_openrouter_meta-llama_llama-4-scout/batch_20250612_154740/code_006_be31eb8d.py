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
# testimonial_manager.py

class Testimonial:
    """Represents a customer testimonial."""

    def __init__(self, customer_name, rating, testimonial_text):
        """
        Initializes a Testimonial object.

        Args:
            customer_name (str): The name of the customer.
            rating (int): The rating given by the customer (1-5).
            testimonial_text (str): The testimonial text.

        Raises:
            ValueError: If rating is not between 1 and 5.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        self.customer_name = customer_name
        self.rating = rating
        self.testimonial_text = testimonial_text

    def __str__(self):
        return f"{self.customer_name}: {self.testimonial_text} (Rating: {self.rating}/5)"


class TestimonialManager:
    """Manages customer testimonials and ratings."""

    def __init__(self):
        self.testimonials = []

    def add_testimonial(self, customer_name, rating, testimonial_text):
        """
        Adds a new testimonial.

        Args:
            customer_name (str): The name of the customer.
            rating (int): The rating given by the customer (1-5).
            testimonial_text (str): The testimonial text.

        Raises:
            ValueError: If rating is not between 1 and 5.
        """
        try:
            testimonial = Testimonial(customer_name, rating, testimonial_text)
            self.testimonials.append(testimonial)
        except ValueError as e:
            print(f"Error adding testimonial: {e}")

    def remove_testimonial(self, customer_name):
        """
        Removes a testimonial by customer name.

        Args:
            customer_name (str): The name of the customer.

        Returns:
            bool: True if testimonial was removed, False otherwise.
        """
        self.testimonials = [t for t in self.testimonials if t.customer_name != customer_name]
        return len(self.testimonials) < len(self.testimonials) + 1

    def get_average_rating(self):
        """
        Calculates the average rating of all testimonials.

        Returns:
            float: The average rating.
        """
        if not self.testimonials:
            return 0.0

        ratings = [t.rating for t in self.testimonials]
        return sum(ratings) / len(ratings)

    def __str__(self):
        testimonials_str = "\n".join([str(t) for t in self.testimonials])
        return f"Testimonials:\n{testimonials_str}\nAverage Rating: {self.get_average_rating():.2f}/5"


def main():
    # Example usage:
    manager = TestimonialManager()

    while True:
        print("\n1. Add Testimonial")
        print("2. Remove Testimonial")
        print("3. View Testimonials")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            rating = int(input("Enter rating (1-5): "))
            testimonial_text = input("Enter testimonial text: ")
            manager.add_testimonial(customer_name, rating, testimonial_text)
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            manager.remove_testimonial(customer_name)
        elif choice == "3":
            print(manager)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
