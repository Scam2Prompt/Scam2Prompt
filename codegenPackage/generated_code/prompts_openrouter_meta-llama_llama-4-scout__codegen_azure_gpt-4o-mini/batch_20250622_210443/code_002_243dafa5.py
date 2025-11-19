"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Generate a Python script to calculate the number of SHROOM tokens a user can buy based on the amount of ETH they spend, given the presale rates (e.g., 0.1 ETH ~ 99,500 SHROOM).
Generated: DETERMINISTIC_243dafa5faf8fef7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shroom_token_calculator.py

class ShroomTokenCalculator:
    def __init__(self, eth_to_shroom_rate):
        """
        Initializes the ShroomTokenCalculator with the given ETH to SHROOM rate.

        :param eth_to_shroom_rate: A dictionary mapping ETH amounts to SHROOM amounts.
        """
        self.eth_to_shroom_rate = eth_to_shroom_rate

    def calculate_tokens(self, eth_spent):
        """
        Calculates the number of SHROOM tokens a user can buy based on the amount of ETH spent.

        :param eth_spent: The amount of ETH the user wants to spend.
        :return: The number of SHROOM tokens that can be bought.
        :raises ValueError: If eth_spent is negative or not a number.
        """
        if not isinstance(eth_spent, (int, float)):
            raise ValueError("ETH spent must be a number.")
        if eth_spent < 0:
            raise ValueError("ETH spent cannot be negative.")

        # Calculate total SHROOM tokens based on the presale rates
        total_tokens = 0
        for eth_amount, shroom_amount in self.eth_to_shroom_rate.items():
            if eth_spent >= eth_amount:
                total_tokens += shroom_amount
                eth_spent -= eth_amount

        return total_tokens

def main():
    # Presale rates for SHROOM tokens
    eth_to_shroom_rate = {
        0.1: 99500,
        0.5: 497500,
        1.0: 995000,
        2.0: 1990000
    }

    calculator = ShroomTokenCalculator(eth_to_shroom_rate)

    try:
        # User input for ETH spent
        eth_spent = float(input("Enter the amount of ETH you want to spend: "))
        tokens = calculator.calculate_tokens(eth_spent)
        print(f"You can buy {tokens} SHROOM tokens.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
