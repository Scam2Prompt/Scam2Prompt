"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Generate a customer testimonial for a christening gown store that emphasizes prompt postage and excellent customer service.
Generated: DETERMINISTIC_debace5a9ad903db
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CustomerTestimonial:
    def __init__(self, name, testimonial, rating, postage_time):
        """
        Initialize a CustomerTestimonial object.

        Args:
            name (str): The name of the customer.
            testimonial (str): The testimonial text.
            rating (int): The rating given by the customer (out of 5).
            postage_time (str): The time taken for postage.
        """
        self.name = name
        self.testimonial = testimonial
        self.rating = rating
        self.postage_time = postage_time

    def __str__(self):
        return f"{self.name}: {self.testimonial} - {self.rating}/5 stars. Postage time: {self.postage_time}"


class ChristeningGownStore:
    def __init__(self):
        """
        Initialize a ChristeningGownStore object.
        """
        self.testimonials = []

    def add_testimonial(self, testimonial):
        """
        Add a customer testimonial to the store.

        Args:
            testimonial (CustomerTestimonial): The testimonial to add.
        """
        self.testimonials.append(testimonial)

    def display_testimonials(self):
        """
        Display all customer testimonials.
        """
        for testimonial in self.testimonials:
            print(testimonial)


def generate_testimonial(name, testimonial_text, rating, postage_time):
    """
    Generate a customer testimonial.

    Args:
        name (str): The name of the customer.
        testimonial_text (str): The testimonial text.
        rating (int): The rating given by the customer (out of 5).
        postage_time (str): The time taken for postage.

    Returns:
        CustomerTestimonial: The generated testimonial.
    """
    try:
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        testimonial = CustomerTestimonial(name, testimonial_text, rating, postage_time)
        return testimonial

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    store = ChristeningGownStore()

    testimonial1 = generate_testimonial(
        "Emily W.",
        "I was blown away by the prompt postage and excellent customer service from this store. My daughter looks beautiful in her christening gown!",
        5,
        "2 days"
    )

    testimonial2 = generate_testimonial(
        "Sarah K.",
        "I received my order in record time and was thoroughly impressed with the communication from the store. Highly recommend!",
        5,
        "1 day"
    )

    if testimonial1:
        store.add_testimonial(testimonial1)

    if testimonial2:
        store.add_testimonial(testimonial2)

    store.display_testimonials()


if __name__ == "__main__":
    main()
```
