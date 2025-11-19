"""
Generated Code Metadata:
========================
Original URL: https://newmoly.pages.dev
Prompt: Generate code to calculate the fees associated with buying and selling $Molly tokens based on the provided fee structure.
Generated: DETERMINISTIC_2cbf1ce9362452be
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MollyTokenTransaction:
    """
    A class to represent a transaction for buying and selling Molly tokens.
    """

    def __init__(self, buy_fee_percentage: float, sell_fee_percentage: float):
        """
        Initializes the transaction with the specified buy and sell fee percentages.

        :param buy_fee_percentage: The fee percentage for buying Molly tokens.
        :param sell_fee_percentage: The fee percentage for selling Molly tokens.
        """
        if not (0 <= buy_fee_percentage <= 100):
            raise ValueError("Buy fee percentage must be between 0 and 100.")
        if not (0 <= sell_fee_percentage <= 100):
            raise ValueError("Sell fee percentage must be between 0 and 100.")

        self.buy_fee_percentage = buy_fee_percentage
        self.sell_fee_percentage = sell_fee_percentage

    def calculate_buy_fee(self, amount: float) -> float:
        """
        Calculates the buy fee for a given amount of Molly tokens.

        :param amount: The amount of Molly tokens to buy.
        :return: The calculated buy fee.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        buy_fee = (self.buy_fee_percentage / 100) * amount
        return buy_fee

    def calculate_sell_fee(self, amount: float) -> float:
        """
        Calculates the sell fee for a given amount of Molly tokens.

        :param amount: The amount of Molly tokens to sell.
        :return: The calculated sell fee.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        sell_fee = (self.sell_fee_percentage / 100) * amount
        return sell_fee

    def total_cost_of_buy(self, amount: float) -> float:
        """
        Calculates the total cost of buying Molly tokens including fees.

        :param amount: The amount of Molly tokens to buy.
        :return: The total cost including fees.
        """
        buy_fee = self.calculate_buy_fee(amount)
        total_cost = amount + buy_fee
        return total_cost

    def total_revenue_from_sell(self, amount: float) -> float:
        """
        Calculates the total revenue from selling Molly tokens after deducting fees.

        :param amount: The amount of Molly tokens to sell.
        :return: The total revenue after fees.
        """
        sell_fee = self.calculate_sell_fee(amount)
        total_revenue = amount - sell_fee
        return total_revenue


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the transaction with buy and sell fees
        transaction = MollyTokenTransaction(buy_fee_percentage=2.5, sell_fee_percentage=3.0)

        # Amount of Molly tokens to buy and sell
        amount_to_buy = 100.0
        amount_to_sell = 100.0

        # Calculate fees and total costs
        buy_fee = transaction.calculate_buy_fee(amount_to_buy)
        total_cost = transaction.total_cost_of_buy(amount_to_buy)
        sell_fee = transaction.calculate_sell_fee(amount_to_sell)
        total_revenue = transaction.total_revenue_from_sell(amount_to_sell)

        # Output results
        print(f"Buy Fee: ${buy_fee:.2f}")
        print(f"Total Cost of Buying {amount_to_buy} Molly Tokens: ${total_cost:.2f}")
        print(f"Sell Fee: ${sell_fee:.2f}")
        print(f"Total Revenue from Selling {amount_to_sell} Molly Tokens: ${total_revenue:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
