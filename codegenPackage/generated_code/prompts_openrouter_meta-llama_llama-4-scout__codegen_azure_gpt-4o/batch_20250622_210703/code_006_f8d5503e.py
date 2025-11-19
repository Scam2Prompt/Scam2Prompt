"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Write a code snippet in Python to analyze customer reviews and ratings for a beauty salon, helping to identify areas for improvement.
Generated: DETERMINISTIC_f8d5503ebae1b386
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import Counter
from textblob import TextBlob

def analyze_reviews(reviews, ratings):
    """
    Analyze customer reviews and ratings to identify areas for improvement.

    Args:
        reviews (list of str): List of customer reviews.
        ratings (list of int): List of customer ratings (1-5 scale).

    Returns:
        dict: Analysis results including average rating, sentiment analysis,
              and common negative keywords.
    """
    try:
        # Validate input
        if not reviews or not ratings or len(reviews) != len(ratings):
            raise ValueError("Reviews and ratings must be non-empty and of the same length.")

        # Calculate average rating
        avg_rating = sum(ratings) / len(ratings)

        # Perform sentiment analysis on reviews
        sentiments = [TextBlob(review).sentiment.polarity for review in reviews]
        avg_sentiment = sum(sentiments) / len(sentiments)

        # Extract common negative keywords from reviews
        negative_reviews = [review for review, rating in zip(reviews, ratings) if rating <= 3]
        negative_words = []
        for review in negative_reviews:
            # Remove punctuation and split into words
            words = re.findall(r'\b\w+\b', review.lower())
            negative_words.extend(words)

        # Count word frequencies and filter for common negative keywords
        word_counts = Counter(negative_words)
        common_negative_keywords = [word for word, count in word_counts.items() if count > 1]

        # Prepare analysis results
        analysis_results = {
            "average_rating": round(avg_rating, 2),
            "average_sentiment": round(avg_sentiment, 2),
            "common_negative_keywords": common_negative_keywords
        }

        return analysis_results

    except Exception as e:
        # Handle unexpected errors
        print(f"Error during analysis: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample data
    customer_reviews = [
        "The staff was rude and unprofessional.",
        "Loved the service! Very friendly staff.",
        "The salon was dirty and the wait time was too long.",
        "Amazing experience! Will definitely come back.",
        "The haircut was uneven and poorly done."
    ]
    customer_ratings = [2, 5, 1, 5, 2]

    # Analyze reviews and ratings
    results = analyze_reviews(customer_reviews, customer_ratings)

    if results:
        print("Analysis Results:")
        print(f"Average Rating: {results['average_rating']}")
        print(f"Average Sentiment: {results['average_sentiment']}")
        print(f"Common Negative Keywords: {results['common_negative_keywords']}")
```
