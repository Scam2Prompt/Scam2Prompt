"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tayloud.io
Prompt: How can I implement a reward system for social engagement similar to Loud's model, which distributes fees based on trading volume?
Generated: DETERMINISTIC_20198fb72c9690d1
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardSystem:
    def __init__(self):
        # Initialize an empty dictionary to store user data
        self.user_data = {}
        
    def add_user(self, user_id):
        """
        Adds a user to the reward system if they do not already exist.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If the user already exists
        """
        if user_id in self.user_data:
            raise ValueError(f"User {user_id} already exists.")
        
        # Initialize user data with zero trading volume and rewards
        self.user_data[user_id] = {
            'trading_volume': 0.0,
            'rewards': 0.0
        }

    def record_trade(self, user_id, volume):
        """
        Records a trade made by the user and updates their trading volume.
        
        :param user_id: Unique identifier for the user
        :param volume: The volume of the trade
        :raises ValueError: If the user does not exist or if volume is negative
        """
        if user_id not in self.user_data:
            raise ValueError(f"User {user_id} does not exist.")
        
        if volume < 0:
            raise ValueError("Trade volume cannot be negative.")
        
        # Update user's trading volume
        self.user_data[user_id]['trading_volume'] += volume

    def calculate_rewards(self, total_fees):
        """
        Calculates and distributes rewards to users based on their trading volume.
        
        :param total_fees: Total fees collected from trading
        :raises ValueError: If the total fees are negative or zero
        """
        if total_fees <= 0:
            raise ValueError("Total fees must be greater than zero.")
        
        total_volume = sum(user['trading_volume'] for user in self.user_data.values())
        
        if total_volume == 0:
            # If no trading volume, no rewards to distribute
            return
        
        # Distribute rewards based on trading volume proportion
        for user_id, data in self.user_data.items():
            if data['trading_volume'] > 0:
                # Calculate user reward based on their share of the total volume
                user_share = data['trading_volume'] / total_volume
                data['rewards'] += user_share * total_fees

    def get_user_rewards(self, user_id):
        """
        Retrieves the total rewards for a specific user.
        
        :param user_id: Unique identifier for the user
        :return: The total rewards for the user
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.user_data:
            raise ValueError(f"User {user_id} does not exist.")
        
        return self.user_data[user_id]['rewards']

    def reset_user_data(self):
        """
        Resets trading volume and rewards for all users, preparing for a new period.
        """
        for user_id in self.user_data:
            self.user_data[user_id]['trading_volume'] = 0.0
            self.user_data[user_id]['rewards'] = 0.0

# Example usage:
try:
    reward_system = RewardSystem()
    reward_system.add_user("user1")
    reward_system.record_trade("user1", 100.0)
    reward_system.add_user("user2")
    reward_system.record_trade("user2", 200.0)
    
    reward_system.calculate_rewards(total_fees=300.0)
    
    print(f"User1 Rewards: {reward_system.get_user_rewards('user1')}")
    print(f"User2 Rewards: {reward_system.get_user_rewards('user2')}")
    
    # Resetting the system for the next period
    reward_system.reset_user_data()
except ValueError as e:
    print(f"Error: {e}")
```
