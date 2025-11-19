"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Write a Python script to analyze customer reviews from RanchiOffline's website and generate insights about customer satisfaction with their services.
Generated: DETERMINISTIC_ba729acddb5f0a86
Batch ID: 20250612_153225
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
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import logging
from typing import List, Dict, Tuple, Optional

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
    A class to analyze customer reviews and generate insights about customer satisfaction.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the ReviewAnalyzer with the path to the review data.
        
        Args:
            data_path (str): Path to the CSV file containing review data
        """
        self.data_path = data_path
        self.reviews_df = None
        self.insights = {}
        
    def load_data(self) -> None:
        """
        Load review data from the specified CSV file.
        Handles potential file reading errors.
        """
        try:
            self.reviews_df = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")
            
            # Check required columns
            required_columns = {'review_text', 'rating', 'date'}
            if not required_columns.issubset(self.reviews_df.columns):
                missing = required_columns - set(self.reviews_df.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise
    
    def clean_text(self, text: str) -> str:
        """
        Clean review text by removing special characters, extra spaces, etc.
        
        Args:
            text (str): Raw review text
            
        Returns:
            str: Cleaned review text
        """
        if not isinstance(text, str):
            return ""
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def analyze_sentiment(self, text: str) -> float:
        """
        Perform sentiment analysis on review text using TextBlob.
        
        Args:
            text (str): Review text to analyze
            
        Returns:
            float: Sentiment polarity score (-1 to 1)
        """
        try:
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        except Exception as e:
            logging.warning(f"Error analyzing sentiment: {str(e)}")
            return 0.0
    
    def categorize_sentiment(self, score: float) -> str:
        """
        Categorize sentiment score into positive, neutral, or negative.
        
        Args:
            score (float): Sentiment polarity score
            
        Returns:
            str: Sentiment category
        """
        if score > 0.1:
            return "positive"
        elif score < -0.1:
            return "negative"
        else:
            return "neutral"
    
    def preprocess_reviews(self) -> None:
        """
        Preprocess reviews by cleaning text and adding sentiment analysis columns.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        logging.info("Preprocessing reviews...")
        
        # Clean review text
        self.reviews_df['cleaned_text'] = self.reviews_df['review_text'].apply(self.clean_text)
        
        # Analyze sentiment
        self.reviews_df['sentiment_score'] = self.reviews_df['cleaned_text'].apply(self.analyze_sentiment)
        self.reviews_df['sentiment'] = self.reviews_df['sentiment_score'].apply(self.categorize_sentiment)
        
        # Convert date to datetime
        self.reviews_df['date'] = pd.to_datetime(self.reviews_df['date'], errors='coerce')
        
        logging.info("Preprocessing completed.")
    
    def generate_insights(self) -> Dict:
        """
        Generate insights from the review data including:
        - Overall satisfaction metrics
        - Sentiment distribution
        - Common positive/negative words
        - Rating distribution
        - Temporal trends
        
        Returns:
            Dict: Dictionary containing all generated insights
        """
        if self.reviews_df is None:
            raise ValueError("Data not processed. Call preprocess_reviews() first.")
            
        logging.info("Generating insights...")
        
        # Basic statistics
        self.insights['total_reviews'] = len(self.reviews_df)
        self.insights['average_rating'] = self.reviews_df['rating'].mean()
        
        # Sentiment distribution
        sentiment_counts = self.reviews_df['sentiment'].value_counts(normalize=True)
        self.insights['sentiment_distribution'] = sentiment_counts.to_dict()
        
        # Rating distribution
        rating_counts = self.reviews_df['rating'].value_counts().sort_index()
        self.insights['rating_distribution'] = rating_counts.to_dict()
        
        # Temporal trends (monthly)
        if 'date' in self.reviews_df.columns and not self.reviews_df['date'].isnull().all():
            monthly_trends = self.reviews_df.set_index('date').resample('M').agg({
                'rating': 'mean',
                'sentiment_score': 'mean',
                'review_text': 'count'
            })
            self.insights['monthly_trends'] = monthly_trends.to_dict('index')
        
        # Common words
        self._generate_word_clouds()
        
        logging.info("Insights generated successfully.")
        return self.insights
    
    def _generate_word_clouds(self) -> None:
        """
        Generate word clouds for positive and negative reviews.
        """
        try:
            # Positive reviews word cloud
            positive_reviews = ' '.join(self.reviews_df[self.reviews_df['sentiment'] == 'positive']['cleaned_text'])
            if positive_reviews:
                wordcloud_pos = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews)
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud_pos, interpolation='bilinear')
                plt.axis('off')
                plt.title('Most Common Positive Words')
                plt.savefig('positive_words.png', bbox_inches='tight')
                plt.close()
            
            # Negative reviews word cloud
            negative_reviews = ' '.join(self.reviews_df[self.reviews_df['sentiment'] == 'negative']['cleaned_text'])
            if negative_reviews:
                wordcloud_neg = WordCloud(width=800, height=400, background_color='white').generate(negative_reviews)
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud_neg, interpolation='bilinear')
                plt.axis('off')
                plt.title('Most Common Negative Words')
                plt.savefig('negative_words.png', bbox_inches='tight')
                plt.close()
                
            self.insights['wordclouds_generated'] = True
        except Exception as e:
            logging.error(f"Error generating word clouds: {str(e)}")
            self.insights['wordclouds_generated'] = False
    
    def save_insights(self, output_path: str = 'insights.json') -> None:
        """
        Save generated insights to a JSON file.
        
        Args:
            output_path (str): Path to save the insights file
        """
        try:
            import json
            with open(output_path, 'w') as f:
                json.dump(self.insights, f, indent=4)
            logging.info(f"Insights saved to {output_path}")
        except Exception as e:
            logging.error(f"Error saving insights: {str(e)}")
            raise
    
    def visualize_insights(self) -> None:
        """
        Generate visualizations for key insights.
        """
        try:
            # Sentiment distribution pie chart
            plt.figure(figsize=(8, 6))
            self.reviews_df['sentiment'].value_counts().plot.pie(
                autopct='%1.1f%%',
                colors=['green', 'red', 'gray']
            )
            plt.title('Sentiment Distribution')
            plt.savefig('sentiment_distribution.png', bbox_inches='tight')
            plt.close()
            
            # Rating distribution bar chart
            plt.figure(figsize=(8, 6))
            self.reviews_df['rating'].value_counts().sort_index().plot.bar()
            plt.title('Rating Distribution')
            plt.xlabel('Rating')
            plt.ylabel('Count')
            plt.savefig('rating_distribution.png', bbox_inches='tight')
            plt.close()
            
            # Monthly trends if available
            if 'monthly_trends' in self.insights:
                monthly_data = pd.DataFrame.from_dict(self.insights['monthly_trends'], orient='index')
                plt.figure(figsize=(12, 6))
                monthly_data['rating'].plot(label='Average Rating')
                monthly_data['sentiment_score'].plot
