"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signalsx.com
Prompt: Create a program to simulate the Swiss Franc shock of 2015, modeling the risks of overleveraging in forex trading as described by SignalsX.
Generated: DETERMINISTIC_327727bc748e9474
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to simulate the Swiss Franc shock of 2015, modeling the risks of overleveraging in forex trading.
This program calculates the impact of a sudden currency appreciation on traders with leveraged positions.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import random

class ForexTrader:
    """
    Class representing a forex trader, including their account balance, leverage, and trade details.
    """
    def __init__(self, name: str, account_balance: float, leverage: float):
        """
        Initialize a ForexTrader instance.
        
        :param name: Name of the trader.
        :param account_balance: Initial account balance in USD.
        :param leverage: Leverage ratio (e.g., 10 for 10:1 leverage).
        """
        self.name = name
        self.account_balance = account_balance
        self.leverage = leverage
        self.position = None  # Represents the trader's current trading position (None if no active trade)

    def open_position(self, opening_price: float, position_size: float):
        """
        Open a leveraged trading position.
        
        :param opening_price: The price at which the position is opened.
        :param position_size: Size of the position (in terms of base currency).
        """
        if position_size * self.leverage > self.account_balance:
            raise ValueError("Insufficient balance to open the position with the specified leverage.")
        
        self.position = {
            'opening_price': opening_price,
            'size': position_size
        }
        print(f"{self.name} opened a position: {self.position}")

    def close_position(self, closing_price: float):
        """
        Close the current trading position and calculate profit/loss.
        
        :param closing_price: The price at which the position is closed.
        """
        if not self.position:
            raise ValueError("No active position to close.")
        
        opening_price = self.position['opening_price']
        position_size = self.position['size']
        price_change = closing_price - opening_price
        profit_loss = price_change * position_size * self.leverage
        
        self.account_balance += profit_loss
        print(f"{self.name} closed the position. Profit/Loss: {profit_loss:.2f} USD")
        
        # Reset position
        self.position = None

    def __str__(self):
        return f"Trader {self.name}: Balance = {self.account_balance:.2f} USD, Leverage = {self.leverage}"


def simulate_swiss_franc_shock(traders):
    """
    Simulate the Swiss Franc shock of 2015, where the price of CHF/USD skyrockets unexpectedly.
    
    :param traders: List of ForexTrader instances to simulate the shock for.
    """
    print("Simulating Swiss Franc shock...")
    
    initial_price = 1.20  # Initial CHF/USD price before the shock
    shock_price = 0.88    # Price after the shock
    
    for trader in traders:
        try:
            # Randomly determine position size for each trader
            position_size = random.uniform(1000, 5000)  # Position size in CHF
            
            # Trader opens a position before the shock
            trader.open_position(opening_price=initial_price, position_size=position_size)
            
            # Trader closes the position after the shock
            trader.close_position(closing_price=shock_price)
            
            print(trader)
        except Exception as e:
            print(f"Error for {trader.name}: {e}")
            print(f"{trader.name} balance might be wiped out due to overleveraging.")


def main():
    """
    Main function to execute the simulation.
    """
    print("Swiss Franc Shock Simulation - Forex Trading Risk Model\n")
    
    # Create a list of traders with varying account balances and leverage ratios
    traders = [
        ForexTrader("Alice", account_balance=10000, leverage=10),
        ForexTrader("Bob", account_balance=5000, leverage=20),
        ForexTrader("Charlie", account_balance=20000, leverage=15),
    ]
    
    # Run the simulation
    simulate_swiss_franc_shock(traders)


if __name__ == "__main__":
    main()
```
