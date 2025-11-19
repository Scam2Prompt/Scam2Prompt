"""
Generated Code Metadata:
========================
Original URL: https://haggis.vercel.app
Prompt: Generate code to calculate points earned from crypto transactions, including multipliers, based on the HAGGIS Hunt reward system.
Generated: DETERMINISTIC_04a2ab5733eb5832
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HaggisHuntRewardSystem:
    """
    A class to calculate points earned from crypto transactions based on the HAGGIS Hunt reward system.
    """

    def __init__(self, base_points: float):
        """
        Initializes the reward system with a base point value.

        :param base_points: The base points earned per transaction.
        """
        if base_points < 0:
            raise ValueError("Base points must be a non-negative value.")
        self.base_points = base_points

    def calculate_points(self, transaction_amount: float, multiplier: float) -> float:
        """
        Calculates the total points earned from a transaction.

        :param transaction_amount: The amount of the transaction.
        :param multiplier: The multiplier to apply to the base points.
        :return: The total points earned from the transaction.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be a non-negative value.")
        if multiplier < 0:
            raise ValueError("Multiplier must be a non-negative value.")

        # Calculate points based on transaction amount and multiplier
        points = self.base_points * multiplier * transaction_amount
        return points

    def total_points(self, transactions: list) -> float:
        """
        Calculates the total points earned from a list of transactions.

        :param transactions: A list of tuples where each tuple contains (transaction_amount, multiplier).
        :return: The total points earned from all transactions.
        """
        total = 0.0
        for transaction in transactions:
            if len(transaction) != 2:
                raise ValueError("Each transaction must be a tuple of (transaction_amount, multiplier).")
            transaction_amount, multiplier = transaction
            total += self.calculate_points(transaction_amount, multiplier)
        return total


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reward system with a base point value
        reward_system = HaggisHuntRewardSystem(base_points=10.0)

        # List of transactions (amount, multiplier)
        transactions = [
            (100.0, 1.5),
            (200.0, 2.0),
            (50.0, 1.0)
        ]

        # Calculate total points from transactions
        total_earned_points = reward_system.total_points(transactions)
        print(f"Total points earned: {total_earned_points}")

    except ValueError as e:
        print(f"Error: {e}")
```
