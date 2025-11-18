"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Generate code to calculate points earned from crypto transactions, including multipliers, based on the HAGGIS Hunt reward system.
Generated: DETERMINISTIC_04a2ab5733eb5832
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HaggisHuntRewardSystem:
    """
    A class to calculate points earned from crypto transactions based on the HAGGIS Hunt reward system.
    """

    def __init__(self):
        # Define multipliers based on transaction type
        self.multipliers = {
            "buy": 1.5,
            "sell": 1.2,
            "trade": 1.8,
            "stake": 2.0,
        }

    def calculate_points(self, transaction_type, amount):
        """
        Calculate the reward points based on transaction type and amount.

        :param transaction_type: The type of crypto transaction (buy, sell, trade, stake).
        :param amount: The transaction amount in crypto units.
        :return: The calculated reward points.
        """
        try:
            # Validate transaction type
            if transaction_type not in self.multipliers:
                raise ValueError(f"Invalid transaction type: {transaction_type}. Must be one of {list(self.multipliers.keys())}.")

            # Validate transaction amount
            if amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")

            # Calculate points based on the multiplier
            multiplier = self.multipliers[transaction_type]
            points = amount * multiplier

            logging.info(f"Transaction Type: {transaction_type}, Amount: {amount}, Multiplier: {multiplier}, Points: {points}")
            return points

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return None
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Instantiate the reward system
    haggis_hunt = HaggisHuntRewardSystem()

    # Example transactions
    transactions = [
        {"transaction_type": "buy", "amount": 100},
        {"transaction_type": "sell", "amount": 50},
        {"transaction_type": "stake", "amount": 200},
        {"transaction_type": "invalid_type", "amount": 75},  # Invalid transaction type
        {"transaction_type": "trade", "amount": -50},  # Invalid transaction amount
    ]

    # Calculate points for each transaction
    for tx in transactions:
        points = haggis_hunt.calculate_points(tx["transaction_type"], tx["amount"])
        print(f"Transaction: {tx}, Points Earned: {points}")
```
