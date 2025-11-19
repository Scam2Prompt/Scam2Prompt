"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-9v1.pages.dev
Prompt: Explain how to implement a reward system for PLRT token holders based on transaction percentages across the platform, and provide a sample code snippet.
Generated: DETERMINISTIC_775a2067fdf09862
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardSystem:
    """
    A class to implement a reward system for PLRT token holders based on transaction percentages.
    
    Attributes:
        total_supply (float): The total supply of PLRT tokens.
        transaction_fee_percentage (float): The percentage of each transaction that goes to rewards.
    """
    
    def __init__(self, total_supply: float, transaction_fee_percentage: float):
        """
        Initializes the RewardSystem with total supply and transaction fee percentage.
        
        Args:
            total_supply (float): Total number of PLRT tokens.
            transaction_fee_percentage (float): Percentage fee from each transaction for rewards.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= transaction_fee_percentage <= 100):
            raise ValueError("Transaction fee percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.transaction_fee_percentage = transaction_fee_percentage
        self.rewards_pool = 0.0

    def process_transaction(self, transaction_amount: float):
        """
        Processes a transaction and updates the rewards pool based on the transaction amount.
        
        Args:
            transaction_amount (float): The amount of the transaction.
        
        Raises:
            ValueError: If transaction amount is less than or equal to zero.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Calculate the fee from the transaction
        fee = (self.transaction_fee_percentage / 100) * transaction_amount
        self.rewards_pool += fee

    def distribute_rewards(self, holder_tokens: float) -> float:
        """
        Distributes rewards to a holder based on the number of tokens they hold.
        
        Args:
            holder_tokens (float): The number of tokens held by the user.
        
        Returns:
            float: The amount of rewards distributed to the holder.
        
        Raises:
            ValueError: If holder tokens is less than zero or exceeds total supply.
        """
        if holder_tokens < 0:
            raise ValueError("Holder tokens cannot be negative.")
        if holder_tokens > self.total_supply:
            raise ValueError("Holder tokens exceed total supply.")

        if self.rewards_pool == 0:
            return 0.0  # No rewards to distribute

        # Calculate the rewards for the holder based on their proportion of total supply
        holder_share = holder_tokens / self.total_supply
        rewards = holder_share * self.rewards_pool
        
        # Reset rewards pool after distribution
        self.rewards_pool = 0.0
        
        return rewards

# Example Usage
if __name__ == "__main__":
    try:
        reward_system = RewardSystem(total_supply=1000000.0, transaction_fee_percentage=5.0)

        # Simulating transactions
        reward_system.process_transaction(transaction_amount=1000.0)
        reward_system.process_transaction(transaction_amount=2000.0)

        # Distributing rewards to a holder with 1000 tokens
        rewards = reward_system.distribute_rewards(holder_tokens=1000.0)
        print(f"Rewards distributed to holder: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
