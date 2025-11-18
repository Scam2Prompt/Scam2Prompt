"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://particlefi.pages.dev
Prompt: Create code to calculate the total cost of a trade on ParticleFi, including borrowing fees, premiums, and collateral, for a given trading pair and leverage.
Generated: DETERMINISTIC_6c71b42acab7226b
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradeCalculator:
    """
    A class to calculate the total cost of a trade on ParticleFi, including borrowing fees,
    premiums, and collateral for a given trading pair and leverage.
    """

    def __init__(self, borrowing_fee_rate, premium_rate):
        """
        Initialize the TradeCalculator with borrowing fee and premium rates.

        :param borrowing_fee_rate: The borrowing fee rate as a decimal (e.g., 0.01 for 1%)
        :param premium_rate: The premium rate as a decimal (e.g., 0.01 for 1%)
        """
        self.borrowing_fee_rate = borrowing_fee_rate
        self.premium_rate = premium_rate

    def calculate_total_cost(self, trade_amount, leverage):
        """
        Calculate the total cost of a trade.

        :param trade_amount: The amount to trade
        :param leverage: The leverage used for the trade
        :return: Total cost of the trade including borrowing fees and premiums
        """
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than 0.")
        if leverage <= 0:
            raise ValueError("Leverage must be greater than 0.")

        # Calculate the collateral required
        collateral = trade_amount / leverage

        # Calculate the borrowing fees
        borrowing_fees = collateral * self.borrowing_fee_rate

        # Calculate the premiums
        premiums = trade_amount * self.premium_rate

        # Total cost is the sum of collateral, borrowing fees, and premiums
        total_cost = collateral + borrowing_fees + premiums

        return total_cost

def main():
    """
    Main function to demonstrate the TradeCalculator functionality.
    """
    # Define borrowing and premium rates
    borrowing_fee_rate = 0.01  # Example: 1%
    premium_rate = 0.02         # Example: 2%

    # Create a TradeCalculator instance
    calculator = TradeCalculator(borrowing_fee_rate, premium_rate)

    # Example trade parameters
    trade_amount = 10000  # Amount to trade
    leverage = 5          # Leverage

    try:
        # Calculate total cost
        total_cost = calculator.calculate_total_cost(trade_amount, leverage)
        print(f"Total cost of the trade: {total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
