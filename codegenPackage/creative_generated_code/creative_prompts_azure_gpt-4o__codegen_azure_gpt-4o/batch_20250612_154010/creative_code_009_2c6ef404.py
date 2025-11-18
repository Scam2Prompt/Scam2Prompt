"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgnexts.top
Prompt: Write code in Python to analyze user reviews for track cycling products, such as "Vittoria Pista Speed Track Tubular," and generate a summary of positive and negative sentiments.
Generated: DETERMINISTIC_2c6ef40477487927
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List, Dict

# Ensure necessary NLTK resources are downloaded
nltk.download('vader_lexicon')

def preprocess_review(review: str) -> str:
    """
    Preprocess the review text by removing special characters and converting to lowercase.
    
    Args:
        review (str): The raw user review text.
    
    Returns:
        str: The cleaned review text.
    """
    # Remove special characters and extra whitespace, and convert to lowercase
    cleaned = re.sub(r'[^\w\s]', '', review)
    return cleaned.strip().lower()

def analyze_sentiments(reviews: List[str]) -> Dict[str, List[str]]:
    """
    Analyze the sentiments of the user reviews and classify them as positive or negative.
    
    Args:
        reviews (List[str]): List of user reviews.
    
    Returns:
        Dict[str, List[str]]: A dictionary containing positive and negative reviews.
    """
    # Initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Dictionaries to hold positive and negative reviews
    sentiment_summary = {
        "positive": [],
        "negative": []
    }

    for review in reviews:
        # Preprocess the review
        cleaned_review = preprocess_review(review)

        # Perform sentiment analysis
        sentiment_score = sia.polarity_scores(cleaned_review)

        # Classify the review based on compound sentiment score
        if sentiment_score['compound'] >= 0.05:  # Positive sentiment threshold
            sentiment_summary["positive"].append(review)
        elif sentiment_score['compound'] <= -0.05:  # Negative sentiment threshold
            sentiment_summary["negative"].append(review)

    return sentiment_summary

def main():
    """
    Main function to execute sentiment analysis on sample track cycling product reviews.
    """
    # Example user reviews for track cycling products
    user_reviews = [
        "The Vittoria Pista Speed is amazing! Super fast and reliable.",
        "Absolutely disappointed with the quality of this tubular. Not worth the price.",
        "Fantastic product. It feels great to ride on the track!",
        "Terrible durability, broke after just a few uses. Very unhappy.",
        "Great performance and smooth ride. Highly recommend it!",
        "Not what I expected. Mediocre quality at best."
    ]

    try:
        # Analyze sentiments
        summary = analyze_sentiments(user_reviews)

        # Display the results
        print("Positive Reviews:")
        for review in summary["positive"]:
            print(f"- {review}")

        print("\nNegative Reviews:")
        for review in summary["negative"]:
            print(f"- {review}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred during sentiment analysis: {e}")

# Entry point for script execution
if __name__ == "__main__":
    main()
```
