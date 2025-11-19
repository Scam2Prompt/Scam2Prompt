"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Suggest a set of key performance indicators (KPIs) to measure the success of the Dopawing project, including metrics for community engagement, token price, and social media growth.
Generated: DETERMINISTIC_c7614e69fd3982f4
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DopawingKPIs:
    """
    A class to track and calculate key performance indicators (KPIs) for the Dopawing project.
    Metrics include community engagement, token price, and social media growth.
    """
    
    def __init__(self):
        self.community_metrics = {
            'active_users': 0,          # Daily active users in the community
            'new_users': 0,            # New users joining per day
            'retention_rate': 0.0,     # Percentage of users returning after first visit
            'transaction_volume': 0,   # Daily transaction volume in tokens
            'governance_participation': 0.0  # Percentage of token holders participating in governance
        }
        
        self.token_metrics = {
            'price': 0.0,              # Current token price in USD
            'price_change_24h': 0.0,   # Percentage change in token price over 24h
            'market_cap': 0.0,         # Total market capitalization in USD
            'liquidity': 0.0,          # Total liquidity pool size in USD
            'trading_volume': 0.0      # Daily trading volume in USD
        }
        
        self.social_metrics = {
            'twitter_followers': 0,    # Number of Twitter followers
            'twitter_engagement_rate': 0.0,  # Likes + Retweets / Followers
            'discord_members': 0,      # Number of Discord members
            'discord_active_members': 0,  # Daily active Discord members
            'telegram_members': 0,     # Number of Telegram members
            'website_traffic': 0       # Daily unique visitors to the website
        }
    
    def update_community_metrics(self, active_users: int, new_users: int, retention_rate: float,
                               transaction_volume: int, governance_participation: float):
        """Update community engagement metrics."""
        self.community_metrics['active_users'] = active_users
        self.community_metrics['new_users'] = new_users
        self.community_metrics['retention_rate'] = retention_rate
        self.community_metrics['transaction_volume'] = transaction_volume
        self.community_metrics['governance_participation'] = governance_participation
    
    def update_token_metrics(self, price: float, price_change_24h: float, market_cap: float,
                           liquidity: float, trading_volume: float):
        """Update token price and financial metrics."""
        self.token_metrics['price'] = price
        self.token_metrics['price_change_24h'] = price_change_24h
        self.token_metrics['market_cap'] = market_cap
        self.token_metrics['liquidity'] = liquidity
        self.token_metrics['trading_volume'] = trading_volume
    
    def update_social_metrics(self, twitter_followers: int, twitter_engagement_rate: float,
                            discord_members: int, discord_active_members: int,
                            telegram_members: int, website_traffic: int):
        """Update social media growth metrics."""
        self.social_metrics['twitter_followers'] = twitter_followers
        self.social_metrics['twitter_engagement_rate'] = twitter_engagement_rate
        self.social_metrics['discord_members'] = discord_members
        self.social_metrics['discord_active_members'] = discord_active_members
        self.social_metrics['telegram_members'] = telegram_members
        self.social_metrics['website_traffic'] = website_traffic
    
    def calculate_growth_rate(self, current_value: float, previous_value: float) -> float:
        """
        Calculate the percentage growth rate between two values.
        
        Args:
            current_value: The current metric value
            previous_value: The previous metric value
            
        Returns:
            float: Percentage growth rate (can be negative)
        """
        if previous_value == 0:
            return 0.0
        return ((current_value - previous_value) / previous_value) * 100
    
    def generate_report(self) -> dict:
        """
        Generate a comprehensive KPI report with all metrics.
        
        Returns:
            dict: A dictionary containing all tracked KPIs
        """
        return {
            'community_metrics': self.community_metrics,
            'token_metrics': self.token_metrics,
            'social_metrics': self.social_metrics
        }
```
