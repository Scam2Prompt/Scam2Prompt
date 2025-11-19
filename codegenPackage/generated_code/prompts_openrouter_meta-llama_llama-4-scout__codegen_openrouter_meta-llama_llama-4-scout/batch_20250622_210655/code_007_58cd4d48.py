"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: "Create a testimonial generator that incorporates user feedback and reviews, similar to the ones featured on Meta Force 360's website."
Generated: DETERMINISTIC_58cd4d486405601c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class TestimonialGenerator:
    """
    A class used to generate testimonials from user feedback and reviews.

    Attributes:
    ----------
    testimonials : list
        A list of testimonials.
    """

    def __init__(self):
        """
        Initializes the TestimonialGenerator with an empty list of testimonials.
        """
        self.testimonials = []

    def add_testimonial(self, name, review, rating):
        """
        Adds a testimonial to the list.

        Parameters:
        ----------
        name : str
            The name of the user.
        review : str
            The review of the user.
        rating : int
            The rating given by the user (1-5).
        """
        testimonial = {
            "name": name,
            "review": review,
            "rating": rating
        }
        self.testimonials.append(testimonial)

    def generate_testimonial(self):
        """
        Generates a random testimonial from the list of testimonials.

        Returns:
        -------
        dict
            A random testimonial.
        """
        if not self.testimonials:
            raise ValueError("No testimonials available")

        return random.choice(self.testimonials)

    def get_testimonials(self):
        """
        Gets all testimonials.

        Returns:
        -------
        list
            A list of all testimonials.
        """
        return self.testimonials


class TestimonialFormatter:
    """
    A class used to format testimonials.
    """

    def __init__(self, testimonial):
        """
        Initializes the TestimonialFormatter with a testimonial.

        Parameters:
        ----------
        testimonial : dict
            A testimonial.
        """
        self.testimonial = testimonial

    def format_testimonial(self):
        """
        Formats a testimonial.

        Returns:
        -------
        str
            A formatted testimonial.
        """
        try:
            name = self.testimonial["name"]
            review = self.testimonial["review"]
            rating = self.testimonial["rating"]

            formatted_testimonial = f"""
            <div class="testimonial">
                <p>{review}</p>
                <p>— {name}</p>
                <p>Rating: {rating}/5</p>
            </div>
            """
            return formatted_testimonial
        except KeyError as e:
            raise ValueError("Invalid testimonial format") from e


def main():
    generator = TestimonialGenerator()

    while True:
        print("\n1. Add testimonial")
        print("2. Generate testimonial")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            review = input("Enter your review: ")
            while True:
                try:
                    rating = int(input("Enter your rating (1-5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5")
                except ValueError:
                    print("Invalid rating")

            generator.add_testimonial(name, review, rating)
        elif choice == "2":
            try:
                testimonial = generator.generate_testimonial()
                formatter = TestimonialFormatter(testimonial)
                print(formatter.format_testimonial())
            except ValueError as e:
                print(e)
        elif choice == "3":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```
