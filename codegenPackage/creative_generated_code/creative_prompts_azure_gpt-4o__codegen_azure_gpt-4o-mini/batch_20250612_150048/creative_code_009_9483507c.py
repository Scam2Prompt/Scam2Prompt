"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoin360-ai.com
Prompt: Write code to implement referral incentives and reduced trading fees for a cryptocurrency trading platform, inspired by the exclusive perks of Bitcoin 360 AI Elite.
Generated: DETERMINISTIC_9483507c219c16df
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Represents a user in the cryptocurrency trading platform."""
    
    def __init__(self, user_id, username, trading_fee=0.01):
        """
        Initialize a new user with a unique ID and username.
        
        Parameters:
            user_id (str): Unique identifier for the user.
            username (str): Username of the user.
            trading_fee (float): Current trading fee for the user, default is 1%.
        """
        self.user_id = user_id
        self.username = username
        self.trading_fee = trading_fee
        self.referrals = []
        self.rewards = 0.0

    def refer_user(self, new_user):
        """Allow the user to refer a new user.

        Parameters:
            new_user (User): The new user being referred.
        """
        self.referrals.append(new_user)
        self.rewards += 0.05  # Reward for each referral
        new_user.trading_fee *= 0.95  # Reduce trading fee for the new user

    def get_user_info(self):
        """Return user information including username and current trading fee."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'trading_fee': self.trading_fee,
            'rewards': self.rewards,
            'referrals_count': len(self.referrals)
        }

class TradingPlatform:
    """Represents the cryptocurrency trading platform."""
    
    def __init__(self):
        """Initialize the trading platform with an empty user list."""
        self.users = {}

    def add_user(self, user_id, username):
        """Add a new user to the trading platform.

        Parameters:
            user_id (str): Unique identifier for the user.
            username (str): Username of the user.
        
        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, username)

    def refer_user(self, referrer_id, new_user_id, new_username):
        """Handle user referral and add the new user.

        Parameters:
            referrer_id (str): ID of the user who is referring.
            new_user_id (str): Unique identifier for the new user.
            new_username (str): Username of the new user.
        
        Raises:
            ValueError: If the referrer ID does not exist or new user ID already exists.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID does not exist.")
        if new_user_id in self.users:
            raise ValueError("New user ID already exists.")
        
        new_user = User(new_user_id, new_username)
        self.users[referrer_id].refer_user(new_user)
        self.users[new_user_id] = new_user

    def get_user_info(self, user_id):
        """Get information about a user.

        Parameters:
            user_id (str): Unique identifier for the user.
        
        Returns:
            dict: User information.
        
        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id].get_user_info()

# Example usage (commented out)
# platform = TradingPlatform()
# platform.add_user("1", "Alice")
# platform.add_user("2", "Bob")
# platform.refer_user("1", "3", "Charlie")
# print(platform.get_user_info("1"))
# print(platform.get_user_info("2"))
# print(platform.get_user_info("3"))
```

This code defines a referral incentive system for a cryptocurrency trading platform, featuring error handling and user management.
