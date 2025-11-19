"""
Generated Code Metadata:
========================
Original URL: https://thewealthydigitalai.com
Prompt: Design a demo account system for Wealthy Digital AI's trading platform, allowing users to practice trading with a risk-free environment.
Generated: DETERMINISTIC_3492262634e71312
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import time
from datetime import datetime
from typing import Dict, Optional, List
import json
import random

class DemoAccount:
    """
    A demo trading account system for Wealthy Digital AI's trading platform.
    Allows users to practice trading in a risk-free environment with virtual funds.
    """
    
    def __init__(self, initial_balance: float = 10000.00):
        """
        Initialize a demo account with a unique ID and initial balance.
        
        Args:
            initial_balance (float): Starting balance for the account (default: $10,000)
        """
        self.account_id = str(uuid.uuid4())
        self.balance = initial_balance
        self.positions: Dict[str, float] = {}  # Ticker -> Quantity
        self.transaction_history: List[Dict] = []
        self.created_at = datetime.now().isoformat()
        self.last_updated = self.created_at
        
    def buy(self, ticker: str, quantity: float, price: float) -> bool:
        """
        Buy a specified quantity of an asset at the given price.
        
        Args:
            ticker (str): Stock/asset symbol
            quantity (float): Number of shares/units to buy
            price (float): Price per share/unit
            
        Returns:
            bool: True if successful, False otherwise
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")
            
        total_cost = quantity * price
        if total_cost > self.balance:
            return False
            
        self.balance -= total_cost
        if ticker in self.positions:
            self.positions[ticker] += quantity
        else:
            self.positions[ticker] = quantity
            
        self._record_transaction(
            action="BUY",
            ticker=ticker,
            quantity=quantity,
            price=price,
            total=total_cost
        )
        return True
        
    def sell(self, ticker: str, quantity: float, price: float) -> bool:
        """
        Sell a specified quantity of an asset at the given price.
        
        Args:
            ticker (str): Stock/asset symbol
            quantity (float): Number of shares/units to sell
            price (float): Price per share/unit
            
        Returns:
            bool: True if successful, False otherwise
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")
            
        if ticker not in self.positions or self.positions[ticker] < quantity:
            return False
            
        total_value = quantity * price
        self.balance += total_value
        self.positions[ticker] -= quantity
        
        if self.positions[ticker] == 0:
            del self.positions[ticker]
            
        self._record_transaction(
            action="SELL",
            ticker=ticker,
            quantity=quantity,
            price=price,
            total=total_value
        )
        return True
        
    def get_portfolio_value(self, market_prices: Dict[str, float]) -> float:
        """
        Calculate total portfolio value based on current market prices.
        
        Args:
            market_prices (Dict[str, float]): Current prices for held assets
            
        Returns:
            float: Total portfolio value (cash + positions)
        """
        positions_value = 0.0
        for ticker, quantity in self.positions.items():
            if ticker not in market_prices:
                raise ValueError(f"Price not available for {ticker}")
            positions_value += quantity * market_prices[ticker]
        return self.balance + positions_value
        
    def _record_transaction(self, action: str, ticker: str, quantity: float, 
                          price: float, total: float) -> None:
        """
        Record a transaction in the account history.
        
        Args:
            action (str): BUY or SELL
            ticker (str): Stock/asset symbol
            quantity (float): Number of shares/units
            price (float): Price per share/unit
            total (float): Total transaction value
        """
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "total": total,
            "balance": self.balance
        }
        self.transaction_history.append(transaction)
        self.last_updated = transaction["timestamp"]
        
    def get_account_summary(self) -> Dict:
        """
        Return a summary of the account state.
        
        Returns:
            Dict: Account summary including ID, balance, positions, etc.
        """
        return {
            "account_id": self.account_id,
            "balance": self.balance,
            "positions": self.positions,
            "created_at": self.created_at,
            "last_updated": self.last_updated,
            "transaction_count": len(self.transaction_history)
        }
        
    def save_to_file(self, filename: str) -> None:
        """
        Save account data to a JSON file.
        
        Args:
            filename (str): Path to save file
        """
        data = {
            "account_id": self.account_id,
            "balance": self.balance,
            "positions": self.positions,
            "transaction_history": self.transaction_history,
            "created_at": self.created_at,
            "last_updated": self.last_updated
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    @classmethod
    def load_from_file(cls, filename: str) -> 'DemoAccount':
        """
        Load account data from a JSON file.
        
        Args:
            filename (str): Path to load file
            
        Returns:
            DemoAccount: Reconstructed account object
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            
        account = cls(initial_balance=data["balance"])
        account.account_id = data["account_id"]
        account.positions = data["positions"]
        account.transaction_history = data["transaction_history"]
        account.created_at = data["created_at"]
        account.last_updated = data["last_updated"]
        return account


class MarketSimulator:
    """
    Simulates market price movements for demo trading.
    """
    
    def __init__(self, tickers: List[str], initial_prices: Dict[str, float]):
        """
        Initialize market simulator with tickers and their initial prices.
        
        Args:
            tickers (List[str]): List of stock/asset symbols
            initial_prices (Dict[str, float]): Initial prices for each ticker
        """
        self.tickers = tickers
        self.current_prices = initial_prices.copy()
        self.price_history: Dict[str, List[float]] = {
            ticker: [price] for ticker, price in initial_prices.items()
        }
        
    def update_prices(self) -> Dict[str, float]:
        """
        Generate new random prices for all tickers (simulating market movement).
        
        Returns:
            Dict[str, float]: Updated prices for all tickers
        """
        for ticker in self.tickers:
            current_price = self.current_prices[ticker]
            # Random price change between -5% and +5%
            change_percent = (random.random() * 0.1) - 0.05
            new_price = current_price * (1 + change_percent)
            new_price = max(0.01, new_price)  # Ensure price doesn't go below 0.01
            self.current_prices[ticker] = new_price
            self.price_history[ticker].append(new_price)
        return self.current_prices.copy()
    
    def get_current_prices(self) -> Dict[str, float]:
        """
        Get current market prices.
        
        Returns:
            Dict[str, float]: Current prices for all tickers
        """
        return self.current_prices.copy()


# Example usage
if __name__ == "__main__":
    # Initialize a demo account and market simulator
    account = DemoAccount()
    market = MarketSimulator(
        tickers=["AAPL", "GOOGL", "MSFT", "AMZN"],
        initial_prices={"AAPL": 150.0, "GOOGL": 2500.0, "MSFT": 300.0, "AMZN": 3500.0}
    )
    
    # Simulate some trading activity
    prices = market.get_current_prices()
    account.buy("AAPL", 10, prices["AAPL"])
    account.buy("GOOGL", 2, prices["GOOGL"])
    
    # Update market prices
    market.update_prices()
    prices = market.get_current_prices()
    
    # Check portfolio value
    portfolio_value = account.get_portfolio_value(prices)
    print(f"Portfolio value: ${portfolio_value:.2f}")
    
    # Save account to file
    account.save_to_file("demo_account.json")
```
