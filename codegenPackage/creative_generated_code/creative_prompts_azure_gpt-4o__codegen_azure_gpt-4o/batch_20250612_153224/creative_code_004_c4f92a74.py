"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Write a script to manage customer reviews and satisfaction ratings for cleaning services. Include functionality to store feedback and calculate overall satisfaction scores.
Generated: DETERMINISTIC_c4f92a7425aab3f0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import statistics

class CleaningServiceReviews:
    """
    A class to manage customer reviews and satisfaction ratings
    for a cleaning service.
    """
    def __init__(self, storage_file="reviews.json"):
        """
        Initializes the CleaningServiceReviews instance.
        
        :param storage_file: File to store reviews data.
        """
        self.storage_file = storage_file
        self.reviews = self._load_reviews()

    def _load_reviews(self):
        """
        Loads reviews from the storage file.
        
        :return: List of reviews (empty list if file doesn't exist or is empty).
        """
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # File not found or is empty/corrupted, return an empty list
            return []

    def save_reviews(self):
        """
        Saves the reviews to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.reviews, file, indent=4)
        except Exception as e:
            print(f"Error saving reviews: {e}")

    def add_review(self, customer_name, satisfaction_rating, feedback):
        """
        Adds a review to the system.
        
        :param customer_name: Name of the customer providing the review.
        :param satisfaction_rating: Satisfaction rating (1-5 scale).
        :param feedback: Textual feedback from the customer.
        :raise ValueError: If satisfaction_rating is not between 1 and 5.
        """
        if not (1 <= satisfaction_rating <= 5):
            raise ValueError("Satisfaction rating must be between 1 and 5.")
        
        review = {
            "customer_name": customer_name,
            "satisfaction_rating": satisfaction_rating,
            "feedback": feedback
        }
        self.reviews.append(review)
        self.save_reviews()
        print("Review added successfully.")

    def calculate_average_satisfaction(self):
        """
        Calculates the average satisfaction rating.
        
        :return: Average satisfaction rating or None if no reviews exist.
        """
        if not self.reviews:
            return None
        
        ratings = [review["satisfaction_rating"] for review in self.reviews]
        return statistics.mean(ratings)

    def display_reviews(self):
        """
        Displays all reviews in a readable format.
        """
        if not self.reviews:
            print("No reviews available.")
            return
        
        print("Customer Reviews:")
        for index, review in enumerate(self.reviews, start=1):
            print(f"\nReview #{index}:")
            print(f"Customer Name: {review['customer_name']}")
            print(f"Satisfaction Rating: {review['satisfaction_rating']}/5")
            print(f"Feedback: {review['feedback']}")

# Example usage
if __name__ == "__main__":
    # Create instance of CleaningServiceReviews
    reviews_manager = CleaningServiceReviews()

    # Add a few sample reviews
    try:
        reviews_manager.add_review("Alice", 5, "Excellent service!")
        reviews_manager.add_review("Bob", 4, "Very good, but could improve punctuality.")
    except ValueError as e:
        print(e)

    # Display all reviews
    reviews_manager.display_reviews()

    # Calculate and display average satisfaction rating
    avg_satisfaction = reviews_manager.calculate_average_satisfaction()
    if avg_satisfaction is not None:
        print(f"\nOverall Average Satisfaction Rating: {avg_satisfaction:.2f}/5")
    else:
        print("\nNo ratings available to calculate average satisfaction.")
```
