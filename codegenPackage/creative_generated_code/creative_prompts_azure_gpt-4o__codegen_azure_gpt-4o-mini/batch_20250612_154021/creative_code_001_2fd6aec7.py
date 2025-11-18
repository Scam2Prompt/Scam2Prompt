"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trog-three.vercel.app
Prompt: Generate code to calculate reward points based on crypto transactions (buy, swap, top-up) and apply multipliers for TROG Tokens, as outlined in the TROG Hunt campaign.
Generated: DETERMINISTIC_2fd6aec72af3b683
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionType:
    """Enum to define various transaction types."""
    BUY = "buy"
    SWAP = "swap"
    TOP_UP = "top_up"


class RewardCalculator:
    """Class to calculate reward points based on crypto transactions."""

    def __init__(self, base_rate=1.0, trog_multiplier=2.0):
        """
        Initialize the RewardCalculator with base rate and TROG multiplier.

        Args:
            base_rate (float): The base rate for calculating reward points.
            trog_multiplier (float): The multiplier for transactions involving TROG tokens.
        """
        self.base_rate = base_rate
        self.trog_multiplier = trog_multiplier

    def calculate_reward(self, transaction_type, amount, is_trog=False):
        """
        Calculate the reward points for a given transaction.

        Args:
            transaction_type (str): The type of transaction (buy, swap, top-up).
            amount (float): The amount involved in the transaction.
            is_trog (bool): Indicates if the transaction involves TROG tokens.

        Returns:
            float: The calculated reward points.

        Raises:
            ValueError: If the transaction type is invalid or amount is negative.
        """
        if transaction_type not in (TransactionType.BUY, TransactionType.SWAP, TransactionType.TOP_UP):
            raise ValueError(f"Invalid transaction type: {transaction_type}")
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")
        
        # Calculate base reward points
        reward_points = amount * self.base_rate
        
        # Apply TROG multiplier if applicable
        if is_trog:
            reward_points *= self.trog_multiplier
        
        return reward_points


def process_transactions(transactions):
    """
    Process a list of transactions to calculate total reward points.

    Args:
        transactions (list): A list of dictionaries where each dictionary contains:
                             - 'type': Transaction type (buy, swap, top-up)
                             - 'amount': Transaction amount (float)
                             - 'is_trog': If the transaction involves TROG tokens (bool)

    Returns:
        float: Total reward points from all transactions.
    """
    calculator = RewardCalculator()
    total_rewards = 0.0

    for transaction in transactions:
        try:
            total_rewards += calculator.calculate_reward(
                transaction['type'],
                transaction['amount'],
                transaction.get('is_trog', False)
            )
        except ValueError as e:
            print(f"Error processing transaction {transaction}: {e}")

    return total_rewards


# Example usage
if __name__ == "__main__":
    transactions = [
        {"type": TransactionType.BUY, "amount": 100, "is_trog": True},
        {"type": TransactionType.SWAP, "amount": 50, "is_trog": False},
        {"type": TransactionType.TOP_UP, "amount": 200, "is_trog": True},
    ]

    total_points = process_transactions(transactions)
    print(f"Total reward points earned: {total_points}")
```

This code defines a reward points calculator for crypto transactions, incorporating best practices such as error handling and clear documentation.
