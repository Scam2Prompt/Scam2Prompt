"""
Generated Code Metadata:
========================
Original URL: https://algobitmarket.com
Prompt: Write a function to calculate spreads and leverage for AlgoBitMarket's BASIC and PREMIUM account types based on the provided trading conditions.
Generated: DETERMINISTIC_5720da3905f2b783
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AlgoBitMarket:
    """
    A class to represent the AlgoBitMarket trading platform.
    """

    def __init__(self, account_type: str):
        """
        Initializes the AlgoBitMarket instance with the specified account type.

        :param account_type: The type of account ('BASIC' or 'PREMIUM').
        """
        if account_type not in ['BASIC', 'PREMIUM']:
            raise ValueError("Account type must be 'BASIC' or 'PREMIUM'.")
        self.account_type = account_type

    def calculate_spread(self, bid_price: float, ask_price: float) -> float:
        """
        Calculates the spread between the bid and ask prices.

        :param bid_price: The highest price a buyer is willing to pay.
        :param ask_price: The lowest price a seller is willing to accept.
        :return: The spread as a float.
        """
        if bid_price < 0 or ask_price < 0:
            raise ValueError("Bid and ask prices must be non-negative.")
        spread = ask_price - bid_price
        return spread

    def calculate_leverage(self, margin: float) -> float:
        """
        Calculates the leverage based on the account type and margin.

        :param margin: The amount of capital used to open a position.
        :return: The leverage as a float.
        """
        if margin <= 0:
            raise ValueError("Margin must be a positive value.")
        
        leverage = 0
        if self.account_type == 'BASIC':
            leverage = 2  # Example leverage for BASIC account
        elif self.account_type == 'PREMIUM':
            leverage = 5  # Example leverage for PREMIUM account
        
        return leverage

    def calculate_spread_and_leverage(self, bid_price: float, ask_price: float, margin: float):
        """
        Calculates both the spread and leverage based on the provided trading conditions.

        :param bid_price: The highest price a buyer is willing to pay.
        :param ask_price: The lowest price a seller is willing to accept.
        :param margin: The amount of capital used to open a position.
        :return: A dictionary containing the spread and leverage.
        """
        spread = self.calculate_spread(bid_price, ask_price)
        leverage = self.calculate_leverage(margin)
        
        return {
            'spread': spread,
            'leverage': leverage
        }


# Example usage:
if __name__ == "__main__":
    try:
        account = AlgoBitMarket('PREMIUM')
        result = account.calculate_spread_and_leverage(bid_price=100.0, ask_price=105.0, margin=1000.0)
        print(f"Spread: {result['spread']}, Leverage: {result['leverage']}")
    except ValueError as e:
        print(f"Error: {e}")
```
