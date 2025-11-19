"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradegptapp.com
Prompt: Describe how to set up a risk-free demo mode with TradeGPT to test trading strategies before investing real money.
Generated: DETERMINISTIC_ee8531bad34d2c2a
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TradeGPTDemoMode:
    """
    A class to simulate a risk-free demo trading environment for testing strategies.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the demo mode with a virtual balance.
        
        :param initial_balance: Starting virtual balance for the demo account.
        """
        self.virtual_balance = initial_balance
        self.trade_history = []

    def simulate_trade(self, trade_type, amount, price):
        """
        Simulates a trade in demo mode.

        :param trade_type: Type of trade, either "buy" or "sell".
        :param amount: The quantity of the asset being traded.
        :param price: The price per unit of the asset.
        :return: Success message or error.
        """
        try:
            if trade_type not in ["buy", "sell"]:
                raise ValueError("Invalid trade type. Must be 'buy' or 'sell'.")
            
            # Calculate transaction cost
            transaction_cost = amount * price

            if trade_type == "buy":
                # Check if there are sufficient funds
                if self.virtual_balance < transaction_cost:
                    raise ValueError("Insufficient funds to execute the trade.")
                self.virtual_balance -= transaction_cost
            elif trade_type == "sell":
                # Simulate profit/loss for a sale (randomized for demo purposes)
                profit_or_loss = random.uniform(-0.1, 0.1)  # Random +/- 10%
                transaction_cost += transaction_cost * profit_or_loss
                self.virtual_balance += transaction_cost

            # Record the trade in history
            trade_record = {
                "type": trade_type,
                "amount": amount,
                "price": price,
                "transaction_cost": transaction_cost,
                "balance_after_trade": self.virtual_balance
            }
            self.trade_history.append(trade_record)
            return f"Trade executed: {trade_record}"

        except ValueError as e:
            return f"Error executing trade: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def get_trade_history(self):
        """
        Returns the trade history.
        
        :return: List of all executed trades.
        """
        return self.trade_history

    def get_virtual_balance(self):
        """
        Returns the current virtual balance in demo mode.
        
        :return: Current virtual balance.
        """
        return self.virtual_balance


# Example usage
if __name__ == "__main__":
    # Initialize the demo mode with a $10,000 virtual balance
    demo_account = TradeGPTDemoMode(initial_balance=10000)

    # Simulate trades
    print(demo_account.simulate_trade("buy", 50, 100))  # Buy 50 units at $100 each
    print(demo_account.simulate_trade("sell", 30, 120))  # Sell 30 units at $120 each

    # Get the virtual balance after trades
    print(f"Virtual Balance: ${demo_account.get_virtual_balance()}")

    # Get the trade history
    print("Trade History:")
    for trade in demo_account.get_trade_history():
        print(trade)
```
