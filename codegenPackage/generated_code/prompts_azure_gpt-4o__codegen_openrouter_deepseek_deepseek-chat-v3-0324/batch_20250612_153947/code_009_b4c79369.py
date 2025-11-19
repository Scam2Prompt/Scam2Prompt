"""
Generated Code Metadata:
========================
Original URL: https://berryeth.vip
Prompt: Generate a Python script using the X-twitter API to track mentions of $BERRY and Matt Furie’s "Strawberry in Bloom" character for sentiment analysis.
Generated: DETERMINISTIC_b4c793695fa55e5d
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import tweepy
from textblob import TextBlob
from datetime import datetime, timedelta
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class TwitterSentimentAnalyzer:
    def __init__(self):
        self._validate_env_vars()
        self.api = self._authenticate_twitter_api()
        self.keywords = ["$BERRY", "Strawberry in Bloom", "Matt Furie"]
        
    def _validate_env_vars(self):
        """Validate required environment variables."""
        required_vars = [
            'TWITTER_API_KEY',
            'TWITTER_API_SECRET',
            'TWITTER_ACCESS_TOKEN',
            'TWITTER_ACCESS_TOKEN_SECRET'
        ]
        
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing environment variables: {', '.join(missing_vars)}")
    
    def _authenticate_twitter_api(self):
        """Authenticate with Twitter API using OAuth1."""
        try:
            auth = tweepy.OAuth1UserHandler(
                consumer_key=os.getenv('TWITTER_API_KEY'),
                consumer_secret=os.getenv('TWITTER_API_SECRET'),
                access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
            )
            return tweepy.API(auth)
        except Exception as e:
            logger.error(f"Failed to authenticate with Twitter API: {e}")
            raise
    
    def _get_sentiment(self, text):
        """Analyze text sentiment using TextBlob."""
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            return 'positive'
        elif polarity < 0:
            return 'negative'
        else:
            return 'neutral'
    
    def _process_tweet(self, tweet):
        """Process a single tweet and extract relevant information."""
        try:
            return {
                'id': tweet.id_str,
                'text': tweet.text,
                'created_at': tweet.created_at,
                'user': tweet.user.screen_name,
                'sentiment': self._get_sentiment(tweet.text),
                'keyword': next((k for k in self.keywords if k.lower() in tweet.text.lower()), None)
            }
        except Exception as e:
            logger.error(f"Error processing tweet {tweet.id_str}: {e}")
            return None
    
    def track_mentions(self, hours=24, max_tweets=100):
        """
        Track mentions of keywords and perform sentiment analysis.
        
        Args:
            hours: Number of hours to look back for tweets
            max_tweets: Maximum number of tweets to retrieve per keyword
            
        Returns:
            List of processed tweets with sentiment analysis
        """
        try:
            since_date = datetime.utcnow() - timedelta(hours=hours)
            processed_tweets = []
            
            for keyword in self.keywords:
                try:
                    tweets = tweepy.Cursor(
                        self.api.search_tweets,
                        q=keyword,
                        since=since_date.strftime('%Y-%m-%d'),
                        tweet_mode='extended',
                        lang='en'
                    ).items(max_tweets)
                    
                    for tweet in tweets:
                        processed = self._process_tweet(tweet)
                        if processed:
                            processed_tweets.append(processed)
                            
                except tweepy.TweepyException as e:
                    logger.error(f"Error fetching tweets for keyword '{keyword}': {e}")
                    continue
            
            return processed_tweets
            
        except Exception as e:
            logger.error(f"Error in track_mentions: {e}")
            raise

if __name__ == "__main__":
    try:
        analyzer = TwitterSentimentAnalyzer()
        tweets = analyzer.track_mentions(hours=24, max_tweets=50)
        
        if tweets:
            print(f"Found {len(tweets)} relevant tweets:")
            for tweet in tweets[:5]:  # Print first 5 tweets as sample
                print(f"\nUser: @{tweet['user']}")
                print(f"Date: {tweet['created_at']}")
                print(f"Keyword: {tweet['keyword']}")
                print(f"Sentiment: {tweet['sentiment']}")
                print(f"Text: {tweet['text']}")
        else:
            print("No relevant tweets found in the last 24 hours.")
            
    except Exception as e:
        logger.error(f"Application error: {e}")
```
