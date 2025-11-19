"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidnueyp2x4qveeg7e4goxah3h5vtflv2thqjuzrrkqz4ctteeuxr4.ipfs.dweb.link
Prompt: How can I set up a rewards system for token exchanges in a project inspired by Puff The Dragon's ecosystem?
Generated: DETERMINISTIC_33d95b90f462c47a
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class RewardsSystem:
    """
    A class to handle the rewards system for token exchanges.
    
    Attributes:
        user_rewards (dict): A dictionary to store user rewards.
        exchange_rate (float): The rate at which tokens are exchanged for rewards.
    """

    def __init__(self, exchange_rate: float):
        """
        Initializes the RewardsSystem with a given exchange rate.
        
        Args:
            exchange_rate (float): The number of rewards per token.
        
        Raises:
            ValueError: If the exchange rate is non-positive.
        """
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be a positive number.")
        
        self.user_rewards = {}
        self.exchange_rate = exchange_rate

    def exchange_tokens(self, user_id: str, tokens: int) -> float:
        """
        Exchange tokens for rewards for a specified user.
        
        Args:
            user_id (str): The ID of the user exchanging tokens.
            tokens (int): The number of tokens to exchange.
        
        Returns:
            float: The amount of rewards earned.
        
        Raises:
            ValueError: If the number of tokens is negative.
        """
        if tokens < 0:
            raise ValueError("Tokens to exchange must be a non-negative integer.")
        
        # Calculate rewards based on tokens exchanged
        rewards = tokens * self.exchange_rate
        
        # Update user rewards
        if user_id in self.user_rewards:
            self.user_rewards[user_id] += rewards
        else:
            self.user_rewards[user_id] = rewards
        
        return rewards

    def get_user_rewards(self, user_id: str) -> float:
        """
        Retrieve the total rewards for a specified user.
        
        Args:
            user_id (str): The ID of the user.
        
        Returns:
            float: The total rewards for the user, zero if none.
        """
        return self.user_rewards.get(user_id, 0.0)

    def reset_rewards(self, user_id: str):
        """
        Reset the rewards for a specified user.
        
        Args:
            user_id (str): The ID of the user to reset rewards for.
        
        Raises:
            KeyError: If the user ID does not exist.
        """
        if user_id not in self.user_rewards:
            raise KeyError(f"User ID '{user_id}' does not exist.")
        
        self.user_rewards[user_id] = 0.0


# Example of usage
if __name__ == "__main__":
    try:
        rewards_system = RewardsSystem(exchange_rate=10.0)  # 10 rewards per token

        # Exchange tokens
        user_id = "user123"
        rewards_earned = rewards_system.exchange_tokens(user_id, 5)
        print(f"Rewards earned by {user_id}: {rewards_earned}")

        # Get user rewards
        total_rewards = rewards_system.get_user_rewards(user_id)
        print(f"Total rewards for {user_id}: {total_rewards}")

        # Reset user rewards
        rewards_system.reset_rewards(user_id)
        print(f"Rewards after reset for {user_id}: {rewards_system.get_user_rewards(user_id)}")

    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```
