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
class MollyTokenTransaction:
    def __init__(self, buy_fee_percent: float, sell_fee_percent: float):
        """
        Initialize the MollyTokenTransaction class with the defined buy and sell fees.

        :param buy_fee_percent: The fee percentage for buying Molly tokens (in decimal).
        :param sell_fee_percent: The fee percentage for selling Molly tokens (in decimal).
        """
        if not (0 <= buy_fee_percent < 1) or not (0 <= sell_fee_percent < 1):
            raise ValueError("Fees must be between 0 and 1 (inclusive of 0, exclusive of 1).")

        self.buy_fee_percent = buy_fee_percent
        self.sell_fee_percent = sell_fee_percent

    def calculate_buy_fee(self, amount: float) -> float:
        """
        Calculate the buy fee based on the provided amount of Molly tokens.

        :param amount: The amount of Molly tokens being purchased.
        :return: The calculated buy fee.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")
        
        buy_fee = amount * self.buy_fee_percent
        return buy_fee

    def calculate_sell_fee(self, amount: float) -> float:
        """
        Calculate the sell fee based on the provided amount of Molly tokens.

        :param amount: The amount of Molly tokens being sold.
        :return: The calculated sell fee.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")

        sell_fee = amount * self.sell_fee_percent
        return sell_fee

    def total_cost_of_buy(self, amount: float) -> float:
        """
        Calculate the total cost when buying Molly tokens, including fees.

        :param amount: The amount of Molly tokens being purchased.
        :return: The total cost including fees.
        """
        fee = self.calculate_buy_fee(amount)
        total_cost = amount + fee
        return total_cost

    def total_amount_received_from_sell(self, amount: float) -> float:
        """
        Calculate the total amount received when selling Molly tokens, after fees.

        :param amount: The amount of Molly tokens being sold.
        :return: The total amount received after deducting fees.
        """
        fee = self.calculate_sell_fee(amount)
        total_received = amount - fee
        return total_received


# Example usage:
if __name__ == "__main__":
    try:
        # Set up the transaction with fees (e.g., 2% buy fee and 1.5% sell fee)
        transaction = MollyTokenTransaction(buy_fee_percent=0.02, sell_fee_percent=0.015)

        # Example amounts
        amount_to_buy = 1000  # Number of tokens to buy
        amount_to_sell = 500   # Number of tokens to sell

        # Calculate and print fees and totals
        buy_fee = transaction.calculate_buy_fee(amount_to_buy)
        print(f"Buy Fee for {amount_to_buy} Molly tokens: ${buy_fee:.2f}")

        total_cost = transaction.total_cost_of_buy(amount_to_buy)
        print(f"Total cost for {amount_to_buy} Molly tokens (including fee): ${total_cost:.2f}")

        sell_fee = transaction.calculate_sell_fee(amount_to_sell)
        print(f"Sell Fee for {amount_to_sell} Molly tokens: ${sell_fee:.2f}")

        total_received = transaction.total_amount_received_from_sell(amount_to_sell)
        print(f"Total received from selling {amount_to_sell} Molly tokens (after fee): ${total_received:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
