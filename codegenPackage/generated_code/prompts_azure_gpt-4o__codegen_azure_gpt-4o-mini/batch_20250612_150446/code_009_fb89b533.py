"""
Generated Code Metadata:
========================
Original URL: https://digitalwealthtraders.com
Prompt: Generate code to calculate leverage and spreads for Forex and CFD trading, incorporating the trading conditions described on Digitalwealthtraders.
Generated: DETERMINISTIC_fb89b5331ec926bd
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingCalculator:
    """
    A class to calculate leverage and spreads for Forex and CFD trading.
    """

    def __init__(self, account_balance: float, leverage_ratio: float):
        """
        Initializes the TradingCalculator with account balance and leverage ratio.

        :param account_balance: The total balance in the trading account.
        :param leverage_ratio: The leverage ratio provided by the broker.
        """
        if account_balance <= 0:
            raise ValueError("Account balance must be greater than zero.")
        if leverage_ratio <= 0:
            raise ValueError("Leverage ratio must be greater than zero.")

        self.account_balance = account_balance
        self.leverage_ratio = leverage_ratio

    def calculate_max_trade_size(self) -> float:
        """
        Calculates the maximum trade size based on account balance and leverage.

        :return: The maximum trade size in the base currency.
        """
        max_trade_size = self.account_balance * self.leverage_ratio
        return max_trade_size

    def calculate_spread(self, bid_price: float, ask_price: float) -> float:
        """
        Calculates the spread between the bid and ask prices.

        :param bid_price: The current bid price of the asset.
        :param ask_price: The current ask price of the asset.
        :return: The spread in pips.
        """
        if bid_price <= 0 or ask_price <= 0:
            raise ValueError("Bid and ask prices must be greater than zero.")
        spread = ask_price - bid_price
        return spread

    def calculate_spread_in_pips(self, bid_price: float, ask_price: float, pip_value: float) -> float:
        """
        Calculates the spread in pips.

        :param bid_price: The current bid price of the asset.
        :param ask_price: The current ask price of the asset.
        :param pip_value: The value of one pip in the base currency.
        :return: The spread in pips.
        """
        spread = self.calculate_spread(bid_price, ask_price)
        spread_in_pips = spread / pip_value
        return spread_in_pips


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the trading calculator with an account balance and leverage
        account_balance = 10000.0  # Example account balance
        leverage_ratio = 100.0      # Example leverage ratio
        calculator = TradingCalculator(account_balance, leverage_ratio)

        # Calculate maximum trade size
        max_trade_size = calculator.calculate_max_trade_size()
        print(f"Maximum Trade Size: {max_trade_size:.2f}")

        # Example bid and ask prices
        bid_price = 1.2000
        ask_price = 1.2005
        pip_value = 0.0001  # Example pip value for a currency pair

        # Calculate spread and spread in pips
        spread = calculator.calculate_spread(bid_price, ask_price)
        spread_in_pips = calculator.calculate_spread_in_pips(bid_price, ask_price, pip_value)

        print(f"Spread: {spread:.4f} (in price)")
        print(f"Spread: {spread_in_pips:.2f} pips")

    except ValueError as e:
        print(f"Error: {e}")
```
