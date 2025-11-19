"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Explain the concept of Loud and how it utilizes trading volume to reward top contributors to discussions about a specific coin.
Generated: DETERMINISTIC_f4a03bb8f7327aaa
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Loud:
    """
    A class that implements a reward system based on trading volume and discussion contributions.
    """
    
    def __init__(self, coin_id: str, volume_threshold: float):
        """
        Initialize Loud with a specific coin and volume threshold.
        
        Args:
            coin_id: Unique identifier for the coin/token
            volume_threshold: Minimum trading volume required to be eligible for rewards
        """
        self.coin_id = coin_id
        self.volume_threshold = volume_threshold
        self.contributors = {}  # {user_id: {'posts': int, 'upvotes': int, 'reward': float}}
        self.trading_volume = 0.0
        
    def update_trading_volume(self, new_volume: float) -> None:
        """
        Update the current trading volume for the coin.
        
        Args:
            new_volume: Latest trading volume amount
        """
        if new_volume < 0:
            raise ValueError("Trading volume cannot be negative")
        self.trading_volume = new_volume
        
    def add_contribution(self, user_id: str, post_value: int = 1, upvotes: int = 0) -> None:
        """
        Record a user's contribution to the discussion.
        
        Args:
            user_id: Unique identifier for the user
            post_value: Value of the post (default 1)
            upvotes: Number of upvotes received (default 0)
        """
        if post_value <= 0:
            raise ValueError("Post value must be positive")
        if upvotes < 0:
            raise ValueError("Upvotes cannot be negative")
            
        if user_id not in self.contributors:
            self.contributors[user_id] = {
                'posts': 0,
                'upvotes': 0,
                'reward': 0.0
            }
            
        self.contributors[user_id]['posts'] += post_value
        self.contributors[user_id]['upvotes'] += upvotes
        
    def calculate_rewards(self, reward_pool: float) -> dict:
        """
        Calculate rewards for contributors based on their engagement and trading volume.
        
        Args:
            reward_pool: Total amount of rewards to distribute
            
        Returns:
            Dictionary mapping user_ids to their calculated rewards
        """
        if reward_pool <= 0:
            raise ValueError("Reward pool must be positive")
        if self.trading_volume < self.volume_threshold:
            return {}  # No rewards if volume threshold not met
            
        # Calculate total engagement points
        total_points = sum(
            contrib['posts'] * 0.7 + contrib['upvotes'] * 0.3
            for contrib in self.contributors.values()
        )
        
        if total_points == 0:
            return {}  # No rewards if no engagement
            
        # Distribute rewards proportionally
        rewards = {}
        for user_id, contrib in self.contributors.items():
            user_points = contrib['posts'] * 0.7 + contrib['upvotes'] * 0.3
            reward = (user_points / total_points) * reward_pool
            rewards[user_id] = reward
            contrib['reward'] = reward
            
        return rewards
    
    def get_top_contributors(self, top_n: int = 10) -> list:
        """
        Get the top contributors by engagement score.
        
        Args:
            top_n: Number of top contributors to return
            
        Returns:
            List of tuples (user_id, engagement_score) sorted descending
        """
        if top_n <= 0:
            raise ValueError("top_n must be positive")
            
        contributors_with_scores = [
            (user_id, contrib['posts'] * 0.7 + contrib['upvotes'] * 0.3)
            for user_id, contrib in self.contributors.items()
        ]
        
        # Sort by engagement score descending
        sorted_contributors = sorted(
            contributors_with_scores,
            key=lambda x: x[1],
            reverse=True
        )
        
        return sorted_contributors[:top_n]
```
