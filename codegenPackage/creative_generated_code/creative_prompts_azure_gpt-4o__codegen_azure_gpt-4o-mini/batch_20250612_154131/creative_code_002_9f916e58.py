"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Create a script to analyze customer reviews and feedback for a garage door service company, similar to the testimonials provided on Trimatic Puertas Automáticas' website.
Generated: DETERMINISTIC_9f916e5845e04d97
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Ensure that necessary NLTK resources are downloaded
nltk.download('vader_lexicon')

class ReviewAnalyzer:
    def __init__(self, reviews: pd.DataFrame):
        """
        Initialize the ReviewAnalyzer with a DataFrame of reviews.

        Parameters:
            reviews (pd.DataFrame): A DataFrame containing customer reviews with a 'text' column.
        """
        self.reviews = reviews
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiments(self):
        """
        Analyze the sentiments of customer reviews and add a sentiment score to the DataFrame.
        """
        try:
            # Calculate sentiment scores
            self.reviews['sentiment'] = self.reviews['text'].apply(lambda x: self.sia.polarity_scores(x)['compound'])
        except Exception as e:
            print(f"An error occurred while analyzing sentiments: {e}")

    def summarize_results(self):
        """
        Summarize the sentiment analysis results by calculating the average sentiment score.
        
        Returns:
            dict: A dictionary containing summary metrics.
        """
        try:
            average_sentiment = self.reviews['sentiment'].mean()
            positive_reviews = self.reviews[self.reviews['sentiment'] > 0].shape[0]
            total_reviews = self.reviews.shape[0]

            summary = {
                'average_sentiment': average_sentiment,
                'positive_reviews': positive_reviews,
                'total_reviews': total_reviews
            }
            return summary
        except Exception as e:
            print(f"An error occurred while summarizing results: {e}")
            return None

    def plot_sentiment_distribution(self):
        """
        Plot the distribution of sentiment scores for the reviews.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.hist(self.reviews['sentiment'], bins=30, color='blue', alpha=0.7)
            plt.title('Distribution of Sentiment Scores')
            plt.xlabel('Sentiment Score')
            plt.ylabel('Frequency')
            plt.axvline(0, color='red', linestyle='dashed', linewidth=1)  # Line at neutral sentiment
            plt.grid(axis='y', alpha=0.75)
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting sentiment distribution: {e}")

def main():
    # Sample data creation for testing
    data = {
        'text': [
            "Great service, very professional and fast!",
            "I am very disappointed with the installation.",
            "Excellent customer support and timely response.",
            "Not satisfied with the product quality.",
            "The team was friendly and did a fantastic job!"
        ]
    }
    
    # Create a DataFrame from the sample data
    reviews_df = pd.DataFrame(data)

    # Initialize the ReviewAnalyzer
    analyzer = ReviewAnalyzer(reviews_df)

    # Analyze sentiments
    analyzer.analyze_sentiments()

    # Summarize the results
    summary = analyzer.summarize_results()
    if summary:
        print("Summary of Sentiment Analysis:")
        print(summary)

    # Plot the sentiment distribution
    analyzer.plot_sentiment_distribution()

if __name__ == "__main__":
    main()
```
