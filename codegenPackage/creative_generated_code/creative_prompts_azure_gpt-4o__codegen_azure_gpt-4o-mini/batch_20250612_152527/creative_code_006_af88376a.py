"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.depanten-gel.click
Prompt: Write Python code to analyze customer reviews and ratings for a product like Depanten using sentiment analysis.
Generated: DETERMINISTIC_af88376ae8510c99
Batch ID: 20250612_152527
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

# Set up logging for error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReviewAnalyzer:
    def __init__(self, reviews):
        """
        Initializes the ReviewAnalyzer with a DataFrame of reviews.

        :param reviews: A pandas DataFrame containing the customer reviews and ratings.
        """
        self.reviews = reviews

    def analyze_sentiment(self):
        """
        Analyzes the sentiment of each review using TextBlob.
        Adds a 'sentiment' column to the DataFrame with polarity scores.
        """
        try:
            # Ensure the 'review' column exists
            if 'review' not in self.reviews.columns:
                raise ValueError("Input DataFrame must contain a 'review' column.")
            
            # Apply TextBlob sentiment analysis to each review
            self.reviews['sentiment'] = self.reviews['review'].apply(lambda x: TextBlob(x).sentiment.polarity)
            logging.info("Sentiment analysis applied successfully.")
        except Exception as e:
            logging.error(f"Error during sentiment analysis: {e}")
            raise

    def get_summary(self):
        """
        Generates a summary of the sentiment analysis, including
        the average rating and average sentiment polarity.

        :return: A dictionary summarizing the analysis.
        """
        try:
            if 'rating' not in self.reviews.columns:
                raise ValueError("Input DataFrame must contain a 'rating' column.")
                
            average_rating = self.reviews['rating'].mean()
            average_sentiment = self.reviews['sentiment'].mean()

            summary = {
                'average_rating': average_rating,
                'average_sentiment': average_sentiment,
                'total_reviews': len(self.reviews)
            }
            
            logging.info("Summary generated successfully.")
            return summary
        except Exception as e:
            logging.error(f"Error during summary generation: {e}")
            raise

def main():
    # Sample data for testing
    data = {
        'review': [
            "I love this product! It works wonders.",
            "Not what I expected, very disappointed.",
            "Okay product, does the job.",
            "Fantastic! Highly recommend it.",
            "Worst purchase ever. I want a refund."
        ],
        'rating': [5, 2, 3, 5, 1]
    }
    
    # Create a DataFrame from the sample data
    reviews_df = pd.DataFrame(data)
    
    # Initialize the ReviewAnalyzer with the reviews DataFrame
    analyzer = ReviewAnalyzer(reviews_df)
    
    # Perform sentiment analysis
    analyzer.analyze_sentiment()
    
    # Get the summary of the analysis
    summary = analyzer.get_summary()
    
    # Print the summary
    print(summary)

if __name__ == "__main__":
    main()
```
