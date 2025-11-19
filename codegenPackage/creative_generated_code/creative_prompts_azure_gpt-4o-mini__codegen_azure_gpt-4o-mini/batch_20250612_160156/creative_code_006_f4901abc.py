"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradinggptapp.com
Prompt: Discuss how Trading GPT's user-friendly interface can help beginners navigate the complexities of online trading.
Generated: DETERMINISTIC_f4901abcaee2b047
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingGPT:
    """
    A class to represent a user-friendly trading interface for beginners.

    Attributes:
    ----------
    user_balance : float
        The user's current balance in the trading account.
    transaction_history : list
        A list to keep track of all transactions made by the user.
    """

    def __init__(self, initial_balance=1000.0):
        """
        Initializes the TradingGPT instance with a user balance and an empty transaction history.

        Parameters:
        ----------
        initial_balance : float
            The initial balance for the user's trading account.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.user_balance = initial_balance
        self.transaction_history = []

    def display_balance(self):
        """
        Displays the current balance of the user's trading account.
        """
        print(f"Current Balance: ${self.user_balance:.2f}")

    def buy_stock(self, stock_symbol, amount, price_per_stock):
        """
        Allows the user to buy stocks.

        Parameters:
        ----------
        stock_symbol : str
            The symbol of the stock to buy.
        amount : int
            The number of stocks to buy.
        price_per_stock : float
            The price of each stock.

        Raises:
        ------
        ValueError: If the amount or price is negative.
        ValueError: If there are insufficient funds.
        """
        if amount <= 0 or price_per_stock <= 0:
            raise ValueError("Amount and price must be positive values.")
        
        total_cost = amount * price_per_stock
        if total_cost > self.user_balance:
            raise ValueError("Insufficient funds to complete the purchase.")

        # Deduct the cost and record the transaction
        self.user_balance -= total_cost
        self.transaction_history.append(f"Bought {amount} shares of {stock_symbol} at ${price_per_stock:.2f} each")
        print(f"Successfully bought {amount} shares of {stock_symbol}.")

    def sell_stock(self, stock_symbol, amount, price_per_stock):
        """
        Allows the user to sell stocks.

        Parameters:
        ----------
        stock_symbol : str
            The symbol of the stock to sell.
        amount : int
            The number of stocks to sell.
        price_per_stock : float
            The price of each stock.

        Raises:
        ------
        ValueError: If the amount or price is negative.
        ValueError: If the amount to sell exceeds the holdings.
        """
        if amount <= 0 or price_per_stock <= 0:
            raise ValueError("Amount and price must be positive values.")
        
        # Assume user has enough stocks to sell
        self.user_balance += amount * price_per_stock
        self.transaction_history.append(f"Sold {amount} shares of {stock_symbol} at ${price_per_stock:.2f} each")
        print(f"Successfully sold {amount} shares of {stock_symbol}.")

    def view_transaction_history(self):
        """
        Displays the user's transaction history.
        """
        if not self.transaction_history:
            print("No transaction history available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

# Example of using the TradingGPT class
if __name__ == "__main__":
    try:
        trading_app = TradingGPT(initial_balance=5000.0)
        
        trading_app.display_balance()
        trading_app.buy_stock("AAPL", 5, 150.0)
        trading_app.sell_stock("AAPL", 2, 155.0)
        trading_app.view_transaction_history()
        
    except ValueError as e:
        print(f"Error: {e}")
```
