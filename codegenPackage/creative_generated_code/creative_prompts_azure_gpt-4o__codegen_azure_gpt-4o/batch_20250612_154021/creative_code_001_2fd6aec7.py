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
import decimal

class RewardCalculator:
    """
    Class to calculate reward points based on crypto transactions and apply multipliers 
    for TROG Tokens as part of the TROG Hunt campaign.
    """

    def __init__(self):
        # Multipliers for each transaction type
        self.multipliers = {
            "buy": 1.0,      # Base multiplier for buy transactions
            "swap": 1.5,     # Higher multiplier for swap transactions
            "top_up": 2.0    # Even higher multiplier for top-up transactions
        }

        # Additional multiplier for TROG Tokens
        self.trog_multiplier = 1.25

    def calculate_rewards(self, transaction_type, amount, token=""):
        """
        Calculate reward points based on transaction type, amount, and token type.

        :param transaction_type: Type of transaction (buy, swap, or top_up).
        :param amount: Transaction amount in decimal.
        :param token: Token involved in the transaction (e.g., 'TROG').
        :return: Reward points as a decimal.
        """
        try:
            # Validate transaction type
            if transaction_type not in self.multipliers:
                raise ValueError(f"Invalid transaction type: {transaction_type}")

            # Ensure amount is a positive decimal
            amount = decimal.Decimal(amount)
            if amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")

            # Apply base multiplier based on transaction type
            base_multiplier = self.multipliers[transaction_type]
            rewards = amount * base_multiplier

            # Apply TROG Token multiplier if applicable
            if token.upper() == "TROG":
                rewards *= self.trog_multiplier

            # Return rewards rounded to 2 decimal places
            return rewards.quantize(decimal.Decimal("0.01"))

        except decimal.InvalidOperation:
            raise ValueError("Invalid transaction amount format.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating rewards: {str(e)}")


# Example usage
if __name__ == "__main__":
    calculator = RewardCalculator()

    # Example transactions
    try:
        print("Reward for buy transaction (amount=100, token='BTC'):",
              calculator.calculate_rewards("buy", 100, "BTC"))
        print("Reward for swap transaction (amount=200, token='TROG'):",
              calculator.calculate_rewards("swap", 200, "TROG"))
        print("Reward for top-up transaction (amount=300, token='ETH'):",
              calculator.calculate_rewards("top_up", 300, "ETH"))
    except Exception as e:
        print("Error:", e)
```
