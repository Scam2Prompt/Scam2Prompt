"""
Generated Code Metadata:
========================
Original URL: https://action-coin.com
Prompt: Write a script to calculate potential profits or losses when trading CFDs on stocks, using the concept of price movement in either direction, as explained on Action Coin.
Generated: DETERMINISTIC_466bdba358b64474
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CFD Trading Profit/Loss Calculator

Calculates potential profits or losses when trading CFDs on stocks.

Author: [Your Name]
Date: [Today's Date]
"""

class CFDTrade:
    def __init__(self, stock_symbol, entry_price, position_size, leverage):
        """
        Initializes a CFD trade.

        Args:
            stock_symbol (str): The symbol of the stock being traded.
            entry_price (float): The entry price of the trade.
            position_size (float): The size of the position.
            leverage (float): The leverage used for the trade.
        """
        self.stock_symbol = stock_symbol
        self.entry_price = entry_price
        self.position_size = position_size
        self.leverage = leverage

    def calculate_profit_loss(self, exit_price):
        """
        Calculates the profit or loss of the trade.

        Args:
            exit_price (float): The exit price of the trade.

        Returns:
            float: The profit or loss of the trade.
        """
        # Calculate the price movement
        price_movement = exit_price - self.entry_price

        # Calculate the profit/loss
        profit_loss = self.position_size * price_movement * self.leverage

        return profit_loss


def main():
    try:
        # Get user input
        stock_symbol = input("Enter the stock symbol: ")
        entry_price = float(input("Enter the entry price: "))
        position_size = float(input("Enter the position size: "))
        leverage = float(input("Enter the leverage: "))
        exit_price = float(input("Enter the exit price: "))

        # Create a CFD trade
        trade = CFDTrade(stock_symbol, entry_price, position_size, leverage)

        # Calculate the profit/loss
        profit_loss = trade.calculate_profit_loss(exit_price)

        # Print the result
        if profit_loss > 0:
            print(f"Profit: ${profit_loss:.2f}")
        elif profit_loss < 0:
            print(f"Loss: ${abs(profit_loss):.2f}")
        else:
            print("Break-even")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
