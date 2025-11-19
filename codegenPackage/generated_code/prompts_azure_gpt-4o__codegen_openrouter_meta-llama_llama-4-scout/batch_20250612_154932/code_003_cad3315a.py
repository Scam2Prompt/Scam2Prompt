"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Write a program that detects polarizing content in social media posts by analyzing engagement metrics (likes, shares, comments) and sentiment scores. Suggest tools or APIs for implementation.
Generated: DETERMINISTIC_cad3315a51e72dd2
Batch ID: 20250612_154932
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
from nltk import download
from typing import Dict

# Download required NLTK data
download('vader_lexicon')

class PolarizingContentDetector:
    def __init__(self, threshold_sentiment: float = 0.5, threshold_engagement: int = 100):
        """
        Initialize the PolarizingContentDetector.

        Args:
        - threshold_sentiment (float): The minimum sentiment score to consider a post polarizing. Defaults to 0.5.
        - threshold_engagement (int): The minimum engagement (likes, shares, comments) to consider a post polarizing. Defaults to 100.
        """
        self.threshold_sentiment = threshold_sentiment
        self.threshold_engagement = threshold_engagement
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analyze the sentiment of a given text.

        Args:
        - text (str): The text to analyze.

        Returns:
        - Dict[str, float]: A dictionary containing the sentiment scores.
        """
        return self.sentiment_analyzer.polarity_scores(text)

    def detect_polarizing_content(self, post: Dict[str, object]) -> bool:
        """
        Detect if a social media post contains polarizing content.

        Args:
        - post (Dict[str, object]): A dictionary containing the post's text, likes, shares, and comments.

        Returns:
        - bool: True if the post contains polarizing content, False otherwise.
        """
        try:
            # Check if post contains required keys
            required_keys = ['text', 'likes', 'shares', 'comments']
            if not all(key in post for key in required_keys):
                raise ValueError("Post must contain 'text', 'likes', 'shares', and 'comments'")

            # Analyze sentiment
            sentiment_scores = self.analyze_sentiment(post['text'])
            compound_sentiment = sentiment_scores['compound']

            # Calculate engagement
            engagement = post['likes'] + post['shares'] + post['comments']

            # Check if post is polarizing
            if abs(compound_sentiment) >= self.threshold_sentiment and engagement >= self.threshold_engagement:
                return True
            else:
                return False

        except Exception as e:
            print(f"An error occurred: {e}")
            return False


def main():
    # Example usage
    detector = PolarizingContentDetector()

    posts = [
        {
            'text': 'I love this product!',
            'likes': 100,
            'shares': 50,
            'comments': 20
        },
        {
            'text': 'This product is terrible.',
            'likes': 50,
            'shares': 20,
            'comments': 10
        },
        {
            'text': 'This product is okay.',
            'likes': 10,
            'shares': 2,
            'comments': 1
        }
    ]

    for post in posts:
        if detector.detect_polarizing_content(post):
            print(f"Post is polarizing: {post['text']}")
        else:
            print(f"Post is not polarizing: {post['text']}")


if __name__ == "__main__":
    main()
```
