"""
Generated Code Metadata:
========================
Original URL: https://creatoro.me
Prompt: Create a program that integrates CREATORO's AI investment system with social media platforms like Twitter and Reddit to gather sentiment analysis for meme coin investments.
Generated: DETERMINISTIC_7df3309ec4f61ae3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import tweepy
import praw
from textblob import TextBlob
import pandas as pd
import numpy as np
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SentimentAnalysis:
    def __init__(self, twitter_api_keys, reddit_api_keys):
        """
        Initialize the SentimentAnalysis class.

        Args:
        - twitter_api_keys (dict): Dictionary containing Twitter API keys.
        - reddit_api_keys (dict): Dictionary containing Reddit API keys.
        """
        self.twitter_api_keys = twitter_api_keys
        self.reddit_api_keys = reddit_api_keys

    def twitter_sentiment_analysis(self, hashtag):
        """
        Perform sentiment analysis on Twitter posts.

        Args:
        - hashtag (str): Hashtag to search for.

        Returns:
        - A list of dictionaries containing tweet text and sentiment polarity.
        """
        try:
            # Authenticate with Twitter API
            auth = tweepy.OAuthHandler(self.twitter_api_keys['consumer_key'], self.twitter_api_keys['consumer_secret'])
            auth.set_access_token(self.twitter_api_keys['access_token'], self.twitter_api_keys['access_token_secret'])
            api = tweepy.API(auth)

            # Search for tweets with the given hashtag
            tweets = tweepy.Cursor(api.search_tweets, q=hashtag).items(100)

            # Analyze sentiment of each tweet
            tweet_sentiments = []
            for tweet in tweets:
                analysis = TextBlob(tweet.text)
                if analysis.sentiment.polarity > 0:
                    sentiment = 'Positive'
                elif analysis.sentiment.polarity < 0:
                    sentiment = 'Negative'
                else:
                    sentiment = 'Neutral'
                tweet_sentiments.append({
                    'text': tweet.text,
                    'sentiment': sentiment,
                    'polarity': analysis.sentiment.polarity
                })

            return tweet_sentiments

        except tweepy.TweepyException as e:
            logging.error(f"Twitter API error: {e}")
            return []

    def reddit_sentiment_analysis(self, subreddit, keyword):
        """
        Perform sentiment analysis on Reddit posts.

        Args:
        - subreddit (str): Subreddit to search in.
        - keyword (str): Keyword to search for.

        Returns:
        - A list of dictionaries containing post text and sentiment polarity.
        """
        try:
            # Authenticate with Reddit API
            reddit = praw.Reddit(client_id=self.reddit_api_keys['client_id'],
                                 client_secret=self.reddit_api_keys['client_secret'],
                                 user_agent=self.reddit_api_keys['user_agent'])

            # Search for posts in the given subreddit
            posts = reddit.subreddit(subreddit).search(query=keyword, limit=100)

            # Analyze sentiment of each post
            post_sentiments = []
            for post in posts:
                analysis = TextBlob(post.selftext)
                if analysis.sentiment.polarity > 0:
                    sentiment = 'Positive'
                elif analysis.sentiment.polarity < 0:
                    sentiment = 'Negative'
                else:
                    sentiment = 'Neutral'
                post_sentiments.append({
                    'text': post.selftext,
                    'sentiment': sentiment,
                    'polarity': analysis.sentiment.polarity
                })

            return post_sentiments

        except praw.exceptions.RedditorNotFound:
            logging.error(f"Reddit subreddit not found: {subreddit}")
            return []
        except praw.exceptions.APIException as e:
            logging.error(f"Reddit API error: {e}")
            return []

def main():
    # Twitter API keys
    twitter_api_keys = {
        'consumer_key': 'your_consumer_key',
        'consumer_secret': 'your_consumer_secret',
        'access_token': 'your_access_token',
        'access_token_secret': 'your_access_token_secret'
    }

    # Reddit API keys
    reddit_api_keys = {
        'client_id': 'your_client_id',
        'client_secret': 'your_client_secret',
        'user_agent': 'your_user_agent'
    }

    # Initialize sentiment analysis
    sentiment_analysis = SentimentAnalysis(twitter_api_keys, reddit_api_keys)

    # Perform Twitter sentiment analysis
    hashtag = '#meme_coin'
    tweet_sentiments = sentiment_analysis.twitter_sentiment_analysis(hashtag)
    df_tweets = pd.DataFrame(tweet_sentiments)
    print("Twitter Sentiment Analysis:")
    print(df_tweets)

    # Perform Reddit sentiment analysis
    subreddit = 'meme coins'
    keyword = 'meme coin investment'
    post_sentiments = sentiment_analysis.reddit_sentiment_analysis(subreddit, keyword)
    df_posts = pd.DataFrame(post_sentiments)
    print("\nReddit Sentiment Analysis:")
    print(df_posts)

if __name__ == "__main__":
    main()
```
