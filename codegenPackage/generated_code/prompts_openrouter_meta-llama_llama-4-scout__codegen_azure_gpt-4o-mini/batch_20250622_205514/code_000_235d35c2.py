"""
Generated Code Metadata:
========================
Original URL: https://andreeabalogh.com
Prompt: Write a review of the book "Love On Tour" by Lee Adams in the style of Andreea Balogh.
Generated: DETERMINISTIC_235d35c22f8863ee
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BookReview:
    """
    A class to represent a book review.

    Attributes:
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    review_text : str
        The content of the review.
    rating : int
        The rating given to the book (1 to 5).
    """

    def __init__(self, title, author, review_text, rating):
        """
        Initializes the BookReview with title, author, review text, and rating.

        Parameters:
        ----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        review_text : str
            The content of the review.
        rating : int
            The rating given to the book (1 to 5).
        """
        self.title = title
        self.author = author
        self.review_text = review_text
        self.rating = self.validate_rating(rating)

    def validate_rating(self, rating):
        """
        Validates the rating to ensure it is between 1 and 5.

        Parameters:
        ----------
        rating : int
            The rating to validate.

        Returns:
        -------
        int
            The validated rating.

        Raises:
        ------
        ValueError
            If the rating is not between 1 and 5.
        """
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return rating

    def display_review(self):
        """
        Displays the formatted review of the book.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Rating: {self.rating}/5")
        print("Review:")
        print(self.review_text)

def main():
    """
    Main function to create and display a book review.
    """
    try:
        # Create a review for "Love On Tour" by Lee Adams
        review = BookReview(
            title="Love On Tour",
            author="Lee Adams",
            review_text=(
                "In 'Love On Tour', Lee Adams takes readers on an emotional journey "
                "that beautifully captures the essence of love and the complexities "
                "that come with it. The characters are well-developed, and the narrative "
                "is both engaging and thought-provoking. Adams' writing style is lyrical, "
                "making it a pleasure to read. This book is a must-read for anyone who "
                "believes in the transformative power of love."
            ),
            rating=5
        )

        # Display the review
        review.display_review()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
