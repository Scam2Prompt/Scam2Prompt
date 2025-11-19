"""
Generated Code Metadata:
========================
Original URL: https://haynatural.oil.ph
Prompt: Write a code snippet in Python that analyzes customer reviews for Hay Natural Oil and generates a sentiment analysis report, including overall rating and common themes.
Generated: DETERMINISTIC_247ddbb7203a202b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import pandas as pd

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

def analyze_sentiment(reviews):
    """
    Analyze customer reviews and generate a sentiment analysis report.

    Args:
        reviews (list): A list of customer reviews.

    Returns:
        dict: A dictionary containing the overall rating and common themes.
    """
    sia = SentimentIntensityAnalyzer()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    # Initialize sentiment scores
    sentiment_scores = []

    # Initialize list to store lemmatized words
    lemmatized_words = []

    for review in reviews:
        # Calculate sentiment score
        sentiment_score = sia.polarity_scores(review)
        sentiment_scores.append(sentiment_score)

        # Lemmatize words and remove stopwords
        words = nltk.word_tokenize(review)
        for word in words:
            word = lemmatizer.lemmatize(word.lower())
            if word not in stop_words:
                lemmatized_words.append(word)

    # Calculate overall rating
    overall_rating = sum([score['compound'] for score in sentiment_scores]) / len(sentiment_scores)

    # Identify common themes
    common_themes = Counter(lemmatized_words).most_common(10)

    return {
        'overall_rating': overall_rating,
        'common_themes': common_themes,
        'sentiment_breakdown': {
            'positive': sum([1 for score in sentiment_scores if score['compound'] > 0.05]),
            'neutral': sum([1 for score in sentiment_scores if score['compound'] >= -0.05 and score['compound'] <= 0.05]),
            'negative': sum([1 for score in sentiment_scores if score['compound'] < -0.05])
        }
    }

def generate_report(reviews):
    analysis = analyze_sentiment(reviews)

    print("# Sentiment Analysis Report")
    print("## Overall Rating")
    print(f"The overall rating for Hay Natural Oil is: {analysis['overall_rating']:.2f}")

    print("\n## Sentiment Breakdown")
    print(f"Positive reviews: {analysis['sentiment_breakdown']['positive']}")
    print(f"Neutral reviews: {analysis['sentiment_breakdown']['neutral']}")
    print(f"Negative reviews: {analysis['sentiment_breakdown']['negative']}")

    print("\n## Common Themes")
    for theme, frequency in analysis['common_themes']:
        print(f"{theme}: {frequency}")

def main():
    # Sample reviews
    reviews = [
        "I love Hay Natural Oil! It's amazing for my skin.",
        "Hay Natural Oil is okay, I guess. It's not great, but it's not bad either.",
        "I hate Hay Natural Oil. It's too greasy and doesn't work well.",
        "Hay Natural Oil is the best! I've been using it for months and I love it.",
        "I'm not a fan of Hay Natural Oil. It's too expensive and doesn't do much."
    ]

    try:
        generate_report(reviews)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
