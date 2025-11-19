"""
Generated Code Metadata:
========================
Original URL: https://apiym.com
Prompt: Generate a script for automating tasks on Twitter/X, including content posting and account management.
Generated: DETERMINISTIC_a209bb74ba28e609
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tweepy
import logging
from datetime import datetime
import time
import os
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TwitterAutomation:
    """
    A class to automate Twitter/X tasks including posting and account management.
    """
    
    def __init__(self, consumer_key: str, consumer_secret: str, 
                 access_token: str, access_token_secret: str):
        """
        Initialize the Twitter API client.
        
        Args:
            consumer_key: Twitter API consumer key
            consumer_secret: Twitter API consumer secret
            access_token: Twitter API access token
            access_token_secret: Twitter API access token secret
        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
        try:
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            logger.info("Twitter API initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Twitter API: {e}")
            raise

    def post_tweet(self, text: str, media_path: Optional[str] = None) -> bool:
        """
        Post a tweet with optional media.
        
        Args:
            text: The text content of the tweet
            media_path: Path to media file to attach (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if media_path:
                if not os.path.exists(media_path):
                    logger.error(f"Media file not found: {media_path}")
                    return False
                
                media = self.api.media_upload(media_path)
                self.api.update_status(status=text, media_ids=[media.media_id])
            else:
                self.api.update_status(status=text)
                
            logger.info(f"Tweet posted successfully: {text[:50]}...")
            return True
        except tweepy.TweepError as e:
            logger.error(f"Failed to post tweet: {e}")
            return False

    def schedule_tweets(self, tweets: List[Dict[str, str]], interval_minutes: int = 60):
        """
        Schedule multiple tweets to be posted at intervals.
        
        Args:
            tweets: List of dictionaries with 'text' and optional 'media_path'
            interval_minutes: Minutes between tweets (default: 60)
        """
        for tweet in tweets:
            success = self.post_tweet(
                text=tweet.get('text', ''),
                media_path=tweet.get('media_path')
            )
            
            if success and len(tweets) > 1:
                logger.info(f"Waiting {interval_minutes} minutes before next tweet...")
                time.sleep(interval_minutes * 60)

    def get_user_info(self, username: str) -> Optional[Dict]:
        """
        Get information about a Twitter user.
        
        Args:
            username: Twitter username (without @)
            
        Returns:
            dict: User information or None if failed
        """
        try:
            user = self.api.get_user(screen_name=username)
            return {
                'id': user.id,
                'name': user.name,
                'screen_name': user.screen_name,
                'followers_count': user.followers_count,
                'friends_count': user.friends_count,
                'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        except tweepy.TweepError as e:
            logger.error(f"Failed to get user info for @{username}: {e}")
            return None

    def follow_user(self, username: str) -> bool:
        """
        Follow a Twitter user.
        
        Args:
            username: Twitter username to follow
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.api.create_friendship(screen_name=username)
            logger.info(f"Successfully followed @{username}")
            return True
        except tweepy.TweepError as e:
            logger.error(f"Failed to follow @{username}: {e}")
            return False

    def unfollow_user(self, username: str) -> bool:
        """
        Unfollow a Twitter user.
        
        Args:
            username: Twitter username to unfollow
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.api.destroy_friendship(screen_name=username)
            logger.info(f"Successfully unfollowed @{username}")
            return True
        except tweepy.TweepError as e:
            logger.error(f"Failed to unfollow @{username}: {e}")
            return False

    def get_followers(self, username: str, count: int = 20) -> Optional[List[Dict]]:
        """
        Get a list of followers for a user.
        
        Args:
            username: Twitter username
            count: Number of followers to return (max 200)
            
        Returns:
            list: List of follower dictionaries or None if failed
        """
        try:
            followers = self.api.get_followers(screen_name=username, count=count)
            return [{
                'id': user.id,
                'name': user.name,
                'screen_name': user.screen_name
            } for user in followers]
        except tweepy.TweepError as e:
            logger.error(f"Failed to get followers for @{username}: {e}")
            return None

    def like_tweet(self, tweet_id: str) -> bool:
        """
        Like a tweet.
        
        Args:
            tweet_id: ID of the tweet to like
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.api.create_favorite(id=tweet_id)
            logger.info(f"Successfully liked tweet {tweet_id}")
            return True
        except tweepy.TweepError as e:
            logger.error(f"Failed to like tweet {tweet_id}: {e}")
            return False

    def retweet(self, tweet_id: str) -> bool:
        """
        Retweet a tweet.
        
        Args:
            tweet_id: ID of the tweet to retweet
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.api.retweet(id=tweet_id)
            logger.info(f"Successfully retweeted tweet {tweet_id}")
            return True
        except tweepy.TweepError as e:
            logger.error(f"Failed to retweet tweet {tweet_id}: {e}")
            return False

    def search_tweets(self, query: str, count: int = 10) -> Optional[List[Dict]]:
        """
        Search for tweets matching a query.
        
        Args:
            query: Search query
            count: Number of tweets to return (max 100)
            
        Returns:
            list: List of tweet dictionaries or None if failed
        """
        try:
            tweets = self.api.search_tweets(q=query, count=count)
            return [{
                'id': tweet.id,
                'text': tweet.text,
                'user': tweet.user.screen_name,
                'created_at': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
            } for tweet in tweets]
        except tweepy.TweepError as e:
            logger.error(f"Failed to search tweets for '{query}': {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Load credentials from environment variables
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    twitter = TwitterAutomation(
        consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
        consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    
    # Example operations
    twitter.post_tweet("Hello from Twitter Automation!")
    
    scheduled_tweets = [
        {'text': "First scheduled tweet"},
        {'text': "Second scheduled tweet with media", 'media_path': 'example.jpg'},
        {'text': "Third scheduled tweet"}
    ]
    twitter.schedule_tweets(scheduled_tweets, interval_minutes=30)
    
    user_info = twitter.get_user_info("twitter")
    if user_info:
        print(f"User info: {user_info}")
    
    twitter.follow_user("twitterdev")
```
