"""
Generated Code Metadata:
========================
Original URL: https://tayloud.io
Prompt: Create a program that tracks social media engagement (e.g., tweets) and calculates "mindshare" rankings for Loud contributors, updating hourly as described in the Loud experiment.
Generated: DETERMINISTIC_5266bacc0c914f6c
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tweepy
import time
import sqlite3
from datetime import datetime, timedelta
from collections import defaultdict
import logging
from typing import Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SocialMediaTracker:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
        Initialize the social media tracker with Twitter API credentials.
        
        Args:
            consumer_key: Twitter API consumer key
            consumer_secret: Twitter API consumer secret
            access_token: Twitter API access token
            access_token_secret: Twitter API access token secret
        """
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        
        # Initialize database
        self.db_conn = sqlite3.connect('mindshare.db')
        self._init_db()
        
        # Track engagement metrics
        self.engagement_counts = defaultdict(lambda: defaultdict(int))
        
    def _init_db(self) -> None:
        """Initialize database tables if they don't exist."""
        cursor = self.db_conn.cursor()
        
        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contributors (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                display_name TEXT,
                follower_count INTEGER,
                last_updated TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS engagements (
                id INTEGER PRIMARY KEY,
                contributor_id INTEGER,
                timestamp TIMESTAMP,
                likes INTEGER,
                retweets INTEGER,
                replies INTEGER,
                FOREIGN KEY (contributor_id) REFERENCES contributors (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mindshare_rankings (
                id INTEGER PRIMARY KEY,
                contributor_id INTEGER,
                timestamp TIMESTAMP,
                score REAL,
                rank INTEGER,
                FOREIGN KEY (contributor_id) REFERENCES contributors (id)
            )
        ''')
        
        self.db_conn.commit()
    
    def _get_contributor_id(self, username: str) -> int:
        """
        Get or create a contributor ID for the given username.
        
        Args:
            username: Twitter username
            
        Returns:
            Contributor ID
        """
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT id FROM contributors WHERE username = ?', (username,))
        result = cursor.fetchone()
        
        if result:
            return result[0]
        else:
            # Get user info from Twitter API
            try:
                user = self.api.get_user(screen_name=username)
                cursor.execute(
                    'INSERT INTO contributors (username, display_name, follower_count, last_updated) VALUES (?, ?, ?, ?)',
                    (username, user.name, user.followers_count, datetime.utcnow())
                )
                self.db_conn.commit()
                return cursor.lastrowid
            except tweepy.TweepError as e:
                logger.error(f"Error fetching user {username}: {e}")
                raise
    
    def track_engagement(self, tweet_id: int) -> None:
        """
        Track engagement metrics for a specific tweet.
        
        Args:
            tweet_id: ID of the tweet to track
        """
        try:
            tweet = self.api.get_status(tweet_id, tweet_mode='extended')
            contributor_id = self._get_contributor_id(tweet.user.screen_name)
            
            # Record engagement
            cursor = self.db_conn.cursor()
            cursor.execute(
                '''INSERT INTO engagements 
                (contributor_id, timestamp, likes, retweets, replies) 
                VALUES (?, ?, ?, ?, ?)''',
                (
                    contributor_id,
                    datetime.utcnow(),
                    tweet.favorite_count,
                    tweet.retweet_count,
                    len(tweet._json.get('replies', []))
                )
            )
            self.db_conn.commit()
            
            # Update in-memory counts for mindshare calculation
            self.engagement_counts[contributor_id]['likes'] += tweet.favorite_count
            self.engagement_counts[contributor_id]['retweets'] += tweet.retweet_count
            self.engagement_counts[contributor_id]['replies'] += len(tweet._json.get('replies', []))
            
        except tweepy.TweepError as e:
            logger.error(f"Error tracking tweet {tweet_id}: {e}")
    
    def calculate_mindshare(self) -> List[Tuple[int, float]]:
        """
        Calculate mindshare scores for all contributors based on recent engagement.
        
        Returns:
            List of tuples (contributor_id, score) sorted by score descending
        """
        # Calculate scores (weighted sum of engagement metrics)
        scores = []
        for contributor_id, metrics in self.engagement_counts.items():
            score = (
                metrics['likes'] * 0.4 + 
                metrics['retweets'] * 0.5 + 
                metrics['replies'] * 0.1
            )
            scores.append((contributor_id, score))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores
    
    def update_rankings(self) -> None:
        """Update mindshare rankings in the database."""
        scores = self.calculate_mindshare()
        timestamp = datetime.utcnow()
        
        cursor = self.db_conn.cursor()
        
        # Clear previous rankings for this hour
        cursor.execute(
            'DELETE FROM mindshare_rankings WHERE timestamp >= ? AND timestamp < ?',
            (
                timestamp.replace(minute=0, second=0, microsecond=0),
                timestamp.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
            )
        )
        
        # Insert new rankings
        for rank, (contributor_id, score) in enumerate(scores, start=1):
            cursor.execute(
                '''INSERT INTO mindshare_rankings 
                (contributor_id, timestamp, score, rank) 
                VALUES (?, ?, ?, ?)''',
                (contributor_id, timestamp, score, rank)
            )
        
        self.db_conn.commit()
        logger.info(f"Updated mindshare rankings for {len(scores)} contributors")
        
        # Reset engagement counts for next period
        self.engagement_counts.clear()
    
    def run_hourly(self) -> None:
        """Run the tracker on an hourly basis."""
        while True:
            try:
                self.update_rankings()
                logger.info("Waiting for next hourly update...")
                time.sleep(3600)  # Sleep for 1 hour
            except Exception as e:
                logger.error(f"Error in hourly update: {e}")
                time.sleep(60)  # Wait 1 minute before retrying
    
    def close(self) -> None:
        """Clean up resources."""
        self.db_conn.close()

# Example usage
if __name__ == "__main__":
    # Replace with your actual Twitter API credentials
    CONSUMER_KEY = 'your_consumer_key'
    CONSUMER_SECRET = 'your_consumer_secret'
    ACCESS_TOKEN = 'your_access_token'
    ACCESS_TOKEN_SECRET = 'your_access_token_secret'
    
    tracker = SocialMediaTracker(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET
    )
    
    try:
        # Example: Track some initial tweets (in a real app, you'd get these from a stream or search)
        # tracker.track_engagement(1234567890)  # Replace with actual tweet IDs
        # tracker.track_engagement(2345678901)
        
        # Start the hourly update cycle
        tracker.run_hourly()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        tracker.close()
```
