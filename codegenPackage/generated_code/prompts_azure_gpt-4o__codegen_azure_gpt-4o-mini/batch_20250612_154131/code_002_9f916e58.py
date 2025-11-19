"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a script to analyze customer reviews and feedback for a garage door service company, similar to the testimonials provided on Trimatic Puertas Automáticas' website.
Generated: DETERMINISTIC_9f916e5845e04d97
Batch ID: 20250612_154131
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
        Initializes the ReviewAnalyzer with a list of reviews.

        :param reviews: List of customer reviews (strings)
        """
        self.reviews = reviews
        self.sentiment_results = []

    def analyze_sentiment(self):
        """
        Analyzes the sentiment of each review using TextBlob.
        Stores the results in the sentiment_results attribute.
        """
        for review in self.reviews:
            try:
                analysis = TextBlob(review)
                sentiment = analysis.sentiment
                self.sentiment_results.append({
                    'review': review,
                    'polarity': sentiment.polarity,
                    'subjectivity': sentiment.subjectivity
                })
                logging.info(f"Analyzed review: {review} | Polarity: {sentiment.polarity} | Subjectivity: {sentiment.subjectivity}")
            except Exception as e:
                logging.error(f"Error analyzing review: {review} | Error: {str(e)}")

    def get_summary(self):
        """
        Generates a summary of the sentiment analysis.

        :return: A dictionary containing average polarity and subjectivity
        """
        if not self.sentiment_results:
            logging.warning("No sentiment results available. Please run analyze_sentiment() first.")
            return {}

        total_polarity = sum(result['polarity'] for result in self.sentiment_results)
        total_subjectivity = sum(result['subjectivity'] for result in self.sentiment_results)
        count = len(self.sentiment_results)

        summary = {
            'average_polarity': total_polarity / count,
            'average_subjectivity': total_subjectivity / count,
            'total_reviews': count
        }
        logging.info(f"Summary of sentiment analysis: {summary}")
        return summary

def main():
    # Sample reviews for analysis
    reviews = [
        "Great service! The installation was quick and professional.",
        "I had a problem with my garage door, but they fixed it promptly.",
        "The technician was rude and unhelpful.",
        "Excellent quality doors and very friendly staff.",
        "I am not satisfied with the service provided."
    ]

    # Create an instance of ReviewAnalyzer
    analyzer = ReviewAnalyzer(reviews)

    # Analyze the sentiment of the reviews
    analyzer.analyze_sentiment()

    # Get and print the summary of the analysis
    summary = analyzer.get_summary()
    print("Sentiment Analysis Summary:")
    print(summary)

if __name__ == "__main__":
    main()
```
