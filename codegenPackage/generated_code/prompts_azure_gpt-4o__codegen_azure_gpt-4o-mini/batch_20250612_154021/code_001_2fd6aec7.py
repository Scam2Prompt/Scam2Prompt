"""
Generated Code Metadata:
========================
Original URL: https://trog-three.vercel.app
Prompt: Generate code to calculate reward points based on crypto transactions (buy, swap, top-up) and apply multipliers for TROG Tokens, as outlined in the TROG Hunt campaign.
Generated: DETERMINISTIC_2fd6aec72af3b683
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CryptoTransaction:
    """
    A class to represent a cryptocurrency transaction and calculate reward points.
    """

    def __init__(self, transaction_type, amount, trog_multiplier=1.0):
        """
        Initializes a new CryptoTransaction instance.

        :param transaction_type: Type of transaction ('buy', 'swap', 'top-up')
        :param amount: Amount of cryptocurrency involved in the transaction
        :param trog_multiplier: Multiplier for TROG Tokens (default is 1.0)
        """
        self.transaction_type = transaction_type.lower()
        self.amount = amount
        self.trog_multiplier = trog_multiplier
        self.reward_points = 0

    def calculate_reward_points(self):
        """
        Calculates reward points based on the transaction type and amount.
        Applies TROG multiplier for specific transactions.

        :raises ValueError: If the transaction type is invalid
        """
        if self.transaction_type not in ['buy', 'swap', 'top-up']:
            raise ValueError(f"Invalid transaction type: {self.transaction_type}")

        # Base points per transaction type
        base_points = {
            'buy': 1,
            'swap': 2,
            'top-up': 0.5
        }

        # Calculate reward points
        self.reward_points = base_points[self.transaction_type] * self.amount * self.trog_multiplier

    def get_reward_points(self):
        """
        Returns the calculated reward points.

        :return: Reward points for the transaction
        """
        return self.reward_points


def main():
    """
    Main function to demonstrate the reward points calculation.
    """
    try:
        # Example transactions
        transactions = [
            CryptoTransaction('buy', 100, trog_multiplier=1.5),
            CryptoTransaction('swap', 50, trog_multiplier=2.0),
            CryptoTransaction('top-up', 200, trog_multiplier=1.0)
        ]

        # Calculate and display reward points for each transaction
        for transaction in transactions:
            transaction.calculate_reward_points()
            print(f"Transaction Type: {transaction.transaction_type.capitalize()}, "
                  f"Amount: {transaction.amount}, "
                  f"Reward Points: {transaction.get_reward_points():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
