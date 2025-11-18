"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Create a program that uses sentiment analysis to evaluate user comments on SRH Life Foundation articles, focusing on topics like "preventative health checks" and "customizing countertops."
Generated: DETERMINISTIC_522a05ddbd2c7138
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.srhlifefoundation.org/comments": {
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
import pandas as pd
from textblob import TextBlob
import requests
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentAnalyzer:
    """A class to analyze the sentiment of user comments."""

    def __init__(self, keywords):
        """
        Initializes the SentimentAnalyzer with specific keywords.

        Args:
            keywords (list): A list of keywords to filter comments.
        """
        self.keywords = keywords

    def fetch_comments(self, url):
        """
        Fetches user comments from a given URL.

        Args:
            url (str): The URL to fetch comments from.

        Returns:
            list: A list of comments.

        Raises:
            Exception: If the request to the URL fails.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP issues
            comments = response.json().get('comments', [])
            logging.info(f"Fetched {len(comments)} comments from {url}.")
            return comments
        except Exception as e:
            logging.error(f"Error fetching comments: {e}")
            raise

    def filter_comments(self, comments):
        """
        Filters comments based on the predefined keywords.

        Args:
            comments (list): The list of comments to filter.

        Returns:
            list: Filtered comments containing at least one of the keywords.
        """
        filtered_comments = [comment for comment in comments if any(keyword in comment for keyword in self.keywords)]
        logging.info(f"Filtered down to {len(filtered_comments)} comments containing keywords.")
        return filtered_comments

    def analyze_sentiment(self, comments):
        """
        Analyzes the sentiment of each comment and returns the results.

        Args:
            comments (list): A list of comments to analyze.

        Returns:
            list: A list of tuples containing the comment and its sentiment polarity.
        """
        results = []
        for comment in comments:
            sentiment = TextBlob(comment).sentiment.polarity
            results.append((comment, sentiment))
            logging.info(f"Analyzed comment: {comment} | Sentiment: {sentiment}")
        return results

def main():
    # Define keywords related to the topics of interest
    keywords = ["preventative health checks", "customizing countertops"]
    
    # Create a sentiment analyzer instance
    analyzer = SentimentAnalyzer(keywords)

    # Define the URL of the comments API (placeholder URL)
    url = "https://api.srhlifefoundation.org/comments"

    try:
        # Fetch user comments from the API
        comments = analyzer.fetch_comments(url)

        # Filter comments based on keywords
        filtered_comments = analyzer.filter_comments(comments)

        # Analyze the sentiment of the filtered comments
        sentiment_results = analyzer.analyze_sentiment(filtered_comments)

        # Print the sentiment analysis results
        for comment, sentiment in sentiment_results:
            print(f"Comment: {comment}\nSentiment Polarity: {sentiment}\n")
    
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
```

Make sure you have the necessary libraries installed before running the code:
```bash
pip install pandas textblob requests
```
