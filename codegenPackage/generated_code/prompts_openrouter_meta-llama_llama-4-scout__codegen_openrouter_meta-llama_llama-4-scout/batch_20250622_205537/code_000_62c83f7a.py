"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Write a Python script to manage a TV aerial installation company's client reviews and ratings, including storing customer feedback and calculating overall ratings.
Generated: DETERMINISTIC_62c83f7ae358acbc
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tv_aerial_reviews.py

class Review:
    """Represents a customer review with a rating and feedback."""

    def __init__(self, rating, feedback):
        """
        Initializes a Review object.

        Args:
            rating (int): The rating given by the customer (1-5).
            feedback (str): The customer's feedback.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self.rating = rating
        self.feedback = feedback


class TVAerialReviewManager:
    """Manages customer reviews and ratings for a TV aerial installation company."""

    def __init__(self):
        """Initializes a TVAerialReviewManager object."""
        self.reviews = []

    def add_review(self, review):
        """
        Adds a customer review.

        Args:
            review (Review): The review to add.

        Raises:
            TypeError: If the review is not a Review object.
        """
        if not isinstance(review, Review):
            raise TypeError("Review must be a Review object")
        self.reviews.append(review)

    def calculate_overall_rating(self):
        """
        Calculates the overall rating.

        Returns:
            float: The overall rating (out of 5).
        """
        if not self.reviews:
            return 0.0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

    def get_reviews(self):
        """
        Gets all customer reviews.

        Returns:
            list[Review]: A list of all customer reviews.
        """
        return self.reviews


def main():
    # Create a review manager
    review_manager = TVAerialReviewManager()

    while True:
        print("\nTV Aerial Review Manager")
        print("1. Add Review")
        print("2. Calculate Overall Rating")
        print("3. View Reviews")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                rating = int(input("Enter rating (1-5): "))
                feedback = input("Enter feedback: ")
                review = Review(rating, feedback)
                review_manager.add_review(review)
                print("Review added successfully!")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        elif choice == "2":
            overall_rating = review_manager.calculate_overall_rating()
            print(f"Overall Rating: {overall_rating:.2f}/5")
        elif choice == "3":
            reviews = review_manager.get_reviews()
            if not reviews:
                print("No reviews yet!")
            else:
                for i, review in enumerate(reviews, start=1):
                    print(f"Review {i}:")
                    print(f"Rating: {review.rating}/5")
                    print(f"Feedback: {review.feedback}")
                    print()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
