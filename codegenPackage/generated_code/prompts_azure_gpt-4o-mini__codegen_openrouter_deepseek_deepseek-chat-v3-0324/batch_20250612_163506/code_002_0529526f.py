"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Write a Python function that simulates trading scenarios based on the ethical conduct and professional quality principles emphasized by GCap Markets.
Generated: DETERMINISTIC_0529526fa98f13fd
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, Tuple, Optional

class TradingSimulator:
    """
    Simulates trading scenarios based on ethical conduct and professional quality principles.
    
    Attributes:
        balance (float): Current account balance.
        positions (Dict[str, int]): Dictionary holding current positions (ticker: quantity).
        ethical_score (int): Score representing adherence to ethical conduct (0-100).
        professional_score (int): Score representing adherence to professional quality (0-100).
        transaction_history (list): List of all transactions performed.
    """
    
    def __init__(self, initial_balance: float = 100000.0):
        """
        Initialize the trading simulator with an initial balance.
        
        Args:
            initial_balance (float): Starting balance for the simulation. Defaults to 100000.0.
        """
        self.balance = initial_balance
        self.positions: Dict[str, int] = {}
        self.ethical_score = 100  # Start with perfect ethical score
        self.professional_score = 100  # Start with perfect professional score
        self.transaction_history = []
    
    def execute_trade(self, ticker: str, quantity: int, price: float, is_buy: bool) -> Tuple[bool, str]:
        """
        Execute a trade while considering ethical and professional principles.
        
        Args:
            ticker (str): Stock ticker symbol.
            quantity (int): Number of shares to trade.
            price (float): Price per share.
            is_buy (bool): True for buy, False for sell.
            
        Returns:
            Tuple[bool, str]: (success, message) indicating if trade was successful and a message.
        """
        try:
            # Validate inputs
            if not isinstance(ticker, str) or not ticker.isalpha():
                return False, "Invalid ticker symbol"
            if quantity <= 0:
                return False, "Quantity must be positive"
            if price <= 0:
                return False, "Price must be positive"
            
            # Check for ethical violations (simulated)
            if random.random() < 0.05:  # 5% chance of ethical violation
                self.ethical_score = max(0, self.ethical_score - 10)
                return False, "Trade rejected due to potential ethical violation"
            
            # Check for professional quality (simulated)
            if random.random() < 0.03:  # 3% chance of professional lapse
                self.professional_score = max(0, self.professional_score - 5)
                return False, "Trade rejected due to professional standards concern"
            
            # Calculate total cost/proceeds
            total = quantity * price
            
            if is_buy:
                if total > self.balance:
                    return False, "Insufficient funds"
                self.balance -= total
                self.positions[ticker] = self.positions.get(ticker, 0) + quantity
            else:
                if ticker not in self.positions or self.positions[ticker] < quantity:
                    return False, "Insufficient shares to sell"
                self.balance += total
                self.positions[ticker] -= quantity
                if self.positions[ticker] == 0:
                    del self.positions[ticker]
            
            # Record transaction
            transaction = {
                'ticker': ticker,
                'quantity': quantity,
                'price': price,
                'is_buy': is_buy,
                'timestamp': self._get_current_timestamp()
            }
            self.transaction_history.append(transaction)
            
            return True, "Trade executed successfully"
        
        except Exception as e:
            return False, f"Error executing trade: {str(e)}"
    
    def get_portfolio_value(self, market_prices: Dict[str, float]) -> Optional[float]:
        """
        Calculate total portfolio value based on current positions and market prices.
        
        Args:
            market_prices (Dict[str, float]): Current market prices for held positions.
            
        Returns:
            Optional[float]: Total portfolio value or None if calculation fails.
        """
        try:
            position_value = sum(
                quantity * market_prices.get(ticker, 0.0)
                for ticker, quantity in self.positions.items()
            )
            return self.balance + position_value
        except Exception:
            return None
    
    def get_performance_metrics(self) -> Dict[str, float]:
        """
        Get current performance metrics including ethical and professional scores.
        
        Returns:
            Dict[str, float]: Dictionary of performance metrics.
        """
        return {
            'balance': self.balance,
            'ethical_score': self.ethical_score,
            'professional_score': self.professional_score,
            'positions_count': len(self.positions),
            'transaction_count': len(self.transaction_history)
        }
    
    def _get_current_timestamp(self) -> str:
        """
        Generate a simulated timestamp for transactions.
        
        Returns:
            str: Formatted timestamp string.
        """
        from datetime import datetime
        return datetime.now().isoformat()
    
    def __repr__(self) -> str:
        return f"TradingSimulator(balance={self.balance}, positions={len(self.positions)})"
```
