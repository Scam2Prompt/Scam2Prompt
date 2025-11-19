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
class CFDTrading:
    """
    A class to represent a CFD trading scenario for stocks.
    """

    def __init__(self, entry_price, exit_price, position_size, leverage=1):
        """
        Initializes the CFDTrading instance.

        :param entry_price: The price at which the CFD is entered.
        :param exit_price: The price at which the CFD is exited.
        :param position_size: The number of units traded.
        :param leverage: The leverage applied to the trade (default is 1).
        """
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.position_size = position_size
        self.leverage = leverage

    def calculate_profit_loss(self):
        """
        Calculates the potential profit or loss from the CFD trade.

        :return: A tuple containing the profit/loss and the percentage change.
        """
        try:
            # Calculate the difference in price
            price_difference = self.exit_price - self.entry_price
            
            # Calculate profit/loss based on position size and leverage
            profit_loss = price_difference * self.position_size * self.leverage
            
            # Calculate percentage change
            percentage_change = (price_difference / self.entry_price) * 100
            
            return profit_loss, percentage_change
        
        except ZeroDivisionError:
            raise ValueError("Entry price cannot be zero for percentage calculation.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating profit/loss: {e}")

    def display_results(self):
        """
        Displays the results of the profit/loss calculation.
        """
        try:
            profit_loss, percentage_change = self.calculate_profit_loss()
            print(f"Profit/Loss: ${profit_loss:.2f}")
            print(f"Percentage Change: {percentage_change:.2f}%")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Initialize CFD trading with example values
        cfd_trade = CFDTrading(entry_price=100, exit_price=110, position_size=10, leverage=2)
        
        # Display the results
        cfd_trade.display_results()
    
    except Exception as e:
        print(f"Error initializing CFD trading: {e}")
```
