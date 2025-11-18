"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Generate code for a loyalty program system that tracks user activity and calculates rewards, such as cashback, similar to BaxBet's loyalty features.
Generated: DETERMINISTIC_26a14b2887bcd263
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    """
    A class to represent a loyalty program that tracks user activity and calculates rewards.
    """

    def __init__(self):
        """
        Initializes the loyalty program with an empty user activity log and a rewards dictionary.
        """
        self.user_activity = {}
        self.rewards = {}

    def add_user(self, user_id):
        """
        Adds a new user to the loyalty program.
        
        Parameters:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user_id already exists.
        """
        if user_id in self.user_activity:
            raise ValueError(f"User ID {user_id} already exists.")
        
        self.user_activity[user_id] = []
        self.rewards[user_id] = 0.0

    def record_activity(self, user_id, amount):
        """
        Records a user's activity for calculating rewards.
        
        Parameters:
            user_id (str): The unique identifier for the user.
            amount (float): The amount associated with the user's activity.
        
        Raises:
            ValueError: If the user_id does not exist or if amount is negative.
        """
        if user_id not in self.user_activity:
            raise ValueError(f"User ID {user_id} does not exist.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        
        self.user_activity[user_id].append(amount)

    def calculate_rewards(self, user_id):
        """
        Calculates the rewards based on user activity.
        
        Parameters:
            user_id (str): The unique identifier for the user.
        
        Returns:
            float: The total rewards calculated for the user.
        
        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.user_activity:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        total_amount = sum(self.user_activity[user_id])
        cashback_rate = 0.05  # Example cashback rate of 5%
        self.rewards[user_id] = total_amount * cashback_rate
        return self.rewards[user_id]

    def get_rewards(self, user_id):
        """
        Retrieves the current rewards for a specific user.
        
        Parameters:
            user_id (str): The unique identifier for the user.
        
        Returns:
            float: The current rewards for the user.
        
        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.rewards:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.rewards[user_id]

# Example usage:
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Adding users
    loyalty_program.add_user("user123")
    loyalty_program.add_user("user456")

    # Recording activities
    loyalty_program.record_activity("user123", 100.0)
    loyalty_program.record_activity("user123", 200.0)
    loyalty_program.record_activity("user456", 150.0)

    # Calculating rewards
    print(f"User user123 has rewards: {loyalty_program.calculate_rewards('user123')}")
    print(f"User user456 has rewards: {loyalty_program.calculate_rewards('user456')}")
```
