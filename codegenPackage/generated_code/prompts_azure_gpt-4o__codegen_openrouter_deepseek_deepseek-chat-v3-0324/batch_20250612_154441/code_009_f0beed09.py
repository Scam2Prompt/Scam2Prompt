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
import numpy as np
import re
from textblob import TextBlob
from collections import defaultdict
import matplotlib.pyplot as plt

class RubberFlooringAnalyzer:
    """
    A class to analyze customer reviews of rubber flooring products for volleyball courts.
    The analysis is based on criteria from Rubber Flooring Indonesia's blog.
    """
    
    def __init__(self, reviews_data):
        """
        Initialize the analyzer with reviews data.
        
        Args:
            reviews_data (str or pd.DataFrame): Path to CSV file or DataFrame containing reviews.
                                               Expected columns: 'review_text', 'rating', 'product_type'
        """
        if isinstance(reviews_data, str):
            self.reviews = pd.read_csv(reviews_data)
        else:
            self.reviews = reviews_data.copy()
            
        self.criteria = {
            'durability': ['durable', 'long-lasting', 'wear', 'tear', 'last', 'endure'],
            'comfort': ['comfort', 'cushion', 'soft', 'impact', 'joint', 'knee'],
            'traction': ['grip', 'slip', 'traction', 'friction', 'slide'],
            'maintenance': ['clean', 'maintain', 'care', 'wipe', 'wash'],
            'appearance': ['look', 'color', 'design', 'aesthetic', 'appearance']
        }
        
        self.validate_data()
        
    def validate_data(self):
        """Validate the input data has required columns and clean it."""
        required_columns = ['review_text', 'rating', 'product_type']
        if not all(col in self.reviews.columns for col in required_columns):
            raise ValueError(f"Input data must contain these columns: {required_columns}")
            
        # Clean review text
        self.reviews['cleaned_text'] = self.reviews['review_text'].apply(self._clean_text)
        
    def _clean_text(self, text):
        """Clean and preprocess text for analysis."""
        if not isinstance(text, str):
            return ""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        return text
    
    def analyze_sentiment(self):
        """Perform sentiment analysis on reviews using TextBlob."""
        self.reviews['sentiment'] = self.reviews['cleaned_text'].apply(
            lambda x: TextBlob(x).sentiment.polarity
        )
        
    def analyze_criteria_mentions(self):
        """Analyze how often each criteria is mentioned in reviews."""
        criteria_counts = defaultdict(lambda: defaultdict(int))
        
        for _, row in self.reviews.iterrows():
            text = row['cleaned_text']
            for criterion, keywords in self.criteria.items():
                for keyword in keywords:
                    if keyword in text:
                        criteria_counts[row['product_type']][criterion] += 1
                        
        self.criteria_mentions = pd.DataFrame(criteria_counts).fillna(0)
        return self.criteria_mentions
    
    def get_criteria_sentiment(self):
        """Calculate average sentiment for each criteria across product types."""
        criteria_sentiment = defaultdict(lambda: defaultdict(list))
        
        for _, row in self.reviews.iterrows():
            text = row['cleaned_text']
            sentiment = row['sentiment']
            
            for criterion, keywords in self.criteria.items():
                if any(keyword in text for keyword in keywords):
                    criteria_sentiment[row['product_type']][criterion].append(sentiment)
                    
        # Calculate average sentiment
        for product in criteria_sentiment:
            for criterion in criteria_sentiment[product]:
                criteria_sentiment[product][criterion] = np.mean(criteria_sentiment[product][criterion])
                
        self.criteria_sentiment = pd.DataFrame(criteria_sentiment).fillna(0)
        return self.criteria_sentiment
    
    def generate_report(self):
        """Generate a comprehensive analysis report."""
        self.analyze_sentiment()
        mentions = self.analyze_criteria_mentions()
        sentiment = self.get_criteria_sentiment()
        
        report = {
            'overall_sentiment': self.reviews.groupby('product_type')['sentiment'].mean().to_dict(),
            'average_rating': self.reviews.groupby('product_type')['rating'].mean().to_dict(),
            'criteria_mentions': mentions.to_dict(),
            'criteria_sentiment': sentiment.to_dict()
        }
        
        return report
    
    def plot_analysis(self, save_path=None):
        """Visualize the analysis results."""
        report = self.generate_report()
        product_types = list(report['overall_sentiment'].keys())
        
        # Set up subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Rubber Flooring Products Analysis', fontsize=16)
        
        # Plot 1: Overall Sentiment
        axes[0, 0].bar(product_types, report['overall_sentiment'].values())
        axes[0, 0].set_title('Overall Sentiment by Product')
        axes[0, 0].set_ylabel('Sentiment Polarity')
        
        # Plot 2: Average Ratings
        axes[0, 1].bar(product_types, report['average_rating'].values())
        axes[0, 1].set_title('Average Ratings by Product')
        axes[0, 1].set_ylabel('Rating (1-5)')
        
        # Plot 3: Criteria Mentions
        mentions_df = pd.DataFrame(report['criteria_mentions'])
        mentions_df.plot(kind='bar', ax=axes[1, 0])
        axes[1, 0].set_title('Criteria Mentions by Product')
        axes[1, 0].set_ylabel('Mention Count')
        
        # Plot 4: Criteria Sentiment
        sentiment_df = pd.DataFrame(report['criteria_sentiment'])
        sentiment_df.plot(kind='bar', ax=axes[1, 1])
        axes[1, 1].set_title('Criteria Sentiment by Product')
        axes[1, 1].set_ylabel('Average Sentiment')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would be loaded from a file)
    sample_data = {
        'review_text': [
            "This EPDM flooring is very durable and comfortable for volleyball.",
            "TPV rubber has excellent traction but the color fades quickly.",
            "I love how easy it is to clean this EPDM flooring.",
            "The TPV rubber is too hard and hurts my knees during games."
        ],
        'rating': [5, 3, 4, 2],
        'product_type': ['EPDM', 'TPV', 'EPDM', 'TPV']
    }
    
    try:
        analyzer = RubberFlooringAnalyzer(pd.DataFrame(sample_data))
        report = analyzer.generate_report()
        analyzer.plot_analysis()
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
```
