"""
Generated Code Metadata:
========================
Original URL: https://eldoraa.com
Prompt: Write a Python script to analyze customer reviews and ratings for body sprays on an e-commerce platform like Eldoraa and provide insights on product popularity.
Generated: DETERMINISTIC_94a9b6af7f02a5b8
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
from collections import defaultdict
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('review_analysis.log'),
        logging.StreamHandler()
    ]
)

class ReviewAnalyzer:
    """
    A class to analyze customer reviews and ratings for body sprays.
    Provides insights on product popularity based on ratings and sentiment analysis.
    """

    def __init__(self, data_path):
        """
        Initialize the ReviewAnalyzer with the path to the review data.

        Args:
            data_path (str): Path to the CSV file containing review data.
        """
        self.data_path = data_path
        self.reviews_df = None
        self.products = None

    def load_data(self):
        """
        Load and preprocess the review data from the specified CSV file.

        Raises:
            FileNotFoundError: If the data file does not exist.
            ValueError: If the data file is not a valid CSV or missing required columns.
        """
        try:
            # Load the data
            self.reviews_df = pd.read_csv(self.data_path)

            # Check for required columns
            required_columns = {'product_id', 'product_name', 'rating', 'review_text'}
            if not required_columns.issubset(self.reviews_df.columns):
                raise ValueError(
                    f"Data file must contain these columns: {required_columns}"
                )

            # Clean the data
            self.reviews_df = self.reviews_df.dropna(subset=['rating', 'review_text'])
            self.reviews_df['rating'] = pd.to_numeric(
                self.reviews_df['rating'], errors='coerce'
            )
            self.reviews_df = self.reviews_df.dropna(subset=['rating'])

            # Extract unique products
            self.products = self.reviews_df['product_name'].unique()

            logging.info("Data loaded and preprocessed successfully.")

        except FileNotFoundError as e:
            logging.error(f"Data file not found: {e}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def analyze_ratings(self):
        """
        Analyze product ratings to determine popularity based on average ratings.

        Returns:
            dict: A dictionary with product names as keys and average ratings as values.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        try:
            avg_ratings = self.reviews_df.groupby('product_name')['rating'].mean()
            avg_ratings = avg_ratings.sort_values(ascending=False)
            return avg_ratings.to_dict()

        except Exception as e:
            logging.error(f"Error analyzing ratings: {e}")
            raise

    def analyze_sentiment(self):
        """
        Perform sentiment analysis on review texts.

        Returns:
            dict: A dictionary with product names as keys and average sentiment scores as values.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        try:
            sentiment_scores = defaultdict(list)

            for _, row in self.reviews_df.iterrows():
                analysis = TextBlob(str(row['review_text']))
                sentiment_scores[row['product_name']].append(analysis.sentiment.polarity)

            avg_sentiment = {
                product: np.mean(scores) for product, scores in sentiment_scores.items()
            }
            return dict(sorted(avg_sentiment.items(), key=lambda x: x[1], reverse=True))

        except Exception as e:
            logging.error(f"Error performing sentiment analysis: {e}")
            raise

    def generate_insights(self):
        """
        Generate insights by combining rating and sentiment analysis.

        Returns:
            dict: A dictionary containing popularity insights.
        """
        try:
            insights = {
                'top_rated_products': self.analyze_ratings(),
                'most_positive_sentiment': self.analyze_sentiment()
            }
            return insights

        except Exception as e:
            logging.error(f"Error generating insights: {e}")
            raise

    def visualize_insights(self, insights, output_dir='output'):
        """
        Generate visualizations for the insights.

        Args:
            insights (dict): Insights generated by generate_insights().
            output_dir (str): Directory to save visualizations.

        Raises:
            OSError: If the output directory cannot be created.
        """
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Plot top rated products
            plt.figure(figsize=(10, 6))
            products = list(insights['top_rated_products'].keys())
            ratings = list(insights['top_rated_products'].values())
            plt.bar(products, ratings, color='skyblue')
            plt.title('Top Rated Body Sprays')
            plt.xlabel('Product Name')
            plt.ylabel('Average Rating')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'top_rated.png'))
            plt.close()

            # Plot most positive sentiment
            plt.figure(figsize=(10, 6))
            products = list(insights['most_positive_sentiment'].keys())
            sentiment = list(insights['most_positive_sentiment'].values())
            plt.bar(products, sentiment, color='lightgreen')
            plt.title('Most Positive Sentiment in Reviews')
            plt.xlabel('Product Name')
            plt.ylabel('Average Sentiment Score')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'most_positive.png'))
            plt.close()

            logging.info(f"Visualizations saved to {output_dir}")

        except Exception as e:
            logging.error(f"Error generating visualizations: {e}")
            raise

def main():
    """
    Main function to execute the review analysis.
    """
    try:
        # Initialize analyzer with path to reviews data
        analyzer = ReviewAnalyzer('body_spray_reviews.csv')

        # Load and analyze data
        analyzer.load_data()
        insights = analyzer.generate_insights()

        # Print insights
        print("\nTop Rated Products:")
        for product, rating in insights['top_rated_products'].items():
            print(f"{product}: {rating:.2f}")

        print("\nMost Positive Sentiment:")
        for product, sentiment in insights['most_positive_sentiment'].items():
            print(f"{product}: {sentiment:.2f}")

        # Generate visualizations
        analyzer.visualize_insights(insights)

    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == '__main__':
    main()
```
