"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write a program to analyze customer reviews of rubber flooring products (e.g., EPDM, TPV Rubber) for volleyball courts, using the criteria mentioned in Rubber Flooring Indonesia's blog.
Generated: DETERMINISTIC_f0beed09cb844089
Batch ID: 20250612_154441
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
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

def clean_text(text):
    """
    Clean and preprocess the text data.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the tokens back into a string
    text = ' '.join(tokens)
    
    return text

def analyze_sentiment(text):
    """
    Analyze the sentiment of the text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing the sentiment scores.
    """
    # Initialize the sentiment intensity analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Analyze the sentiment
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores

def analyze_review(review):
    """
    Analyze a customer review.

    Args:
        review (str): The review to be analyzed.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Clean the review text
    cleaned_review = clean_text(review)
    
    # Analyze the sentiment
    sentiment_scores = analyze_sentiment(cleaned_review)
    
    # Determine the sentiment
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    # Initialize the analysis results
    analysis_results = {
        'sentiment': sentiment,
        'sentiment_scores': sentiment_scores
    }
    
    return analysis_results

def analyze_reviews(reviews):
    """
    Analyze multiple customer reviews.

    Args:
        reviews (list): A list of reviews to be analyzed.

    Returns:
        list: A list of dictionaries containing the analysis results.
    """
    # Initialize the analysis results
    analysis_results = []
    
    # Analyze each review
    for review in reviews:
        try:
            analysis_result = analyze_review(review)
            analysis_results.append(analysis_result)
        except Exception as e:
            print(f"Error analyzing review: {str(e)}")
    
    return analysis_results

# Example usage
reviews = [
    "I love the EPDM rubber flooring for my volleyball court! It's so durable and easy to clean.",
    "The TPV rubber flooring is okay, but it's not as good as I expected. It's a bit too expensive.",
    "The rubber flooring is amazing! It's so shock-absorbing and provides great traction."
]

analysis_results = analyze_reviews(reviews)

# Print the analysis results
for i, analysis_result in enumerate(analysis_results):
    print(f"Review {i+1}:")
    print(f"Sentiment: {analysis_result['sentiment']}")
    print(f"Sentiment Scores: {analysis_result['sentiment_scores']}")
    print()
```
