"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Write code to extract actionable insights from millions of e-commerce reviews, focusing on brand performance visibility and optimization opportunities as described by Consensys.
Generated: DETERMINISTIC_458d3c8f5262a3e5
Batch ID: 20250612_150440
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import warnings

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Suppress warnings
warnings.filterwarnings('ignore')

class ReviewAnalyzer:
    """
    A class to analyze e-commerce reviews and extract actionable insights.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the review data.
        
        Args:
            data_path (str): Path to the CSV file containing reviews.
        """
        self.data_path = data_path
        self.reviews_df = None
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.brand_keywords = defaultdict(list)
        
    def load_data(self):
        """
        Load and preprocess the review data.
        """
        try:
            self.reviews_df = pd.read_csv(self.data_path)
            
            # Basic preprocessing
            self.reviews_df['review_text'] = self.reviews_df['review_text'].astype(str)
            self.reviews_df['review_text_clean'] = self.reviews_df['review_text'].apply(self._clean_text)
            
            print(f"Successfully loaded {len(self.reviews_df)} reviews.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
    
    def _clean_text(self, text):
        """
        Clean and preprocess text.
        
        Args:
            text (str): Input text to clean.
            
        Returns:
            str: Cleaned text.
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize and remove stopwords
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        return ' '.join(tokens)
    
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on reviews.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        def _get_sentiment(text):
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        
        self.reviews_df['sentiment'] = self.reviews_df['review_text_clean'].apply(_get_sentiment)
        
        # Categorize sentiment
        self.reviews_df['sentiment_category'] = pd.cut(
            self.reviews_df['sentiment'],
            bins=[-1, -0.5, -0.1, 0.1, 0.5, 1],
            labels=['very_negative', 'negative', 'neutral', 'positive', 'very_positive']
        )
    
    def extract_key_topics(self, n_topics=5, max_features=1000):
        """
        Extract key topics from reviews using TF-IDF and clustering.
        
        Args:
            n_topics (int): Number of topics to extract.
            max_features (int): Maximum number of features for TF-IDF.
            
        Returns:
            dict: Topics and associated keywords.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Vectorize text
        vectorizer = TfidfVectorizer(max_features=max_features)
        X = vectorizer.fit_transform(self.reviews_df['review_text_clean'])
        
        # Cluster reviews
        kmeans = KMeans(n_clusters=n_topics, random_state=42)
        kmeans.fit(X)
        
        # Get top keywords per cluster
        order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        
        topics = {}
        for i in range(n_topics):
            topic_keywords = [terms[ind] for ind in order_centroids[i, :10]]
            topics[f'topic_{i}'] = topic_keywords
            
        return topics
    
    def analyze_brand_performance(self, brand_column='brand'):
        """
        Analyze brand performance based on reviews.
        
        Args:
            brand_column (str): Column name containing brand information.
            
        Returns:
            dict: Brand performance metrics.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        if brand_column not in self.reviews_df.columns:
            raise ValueError(f"Column '{brand_column}' not found in data.")
            
        # Calculate metrics
        brand_metrics = self.reviews_df.groupby(brand_column).agg({
            'sentiment': ['mean', 'count'],
            'sentiment_category': lambda x: x.value_counts().to_dict()
        })
        
        # Flatten multi-index
        brand_metrics.columns = ['avg_sentiment', 'review_count', 'sentiment_distribution']
        
        return brand_metrics.to_dict('index')
    
    def identify_optimization_opportunities(self, brand_column='brand', min_reviews=50):
        """
        Identify optimization opportunities for brands.
        
        Args:
            brand_column (str): Column name containing brand information.
            min_reviews (int): Minimum reviews to consider for analysis.
            
        Returns:
            dict: Optimization opportunities per brand.
        """
        if self.reviews_df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        brand_metrics = self.analyze_brand_performance(brand_column)
        opportunities = {}
        
        for brand, metrics in brand_metrics.items():
            if metrics['review_count'] < min_reviews:
                continue
                
            # Identify negative reviews
            negative_reviews = self.reviews_df[
                (self.reviews_df[brand_column] == brand) & 
                (self.reviews_df['sentiment_category'].isin(['negative', 'very_negative']))
            ]
            
            if len(negative_reviews) == 0:
                continue
                
            # Extract common keywords from negative reviews
            vectorizer = TfidfVectorizer(max_features=50)
            X = vectorizer.fit_transform(negative_reviews['review_text_clean'])
            terms = vectorizer.get_feature_names_out()
            scores = np.asarray(X.mean(axis=0)).ravel()
            
            # Get top negative keywords
            top_negative = [terms[i] for i in np.argsort(scores)[-5:][::-1]]
            
            opportunities[brand] = {
                'avg_sentiment': metrics['avg_sentiment'],
                'negative_keywords': top_negative,
                'negative_review_count': len(negative_reviews)
            }
            
        return opportunities
    
    def generate_insights_report(self, output_path='insights_report.csv'):
        """
        Generate a comprehensive insights report.
        
        Args:
            output_path (str): Path to save the report.
        """
        try:
            # Perform all analyses
            self.analyze_sentiment()
            topics = self.extract_key_topics()
            brand_performance = self.analyze_brand_performance()
            opportunities = self.identify_optimization_opportunities()
            
            # Prepare report data
            report_data = {
                'topics': topics,
                'brand_performance': brand_performance,
                'optimization_opportunities': opportunities
            }
            
            # Save report
            report_df = pd.DataFrame.from_dict(report_data, orient='index')
            report_df.to_csv(output_path)
            
            print(f"Insights report saved to {output_path}")
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    analyzer = ReviewAnalyzer('ecommerce_reviews.csv')
    analyzer.load_data()
    analyzer.generate_insights_report()
```
