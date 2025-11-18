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
import pandas as pd
from textblob import TextBlob
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewAnalyzer:
    def __init__(self, reviews_data: pd.DataFrame):
        """
        Initializes the ReviewAnalyzer with a DataFrame of reviews.

        :param reviews_data: A DataFrame containing at least 'review' and 'rating' columns.
        """
        if 'review' not in reviews_data.columns or 'rating' not in reviews_data.columns:
            logging.error("DataFrame must contain 'review' and 'rating' columns.")
            raise ValueError("DataFrame must contain 'review' and 'rating' columns.")
        
        self.reviews_data = reviews_data
    
    def analyze_sentiment(self):
        """
        Analyzes the sentiment of each review using TextBlob and adds the results to the DataFrame.
        """
        try:
            self.reviews_data['sentiment'] = self.reviews_data['review'].apply(self._get_sentiment)
            logging.info("Sentiment analysis completed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during sentiment analysis: {e}")
            raise

    @staticmethod
    def _get_sentiment(review: str) -> str:
        """
        Determines the sentiment of a review.

        :param review: A review string.
        :return: Sentiment label: 'Positive', 'Neutral', or 'Negative'.
        """
        analysis = TextBlob(review)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'
    
    def calculate_average_rating(self) -> float:
        """
        Calculates the average rating from the reviews.

        :return: The average rating as a float.
        """
        try:
            average_rating = self.reviews_data['rating'].mean()
            logging.info(f"Calculated average rating: {average_rating}")
            return average_rating
        except Exception as e:
            logging.error(f"An error occurred while calculating average rating: {e}")
            raise

    def get_summary(self) -> dict:
        """
        Provides a summary of the reviews including average rating and sentiment distribution.

        :return: A dictionary with average rating and sentiment counts.
        """
        try:
            sentiment_counts = self.reviews_data['sentiment'].value_counts().to_dict()
            average_rating = self.calculate_average_rating()
            summary = {
                'average_rating': average_rating,
                'sentiment_distribution': sentiment_counts
            }
            logging.info("Summary generated successfully.")
            return summary
        except Exception as e:
            logging.error(f"An error occurred while generating summary: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    # Sample reviews data
    review_data = {
        'review': [
            "Great service, highly recommend!",
            "Not bad, could be better.",
            "Terrible experience, I will not use again.",
            "Excellent translation, very satisfied."
        ],
        'rating': [5, 3, 1, 5]
    }

    # Create a DataFrame
    reviews_df = pd.DataFrame(review_data)

    # Analyze reviews
    analyzer = ReviewAnalyzer(reviews_df)
    analyzer.analyze_sentiment()
    summary = analyzer.get_summary()
    
    print(summary)
```
