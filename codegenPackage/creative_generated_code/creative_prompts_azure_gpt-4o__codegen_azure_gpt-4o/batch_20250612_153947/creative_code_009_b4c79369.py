"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berryeth.vip
Prompt: Generate a Python script using the X-twitter API to track mentions of $BERRY and Matt Furie’s "Strawberry in Bloom" character for sentiment analysis.
Generated: DETERMINISTIC_b4c793695fa55e5d
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import tweepy
from textblob import TextBlob

# Set up Twitter API credentials (replace with your keys/tokens)
API_KEY = os.getenv('TWITTER_API_KEY', 'your_api_key_here')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY', 'your_api_secret_key_here')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', 'your_access_token_here')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', 'your_access_token_secret_here')

# Keywords to track
TRACKED_KEYWORDS = ["$BERRY", "Strawberry in Bloom"]

# Function to perform sentiment analysis on tweet text
def analyze_sentiment(tweet_text):
    """
    Perform sentiment analysis using TextBlob.
    Returns:
        str: Sentiment ("Positive", "Negative", or "Neutral")
    """
    analysis = TextBlob(tweet_text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Tweepy StreamListener class
class MentionStreamListener(tweepy.Stream):
    def on_status(self, status):
        """
        Handles incoming tweets in the stream.
        Args:
            status (Status): The tweet object.
        """
        try:
            # Extract tweet text (handling retweets and extended tweets)
            tweet_text = status.text
            if hasattr(status, "retweeted_status"):  # Retweet case
                tweet_text = status.retweeted_status.text
            elif 'extended_tweet' in status._json:  # Extended tweet case
                tweet_text = status._json['extended_tweet']['full_text']
            
            # Perform sentiment analysis
            sentiment = analyze_sentiment(tweet_text)
            
            # Log the tweet and sentiment
            print(f"Tweet: {tweet_text}\nSentiment: {sentiment}\n")

        except Exception as e:
            # Log any errors during processing
            print(f"Error processing tweet: {e}")

    def on_error(self, status_code):
        """
        Handles errors during streaming.
        Args:
            status_code (int): The error code.
        """
        if status_code == 420:
            # Disconnect the stream if rate-limited
            print("Rate limit exceeded. Disconnecting...")
            return False
        print(f"Error received: {status_code}")

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Initialize stream listener
print("Starting Twitter stream...")
stream = MentionStreamListener(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    # Filter stream to track keywords
    stream.filter(track=TRACKED_KEYWORDS)
except KeyboardInterrupt:
    print("Stream stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
```
