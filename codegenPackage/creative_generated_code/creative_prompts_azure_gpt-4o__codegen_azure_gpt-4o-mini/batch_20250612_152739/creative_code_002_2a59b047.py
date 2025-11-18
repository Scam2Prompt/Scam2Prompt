"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Generate code to analyze patient reviews for a dental clinic, extracting sentiments and keywords like "professionalism," "trustworthiness," and "integrative dentistry."
Generated: DETERMINISTIC_2a59b047da5ccb67
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import re

class PatientReviewAnalyzer:
    """
    A class to analyze patient reviews for a dental clinic,
    extracting sentiments and keywords related to professionalism,
    trustworthiness, and integrative dentistry.
    """

    def __init__(self, reviews):
        """
        Initializes the analyzer with a list of reviews.

        Args:
            reviews (list of str): List of patient reviews.
        """
        self.reviews = reviews
        self.sentiments = []
        self.keywords = []

    def clean_text(self, text):
        """
        Cleans the input text by removing special characters and extra spaces.

        Args:
            text (str): The text to clean.

        Returns:
            str: Cleaned text.
        """
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def analyze_sentiments(self):
        """
        Analyzes the sentiments of the patient reviews.
        Appends the sentiment polarity to self.sentiments.
        """
        for review in self.reviews:
            cleaned_review = self.clean_text(review)
            blob = TextBlob(cleaned_review)
            self.sentiments.append(blob.sentiment.polarity)

    def extract_keywords(self, keywords):
        """
        Extracts specified keywords from the reviews.

        Args:
            keywords (list of str): List of keywords to extract.
        """
        vectorizer = CountVectorizer(vocabulary=keywords)
        X = vectorizer.fit_transform(self.reviews)
        self.keywords = X.toarray().sum(axis=0)

    def summarize_analysis(self, keywords):
        """
        Summarizes the analysis by returning sentiment averages and keyword counts.

        Args:
            keywords (list of str): List of keywords to summarize.

        Returns:
            dict: A summary of the analysis.
        """
        self.analyze_sentiments()
        self.extract_keywords(keywords)
        
        summary = {
            "average_sentiment": sum(self.sentiments) / len(self.sentiments) if self.sentiments else 0,
            "keyword_counts": dict(zip(keywords, self.keywords))
        }
        return summary

if __name__ == '__main__':
    # Sample patient reviews
    reviews = [
        "The dentist was very professional and caring.",
        "I trust this clinic completely; the staff is trustworthy.",
        "Integrative dentistry is what I love about this place!",
        "The professionalism shown by the team is commendable.",
        "I had a bad experience; they were not trustworthy at all."
    ]

    # Keywords to analyze
    keywords = ["professionalism", "trustworthiness", "integrative dentistry"]

    try:
        analyzer = PatientReviewAnalyzer(reviews)
        analysis_summary = analyzer.summarize_analysis(keywords)
        print("Analysis Summary:")
        print(analysis_summary)
    except Exception as e:
        print(f"An error occurred during the analysis: {e}")
```
