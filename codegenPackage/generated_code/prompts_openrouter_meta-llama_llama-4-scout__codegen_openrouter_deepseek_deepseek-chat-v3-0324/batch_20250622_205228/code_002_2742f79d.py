"""
Generated Code Metadata:
========================
Original URL: https://consensys.world
Prompt: Generate a code snippet to categorize and analyze e-commerce reviews using machine learning techniques, such as topic modeling and sentiment analysis.
Generated: DETERMINISTIC_2742f79d5876f3ff
Batch ID: 20250622_205228
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class ReviewAnalyzer:
    """
    A class to categorize and analyze e-commerce reviews using topic modeling and sentiment analysis.
    """
    
    def __init__(self, reviews):
        """
        Initialize the ReviewAnalyzer with a list of reviews.
        
        Args:
            reviews (list): List of review texts
        """
        self.reviews = reviews
        self.cleaned_reviews = None
        self.vectorizer = None
        self.tfidf_matrix = None
        self.lda_model = None
        self.topics = None
        
    def clean_text(self, text):
        """
        Clean and preprocess text by removing special characters, stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to clean
            
        Returns:
            str: Cleaned text
        """
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
        
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words]
        
        # Lemmatize
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        
        return ' '.join(tokens)
    
    def preprocess_reviews(self):
        """
        Preprocess all reviews by cleaning them.
        """
        self.cleaned_reviews = [self.clean_text(review) for review in self.reviews]
    
    def perform_topic_modeling(self, n_topics=5, max_iter=10):
        """
        Perform topic modeling using LDA on the reviews.
        
        Args:
            n_topics (int): Number of topics to identify
            max_iter (int): Maximum number of iterations for LDA
        """
        if not self.cleaned_reviews:
            self.preprocess_reviews()
            
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=1000)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.cleaned_reviews)
        
        # Perform LDA
        self.lda_model = LatentDirichletAllocation(n_components=n_topics, max_iter=max_iter, random_state=42)
        self.lda_model.fit(self.tfidf_matrix)
        
        # Get topics
        self._extract_topics()
    
    def _extract_topics(self):
        """
        Extract and store the top words for each topic.
        """
        if not self.lda_model or not self.vectorizer:
            raise ValueError("Topic modeling must be performed first")
            
        feature_names = self.vectorizer.get_feature_names_out()
        self.topics = []
        
        for topic_idx, topic in enumerate(self.lda_model.components_):
            top_features = [feature_names[i] for i in topic.argsort()[:-6:-1]]
            self.topics.append({
                'topic_id': topic_idx,
                'top_words': top_features
            })
    
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on each review.
        
        Returns:
            list: List of dictionaries containing sentiment analysis results for each review
        """
        results = []
        
        for idx, review in enumerate(self.reviews):
            analysis = TextBlob(review)
            sentiment = 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'
            
            results.append({
                'review_id': idx,
                'text': review,
                'polarity': analysis.sentiment.polarity,
                'subjectivity': analysis.sentiment.subjectivity,
                'sentiment': sentiment
            })
            
        return results
    
    def get_topic_distribution(self):
        """
        Get the topic distribution for each review.
        
        Returns:
            numpy.ndarray: Topic distribution matrix (n_reviews x n_topics)
        """
        if not self.lda_model or not self.tfidf_matrix:
            raise ValueError("Topic modeling must be performed first")
            
        return self.lda_model.transform(self.tfidf_matrix)
    
    def get_topics(self):
        """
        Get the identified topics.
        
        Returns:
            list: List of topics with their top words
        """
        return self.topics

# Example usage
if __name__ == "__main__":
    # Sample reviews
    sample_reviews = [
        "The product is amazing! Works perfectly and exceeded my expectations.",
        "Terrible quality. Broke after just two days of use.",
        "Good value for money but shipping took longer than expected.",
        "The customer service was horrible. They didn't respond to my complaints.",
        "I love this product! It's exactly what I was looking for."
    ]
    
    try:
        # Initialize analyzer
        analyzer = ReviewAnalyzer(sample_reviews)
        
        # Perform topic modeling
        analyzer.perform_topic_modeling(n_topics=3)
        
        # Get topics
        topics = analyzer.get_topics()
        print("Identified Topics:")
        for topic in topics:
            print(f"Topic {topic['topic_id']}: {', '.join(topic['top_words'])}")
        
        # Perform sentiment analysis
        sentiment_results = analyzer.analyze_sentiment()
        print("\nSentiment Analysis Results:")
        for result in sentiment_results:
            print(f"Review {result['review_id']}: {result['sentiment']} (Polarity: {result['polarity']:.2f})")
        
        # Get topic distribution
        topic_dist = analyzer.get_topic_distribution()
        print("\nTopic Distribution:")
        print(topic_dist)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
