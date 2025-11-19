"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-nft1994.vercel.app
Prompt: Explain how the gETH token rewards users for gas fees and provide a code example for calculating potential rewards based on transaction history.
Generated: DETERMINISTIC_cf9dc02bdc8e7a87
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# gETH Token Rewards Calculator

class Transaction:
    """
    Represents a single transaction.
    
    Attributes:
        transaction_id (str): Unique identifier for the transaction.
        gas_used (float): Amount of gas used in the transaction.
        gas_price (float): Price of gas at the time of the transaction.
    """
    def __init__(self, transaction_id: str, gas_used: float, gas_price: float):
        self.transaction_id = transaction_id
        self.gas_used = gas_used
        self.gas_price = gas_price

    def calculate_fee(self) -> float:
        """
        Calculate the transaction fee based on gas used and gas price.
        
        Returns:
            float: The transaction fee in ETH.
        """
        return self.gas_used * self.gas_price


class RewardCalculator:
    """
    Calculates potential gETH rewards from a list of transactions.
    
    Attributes:
        reward_percentage (float): The percentage of gas fees rewarded in gETH.
    """
    def __init__(self, reward_percentage: float):
        if not (0 < reward_percentage <= 100):
            raise ValueError("Reward percentage must be between 0 and 100.")
        self.reward_percentage = reward_percentage / 100  # Convert to decimal

    def calculate_rewards(self, transactions: list) -> float:
        """
        Calculate total gETH rewards from a list of transactions.
        
        Args:
            transactions (list): A list of Transaction objects.
        
        Returns:
            float: Total gETH rewards.
        """
        total_rewards = 0.0
        
        for transaction in transactions:
            try:
                fee = transaction.calculate_fee()
                reward = fee * self.reward_percentage
                total_rewards += reward
            except Exception as e:
                print(f"Error calculating reward for transaction {transaction.transaction_id}: {e}")
        
        return total_rewards

# Example usage
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        Transaction("tx_01", gas_used=21000, gas_price=0.00002),  # Example gas used and gas price
        Transaction("tx_02", gas_used=30000, gas_price=0.000021),
        Transaction("tx_03", gas_used=15000, gas_price=0.000019),
    ]
    
    # Initialize the RewardCalculator with a 10% reward rate
    reward_calculator = RewardCalculator(reward_percentage=10.0)
    
    # Calculate total gETH rewards
    total_rewards = reward_calculator.calculate_rewards(transactions)
    
    # Output the total rewards
    print(f"Total gETH rewards: {total_rewards:.6f} ETH")
```
