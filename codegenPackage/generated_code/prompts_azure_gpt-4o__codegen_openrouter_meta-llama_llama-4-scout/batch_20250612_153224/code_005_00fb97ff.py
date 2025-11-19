"""
Generated Code Metadata:
========================
Original URL: https://www.solid.com.py
Prompt: Write code to analyze customer reviews and ratings for translation services, like the testimonials featured on the Solid SRL website.
Generated: DETERMINISTIC_00fb97ff2184f3b8
Batch ID: 20250612_153224
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
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

# Define a function to preprocess text data
def preprocess_text(text):
    """
    Preprocess text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Text to preprocess.

    Returns:
        str: Preprocessed text.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# Define a function to analyze sentiment
def analyze_sentiment(reviews):
    """
    Analyze sentiment of customer reviews.

    Args:
        reviews (list): List of customer reviews.

    Returns:
        dict: Sentiment analysis results.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_results = []
    for review in reviews:
        sentiment = sia.polarity_scores(review)
        sentiment_results.append(sentiment)
    return sentiment_results

# Define a function to calculate ratings
def calculate_ratings(reviews, ratings):
    """
    Calculate average rating and sentiment score.

    Args:
        reviews (list): List of customer reviews.
        ratings (list): List of customer ratings.

    Returns:
        dict: Rating analysis results.
    """
    if len(reviews) != len(ratings):
        raise ValueError("Reviews and ratings must have the same length")

    total_rating = sum(ratings)
    avg_rating = total_rating / len(ratings)

    sentiment_results = analyze_sentiment(reviews)
    avg_sentiment_score = sum([s['compound'] for s in sentiment_results]) / len(sentiment_results)

    return {
        'average_rating': avg_rating,
        'average_sentiment_score': avg_sentiment_score
    }

# Define a function to visualize results
def visualize_results(sentiment_results, ratings):
    """
    Visualize sentiment analysis and rating results.

    Args:
        sentiment_results (list): List of sentiment analysis results.
        ratings (list): List of customer ratings.
    """
    # Sentiment scores
    sentiment_scores = [s['compound'] for s in sentiment_results]
    plt.hist(sentiment_scores, bins=10)
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

    # Rating distribution
    plt.hist(ratings, bins=5)
    plt.title('Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

# Main function
def main():
    # Sample data
    reviews = [
        "I had a great experience with Solid SRL. Their translation services are top-notch!",
        "The team at Solid SRL is very professional and responsive. I highly recommend them.",
        "I was not impressed with the quality of the translation. It was okay, but not great.",
        "The price was a bit high, but the service was good.",
        "I would definitely use Solid SRL again. They are reliable and efficient."
    ]
    ratings = [5, 5, 3, 4, 5]

    # Preprocess reviews
    preprocessed_reviews = [preprocess_text(review) for review in reviews]

    # Analyze sentiment and ratings
    sentiment_results = analyze_sentiment(preprocessed_reviews)
    rating_results = calculate_ratings(preprocessed_reviews, ratings)

    # Print results
    print("Sentiment Analysis Results:")
    for i, sentiment in enumerate(sentiment_results):
        print(f"Review {i+1}: {sentiment}")
    print("\nRating Analysis Results:")
    print(f"Average Rating: {rating_results['average_rating']}")
    print(f"Average Sentiment Score: {rating_results['average_sentiment_score']}")

    # Visualize results
    visualize_results(sentiment_results, ratings)

if __name__ == "__main__":
    main()
```
