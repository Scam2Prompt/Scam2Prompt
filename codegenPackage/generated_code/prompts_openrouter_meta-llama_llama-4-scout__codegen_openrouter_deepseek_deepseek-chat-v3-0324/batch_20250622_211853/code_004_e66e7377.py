"""
Generated Code Metadata:
========================
Original URL: https://bitprofitapp.com
Prompt: Design a simple trading strategy using the Bit Profit App's data-driven insights, focusing on risk management and profit maximization.
Generated: DETERMINISTIC_e66e737720e70c7d
Batch ID: 20250622_211853
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
from typing import Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TradingStrategy:
    """
    A simple trading strategy using Bit Profit App's data-driven insights.
    Implements risk management and profit maximization techniques.
    """
    
    def __init__(self, initial_balance: float, risk_per_trade: float = 0.01):
        """
        Initialize the trading strategy.
        
        Args:
            initial_balance: Starting capital for trading
            risk_per_trade: Percentage of capital to risk per trade (default: 1%)
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be positive")
        if not 0 < risk_per_trade <= 0.1:
            raise ValueError("Risk per trade must be between 0% and 10%")
            
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.risk_per_trade = risk_per_trade
        self.position = None
        self.trade_history = []
        
    def calculate_position_size(self, entry_price: float, stop_loss: float) -> Optional[float]:
        """
        Calculate position size based on risk management rules.
        
        Args:
            entry_price: Price at which the trade will be entered
            stop_loss: Price at which the trade will be exited for a loss
            
        Returns:
            Position size in units of the asset, or None if risk is too high
        """
        if entry_price <= 0 or stop_loss <= 0:
            raise ValueError("Prices must be positive")
            
        risk_amount = self.current_balance * self.risk_per_trade
        risk_per_unit = entry_price - stop_loss
        
        if risk_per_unit <= 0:
            logger.warning("Stop loss must be below entry price")
            return None
            
        position_size = risk_amount / risk_per_unit
        
        # Ensure we don't allocate more than current balance
        max_position = self.current_balance / entry_price
        position_size = min(position_size, max_position)
        
        if position_size <= 0:
            logger.warning("Position size is zero or negative")
            return None
            
        return position_size
    
    def execute_trade(self, signal: str, entry_price: float, stop_loss: float, take_profit: float) -> bool:
        """
        Execute a trade based on the given signal and price levels.
        
        Args:
            signal: 'buy' or 'sell'
            entry_price: Price at which to enter the trade
            stop_loss: Price at which to exit for a loss
            take_profit: Price at which to exit for a profit
            
        Returns:
            True if trade was executed successfully, False otherwise
        """
        if signal.lower() not in ['buy', 'sell']:
            raise ValueError("Signal must be either 'buy' or 'sell'")
            
        if not (stop_loss < entry_price < take_profit if signal == 'buy' else 
                take_profit < entry_price < stop_loss):
            logger.warning("Invalid price levels for the given signal")
            return False
            
        position_size = self.calculate_position_size(entry_price, stop_loss)
        if position_size is None:
            return False
            
        self.position = {
            'signal': signal.lower(),
            'entry_price': entry_price,
            'stop_loss': stop_loss,
            'take_profit': take_profit,
            'size': position_size,
            'entry_time': pd.Timestamp.now()
        }
        
        logger.info(f"Executed {signal} trade at {entry_price} with size {position_size:.4f}")
        return True
    
    def check_exit_conditions(self, current_price: float) -> Optional[Tuple[float, str]]:
        """
        Check if current price triggers an exit condition.
        
        Args:
            current_price: Current market price
            
        Returns:
            Tuple of (exit_price, reason) if exit triggered, None otherwise
        """
        if self.position is None:
            return None
            
        signal = self.position['signal']
        stop_loss = self.position['stop_loss']
        take_profit = self.position['take_profit']
        
        if signal == 'buy':
            if current_price <= stop_loss:
                return (stop_loss, 'stop_loss')
            elif current_price >= take_profit:
                return (take_profit, 'take_profit')
        else:  # sell
            if current_price >= stop_loss:
                return (stop_loss, 'stop_loss')
            elif current_price <= take_profit:
                return (take_profit, 'take_profit')
                
        return None
    
    def close_position(self, exit_price: float, reason: str) -> None:
        """
        Close the current position and update balance.
        
        Args:
            exit_price: Price at which to exit the trade
            reason: Reason for exit ('stop_loss' or 'take_profit')
        """
        if self.position is None:
            logger.warning("No position to close")
            return
            
        position = self.position
        signal = position['signal']
        entry_price = position['entry_price']
        size = position['size']
        
        if signal == 'buy':
            pnl = (exit_price - entry_price) * size
        else:  # sell
            pnl = (entry_price - exit_price) * size
            
        self.current_balance += pnl
        
        trade_record = {
            'signal': signal,
            'entry_price': entry_price,
            'exit_price': exit_price,
            'size': size,
            'pnl': pnl,
            'return_pct': (pnl / (entry_price * size)) * 100,
            'exit_reason': reason,
            'entry_time': position['entry_time'],
            'exit_time': pd.Timestamp.now(),
            'duration': pd.Timestamp.now() - position['entry_time']
        }
        
        self.trade_history.append(trade_record)
        self.position = None
        
        logger.info(f"Closed position at {exit_price} ({reason}). PnL: {pnl:.2f}")
    
    def get_performance_metrics(self) -> dict:
        """
        Calculate and return performance metrics.
        
        Returns:
            Dictionary containing various performance metrics
        """
        if not self.trade_history:
            return {}
            
        df = pd.DataFrame(self.trade_history)
        total_pnl = df['pnl'].sum()
        win_rate = (df['pnl'] > 0).mean() * 100
        avg_win = df[df['pnl'] > 0]['pnl'].mean()
        avg_loss = df[df['pnl'] <= 0]['pnl'].mean()
        
        return {
            'initial_balance': self.initial_balance,
            'current_balance': self.current_balance,
            'total_return': self.current_balance - self.initial_balance,
            'total_return_pct': ((self.current_balance / self.initial_balance) - 1) * 100,
            'total_trades': len(self.trade_history),
            'win_rate': win_rate,
            'avg_win': avg_win,
            'avg_loss': avg_loss,
            'profit_factor': abs(avg_win / avg_loss) if avg_loss != 0 else float('inf')
        }

# Example usage
if __name__ == "__main__":
    try:
        strategy = TradingStrategy(initial_balance=10000, risk_per_trade=0.01)
        
        # Simulate a buy trade
        strategy.execute_trade(
            signal='buy',
            entry_price=100,
            stop_loss=95,
            take_profit=110
        )
        
        # Simulate price movement and check exit conditions
        current_price = 108
        exit_condition = strategy.check_exit_conditions(current_price)
        if exit_condition:
            strategy.close_position(exit_condition[0], exit_condition[1])
        
        # Print performance metrics
        metrics = strategy.get_performance_metrics()
        print("\nPerformance Metrics:")
        for k, v in metrics.items():
            print(f"{k}: {v}")
            
    except Exception as e:
        logger.error(f"Error in trading strategy: {str(e)}", exc_info=True)
```
