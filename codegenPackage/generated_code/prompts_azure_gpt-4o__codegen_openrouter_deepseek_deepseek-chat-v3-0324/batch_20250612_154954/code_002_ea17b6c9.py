"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Generate code to analyze social media follower growth using the tools reviewed in Fearless Netpreneur's "Top Tools for Building Social Media Lists."
Generated: DETERMINISTIC_ea17b6c984885aaa
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import tweepy
import instaloader
import facebook_scraper
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SocialMediaAnalyzer:
    """
    A class to analyze social media follower growth across multiple platforms.
    Supports Twitter, Instagram, and Facebook.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the analyzer with API credentials and configuration.
        
        Args:
            config: Dictionary containing API credentials and settings
                   Expected keys: twitter, instagram, facebook
        """
        self.config = config
        self.twitter_client = None
        self.instagram_client = None
        
        # Initialize Twitter client if credentials exist
        if 'twitter' in config:
            try:
                auth = tweepy.OAuthHandler(
                    config['twitter']['consumer_key'],
                    config['twitter']['consumer_secret']
                )
                auth.set_access_token(
                    config['twitter']['access_token'],
                    config['twitter']['access_token_secret']
                )
                self.twitter_client = tweepy.API(auth, wait_on_rate_limit=True)
                logger.info("Twitter client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Twitter client: {e}")
        
        # Initialize Instagram client if credentials exist
        if 'instagram' in config:
            try:
                self.instagram_client = instaloader.Instaloader()
                if ('username' in config['instagram'] and 
                    'password' in config['instagram']):
                    self.instagram_client.login(
                        config['instagram']['username'],
                        config['instagram']['password']
                    )
                logger.info("Instagram client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Instagram client: {e}")
    
    def get_twitter_followers(self, username: str) -> Optional[int]:
        """
        Get current follower count for a Twitter account.
        
        Args:
            username: Twitter handle to analyze
            
        Returns:
            Number of followers or None if error occurs
        """
        if not self.twitter_client:
            logger.error("Twitter client not initialized")
            return None
            
        try:
            user = self.twitter_client.get_user(screen_name=username)
            return user.followers_count
        except tweepy.TweepError as e:
            logger.error(f"Twitter API error for {username}: {e}")
            return None
    
    def get_instagram_followers(self, username: str) -> Optional[int]:
        """
        Get current follower count for an Instagram account.
        
        Args:
            username: Instagram handle to analyze
            
        Returns:
            Number of followers or None if error occurs
        """
        if not self.instagram_client:
            logger.error("Instagram client not initialized")
            return None
            
        try:
            profile = instaloader.Profile.from_username(
                self.instagram_client.context, 
                username
            )
            return profile.followers
        except Exception as e:
            logger.error(f"Instagram error for {username}: {e}")
            return None
    
    def get_facebook_followers(self, username: str) -> Optional[int]:
        """
        Get current follower count for a Facebook page.
        
        Args:
            username: Facebook page name or ID to analyze
            
        Returns:
            Number of followers or None if error occurs
        """
        try:
            # Note: facebook-scraper may require cookies for private pages
            page = next(facebook_scraper.get_posts(
                account=username,
                pages=1,
                options={"allow_extra_requests": False}
            ))
            return page['likes']
        except Exception as e:
            logger.error(f"Facebook error for {username}: {e}")
            return None
    
    def track_growth(
        self, 
        platform: str, 
        username: str, 
        days: int = 30
    ) -> Optional[pd.DataFrame]:
        """
        Track follower growth over time for a given account.
        
        Args:
            platform: One of 'twitter', 'instagram', or 'facebook'
            username: Account username to track
            days: Number of days to track (default 30)
            
        Returns:
            DataFrame with date and follower count columns, or None if error
        """
        if platform not in ['twitter', 'instagram', 'facebook']:
            logger.error(f"Unsupported platform: {platform}")
            return None
            
        # Create empty DataFrame to store results
        df = pd.DataFrame(columns=['date', 'followers'])
        
        # Get current date and calculate date range
        end_date = datetime.now()
        start_date = end_date - pd.Timedelta(days=days)
        date_range = pd.date_range(start_date, end_date, freq='D')
        
        # Track followers for each date in range
        for date in date_range:
            try:
                if platform == 'twitter':
                    count = self.get_twitter_followers(username)
                elif platform == 'instagram':
                    count = self.get_instagram_followers(username)
                else:  # facebook
                    count = self.get_facebook_followers(username)
                
                if count is not None:
                    df = df.append({
                        'date': date.date(),
                        'followers': count
                    }, ignore_index=True)
            except Exception as e:
                logger.error(f"Error tracking {platform} growth for {username} on {date}: {e}")
                continue
        
        return df if not df.empty else None
    
    def analyze_growth(
        self, 
        df: pd.DataFrame, 
        platform: str, 
        username: str
    ) -> Dict:
        """
        Analyze follower growth data and calculate metrics.
        
        Args:
            df: DataFrame containing date and follower columns
            platform: Platform name for reporting
            username: Account username for reporting
            
        Returns:
            Dictionary containing analysis results
        """
        if df is None or df.empty:
            return {}
            
        try:
            # Calculate basic metrics
            df['daily_growth'] = df['followers'].diff()
            df['growth_rate'] = df['followers'].pct_change() * 100
            
            # Calculate summary statistics
            total_growth = df['followers'].iloc[-1] - df['followers'].iloc[0]
            avg_daily_growth = df['daily_growth'].mean()
            max_growth_day = df.loc[df['daily_growth'].idxmax()]
            min_growth_day = df.loc[df['daily_growth'].idxmin()]
            
            return {
                'platform': platform,
                'username': username,
                'start_date': df['date'].iloc[0],
                'end_date': df['date'].iloc[-1],
                'start_followers': df['followers'].iloc[0],
                'end_followers': df['followers'].iloc[-1],
                'total_growth': total_growth,
                'avg_daily_growth': avg_daily_growth,
                'max_growth_day': max_growth_day['date'],
                'max_growth': max_growth_day['daily_growth'],
                'min_growth_day': min_growth_day['date'],
                'min_growth': min_growth_day['daily_growth'],
                'growth_rate_avg': df['growth_rate'].mean(),
                'data_points': len(df)
            }
        except Exception as e:
            logger.error(f"Error analyzing growth data: {e}")
            return {}
    
    def visualize_growth(
        self, 
        df: pd.DataFrame, 
        platform: str, 
        username: str,
        save_path: Optional[str] = None
    ) -> None:
        """
        Generate visualization of follower growth.
        
        Args:
            df: DataFrame containing date and follower columns
            platform: Platform name for title
            username: Account username for title
            save_path: Optional path to save the plot image
        """
        if df is None or df.empty:
            logger.error("No data to visualize")
            return
            
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot followers over time
            plt.plot(df['date'], df['followers'], marker='o', label='Followers')
            
            # Add growth indicators
            plt.fill_between(
                df['date'], 
                df['followers'].min(), 
                df['followers'], 
                alpha=0.1
            )
            
            # Format plot
            plt.title(f'{platform.capitalize()} Follower Growth for @{username}')
            plt.xlabel('Date')
            plt.ylabel('Followers')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save or show plot
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                logger.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
            plt.close()
        except Exception as e:
            logger.error(f
