"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: Write code to analyze customer reviews and satisfaction data for gardening projects, similar to the metrics highlighted by City Garden México.
Generated: DETERMINISTIC_98a3e97a9ce37dcb
Batch ID: 20250612_153246
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ReviewAnalyzer:
    """
    A class to analyze customer reviews and satisfaction data for gardening projects.
    """
    
    def __init__(self, reviews_file=None, satisfaction_file=None):
        """
        Initialize the analyzer with optional file paths for reviews and satisfaction data.
        
        Args:
            reviews_file (str): Path to CSV file containing customer reviews
            satisfaction_file (str): Path to CSV file containing satisfaction metrics
        """
        self.reviews_df = None
        self.satisfaction_df = None
        
        if reviews_file:
            self.load_reviews(reviews_file)
        if satisfaction_file:
            self.load_satisfaction(satisfaction_file)
    
    def load_reviews(self, file_path):
        """
        Load customer reviews from a CSV file.
        
        Args:
            file_path (str): Path to CSV file containing reviews
        """
        try:
            self.reviews_df = pd.read_csv(file_path)
            print(f"Successfully loaded reviews data with {len(self.reviews_df)} records.")
        except Exception as e:
            print(f"Error loading reviews data: {str(e)}")
    
    def load_satisfaction(self, file_path):
        """
        Load customer satisfaction data from a CSV file.
        
        Args:
            file_path (str): Path to CSV file containing satisfaction metrics
        """
        try:
            self.satisfaction_df = pd.read_csv(file_path)
            print(f"Successfully loaded satisfaction data with {len(self.satisfaction_df)} records.")
        except Exception as e:
            print(f"Error loading satisfaction data: {str(e)}")
    
    def clean_reviews(self):
        """
        Clean the reviews data by handling missing values and standardizing text.
        """
        if self.reviews_df is None:
            print("No reviews data loaded.")
            return
        
        # Handle missing values
        self.reviews_df.dropna(subset=['review_text'], inplace=True)
        
        # Standardize text
        self.reviews_df['clean_text'] = self.reviews_df['review_text'].str.lower().str.strip()
        
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on the reviews using TextBlob.
        """
        if self.reviews_df is None:
            print("No reviews data loaded.")
            return
        
        if 'clean_text' not in self.reviews_df.columns:
            self.clean_reviews()
        
        def get_sentiment(text):
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        
        self.reviews_df['sentiment'] = self.reviews_df['clean_text'].apply(get_sentiment)
        self.reviews_df['sentiment_category'] = pd.cut(
            self.reviews_df['sentiment'],
            bins=[-1, -0.1, 0.1, 1],
            labels=['Negative', 'Neutral', 'Positive']
        )
    
    def plot_sentiment_distribution(self):
        """
        Plot the distribution of sentiment categories.
        """
        if 'sentiment_category' not in self.reviews_df.columns:
            self.analyze_sentiment()
        
        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.reviews_df, x='sentiment_category', order=['Negative', 'Neutral', 'Positive'])
        plt.title('Distribution of Review Sentiments')
        plt.xlabel('Sentiment Category')
        plt.ylabel('Count')
        plt.show()
    
    def analyze_topics(self, n_topics=3, n_words=5):
        """
        Perform topic modeling on reviews using LDA.
        
        Args:
            n_topics (int): Number of topics to identify
            n_words (int): Number of top words to show per topic
        """
        if self.reviews_df is None:
            print("No reviews data loaded.")
            return
        
        if 'clean_text' not in self.reviews_df.columns:
            self.clean_reviews()
        
        # Create TF-IDF vectorizer
        tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        dtm = tfidf.fit_transform(self.reviews_df['clean_text'])
        
        # Perform LDA
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
        lda.fit(dtm)
        
        # Display top words for each topic
        feature_names = tfidf.get_feature_names_out()
        
        for topic_idx, topic in enumerate(lda.components_):
            top_words = [feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]]
            print(f"Topic {topic_idx + 1}: {', '.join(top_words)}")
    
    def analyze_satisfaction_metrics(self):
        """
        Analyze and visualize customer satisfaction metrics.
        """
        if self.satisfaction_df is None:
            print("No satisfaction data loaded.")
            return
        
        # Calculate basic statistics
        print("\nSatisfaction Metrics Summary:")
        print(self.satisfaction_df.describe())
        
        # Plot satisfaction distribution
        plt.figure(figsize=(10, 6))
        for column in self.satisfaction_df.select_dtypes(include=['number']).columns:
            sns.kdeplot(self.satisfaction_df[column], label=column)
        plt.title('Distribution of Satisfaction Metrics')
        plt.xlabel('Score')
        plt.ylabel('Density')
        plt.legend()
        plt.show()
    
    def correlate_sentiment_satisfaction(self):
        """
        Correlate review sentiment with satisfaction metrics.
        """
        if self.reviews_df is None or self.satisfaction_df is None:
            print("Both reviews and satisfaction data must be loaded.")
            return
        
        if 'sentiment' not in self.reviews_df.columns:
            self.analyze_sentiment()
        
        # Merge data (assuming there's a common customer_id column)
        try:
            merged_df = pd.merge(
                self.reviews_df[['customer_id', 'sentiment']],
                self.satisfaction_df,
                on='customer_id'
            )
            
            # Calculate correlations
            correlation_matrix = merged_df.corr()
            
            # Plot correlation heatmap
            plt.figure(figsize=(8, 6))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
            plt.title('Correlation Between Sentiment and Satisfaction Metrics')
            plt.show()
            
        except Exception as e:
            print(f"Error correlating data: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = ReviewAnalyzer()
    
    # Load sample data (replace with actual file paths)
    try:
        analyzer.load_reviews('sample_reviews.csv')
        analyzer.load_satisfaction('sample_satisfaction.csv')
    except:
        print("Sample files not found. Using empty datasets for demonstration.")
    
    # Perform analyses
    analyzer.clean_reviews()
    analyzer.analyze_sentiment()
    analyzer.plot_sentiment_distribution()
    analyzer.analyze_topics()
    analyzer.analyze_satisfaction_metrics()
    analyzer.correlate_sentiment_satisfaction()
```
