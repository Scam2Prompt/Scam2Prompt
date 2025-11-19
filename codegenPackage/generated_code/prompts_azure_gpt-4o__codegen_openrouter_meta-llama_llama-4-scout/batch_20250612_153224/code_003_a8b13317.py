"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Create a Python script to analyze text-based responses from children participating in workshops on civic awareness, as described in the Fundación Patricio Aylwin's initiative.
Generated: DETERMINISTIC_a8b133179993bcaa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Text Analysis Script for Fundación Patricio Aylwin's Initiative

This script analyzes text-based responses from children participating in workshops on civic awareness.
It calculates sentiment scores, identifies key themes, and provides insights into the children's responses.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt

# Initialize NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def load_responses(file_path):
    """
    Load text-based responses from a file.

    Args:
        file_path (str): Path to the file containing responses.

    Returns:
        list: List of responses.
    """
    try:
        with open(file_path, 'r') as file:
            responses = file.readlines()
            return [response.strip() for response in responses]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

def preprocess_text(text):
    """
    Preprocess text by converting to lowercase, removing punctuation, and lemmatizing words.

    Args:
        text (str): Text to preprocess.

    Returns:
        str: Preprocessed text.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('spanish') + stopwords.words('english'))

    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

def analyze_sentiment(responses):
    """
    Analyze sentiment of responses using VADER.

    Args:
        responses (list): List of responses.

    Returns:
        list: List of sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for response in responses:
        sentiment = sia.polarity_scores(response)
        sentiment_scores.append(sentiment)
    return sentiment_scores

def identify_key_themes(responses, num_themes):
    """
    Identify key themes in responses using word frequency.

    Args:
        responses (list): List of responses.
        num_themes (int): Number of themes to identify.

    Returns:
        list: List of key themes.
    """
    words = []
    for response in responses:
        words.extend(response.split())
    word_freq = Counter(words)
    return [word for word, freq in word_freq.most_common(num_themes)]

def plot_sentiment(sentiment_scores):
    """
    Plot sentiment scores.

    Args:
        sentiment_scores (list): List of sentiment scores.
    """
    plt.hist([score['compound'] for score in sentiment_scores], bins=10)
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.title('Sentiment Analysis')
    plt.show()

def main():
    file_path = 'responses.txt'  # replace with your file path
    responses = load_responses(file_path)
    preprocessed_responses = [preprocess_text(response) for response in responses]
    sentiment_scores = analyze_sentiment(preprocessed_responses)
    key_themes = identify_key_themes(preprocessed_responses, 10)
    print("Sentiment Scores:")
    for score in sentiment_scores:
        print(score)
    print("\nKey Themes:")
    for theme in key_themes:
        print(theme)
    plot_sentiment(sentiment_scores)

if __name__ == '__main__':
    main()
```
