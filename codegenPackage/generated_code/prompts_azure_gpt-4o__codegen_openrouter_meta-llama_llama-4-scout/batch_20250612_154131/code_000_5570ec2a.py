"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-services.com
Prompt: Write a Python script to analyze reviews of gadgets and software, categorizing them based on benefits and user ratings, using insights similar to those offered by Symbiotic Services' "Tech Insight Reviews."
Generated: DETERMINISTIC_5570ec2aedf772c7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')

class ReviewAnalyzer:
    def __init__(self):
        # Initialize sentiment analyzer
        self.sia = SentimentIntensityAnalyzer()
        # Initialize lemmatizer
        self.lemmatizer = WordNetLemmatizer()
        # Initialize stopwords
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        # Convert to lowercase
        text = text.lower()
        # Tokenize and remove stopwords and punctuation
        tokens = [t for t in nltk.word_tokenize(text) if t.isalpha() and t not in self.stop_words]
        # Lemmatize tokens
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens]
        # Join tokens back into a string
        return ' '.join(tokens)

    def analyze_sentiment(self, text):
        # Analyze sentiment using VADER
        sentiment = self.sia.polarity_scores(text)
        return sentiment

    def categorize_review(self, review, rating):
        # Preprocess review text
        review = self.preprocess_text(review)
        # Analyze sentiment
        sentiment = self.analyze_sentiment(review)
        # Determine category based on sentiment and rating
        if sentiment['compound'] > 0.5 and rating >= 4:
            return 'Very Positive'
        elif sentiment['compound'] > 0 and rating >= 3:
            return 'Positive'
        elif sentiment['compound'] < -0.5 and rating <= 2:
            return 'Very Negative'
        elif sentiment['compound'] < 0 and rating <= 3:
            return 'Negative'
        else:
            return 'Neutral'

def load_reviews(file_path):
    try:
        # Load reviews from CSV file
        reviews = pd.read_csv(file_path)
        return reviews
    except Exception as e:
        print(f"Error loading reviews: {e}")
        return None

def main():
    # Load reviews
    reviews = load_reviews('reviews.csv')
    if reviews is not None:
        # Initialize review analyzer
        analyzer = ReviewAnalyzer()
        # Analyze and categorize reviews
        reviews['category'] = reviews.apply(lambda row: analyzer.categorize_review(row['review'], row['rating']), axis=1)
        # Print categorized reviews
        print(reviews)
        # Save categorized reviews to new CSV file
        reviews.to_csv('categorized_reviews.csv', index=False)

if __name__ == "__main__":
    main()
```
