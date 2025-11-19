"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Write a script to analyze customer reviews and ratings, like those found on Acessanet's Google Play and App Store pages, and generate insights on common themes and areas for improvement.
Generated: DETERMINISTIC_c4ea5ede8bc00f06
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt

# Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    """
    Preprocess text by converting to lowercase, removing punctuation and special characters,
    tokenizing, removing stopwords, and lemmatizing.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens

def analyze_sentiment(reviews):
    """
    Analyze sentiment of reviews using VADER sentiment analysis tool.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for review in reviews:
        score = sia.polarity_scores(review)
        sentiment_scores.append(score)
    return sentiment_scores

def extract_insights(reviews):
    """
    Extract insights from reviews by identifying common themes and areas for improvement.
    """
    tokens = []
    for review in reviews:
        tokens.extend(preprocess_text(review))
    token_counts = Counter(tokens)
    common_themes = token_counts.most_common(10)
    return common_themes

def plot_sentiment_distribution(sentiment_scores):
    """
    Plot distribution of sentiment scores.
    """
    positive_scores = [score['compound'] for score in sentiment_scores if score['compound'] > 0]
    neutral_scores = [score['compound'] for score in sentiment_scores if score['compound'] == 0]
    negative_scores = [score['compound'] for score in sentiment_scores if score['compound'] < 0]
    plt.hist([positive_scores, neutral_scores, negative_scores], label=['Positive', 'Neutral', 'Negative'], alpha=0.5)
    plt.legend()
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.title('Sentiment Distribution')
    plt.show()

def main(reviews):
    try:
        sentiment_scores = analyze_sentiment(reviews)
        common_themes = extract_insights(reviews)
        print("Sentiment Analysis:")
        for i, score in enumerate(sentiment_scores):
            print(f"Review {i+1}: {score}")
        print("\nCommon Themes:")
        for theme, count in common_themes:
            print(f"{theme}: {count}")
        plot_sentiment_distribution(sentiment_scores)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
reviews = [
    "I love this app! It's so easy to use and the customer support is great.",
    "The app is okay, but it's not what I expected.",
    "I'm really disappointed with the app. It's slow and crashes a lot.",
    "The app is amazing! I've been using it for weeks and it's been a game changer.",
    "I'm not sure about this app. It's got some good features, but it's also got some bad ones."
]

if __name__ == "__main__":
    main(reviews)
```
