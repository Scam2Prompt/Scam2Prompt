"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradegptapp.com
Prompt: Create a script that simulates TradeGPT's risk-free demo mode, allowing users to test trading strategies without financial risk.
Generated: DETERMINISTIC_c4c546cc7e4ccfe3
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class TradeGPTDemoMode:
    """
    A class to simulate a risk-free demo mode for testing trading strategies.
    This allows users to trade virtual assets without financial risk.
    """

    def __init__(self, starting_balance=10000):
        """
        Initializes the demo trading session.
        
        Args:
            starting_balance (float): The initial virtual balance for the user.
        """
        self.balance = starting_balance
        self.portfolio = {}
        self.trade_history = []
        self.market_data = self._generate_mock_market_data()

    def _generate_mock_market_data(self):
        """
        Generates mock market data for simulation purposes.
        
        Returns:
            dict: Mock market prices for various assets.
        """
        return {
            "AAPL": random.uniform(100, 200),
            "TSLA": random.uniform(200, 300),
            "GOOG": random.uniform(2500, 3000),
            "BTC": random.uniform(20000, 60000),
            "ETH": random.uniform(1000, 4000),
        }

    def get_market_data(self):
        """
        Fetches the latest mock market data.
        
        Returns:
            dict: Current mock prices of assets.
        """
        return self.market_data

    def buy_asset(self, symbol, amount):
        """
        Simulates purchasing an asset.

        Args:
            symbol (str): The asset to purchase (e.g., "AAPL", "BTC").
            amount (float): The amount in dollars to spend on the asset.

        Returns:
            str: Result of the transaction.
        """
        if symbol not in self.market_data:
            return f"Error: Asset {symbol} not found."

        price = self.market_data[symbol]
        quantity = amount / price

        if self.balance >= amount:
            self.balance -= amount
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
            self.trade_history.append(
                {"action": "buy", "symbol": symbol, "amount": amount, "quantity": quantity, "price": price}
            )
            return f"Purchased {quantity:.4f} {symbol} at ${price:.2f}."
        else:
            return "Error: Insufficient balance."

    def sell_asset(self, symbol, quantity):
        """
        Simulates selling an asset.

        Args:
            symbol (str): The asset to sell (e.g., "AAPL", "BTC").
            quantity (float): The amount of the asset to sell.

        Returns:
            str: Result of the transaction.
        """
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            return f"Error: Insufficient {symbol} in portfolio."

        price = self.market_data[symbol]
        amount = quantity * price

        self.portfolio[symbol] -= quantity
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
        self.balance += amount
        self.trade_history.append(
            {"action": "sell", "symbol": symbol, "quantity": quantity, "amount": amount, "price": price}
        )
        return f"Sold {quantity:.4f} {symbol} at ${price:.2f}."

    def get_portfolio(self):
        """
        Retrieves the current portfolio of the user.
        
        Returns:
            dict: The user's virtual portfolio.
        """
        return self.portfolio

    def get_balance(self):
        """
        Retrieves the current balance of the user.
        
        Returns:
            float: The user's virtual balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Retrieves the user's trade history.

        Returns:
            list: List of past transactions.
        """
        return self.trade_history

    def save_session(self, file_name="trade_demo_session.json"):
        """
        Saves the trading session data to a JSON file.

        Args:
            file_name (str): The name of the file to save the session data.
        """
        session_data = {
            "balance": self.balance,
            "portfolio": self.portfolio,
            "trade_history": self.trade_history,
        }
        with open(file_name, "w") as file:
            json.dump(session_data, file, indent=4)

    def load_session(self, file_name="trade_demo_session.json"):
        """
        Loads trading session data from a JSON file.

        Args:
            file_name (str): The name of the file to load session data.
        """
        try:
            with open(file_name, "r") as file:
                session_data = json.load(file)
                self.balance = session_data["balance"]
                self.portfolio = session_data["portfolio"]
                self.trade_history = session_data["trade_history"]
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Starting a new session.")

# -------------------------
# Example usage:
# -------------------------
if __name__ == "__main__":
    # Initialize demo mode with a virtual balance of $10,000
    demo = TradeGPTDemoMode()

    # Display market data
    print("Current Market Data:")
    print(demo.get_market_data())

    # Perform a buy trade
    print(demo.buy_asset("AAPL", 5000))

    # Perform a sell trade
    print(demo.sell_asset("AAPL", 10))

    # View portfolio and balance
    print("Portfolio:", demo.get_portfolio())
    print("Balance:", demo.get_balance())

    # Save the session
    demo.save_session()

    # Load session
    demo.load_session()
    print("Session loaded successfully!")
```
