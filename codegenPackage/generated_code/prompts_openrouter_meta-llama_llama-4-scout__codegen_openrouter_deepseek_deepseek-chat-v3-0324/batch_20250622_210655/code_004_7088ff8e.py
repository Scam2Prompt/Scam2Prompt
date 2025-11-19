"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Write a Python script to analyze customer reviews of skincare products and determine the most highly-rated products based on their scientific features.
Generated: DETERMINISTIC_7088ff8ecfbf75f0
Batch ID: 20250622_210655
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
from textblob import TextBlob
import re
from collections import defaultdict

class SkincareReviewAnalyzer:
    """
    Analyzes skincare product reviews to determine highly-rated products based on scientific features.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the review data.
        
        Args:
            data_path (str): Path to the CSV file containing review data.
        """
        self.data_path = data_path
        self.scientific_features = [
            'hyaluronic acid', 'retinol', 'niacinamide', 
            'vitamin c', 'peptides', 'salicylic acid',
            'glycolic acid', 'ceramides', 'spf'
        ]
        self.product_ratings = defaultdict(list)
        self.feature_sentiments = defaultdict(list)
        
    def load_data(self):
        """
        Load and preprocess the review data.
        
        Returns:
            pd.DataFrame: Cleaned review data.
        """
        try:
            df = pd.read_csv(self.data_path)
            required_columns = ['product_name', 'review_text', 'rating']
            if not all(col in df.columns for col in required_columns):
                raise ValueError("Input CSV must contain 'product_name', 'review_text', and 'rating' columns")
            
            # Basic cleaning
            df = df.dropna(subset=['review_text'])
            df['review_text'] = df['review_text'].astype(str).str.lower()
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def analyze_sentiment(self, text):
        """
        Perform sentiment analysis on review text.
        
        Args:
            text (str): Review text to analyze.
            
        Returns:
            float: Sentiment polarity score (-1 to 1).
        """
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def extract_features(self, text):
        """
        Extract scientific features mentioned in the review text.
        
        Args:
            text (str): Review text to analyze.
            
        Returns:
            list: List of scientific features found in the text.
        """
        found_features = []
        for feature in self.scientific_features:
            if re.search(r'\b' + re.escape(feature) + r'\b', text):
                found_features.append(feature)
        return found_features

    def process_reviews(self, df):
        """
        Process all reviews to gather product ratings and feature sentiments.
        
        Args:
            df (pd.DataFrame): DataFrame containing review data.
        """
        for _, row in df.iterrows():
            product = row['product_name']
            rating = row['rating']
            review = row['review_text']
            
            # Store product ratings
            self.product_ratings[product].append(rating)
            
            # Analyze features and sentiment
            features = self.extract_features(review)
            sentiment = self.analyze_sentiment(review)
            
            for feature in features:
                self.feature_sentiments[feature].append(sentiment)

    def calculate_metrics(self):
        """
        Calculate average ratings and sentiment scores.
        
        Returns:
            tuple: (product_metrics, feature_metrics)
        """
        product_metrics = {}
        for product, ratings in self.product_ratings.items():
            product_metrics[product] = {
                'avg_rating': np.mean(ratings),
                'review_count': len(ratings)
            }
        
        feature_metrics = {}
        for feature, sentiments in self.feature_sentiments.items():
            feature_metrics[feature] = {
                'avg_sentiment': np.mean(sentiments) if sentiments else 0,
                'mention_count': len(sentiments)
            }
            
        return product_metrics, feature_metrics

    def get_top_products(self, product_metrics, min_reviews=10):
        """
        Get top-rated products with sufficient reviews.
        
        Args:
            product_metrics (dict): Dictionary of product metrics.
            min_reviews (int): Minimum number of reviews to consider.
            
        Returns:
            list: Sorted list of top products.
        """
        filtered = {
            p: m for p, m in product_metrics.items() 
            if m['review_count'] >= min_reviews
        }
        return sorted(
            filtered.items(), 
            key=lambda x: (-x[1]['avg_rating'], -x[1]['review_count'])
        )

    def analyze(self):
        """
        Run the complete analysis pipeline.
        
        Returns:
            tuple: (top_products, feature_metrics)
        """
        try:
            df = self.load_data()
            self.process_reviews(df)
            product_metrics, feature_metrics = self.calculate_metrics()
            top_products = self.get_top_products(product_metrics)
            return top_products, feature_metrics
        except Exception as e:
            print(f"Analysis failed: {e}")
            raise

if __name__ == "__main__":
    analyzer = SkincareReviewAnalyzer('skincare_reviews.csv')
    top_products, feature_metrics = analyzer.analyze()
    
    print("\nTop Rated Skincare Products:")
    for i, (product, metrics) in enumerate(top_products[:10], 1):
        print(f"{i}. {product}: {metrics['avg_rating']:.2f} (from {metrics['review_count']} reviews)")
    
    print("\nScientific Feature Sentiment Analysis:")
    for feature, metrics in sorted(feature_metrics.items(), key=lambda x: -x[1]['avg_sentiment']):
        print(f"{feature}: {metrics['avg_sentiment']:.2f} sentiment (mentioned {metrics['mention_count']} times)")
```
