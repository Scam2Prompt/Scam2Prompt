"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: "Write a script to compare different types of toothpaste based on their ingredients and user reviews, using natural language processing techniques."
Generated: DETERMINISTIC_1df246af53811fc0
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure necessary NLTK data is downloaded
nltk.download('vader_lexicon')

# Function to preprocess text data
def preprocess_text(text):
    """
    Cleans and preprocesses text data by removing special characters, 
    converting to lowercase, and stripping extra whitespace.
    """
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    text = text.strip()  # Remove leading/trailing whitespace
    return text

# Function to analyze sentiment of reviews
def analyze_sentiment(reviews):
    """
    Analyzes sentiment of user reviews using NLTK's SentimentIntensityAnalyzer.
    Returns a DataFrame with sentiment scores.
    """
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for review in reviews:
        scores = sid.polarity_scores(review)
        sentiment_scores.append(scores)
    return pd.DataFrame(sentiment_scores)

# Function to compare toothpaste based on ingredients and reviews
def compare_toothpaste(data):
    """
    Compares toothpaste products based on their ingredients and user reviews.
    Uses TF-IDF for ingredient similarity and sentiment analysis for reviews.
    """
    # Preprocess ingredients and reviews
    data['ingredients_clean'] = data['ingredients'].apply(preprocess_text)
    data['reviews_clean'] = data['reviews'].apply(preprocess_text)

    # TF-IDF vectorization for ingredients
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data['ingredients_clean'])
    
    # Compute cosine similarity for ingredients
    ingredient_similarity = cosine_similarity(tfidf_matrix)
    data['ingredient_similarity'] = ingredient_similarity.tolist()

    # Sentiment analysis for reviews
    sentiment_scores = analyze_sentiment(data['reviews_clean'])
    data = pd.concat([data, sentiment_scores], axis=1)

    return data

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        toothpaste_data = pd.DataFrame({
            'product_name': ['Toothpaste A', 'Toothpaste B', 'Toothpaste C'],
            'ingredients': [
                'Fluoride, Sorbitol, Hydrated Silica',
                'Fluoride, Xylitol, Hydrated Silica',
                'Fluoride, Sorbitol, Calcium Carbonate'
            ],
            'reviews': [
                'Great toothpaste! Leaves my teeth feeling clean.',
                'Not bad, but I prefer a stronger mint flavor.',
                'Excellent product! Highly recommend it.'
            ]
        })

        # Compare toothpaste products
        comparison_results = compare_toothpaste(toothpaste_data)

        # Display results
        print("Comparison Results:")
        print(comparison_results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
