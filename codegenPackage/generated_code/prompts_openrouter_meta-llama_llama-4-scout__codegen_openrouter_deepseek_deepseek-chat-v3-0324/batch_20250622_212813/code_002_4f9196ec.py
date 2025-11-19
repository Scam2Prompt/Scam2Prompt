"""
Generated Code Metadata:
========================
Original URL: https://astoricrypto.com
Prompt: Develop a risk management plan for a cryptocurrency portfolio, suggesting an investment of only 5-10% of the portfolio per trade and adjusting risk as profits grow.
Generated: DETERMINISTIC_4f9196ecd9401c61
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Optional

class CryptoTradeRiskManager:
    """
    A risk management system for cryptocurrency trading portfolios.
    Manages position sizing based on portfolio percentage and adjusts risk as profits grow.
    """
    
    def __init__(self, initial_portfolio_value: float, max_trade_percentage: float = 0.1):
        """
        Initialize the risk manager.
        
        Args:
            initial_portfolio_value: Starting value of the portfolio in USD
            max_trade_percentage: Maximum percentage of portfolio to risk per trade (default 10%)
        """
        if initial_portfolio_value <= 0:
            raise ValueError("Portfolio value must be positive")
        if not (0.05 <= max_trade_percentage <= 0.1):
            raise ValueError("Trade percentage must be between 5% and 10%")
            
        self.portfolio_value = initial_portfolio_value
        self.max_trade_percentage = max_trade_percentage
        self.trade_history = []
        self.current_profit = 0.0
        
    def calculate_position_size(self, risk_percentage: Optional[float] = None) -> float:
        """
        Calculate the maximum position size for a new trade.
        
        Args:
            risk_percentage: Optional custom risk percentage for this trade
            
        Returns:
            Maximum position size in USD
        """
        if risk_percentage is None:
            risk_percentage = self.max_trade_percentage
            
        if not (0.05 <= risk_percentage <= 0.1):
            raise ValueError("Risk percentage must be between 5% and 10%")
            
        # Dynamic risk adjustment based on profits
        adjusted_percentage = self._adjust_risk_based_on_profits(risk_percentage)
        return self.portfolio_value * adjusted_percentage
    
    def _adjust_risk_based_on_profits(self, base_percentage: float) -> float:
        """
        Adjust risk percentage based on current profits.
        
        Args:
            base_percentage: The base risk percentage
            
        Returns:
            Adjusted risk percentage
        """
        if self.current_profit > 0:
            # Scale risk proportionally to profits (capped at base percentage)
            profit_factor = min(1.0, self.current_profit / self.portfolio_value)
            return base_percentage * (1 + profit_factor)
        return base_percentage
    
    def record_trade(self, amount: float, profit: float):
        """
        Record a completed trade and update portfolio value.
        
        Args:
            amount: The size of the trade in USD
            profit: Profit/loss from the trade in USD
        """
        if amount <= 0:
            raise ValueError("Trade amount must be positive")
            
        self.trade_history.append({
            'amount': amount,
            'profit': profit,
            'portfolio_value': self.portfolio_value
        })
        
        self.portfolio_value += profit
        self.current_profit = max(0, self.current_profit + profit)
    
    def get_trade_history(self) -> pd.DataFrame:
        """
        Get the complete trade history as a pandas DataFrame.
        
        Returns:
            DataFrame containing all recorded trades
        """
        return pd.DataFrame(self.trade_history)
    
    def get_portfolio_summary(self) -> Dict[str, float]:
        """
        Get current portfolio summary statistics.
        
        Returns:
            Dictionary containing portfolio metrics
        """
        return {
            'current_value': self.portfolio_value,
            'total_profit': sum(t['profit'] for t in self.trade_history),
            'current_risk_percentage': self._adjust_risk_based_on_profits(self.max_trade_percentage),
            'num_trades': len(self.trade_history)
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with $10,000 portfolio
        risk_manager = CryptoTradeRiskManager(initial_portfolio_value=10000.0)
        
        # Calculate position size for a new trade
        position_size = risk_manager.calculate_position_size()
        print(f"Recommended position size: ${position_size:.2f}")
        
        # Simulate a winning trade
        risk_manager.record_trade(amount=position_size, profit=500.0)
        
        # Check new position size after profit
        new_position_size = risk_manager.calculate_position_size()
        print(f"New recommended position size after profit: ${new_position_size:.2f}")
        
        # Get portfolio summary
        summary = risk_manager.get_portfolio_summary()
        print("\nPortfolio Summary:")
        for k, v in summary.items():
            print(f"{k.replace('_', ' ').title()}: {v if isinstance(v, int) else f'${v:.2f}'}")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
