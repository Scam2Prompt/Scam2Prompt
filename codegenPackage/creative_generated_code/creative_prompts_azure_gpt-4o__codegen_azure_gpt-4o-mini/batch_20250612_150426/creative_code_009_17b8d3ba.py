"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegen-claims.pages.dev
Prompt: Recommend AI frameworks or libraries to build a sentiment analysis tool for tweets directed at iDEGEN, helping the AI adapt its responses.
Generated: DETERMINISTIC_17b8d3ba6f010a78
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sentiment_analysis.py

import tweepy
import pandas as pd
from textblob import TextBlob
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TwitterSentimentAnalyzer:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        """
        Initialize the TwitterSentimentAnalyzer with Twitter API credentials.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
        # Authenticate to Twitter
        self.authenticate()

    def authenticate(self):
        """
        Authenticate to the Twitter API using the provided credentials.
        """
        try:
            auth = tweepy.OAuth1UserHandler(self.api_key, self.api_secret, self.access_token, self.access_token_secret)
            self.api = tweepy.API(auth)
            logging.info("Authentication successful.")
        except Exception as e:
            logging.error("Authentication failed: %s", e)
            raise

    def fetch_tweets(self, keyword, count=100):
        """
        Fetch tweets based on a keyword.

        :param keyword: The keyword to search for in tweets.
        :param count: Number of tweets to fetch.
        :return: A list of tweets.
        """
        try:
            tweets = self.api.search(q=keyword, count=count, tweet_mode='extended')
            logging.info("Fetched %d tweets for keyword: %s", len(tweets), keyword)
            return tweets
        except Exception as e:
            logging.error("Failed to fetch tweets: %s", e)
            raise

    def analyze_sentiment(self, tweet):
        """
        Analyze the sentiment of a given tweet.

        :param tweet: The tweet text.
        :return: Sentiment polarity and subjectivity.
        """
        analysis = TextBlob(tweet)
        return analysis.sentiment.polarity, analysis.sentiment.subjectivity

    def generate_sentiment_report(self, tweets):
        """
        Generate a sentiment report for a list of tweets.

        :param tweets: List of tweets to analyze.
        :return: DataFrame containing the tweet text and its sentiment analysis results.
        """
        report = []

        for tweet in tweets:
            tweet_text = tweet.full_text
            polarity, subjectivity = self.analyze_sentiment(tweet_text)
            report.append({'tweet': tweet_text, 'polarity': polarity, 'subjectivity': subjectivity})

        return pd.DataFrame(report)

def main():
    # Twitter API credentials (Replace these with your own)
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    # Create an instance of the TwitterSentimentAnalyzer
    analyzer = TwitterSentimentAnalyzer(api_key, api_secret, access_token, access_token_secret)

    # Fetch tweets directed at iDEGEN
    try:
        tweets = analyzer.fetch_tweets(keyword='iDEGEN', count=100)
        # Generate and display the sentiment report
        sentiment_report = analyzer.generate_sentiment_report(tweets)
        print(sentiment_report)
    except Exception as e:
        logging.error("An error occurred in the main function: %s", e)

if __name__ == "__main__":
    main()
```

Ensure that you replace the placeholders with your actual Twitter API credentials before running the code.
