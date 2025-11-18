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
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Ensure necessary NLTK data is downloaded
nltk.download('vader_lexicon')

class ReviewAnalyzer:
    """
    A class to analyze patient reviews for a dental clinic, extracting sentiments 
    and keywords like "professionalism," "trustworthiness," and "integrative dentistry."
    """
    
    def __init__(self):
        """
        Initializes the analyzer with a sentiment analyzer and keywords to track.
        """
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.keywords = ["professionalism", "trustworthiness", "integrative dentistry"]
    
    def clean_review(self, review):
        """
        Cleans the review text by removing non-alphanumeric characters and extra spaces.
        
        Args:
            review (str): The raw review text.
        
        Returns:
            str: The cleaned review text.
        """
        # Remove non-alphanumeric characters
        cleaned_review = re.sub(r'[^a-zA-Z0-9\s]', '', review)
        # Remove extra spaces
        cleaned_review = re.sub(r'\s+', ' ', cleaned_review).strip()
        return cleaned_review
    
    def analyze_sentiment(self, review):
        """
        Analyzes the sentiment of a given review using VADER Sentiment Analysis.
        
        Args:
            review (str): The cleaned review text.
        
        Returns:
            dict: A dictionary containing sentiment scores ('pos', 'neu', 'neg', 'compound').
        """
        return self.sentiment_analyzer.polarity_scores(review)
    
    def extract_keywords(self, review):
        """
        Extracts occurrences of predefined keywords from a review.
        
        Args:
            review (str): The cleaned review text.
        
        Returns:
            list: A list of keywords found in the review.
        """
        # Convert review to lowercase for case-insensitive matching
        review_lower = review.lower()
        # Check for keywords in the review
        found_keywords = [keyword for keyword in self.keywords if keyword in review_lower]
        return found_keywords
    
    def process_review(self, review):
        """
        Processes a single review, cleaning it, analyzing sentiment, and extracting keywords.
        
        Args:
            review (str): The raw review text.
        
        Returns:
            dict: A dictionary containing the cleaned review, sentiment scores, and keywords.
        """
        try:
            # Clean the review text
            cleaned_review = self.clean_review(review)
            # Analyze sentiment
            sentiment = self.analyze_sentiment(cleaned_review)
            # Extract keywords
            keywords = self.extract_keywords(cleaned_review)
            return {
                "cleaned_review": cleaned_review,
                "sentiment": sentiment,
                "keywords": keywords
            }
        except Exception as e:
            # Log error and return an empty result
            print(f"Error processing review: {e}")
            return {"cleaned_review": None, "sentiment": None, "keywords": []}

# Example usage
if __name__ == "__main__":
    # Instantiate the analyzer
    analyzer = ReviewAnalyzer()
    # Example patient reviews
    reviews = [
        "The staff showed great professionalism and trustworthiness during my visit.",
        "I appreciate their approach to integrative dentistry. Truly amazing!",
        "Not satisfied with the service. Felt unprofessional."
    ]
    
    # Process each review
    for i, review in enumerate(reviews):
        result = analyzer.process_review(review)
        print(f"Review {i + 1}:")
        print(f"  Cleaned Review: {result['cleaned_review']}")
        print(f"  Sentiment: {result['sentiment']}")
        print(f"  Keywords: {result['keywords']}")
        print()
```
