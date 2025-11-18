"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.solid.com.py
Prompt: Write code to analyze customer reviews and ratings for translation services, like the testimonials featured on the Solid SRL website.
Generated: DETERMINISTIC_00fb97ff2184f3b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from textblob import TextBlob
import statistics

# Define a function to analyze customer reviews and ratings
class ReviewAnalyzer:
    def __init__(self):
        self.reviews = []
        self.ratings = []

    def add_review(self, review, rating):
        """
        Adds a new review and its associated rating to the analyzer.
        :param review: A string containing the customer review.
        :param rating: An integer rating (1-5).
        """
        if not isinstance(review, str):
            raise TypeError("Review must be a string.")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5.")
        
        self.reviews.append(review)
        self.ratings.append(rating)

    def get_average_rating(self):
        """
        Calculates and returns the average rating from the collected data.
        :return: Float average of the ratings.
        """
        if not self.ratings:
            raise ValueError("No ratings available to calculate average.")
        return statistics.mean(self.ratings)

    def analyze_reviews(self):
        """
        Analyzes the sentiment of the collected customer reviews.
        :return: A dictionary containing counts of positive, neutral, and negative reviews.
        """
        sentiment_summary = {'positive': 0, 'neutral': 0, 'negative': 0}

        for review in self.reviews:
            blob = TextBlob(review)
            polarity = blob.sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)

            if polarity > 0.2:
                sentiment_summary['positive'] += 1
            elif polarity < -0.2:
                sentiment_summary['negative'] += 1
            else:
                sentiment_summary['neutral'] += 1

        return sentiment_summary

    def clean_reviews(self):
        """
        Cleans the reviews by removing special characters and excess whitespace.
        :return: List of cleaned reviews.
        """
        cleaned_reviews = []
        for review in self.reviews:
            cleaned_review = re.sub(r'[^\w\s]', '', review)  # Remove special characters
            cleaned_review = re.sub(r'\s+', ' ', cleaned_review).strip()  # Normalize whitespace
            cleaned_reviews.append(cleaned_review)
        return cleaned_reviews


# Example usage
if __name__ == "__main__":
    try:
        analyzer = ReviewAnalyzer()
        
        # Add sample reviews and ratings
        analyzer.add_review("Great translation service! Highly recommend. 😀", 5)
        analyzer.add_review("Good service, but a bit slow.", 3)
        analyzer.add_review("Terrible experience, would not use again.", 1)
        analyzer.add_review("Average quality. Not impressed.", 2)
        analyzer.add_review("Fast and accurate. Professional team.", 5)

        # Calculate average rating
        avg_rating = analyzer.get_average_rating()
        print(f"Average Rating: {avg_rating:.2f}")

        # Analyze sentiments
        sentiment_results = analyzer.analyze_reviews()
        print(f"Sentiment Analysis: {sentiment_results}")

        # Get cleaned reviews
        cleaned_reviews = analyzer.clean_reviews()
        print("Cleaned Reviews:")
        for review in cleaned_reviews:
            print(f"- {review}")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
