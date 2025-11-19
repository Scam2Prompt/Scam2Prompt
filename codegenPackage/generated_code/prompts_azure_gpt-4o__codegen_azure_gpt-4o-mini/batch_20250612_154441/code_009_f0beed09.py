"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write a program to analyze customer reviews of rubber flooring products (e.g., EPDM, TPV Rubber) for volleyball courts, using the criteria mentioned in Rubber Flooring Indonesia's blog.
Generated: DETERMINISTIC_f0beed09cb844089
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from textblob import TextBlob
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewAnalyzer:
    def __init__(self, reviews):
        """
        Initialize the ReviewAnalyzer with a list of reviews.

        :param reviews: List of customer reviews (strings)
        """
        self.reviews = reviews
        self.analysis_results = []

    def analyze_reviews(self):
        """
        Analyze the reviews for sentiment and extract key criteria.
        """
        for review in self.reviews:
            try:
                sentiment = self.analyze_sentiment(review)
                criteria = self.extract_criteria(review)
                self.analysis_results.append({
                    'review': review,
                    'sentiment': sentiment,
                    'criteria': criteria
                })
            except Exception as e:
                logging.error(f"Error analyzing review: {review}. Error: {e}")

    @staticmethod
    def analyze_sentiment(review):
        """
        Analyze the sentiment of a review using TextBlob.

        :param review: Customer review (string)
        :return: Sentiment polarity (-1 to 1)
        """
        analysis = TextBlob(review)
        return analysis.sentiment.polarity

    @staticmethod
    def extract_criteria(review):
        """
        Extract relevant criteria from the review based on keywords.

        :param review: Customer review (string)
        :return: List of criteria mentioned in the review
        """
        criteria_keywords = ['durability', 'comfort', 'maintenance', 'price', 'aesthetics']
        found_criteria = [keyword for keyword in criteria_keywords if keyword in review.lower()]
        return found_criteria

    def get_analysis_results(self):
        """
        Get the analysis results.

        :return: List of dictionaries containing review analysis
        """
        return self.analysis_results


def main():
    # Sample reviews for analysis
    sample_reviews = [
        "The EPDM flooring is very durable and easy to maintain.",
        "I love the comfort of the TPV rubber, but it is a bit pricey.",
        "Great aesthetics, but the durability could be better.",
        "Maintenance is a breeze with this flooring, highly recommend!"
    ]

    # Create an instance of ReviewAnalyzer
    analyzer = ReviewAnalyzer(sample_reviews)

    # Analyze the reviews
    analyzer.analyze_reviews()

    # Retrieve and print the analysis results
    results = analyzer.get_analysis_results()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
```
