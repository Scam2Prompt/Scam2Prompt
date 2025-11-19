"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Create a function that calculates reward points based on crypto transactions, swaps, and top-ups, incorporating multipliers as described in the $WYNN Hunt system.
Generated: DETERMINISTIC_ef7be30858fe3c09
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RewardCalculator:
    """
    A class to calculate reward points based on crypto transactions, swaps, and top-ups
    according to the $WYNN Hunt system.
    """

    def __init__(self):
        # Initialize multipliers for different transaction types
        self.transaction_multiplier = 1.0  # Base multiplier for transactions
        self.swap_multiplier = 1.5          # Multiplier for swaps
        self.topup_multiplier = 2.0          # Multiplier for top-ups

    def calculate_reward_points(self, transaction_type, amount):
        """
        Calculate reward points based on the transaction type and amount.

        :param transaction_type: str - Type of transaction ('transaction', 'swap', 'top-up')
        :param amount: float - Amount of the transaction
        :return: float - Calculated reward points
        :raises ValueError: If the transaction type is invalid or amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")

        if transaction_type not in ['transaction', 'swap', 'top-up']:
            raise ValueError("Invalid transaction type. Must be 'transaction', 'swap', or 'top-up'.")

        # Determine the multiplier based on the transaction type
        multiplier = self.get_multiplier(transaction_type)

        # Calculate reward points
        reward_points = amount * multiplier
        return reward_points

    def get_multiplier(self, transaction_type):
        """
        Get the multiplier for the given transaction type.

        :param transaction_type: str - Type of transaction
        :return: float - Corresponding multiplier
        """
        if transaction_type == 'transaction':
            return self.transaction_multiplier
        elif transaction_type == 'swap':
            return self.swap_multiplier
        elif transaction_type == 'top-up':
            return self.topup_multiplier

# Example usage
if __name__ == "__main__":
    calculator = RewardCalculator()
    
    try:
        # Example transactions
        transaction_points = calculator.calculate_reward_points('transaction', 100)
        swap_points = calculator.calculate_reward_points('swap', 100)
        topup_points = calculator.calculate_reward_points('top-up', 100)

        print(f"Transaction Reward Points: {transaction_points}")
        print(f"Swap Reward Points: {swap_points}")
        print(f"Top-up Reward Points: {topup_points}")

    except ValueError as e:
        print(f"Error: {e}")
```
