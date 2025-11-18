"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Provide code to implement a reward multiplier system for crypto transactions, similar to the functionality described in the MELLSTROY Hunt.
Generated: DETERMINISTIC_d018ab9096b8eac6
Batch ID: 20250612_154635
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardMultiplierSystem:
    """
    A class to manage reward multipliers for cryptocurrency transactions.
    
    Attributes:
        base_reward (float): The base reward for a transaction.
        multipliers (dict): A dictionary to hold the multiplier values based on transaction types.
    """

    def __init__(self, base_reward: float):
        """
        Initializes the RewardMultiplierSystem with a base reward.
        
        Args:
            base_reward (float): The base reward amount.
        
        Raises:
            ValueError: If base_reward is negative.
        """
        if base_reward < 0:
            raise ValueError("Base reward must be a non-negative value.")
        self.base_reward = base_reward
        self.multipliers = {
            'standard': 1.0,
            'bonus': 2.0,
            'premium': 3.0,
        }

    def set_multiplier(self, transaction_type: str, multiplier: float) -> None:
        """
        Sets the multiplier for a specific transaction type.
        
        Args:
            transaction_type (str): The type of transaction.
            multiplier (float): The multiplier value to set.
        
        Raises:
            ValueError: If multiplier is negative.
        """
        if multiplier < 0:
            raise ValueError("Multiplier must be a non-negative value.")
        self.multipliers[transaction_type] = multiplier

    def calculate_reward(self, transaction_type: str, amount: float) -> float:
        """
        Calculates the reward for a given transaction type and amount.
        
        Args:
            transaction_type (str): The type of transaction.
            amount (float): The transaction amount.
        
        Returns:
            float: The calculated reward.
        
        Raises:
            ValueError: If transaction_type is not recognized or amount is negative.
        """
        if transaction_type not in self.multipliers:
            raise ValueError("Transaction type is not recognized.")
        if amount < 0:
            raise ValueError("Transaction amount must be a non-negative value.")
        
        multiplier = self.multipliers[transaction_type]
        reward = self.base_reward * multiplier * amount
        return reward

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reward system with a base reward
        reward_system = RewardMultiplierSystem(base_reward=10.0)
        
        # Set a custom multiplier for a new transaction type
        reward_system.set_multiplier('loyalty', 2.5)
        
        # Calculate rewards for different transaction types
        standard_reward = reward_system.calculate_reward('standard', 5.0)
        bonus_reward = reward_system.calculate_reward('bonus', 5.0)
        loyalty_reward = reward_system.calculate_reward('loyalty', 5.0)

        print(f"Standard Reward: {standard_reward}")
        print(f"Bonus Reward: {bonus_reward}")
        print(f"Loyalty Reward: {loyalty_reward}")

    except ValueError as e:
        print(f"Error: {e}")
```
