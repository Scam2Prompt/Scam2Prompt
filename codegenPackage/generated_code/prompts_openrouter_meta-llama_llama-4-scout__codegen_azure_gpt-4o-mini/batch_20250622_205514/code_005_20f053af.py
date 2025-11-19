"""
Generated Code Metadata:
========================
Original URL: https://andreeabalogh.com
Prompt: Write a review of the TV series "Normal People" in a similar style to Andreea Balogh's.
Generated: DETERMINISTIC_20f053affe9623fd
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TVSeriesReview:
    """
    A class to represent a review of a TV series.
    """

    def __init__(self, title, author, review_text, rating):
        """
        Initializes the TVSeriesReview with title, author, review text, and rating.

        :param title: str - The title of the TV series
        :param author: str - The author of the review
        :param review_text: str - The content of the review
        :param rating: float - The rating of the series (0 to 10)
        """
        self.title = title
        self.author = author
        self.review_text = review_text
        self.rating = self.validate_rating(rating)

    @staticmethod
    def validate_rating(rating):
        """
        Validates the rating to ensure it is between 0 and 10.

        :param rating: float - The rating to validate
        :return: float - The validated rating
        :raises ValueError: If the rating is not between 0 and 10
        """
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10.")
        return rating

    def display_review(self):
        """
        Displays the review in a formatted manner.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Rating: {self.rating}/10")
        print("Review:")
        print(self.review_text)

# Example usage
if __name__ == "__main__":
    try:
        review = TVSeriesReview(
            title="Normal People",
            author="Andreea Balogh",
            review_text=(
                "Normal People is a beautifully crafted exploration of love, "
                "intimacy, and the complexities of human relationships. "
                "The series captures the raw emotions and vulnerabilities of its characters, "
                "making it a poignant reflection on the nature of connection. "
                "With stunning performances and a hauntingly beautiful score, "
                "it leaves a lasting impact on the viewer."
            ),
            rating=9.5
        )
        review.display_review()
    except ValueError as e:
        print(f"Error: {e}")
```
