"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Develop a social media analytics tool to monitor and engage with online discussions around human rights and media development, similar to Jusoor International's social media presence."
Generated: DETERMINISTIC_a20c06aa9dde803a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tweepy
import facebook
import requests
from datetime import datetime, timedelta
import pandas as pd
from textblob import TextBlob
import configparser
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SocialMediaMonitor:
    """
    A social media analytics tool to monitor and engage with online discussions
    around human rights and media development.
    """
    
    def __init__(self):
        self.config = self._load_config()
        self.twitter_client = self._init_twitter_client()
        self.facebook_client = self._init_facebook_client()
        self.keywords = [
            "human rights", "media development", "freedom of speech",
            "journalism", "press freedom", "digital rights"
        ]
        
    def _load_config(self) -> configparser.ConfigParser:
        """Load configuration from file."""
        config = configparser.ConfigParser()
        try:
            config.read('config.ini')
            return config
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            raise
            
    def _init_twitter_client(self) -> tweepy.Client:
        """Initialize Twitter API client."""
        try:
            return tweepy.Client(
                bearer_token=self.config['TWITTER']['BEARER_TOKEN'],
                consumer_key=self.config['TWITTER']['API_KEY'],
                consumer_secret=self.config['TWITTER']['API_SECRET'],
                access_token=self.config['TWITTER']['ACCESS_TOKEN'],
                access_token_secret=self.config['TWITTER']['ACCESS_TOKEN_SECRET']
            )
        except Exception as e:
            logger.error(f"Error initializing Twitter client: {e}")
            raise
            
    def _init_facebook_client(self) -> facebook.GraphAPI:
        """Initialize Facebook Graph API client."""
        try:
            return facebook.GraphAPI(
                access_token=self.config['FACEBOOK']['ACCESS_TOKEN'],
                version="3.0"
            )
        except Exception as e:
            logger.error(f"Error initializing Facebook client: {e}")
            raise
            
    def _get_sentiment(self, text: str) -> float:
        """Analyze text sentiment using TextBlob."""
        try:
            analysis = TextBlob(text)
            return analysis.sentiment.polarity
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {e}")
            return 0.0
            
    def monitor_twitter(self, hours: int = 24) -> List[Dict]:
        """
        Monitor Twitter for recent discussions matching keywords.
        
        Args:
            hours: Number of hours to look back for tweets
            
        Returns:
            List of tweet dictionaries with metadata
        """
        try:
            start_time = datetime.utcnow() - timedelta(hours=hours)
            query = " OR ".join(self.keywords)
            
            tweets = self.twitter_client.search_recent_tweets(
                query=query,
                start_time=start_time,
                max_results=100,
                tweet_fields=["created_at", "public_metrics", "author_id"],
                user_fields=["username", "name"],
                expansions=["author_id"]
            )
            
            results = []
            if tweets.data:
                users = {u.id: u for u in tweets.includes['users']}
                for tweet in tweets.data:
                    author = users[tweet.author_id]
                    results.append({
                        'platform': 'twitter',
                        'id': tweet.id,
                        'text': tweet.text,
                        'created_at': tweet.created_at,
                        'author': author.username,
                        'author_name': author.name,
                        'likes': tweet.public_metrics['like_count'],
                        'retweets': tweet.public_metrics['retweet_count'],
                        'replies': tweet.public_metrics['reply_count'],
                        'sentiment': self._get_sentiment(tweet.text)
                    })
            return results
        except Exception as e:
            logger.error(f"Error monitoring Twitter: {e}")
            return []
            
    def monitor_facebook(self, hours: int = 24) -> List[Dict]:
        """
        Monitor Facebook for recent posts matching keywords.
        
        Args:
            hours: Number of hours to look back for posts
            
        Returns:
            List of post dictionaries with metadata
        """
        try:
            since = int((datetime.now() - timedelta(hours=hours)).timestamp())
            results = []
            
            for keyword in self.keywords:
                posts = self.facebook_client.request(
                    'search',
                    {
                        'q': keyword,
                        'type': 'post',
                        'since': since,
                        'fields': 'id,message,created_time,from,shares,comments.limit(0).summary(true),reactions.limit(0).summary(true)'
                    }
                )
                
                if 'data' in posts:
                    for post in posts['data']:
                        if 'message' in post:
                            results.append({
                                'platform': 'facebook',
                                'id': post['id'],
                                'text': post['message'],
                                'created_at': post['created_time'],
                                'author': post['from']['name'],
                                'author_id': post['from']['id'],
                                'shares': post.get('shares', {}).get('count', 0),
                                'comments': post.get('comments', {}).get('summary', {}).get('total_count', 0),
                                'reactions': post.get('reactions', {}).get('summary', {}).get('total_count', 0),
                                'sentiment': self._get_sentiment(post['message'])
                            })
            return results
        except Exception as e:
            logger.error(f"Error monitoring Facebook: {e}")
            return []
            
    def engage_twitter(self, tweet_id: str, reply_text: str) -> bool:
        """Reply to a tweet."""
        try:
            response = self.twitter_client.create_tweet(
                text=reply_text,
                in_reply_to_tweet_id=tweet_id
            )
            return response.data['id'] is not None
        except Exception as e:
            logger.error(f"Error engaging on Twitter: {e}")
            return False
            
    def engage_facebook(self, post_id: str, comment_text: str) -> bool:
        """Comment on a Facebook post."""
        try:
            response = self.facebook_client.put_object(
                parent_object=post_id,
                connection_name='comments',
                message=comment_text
            )
            return 'id' in response
        except Exception as e:
            logger.error(f"Error engaging on Facebook: {e}")
            return False
            
    def generate_report(self, data: List[Dict], output_file: str) -> bool:
        """Generate a CSV report from collected data."""
        try:
            df = pd.DataFrame(data)
            df.to_csv(output_file, index=False)
            return True
        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return False
            
    def run_monitoring(self, hours: int = 24, output_file: str = "report.csv") -> bool:
        """Run monitoring across all platforms and generate report."""
        try:
            twitter_data = self.monitor_twitter(hours)
            facebook_data = self.monitor_facebook(hours)
            all_data = twitter_data + facebook_data
            return self.generate_report(all_data, output_file)
        except Exception as e:
            logger.error(f"Error in monitoring process: {e}")
            return False

if __name__ == "__main__":
    monitor = SocialMediaMonitor()
    if monitor.run_monitoring():
        logger.info("Monitoring completed successfully. Report generated.")
    else:
        logger.error("Monitoring failed. Check logs for details.")
```
