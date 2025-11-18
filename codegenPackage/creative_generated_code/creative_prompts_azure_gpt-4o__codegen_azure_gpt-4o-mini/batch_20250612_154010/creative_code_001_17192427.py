"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vempire-opal.vercel.app
Prompt: Generate code to track and calculate reward multipliers for users swapping, staking, or referring friends on the VEMP Hunt platform.
Generated: DETERMINISTIC_171924276ecf148b
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user on the VEMP Hunt platform with methods to manage rewards.
    """
    
    def __init__(self, user_id):
        """
        Initializes a new user with a unique ID and sets initial reward multipliers.
        
        Args:
            user_id (str): Unique identifier for the user.
        """
        self.user_id = user_id
        self.reward_multiplier = 1.0  # Default multiplier
        self.swap_count = 0
        self.stake_count = 0
        self.referral_count = 0

    def swap(self):
        """
        Increments the swap count and updates the reward multiplier.
        """
        self.swap_count += 1
        self.update_multiplier()
    
    def stake(self):
        """
        Increments the stake count and updates the reward multiplier.
        """
        self.stake_count += 1
        self.update_multiplier()
    
    def refer(self):
        """
        Increments the referral count and updates the reward multiplier.
        """
        self.referral_count += 1
        self.update_multiplier()
    
    def update_multiplier(self):
        """
        Updates the reward multiplier based on the user's activity.
        """
        # Simple reward logic: increase multiplier based on activities
        self.reward_multiplier = 1.0 + (self.swap_count * 0.1) + (self.stake_count * 0.2) + (self.referral_count * 0.3)

    def get_reward_multiplier(self):
        """
        Returns the current reward multiplier for the user.
        
        Returns:
            float: The current reward multiplier.
        """
        return self.reward_multiplier


class RewardTracker:
    """
    Manages multiple users and tracks their reward multipliers.
    """
    
    def __init__(self):
        """
        Initializes the RewardTracker with an empty user registry.
        """
        self.users = {}
    
    def add_user(self, user_id):
        """
        Adds a new user to the tracker.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = User(user_id)
    
    def record_swap(self, user_id):
        """
        Records a swap action for a user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        user = self.get_user(user_id)
        user.swap()
    
    def record_stake(self, user_id):
        """
        Records a stake action for a user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        user = self.get_user(user_id)
        user.stake()
    
    def record_referral(self, user_id):
        """
        Records a referral action for a user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        user = self.get_user(user_id)
        user.refer()
    
    def get_user(self, user_id):
        """
        Retrieves a user object by its ID.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            User: The corresponding User object.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise KeyError(f"User ID {user_id} not found.")
        return self.users[user_id]
    
    def get_reward_multiplier(self, user_id):
        """
        Retrieves the reward multiplier for a specific user.
        
        Args:
            user_id (str): Unique identifier for the user.
        
        Returns:
            float: The user's current reward multiplier.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        user = self.get_user(user_id)
        return user.get_reward_multiplier()


# Example usage
if __name__ == "__main__":
    tracker = RewardTracker()
    
    try:
        tracker.add_user("user123")
        tracker.record_swap("user123")
        tracker.record_stake("user123")
        tracker.record_referral("user123")
        
        multiplier = tracker.get_reward_multiplier("user123")
        print(f"User user123 has a reward multiplier of {multiplier:.2f}")
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
