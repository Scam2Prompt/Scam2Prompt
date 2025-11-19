"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Develop a code snippet to analyze customer testimonials on the Vitality Holistic website, using natural language processing (NLP) techniques to identify common themes and sentiments expressed by clients.
Generated: DETERMINISTIC_3601c8ae4b3cc596
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
import numpy as np
from textblob import TextBlob
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

class TestimonialAnalyzer:
    """
    Analyzes customer testimonials using NLP techniques to extract themes and sentiments.
    """
    
    def __init__(self, testimonial_data):
        """
        Initialize with testimonial data.
        
        Args:
            testimonial_data (list or pd.Series): List of customer testimonials
        """
        if isinstance(testimonial_data, list):
            self.testimonials = pd.Series(testimonial_data)
        else:
            self.testimonials = testimonial_data
            
        self.clean_testimonials = None
        self.themes = None
        self.sentiment_scores = None
        
    def clean_text(self):
        """
        Clean testimonial text by removing special characters and normalizing.
        """
        def _clean(text):
            text = text.lower()
            text = re.sub(r'[^\w\s]', '', text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text
            
        self.clean_testimonials = self.testimonials.apply(_clean)
        
    def analyze_sentiment(self):
        """
        Perform sentiment analysis on testimonials using TextBlob.
        """
        if self.clean_testimonials is None:
            self.clean_text()
            
        self.sentiment_scores = self.clean_testimonials.apply(
            lambda x: TextBlob(x).sentiment.polarity
        )
        
    def extract_themes(self, max_features=50, ngram_range=(1, 2)):
        """
        Extract common themes using TF-IDF vectorization.
        
        Args:
            max_features (int): Maximum number of features to consider
            ngram_range (tuple): Range of n-grams to consider
        """
        if self.clean_testimonials is None:
            self.clean_text()
            
        tfidf = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            stop_words='english'
        )
        
        tfidf_matrix = tfidf.fit_transform(self.clean_testimonials)
        feature_names = tfidf.get_feature_names_out()
        
        # Get top themes by summing TF-IDF scores across all documents
        theme_scores = np.sum(tfidf_matrix.toarray(), axis=0)
        self.themes = dict(zip(feature_names, theme_scores))
        
    def get_common_words(self, top_n=10):
        """
        Get most common words in testimonials.
        
        Args:
            top_n (int): Number of top words to return
            
        Returns:
            list: Top n most common words
        """
        if self.clean_testimonials is None:
            self.clean_text()
            
        all_words = ' '.join(self.clean_testimonials).split()
        word_counts = Counter(all_words)
        return word_counts.most_common(top_n)
        
    def visualize_sentiment(self):
        """
        Visualize sentiment distribution.
        """
        if self.sentiment_scores is None:
            self.analyze_sentiment()
            
        plt.figure(figsize=(8, 6))
        sns.histplot(self.sentiment_scores, bins=20, kde=True)
        plt.title('Distribution of Sentiment Scores')
        plt.xlabel('Sentiment Polarity')
        plt.ylabel('Frequency')
        plt.show()
        
    def visualize_themes(self, top_n=15):
        """
        Visualize top themes.
        
        Args:
            top_n (int): Number of top themes to display
        """
        if self.themes is None:
            self.extract_themes()
            
        sorted_themes = sorted(self.themes.items(), key=lambda x: x[1], reverse=True)[:top_n]
        themes_df = pd.DataFrame(sorted_themes, columns=['Theme', 'Score'])
        
        plt.figure(figsize=(10, 8))
        sns.barplot(x='Score', y='Theme', data=themes_df)
        plt.title('Top Themes in Testimonials')
        plt.tight_layout()
        plt.show()
        
    def generate_report(self):
        """
        Generate a summary report of analysis.
        
        Returns:
            dict: Analysis results including sentiment stats and top themes
        """
        report = {}
        
        if self.sentiment_scores is None:
            self.analyze_sentiment()
            
        report['sentiment_stats'] = {
            'mean': np.mean(self.sentiment_scores),
            'median': np.median(self.sentiment_scores),
            'positive': sum(self.sentiment_scores > 0),
            'neutral': sum(self.sentiment_scores == 0),
            'negative': sum(self.sentiment_scores < 0)
        }
        
        if self.themes is None:
            self.extract_themes()
            
        report['top_themes'] = sorted(self.themes.items(), key=lambda x: x[1], reverse=True)[:10]
        report['common_words'] = self.get_common_words()
        
        return report

# Example usage:
if __name__ == "__main__":
    # Sample testimonials (in production, load from database/API/file)
    testimonials = [
        "Vitality Holistic changed my life! The treatments are amazing.",
        "I feel so much better after just a few sessions. Highly recommend!",
        "The staff is wonderful and the atmosphere is very calming.",
        "Not what I expected. Didn't see much improvement.",
        "Best holistic center in town. Worth every penny."
    ]
    
    analyzer = TestimonialAnalyzer(testimonials)
    analyzer.clean_text()
    analyzer.analyze_sentiment()
    analyzer.extract_themes()
    
    # Generate visualizations
    analyzer.visualize_sentiment()
    analyzer.visualize_themes()
    
    # Get report
    report = analyzer.generate_report()
    print(report)
```
