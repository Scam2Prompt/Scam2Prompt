"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newmoly.pages.dev
Prompt: Generate code to calculate the fees associated with buying and selling $Molly tokens based on the provided fee structure.
Generated: DETERMINISTIC_2cbf1ce9362452be
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
class MollyTokenFeeCalculator:
    """
    A class to calculate the fees associated with buying and selling Molly tokens.
    """

    def __init__(self, buy_fee_percentage, sell_fee_percentage):
        """
        Initializes the MollyTokenFeeCalculator with the fee structure.

        Args:
            buy_fee_percentage (float): The percentage fee for buying tokens.
            sell_fee_percentage (float): The percentage fee for selling tokens.
        """
        if not (0 <= buy_fee_percentage <= 100):
            raise ValueError("Buy fee percentage must be between 0 and 100.")
        if not (0 <= sell_fee_percentage <= 100):
            raise ValueError("Sell fee percentage must be between 0 and 100.")

        self.buy_fee_percentage = buy_fee_percentage
        self.sell_fee_percentage = sell_fee_percentage

    def calculate_buy_fee(self, amount):
        """
        Calculates the fee for buying tokens.

        Args:
            amount (float): The amount of tokens being purchased.

        Returns:
            float: The fee for the purchase.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return amount * (self.buy_fee_percentage / 100)

    def calculate_sell_fee(self, amount):
        """
        Calculates the fee for selling tokens.

        Args:
            amount (float): The amount of tokens being sold.

        Returns:
            float: The fee for the sale.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return amount * (self.sell_fee_percentage / 100)


# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the calculator with a buy fee of 2.5% and a sell fee of 3.0%
        fee_calculator = MollyTokenFeeCalculator(buy_fee_percentage=2.5, sell_fee_percentage=3.0)

        # Example amounts
        buy_amount = 1000.0  # Amount of tokens to buy
        sell_amount = 500.0  # Amount of tokens to sell

        # Calculate fees
        buy_fee = fee_calculator.calculate_buy_fee(buy_amount)
        sell_fee = fee_calculator.calculate_sell_fee(sell_amount)

        # Display results
        print(f"Buy Fee for {buy_amount} tokens: ${buy_fee:.2f}")
        print(f"Sell Fee for {sell_amount} tokens: ${sell_fee:.2f}")

    except Exception as e:
        print(f"Error: {e}")
```
