"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gcapmarkets.com
Prompt: Write a Python function that simulates trading scenarios based on the ethical conduct and professional quality principles emphasized by GCap Markets.
Generated: DETERMINISTIC_0529526fa98f13fd
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Tuple

class Trade:
    """
    A class to represent a trade scenario.
    """

    def __init__(self, asset: str, price: float):
        """
        Initializes a trade with an asset and its price.
        
        :param asset: The name of the asset being traded.
        :param price: The price of the asset.
        """
        self.asset = asset
        self.price = price

    def __str__(self) -> str:
        """
        Returns a string representation of the trade.
        
        :return: A string describing the trade.
        """
        return f"Trade(asset={self.asset}, price={self.price})"


def simulate_trading_scenario(num_trades: int) -> List[Trade]:
    """
    Simulates a trading scenario by generating a list of trades.
    
    :param num_trades: The number of trades to simulate.
    :return: A list of Trade objects.
    :raises ValueError: If num_trades is less than or equal to zero.
    """
    if num_trades <= 0:
        raise ValueError("Number of trades must be greater than zero.")
    
    assets = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    trades = []
    
    for _ in range(num_trades):
        asset = random.choice(assets)
        price = round(random.uniform(100, 1500), 2)  # Prices between $100 and $1500
        trade = Trade(asset, price)
        trades.append(trade)

    return trades


def main():
    """
    Main function to run the trading simulation.
    """
    try:
        num_trades = int(input("Enter the number of trades to simulate: "))
        trades = simulate_trading_scenario(num_trades)
        
        print("\nSimulated Trades:")
        for trade in trades:
            print(trade)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
