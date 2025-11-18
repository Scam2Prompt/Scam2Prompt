"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.nl
Prompt: Using Immediate Peak's emphasis on psychological insights in trading, create a Python program that uses sentiment analysis to evaluate emotional impact on investment decisions.
Generated: DETERMINISTIC_9a47baa36b031ef9
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import requests
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    """
    Class to perform sentiment analysis on textual data related to trading psychology
    and evaluate emotional impacts on investment decisions.
    """

    def __init__(self):
        # Initialize sentiment analysis tools
        self.vader_analyzer = SentimentIntensityAnalyzer()

    def clean_text(self, text):
        """
        Cleans input text by removing unwanted characters, links, and excessive whitespace.

        Args:
            text (str): Raw input text.

        Returns:
            str: Cleaned text.
        """
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
        text = re.sub(r"\s+", " ", text).strip()  # Remove excessive whitespace
        return text

    def analyze_sentiment_vader(self, text):
        """
        Perform sentiment analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner).

        Args:
            text (str): Input text.

        Returns:
            dict: Dictionary of sentiment scores (positive, negative, neutral, compound).
        """
        return self.vader_analyzer.polarity_scores(text)

    def analyze_sentiment_textblob(self, text):
        """
        Perform sentiment analysis using TextBlob.

        Args:
            text (str): Input text.

        Returns:
            dict: Dictionary containing polarity and subjectivity.
        """
        blob = TextBlob(text)
        return {"polarity": blob.polarity, "subjectivity": blob.subjectivity}

    def fetch_latest_news(self, query):
        """
        Fetch latest news related to the query using a mock API endpoint.
        Replace this method with actual API calls for production.

        Args:
            query (str): Query term (e.g., "investment psychology").

        Returns:
            list: List of news articles (mock data).
        """
        # Mock data for demonstration purposes.
        return [
            {"title": "Fear drives major sell-offs in volatile markets"},
            {"title": "Optimistic traders see potential in upcoming earnings"},
            {"title": "Mixed feelings as market uncertainty persists"},
        ]

    def evaluate_sentiments_on_news(self, query):
        """
        Evaluate sentiment scores for news articles related to the input query term.

        Args:
            query (str): Query term related to trading psychology.

        Returns:
            list: List of dictionaries containing article titles and sentiment scores.
        """
        try:
            news_articles = self.fetch_latest_news(query)
            result = []

            for article in news_articles:
                cleaned_text = self.clean_text(article['title'])
                vader_scores = self.analyze_sentiment_vader(cleaned_text)
                textblob_scores = self.analyze_sentiment_textblob(cleaned_text)

                result.append({
                    "title": article["title"],
                    "vader_scores": vader_scores,
                    "textblob_scores": textblob_scores
                })

            return result
        except Exception as e:
            print(f"Error occurred while evaluating sentiments: {e}")
            return []

def main():
    """
    Main function to demonstrate sentiment analysis on trading psychology.
    """
    try:
        query = "investment psychology"
        analyzer = SentimentAnalyzer()

        print(f"Fetching news and analyzing sentiment for query: {query}")
        sentiment_results = analyzer.evaluate_sentiments_on_news(query)

        print("\nSentiment Analysis Results:")
        for result in sentiment_results:
            print(f"\nTitle: {result['title']}")
            print(f"VADER Scores: {result['vader_scores']}")
            print(f"TextBlob Scores: {result['textblob_scores']}")

    except Exception as e:
        print(f"An error occurred in the program: {e}")

if __name__ == "__main__":
    main()
```
