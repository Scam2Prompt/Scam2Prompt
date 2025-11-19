"""
Generated Code Metadata:
========================
Original URL: https://myallora.com
Prompt: Write a customer review for a purchased item from Sophie's Boutique, highlighting the quality, style, and satisfaction with the purchase, especially considering the closure sale.
Generated: DETERMINISTIC_a594cce89a61d428
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CustomerReview:
    def __init__(self, item_name, boutique_name, rating, review_text):
        """
        Initialize a CustomerReview object.

        Args:
            item_name (str): Name of the purchased item.
            boutique_name (str): Name of the boutique where the item was purchased.
            rating (int): Rating given to the item (out of 5).
            review_text (str): Text of the review.
        """
        self.item_name = item_name
        self.boutique_name = boutique_name
        self.rating = rating
        self.review_text = review_text

    def __str__(self):
        return f"Review for {self.item_name} from {self.boutique_name}: {self.review_text} (Rating: {self.rating}/5)"


def create_customer_review(item_name, boutique_name="Sophie's Boutique", rating=5, review_text=""):
    """
    Create a customer review for a purchased item.

    Args:
        item_name (str): Name of the purchased item.
        boutique_name (str, optional): Name of the boutique where the item was purchased. Defaults to "Sophie's Boutique".
        rating (int, optional): Rating given to the item (out of 5). Defaults to 5.
        review_text (str, optional): Text of the review. Defaults to "".

    Returns:
        CustomerReview: A CustomerReview object.

    Raises:
        ValueError: If the rating is not between 1 and 5.
    """
    if not 1 <= rating <= 5:
        raise ValueError("Rating must be between 1 and 5")

    if not review_text:
        review_text = f"I am extremely satisfied with my purchase of {item_name} from {boutique_name}! The quality and style are exceptional, especially considering it was on closure sale."

    return CustomerReview(item_name, boutique_name, rating, review_text)


def main():
    try:
        item_name = "Designer Dress"
        review = create_customer_review(item_name)
        print(review)

        # Example with custom review text and rating
        custom_review = create_customer_review(item_name, rating=4, review_text="The dress is beautiful, but the material could be softer.")
        print(custom_review)

        # Example with invalid rating
        try:
            invalid_review = create_customer_review(item_name, rating=6)
        except ValueError as e:
            print(e)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
