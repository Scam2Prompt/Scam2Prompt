"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Design a system to categorize and prioritize entrepreneur testimonials for a business training course, using natural language processing techniques.
Generated: DETERMINISTIC_d4e6fb95b6dd903f
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import warnings

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

warnings.filterwarnings('ignore')

class TestimonialAnalyzer:
    """
    A system to categorize and prioritize entrepreneur testimonials using NLP techniques.
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.cluster_model = None
        self.optimal_clusters = 0
        
    def preprocess_text(self, text):
        """
        Clean and preprocess text data.
        """
        # Lowercase
        text = text.lower()
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        return ' '.join(tokens)
    
    def determine_optimal_clusters(self, tfidf_matrix, max_clusters=10):
        """
        Find optimal number of clusters using silhouette score.
        """
        best_score = -1
        best_clusters = 2
        
        for n_clusters in range(2, max_clusters + 1):
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            cluster_labels = kmeans.fit_predict(tfidf_matrix)
            silhouette_avg = silhouette_score(tfidf_matrix, cluster_labels)
            
            if silhouette_avg > best_score:
                best_score = silhouette_avg
                best_clusters = n_clusters
                
        return best_clusters
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment polarity and subjectivity.
        """
        analysis = TextBlob(text)
        return {
            'polarity': analysis.sentiment.polarity,
            'subjectivity': analysis.sentiment.subjectivity
        }
    
    def fit(self, testimonials):
        """
        Fit the model to the testimonials data.
        """
        # Preprocess text
        processed_texts = [self.preprocess_text(t) for t in testimonials]
        
        # Vectorize text
        tfidf_matrix = self.vectorizer.fit_transform(processed_texts)
        
        # Determine optimal clusters
        self.optimal_clusters = self.determine_optimal_clusters(tfidf_matrix)
        
        # Train clustering model
        self.cluster_model = KMeans(n_clusters=self.optimal_clusters, random_state=42)
        self.cluster_model.fit(tfidf_matrix)
        
        return self
    
    def predict(self, testimonials):
        """
        Predict categories and priorities for new testimonials.
        """
        if not self.cluster_model:
            raise ValueError("Model has not been fitted yet. Call fit() first.")
            
        # Preprocess text
        processed_texts = [self.preprocess_text(t) for t in testimonials]
        
        # Vectorize text
        tfidf_matrix = self.vectorizer.transform(processed_texts)
        
        # Get predictions
        clusters = self.cluster_model.predict(tfidf_matrix)
        
        # Analyze sentiment for each testimonial
        results = []
        for i, text in enumerate(testimonials):
            sentiment = self.analyze_sentiment(text)
            results.append({
                'text': text,
                'cluster': int(clusters[i]),
                'polarity': sentiment['polarity'],
                'subjectivity': sentiment['subjectivity'],
                'priority_score': self._calculate_priority_score(sentiment)
            })
            
        return pd.DataFrame(results)
    
    def _calculate_priority_score(self, sentiment):
        """
        Calculate priority score based on sentiment analysis.
        """
        # Higher polarity (more positive) and lower subjectivity (more factual) gets higher priority
        return (sentiment['polarity'] + 1) * (1 - sentiment['subjectivity'])


# Example usage
if __name__ == "__main__":
    # Sample testimonials
    testimonials = [
        "This course changed my life! I doubled my revenue in just 3 months.",
        "The content was good but I expected more practical examples.",
        "Waste of money. Didn't learn anything new.",
        "The instructor is amazing! Very knowledgeable and engaging.",
        "It's okay, but not worth the high price.",
        "Best investment I've made in my business education!",
        "Some useful tips but mostly common sense.",
        "The networking opportunities alone were worth the price.",
        "Too theoretical. Needs more hands-on exercises.",
        "Completely transformed how I approach my business strategy."
    ]
    
    analyzer = TestimonialAnalyzer()
    analyzer.fit(testimonials)
    
    new_testimonials = [
        "I'm seeing results already after just two weeks!",
        "Not what I expected. The material was too basic.",
        "The course materials are excellent and well-organized."
    ]
    
    results = analyzer.predict(new_testimonials)
    print(results)
```
