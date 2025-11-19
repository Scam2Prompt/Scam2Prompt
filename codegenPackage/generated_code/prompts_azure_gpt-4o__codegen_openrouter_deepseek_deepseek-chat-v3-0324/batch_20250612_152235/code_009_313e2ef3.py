"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Create a Python script to analyze client feedback and event success metrics, inspired by the webpage's emphasis on improving event outcomes through data-driven strategies.
Generated: DETERMINISTIC_313e2ef3b34d3eb9
Batch ID: 20250612_152235
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
import seaborn as sns
from textblob import TextBlob
import re
from collections import Counter
import logging
from typing import Dict, List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EventAnalyzer:
    """
    A class to analyze client feedback and event success metrics.
    """
    
    def __init__(self, feedback_file: str, metrics_file: str):
        """
        Initialize the analyzer with feedback and metrics data.
        
        Args:
            feedback_file (str): Path to client feedback CSV file
            metrics_file (str): Path to event metrics CSV file
        """
        self.feedback_file = feedback_file
        self.metrics_file = metrics_file
        self.feedback_df = None
        self.metrics_df = None
        
    def load_data(self) -> None:
        """
        Load and validate the input data files.
        """
        try:
            # Load feedback data
            self.feedback_df = pd.read_csv(self.feedback_file)
            required_feedback_cols = {'event_id', 'feedback_text', 'rating', 'timestamp'}
            if not required_feedback_cols.issubset(self.feedback_df.columns):
                raise ValueError(f"Feedback file missing required columns: {required_feedback_cols}")
            
            # Load metrics data
            self.metrics_df = pd.read_csv(self.metrics_file)
            required_metrics_cols = {'event_id', 'attendees', 'duration', 'cost', 'revenue'}
            if not required_metrics_cols.issubset(self.metrics_df.columns):
                raise ValueError(f"Metrics file missing required columns: {required_metrics_cols}")
                
            logger.info("Data loaded successfully")
            
        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise
    
    def clean_feedback_text(self, text: str) -> str:
        """
        Clean feedback text by removing special characters and extra spaces.
        
        Args:
            text (str): Raw feedback text
            
        Returns:
            str: Cleaned feedback text
        """
        if not isinstance(text, str):
            return ""
        
        # Remove special characters except basic punctuation
        text = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", text)
        # Collapse multiple spaces
        text = re.sub(r"\s+", " ", text).strip()
        return text.lower()
    
    def analyze_sentiment(self) -> pd.DataFrame:
        """
        Perform sentiment analysis on feedback text.
        
        Returns:
            pd.DataFrame: DataFrame with sentiment analysis results
        """
        if self.feedback_df is None:
            raise ValueError("Feedback data not loaded")
            
        try:
            # Clean feedback text
            self.feedback_df['cleaned_text'] = self.feedback_df['feedback_text'].apply(self.clean_feedback_text)
            
            # Calculate sentiment polarity (-1 to 1)
            self.feedback_df['sentiment'] = self.feedback_df['cleaned_text'].apply(
                lambda x: TextBlob(x).sentiment.polarity
            )
            
            # Categorize sentiment
            self.feedback_df['sentiment_category'] = pd.cut(
                self.feedback_df['sentiment'],
                bins=[-1, -0.1, 0.1, 1],
                labels=['negative', 'neutral', 'positive']
            )
            
            logger.info("Sentiment analysis completed")
            return self.feedback_df
            
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {e}")
            raise
    
    def calculate_event_metrics(self) -> pd.DataFrame:
        """
        Calculate key event metrics and ROI.
        
        Returns:
            pd.DataFrame: DataFrame with calculated metrics
        """
        if self.metrics_df is None:
            raise ValueError("Metrics data not loaded")
            
        try:
            # Calculate basic metrics
            self.metrics_df['profit'] = self.metrics_df['revenue'] - self.metrics_df['cost']
            self.metrics_df['roi'] = (self.metrics_df['profit'] / self.metrics_df['cost']) * 100
            self.metrics_df['cost_per_attendee'] = self.metrics_df['cost'] / self.metrics_df['attendees']
            
            logger.info("Event metrics calculated")
            return self.metrics_df
            
        except Exception as e:
            logger.error(f"Error calculating event metrics: {e}")
            raise
    
    def merge_datasets(self) -> pd.DataFrame:
        """
        Merge feedback and metrics data for comprehensive analysis.
        
        Returns:
            pd.DataFrame: Merged DataFrame
        """
        try:
            if self.feedback_df is None or self.metrics_df is None:
                raise ValueError("Both datasets must be loaded before merging")
                
            merged_df = pd.merge(
                self.metrics_df,
                self.feedback_df.groupby('event_id').agg({
                    'rating': 'mean',
                    'sentiment': 'mean',
                    'sentiment_category': lambda x: x.mode()[0]
                }).reset_index(),
                on='event_id',
                how='left'
            )
            
            # Fill NA values for events without feedback
            merged_df['rating'] = merged_df['rating'].fillna(0)
            merged_df['sentiment'] = merged_df['sentiment'].fillna(0)
            merged_df['sentiment_category'] = merged_df['sentiment_category'].fillna('neutral')
            
            logger.info("Datasets merged successfully")
            return merged_df
            
        except Exception as e:
            logger.error(f"Error merging datasets: {e}")
            raise
    
    def get_top_keywords(self, n: int = 10, sentiment: Optional[str] = None) -> Dict[str, int]:
        """
        Extract top keywords from feedback text.
        
        Args:
            n (int): Number of top keywords to return
            sentiment (str): Filter by sentiment ('positive', 'negative', 'neutral')
            
        Returns:
            Dict[str, int]: Dictionary of keywords and their counts
        """
        if self.feedback_df is None:
            raise ValueError("Feedback data not loaded")
            
        try:
            df = self.feedback_df.copy()
            
            if sentiment:
                df = df[df['sentiment_category'] == sentiment]
                
            # Tokenize and count words
            words = []
            for text in df['cleaned_text']:
                words.extend(text.split())
                
            # Remove stopwords and short words
            stopwords = {'the', 'and', 'to', 'of', 'a', 'in', 'it', 'is', 'was', 'for', 'on', 'that', 'this'}
            words = [word for word in words if len(word) > 2 and word not in stopwords]
            
            word_counts = Counter(words)
            return dict(word_counts.most_common(n))
            
        except Exception as e:
            logger.error(f"Error extracting keywords: {e}")
            raise
    
    def generate_report(self, output_file: str = "event_analysis_report.html") -> None:
        """
        Generate a comprehensive HTML report with visualizations.
        
        Args:
            output_file (str): Path to save the HTML report
        """
        try:
            # Perform all analyses
            sentiment_df = self.analyze_sentiment()
            metrics_df = self.calculate_event_metrics()
            merged_df = self.merge_datasets()
            
            # Create visualizations
            plt.figure(figsize=(15, 10))
            
            # Sentiment distribution
            plt.subplot(2, 2, 1)
            sns.countplot(data=sentiment_df, x='sentiment_category', order=['positive', 'neutral', 'negative'])
            plt.title('Feedback Sentiment Distribution')
            
            # Rating distribution
            plt.subplot(2, 2, 2)
            sns.histplot(data=sentiment_df, x='rating', bins=5)
            plt.title('Rating Distribution')
            
            # ROI vs Sentiment
            plt.subplot(2, 2, 3)
            sns.boxplot(data=merged_df, x='sentiment_category', y='roi', order=['positive', 'neutral', 'negative'])
            plt.title('ROI by Sentiment Category')
            
            # Top keywords
            top_keywords = self.get_top_keywords(n=5)
            plt.subplot(2, 2, 4)
            plt.bar(top_keywords.keys(), top_keywords.values())
            plt.title('Top 5 Feedback Keywords')
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            
            # Save report
            plt.savefig('temp_plot.png')
            
            # Create HTML report
            html_content = f"""
            <html>
                <head>
                    <title>Event Analysis Report</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; }}
                        h1 {{ color: #2c3e50; }}
                        .section {{
