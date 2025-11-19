"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Write a Python script to analyze current affairs articles, similar to the content provided in the "SHIELD MAGAZINE" for UPSC preparation.
Generated: DETERMINISTIC_b428f7ebd23b69cd
Batch ID: 20250612_164000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/current-affairs-article": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import re

# Ensure the necessary NLTK resources are downloaded
nltk.download('vader_lexicon')
nltk.download('stopwords')

def fetch_article(url):
    """
    Fetches the HTML content of the article from the provided URL.

    Args:
        url (str): The URL of the article to fetch.

    Returns:
        str: The raw text content of the article.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from the article (assumption: articles are in <p> tags)
        paragraphs = soup.find_all('p')
        article_text = ' '.join([para.get_text() for para in paragraphs])
        return article_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")
        return ""

def clean_text(text):
    """
    Cleans the input text by removing special characters, numbers, and stopwords.

    Args:
        text (str): The raw text to clean.

    Returns:
        str: The cleaned text.
    """
    stopwords = set(nltk.corpus.stopwords.words('english'))
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\d+', '', text)      # Remove numbers
    words = text.lower().split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the text using NLTK Sentiment Intensity Analyzer.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: Dictionary containing sentiment scores (positive, neutral, negative, compound).
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

def extract_keywords(text, num_keywords=10):
    """
    Extracts the most common keywords from the text.

    Args:
        text (str): The text to extract keywords from.
        num_keywords (int): The number of keywords to return.

    Returns:
        list: A list of tuples containing keywords and their frequencies.
    """
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(num_keywords)

def main():
    """
    Main function to analyze current affairs articles.
    """
    # Example URL to fetch (can be replaced with actual SHIELD MAGAZINE URL)
    url = "https://example.com/current-affairs-article"

    print("Fetching article...")
    article = fetch_article(url)

    if not article:
        print("Failed to fetch article. Exiting.")
        return

    print("\nCleaning text...")
    cleaned_text = clean_text(article)

    print("\nAnalyzing sentiment...")
    sentiment = analyze_sentiment(cleaned_text)
    print("Sentiment Analysis:")
    print(sentiment)

    print("\nExtracting keywords...")
    keywords = extract_keywords(cleaned_text)
    print("Top Keywords:")
    for keyword, freq in keywords:
        print(f"{keyword}: {freq}")

if __name__ == "__main__":
    main()
```
