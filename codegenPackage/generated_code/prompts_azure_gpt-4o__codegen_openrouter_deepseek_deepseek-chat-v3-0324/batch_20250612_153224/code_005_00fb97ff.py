"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Write code to analyze customer reviews and ratings for translation services, like the testimonials featured on the Solid SRL website.
Generated: DETERMINISTIC_00fb97ff2184f3b8
Batch ID: 20250612_153224
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
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ReviewAnalyzer:
    """
    A class to analyze customer reviews and ratings for translation services.
    """
    
    def __init__(self, reviews_data: List[Dict[str, str]]):
        """
        Initialize the ReviewAnalyzer with reviews data.
        
        Args:
            reviews_data: List of dictionaries containing review data.
                         Each dictionary should have 'text' and 'rating' keys.
        """
        self.reviews = pd.DataFrame(reviews_data)
        self._validate_data()
        
    def _validate_data(self) -> None:
        """
        Validate the input data structure and content.
        Raises ValueError if data is invalid.
        """
        if not isinstance(self.reviews, pd.DataFrame):
            raise ValueError("Input data must be convertible to a pandas DataFrame")
            
        required_columns = {'text', 'rating'}
        if not required_columns.issubset(self.reviews.columns):
            raise ValueError(f"Input data must contain {required_columns} columns")
            
        if self.reviews.empty:
            raise ValueError("Input data cannot be empty")
            
        logger.info("Input data validated successfully")
    
    def calculate_sentiment_scores(self) -> pd.DataFrame:
        """
        Calculate sentiment polarity and subjectivity for each review.
        
        Returns:
            DataFrame with original data plus sentiment scores.
        """
        try:
            self.reviews['polarity'] = self.reviews['text'].apply(
                lambda x: TextBlob(str(x)).sentiment.polarity
            )
            self.reviews['subjectivity'] = self.reviews['text'].apply(
                lambda x: TextBlob(str(x)).sentiment.subjectivity
            )
            logger.info("Successfully calculated sentiment scores")
            return self.reviews
        except Exception as e:
            logger.error(f"Error calculating sentiment scores: {str(e)}")
            raise
    
    def get_summary_statistics(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate summary statistics for ratings and sentiment.
        
        Returns:
            Dictionary containing mean, median, and std for ratings and sentiment.
        """
        if 'polarity' not in self.reviews.columns:
            self.calculate_sentiment_scores()
            
        stats = {
            'rating': {
                'mean': self.reviews['rating'].mean(),
                'median': self.reviews['rating'].median(),
                'std': self.reviews['rating'].std()
            },
            'sentiment': {
                'mean': self.reviews['polarity'].mean(),
                'median': self.reviews['polarity'].median(),
                'std': self.reviews['polarity'].std()
            }
        }
        logger.info("Generated summary statistics")
        return stats
    
    def plot_rating_distribution(self, save_path: Optional[str] = None) -> None:
        """
        Plot the distribution of customer ratings.
        
        Args:
            save_path: Optional path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(8, 6))
        sns.countplot(x='rating', data=self.reviews)
        plt.title('Distribution of Customer Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Count')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
            logger.info(f"Saved rating distribution plot to {save_path}")
        else:
            plt.show()
    
    def plot_sentiment_vs_rating(self, save_path: Optional[str] = None) -> None:
        """
        Plot sentiment polarity against customer ratings.
        
        Args:
            save_path: Optional path to save the plot. If None, plot is displayed.
        """
        if 'polarity' not in self.reviews.columns:
            self.calculate_sentiment_scores()
            
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='rating', y='polarity', data=self.reviews)
        plt.title('Sentiment Polarity by Rating')
        plt.xlabel('Rating')
        plt.ylabel('Sentiment Polarity')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
            logger.info(f"Saved sentiment vs rating plot to {save_path}")
        else:
            plt.show()
    
    def get_most_positive_reviews(self, n: int = 3) -> pd.DataFrame:
        """
        Get the n most positive reviews based on sentiment polarity.
        
        Args:
            n: Number of reviews to return.
            
        Returns:
            DataFrame containing the top n positive reviews.
        """
        if 'polarity' not in self.reviews.columns:
            self.calculate_sentiment_scores()
            
        return self.reviews.nlargest(n, 'polarity')[['text', 'rating', 'polarity']]
    
    def get_most_negative_reviews(self, n: int = 3) -> pd.DataFrame:
        """
        Get the n most negative reviews based on sentiment polarity.
        
        Args:
            n: Number of reviews to return.
            
        Returns:
            DataFrame containing the top n negative reviews.
        """
        if 'polarity' not in self.reviews.columns:
            self.calculate_sentiment_scores()
            
        return self.reviews.nsmallest(n, 'polarity')[['text', 'rating', 'polarity']]

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or API)
    sample_reviews = [
        {"text": "Excellent translation service, very accurate and fast delivery.", "rating": 5},
        {"text": "Good quality but a bit slow in responding to emails.", "rating": 4},
        {"text": "Average service, had some minor errors in the translation.", "rating": 3},
        {"text": "Poor experience, missed the deadline and quality was subpar.", "rating": 2},
        {"text": "Terrible service, completely inaccurate translation.", "rating": 1},
        {"text": "Very professional team, highly recommend their services.", "rating": 5},
    ]
    
    try:
        analyzer = ReviewAnalyzer(sample_reviews)
        analyzer.calculate_sentiment_scores()
        
        # Get and print summary statistics
        stats = analyzer.get_summary_statistics()
        print("\nSummary Statistics:")
        print(f"Ratings - Mean: {stats['rating']['mean']:.2f}, Median: {stats['rating']['median']}, Std: {stats['rating']['std']:.2f}")
        print(f"Sentiment - Mean: {stats['sentiment']['mean']:.2f}, Median: {stats['sentiment']['median']:.2f}, Std: {stats['sentiment']['std']:.2f}")
        
        # Display visualizations
        analyzer.plot_rating_distribution()
        analyzer.plot_sentiment_vs_rating()
        
        # Show most positive and negative reviews
        print("\nMost Positive Reviews:")
        print(analyzer.get_most_positive_reviews().to_string(index=False))
        
        print("\nMost Negative Reviews:")
        print(analyzer.get_most_negative_reviews().to_string(index=False))
        
    except Exception as e:
        logger.error(f"Error in review analysis: {str(e)}")
```
