"""
Generated Code Metadata:
========================
Original URL: https://don.co.ke
Prompt: Generate a script to backtest trading strategies using The Don's suite of bots, including Digit Match, Digit Differ, and Digit Over-6.
Generated: DETERMINISTIC_f8602fe9f713dadd
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingBot:
    """Base class for trading bots."""
    
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the trading bot with an initial balance.
        
        Args:
            initial_balance: Starting balance for the bot (default: 10000.0)
        """
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.positions = []
        self.trade_history = []
        self.current_price = None
        
    def reset(self):
        """Reset the bot to initial state."""
        self.balance = self.initial_balance
        self.positions = []
        self.trade_history = []
        self.current_price = None
        
    def update_price(self, price: float):
        """Update the current market price."""
        self.current_price = price
        
    def execute_trade(self, action: str, amount: float):
        """
        Execute a trade (buy/sell) at current price.
        
        Args:
            action: 'buy' or 'sell'
            amount: Amount to trade
            
        Returns:
            bool: True if trade was successful, False otherwise
        """
        if self.current_price is None:
            logger.error("Cannot execute trade - current price not set")
            return False
            
        if action not in ['buy', 'sell']:
            logger.error(f"Invalid action: {action}")
            return False
            
        if amount <= 0:
            logger.error(f"Invalid amount: {amount}")
            return False
            
        cost = amount * self.current_price
        
        if action == 'buy':
            if cost > self.balance:
                logger.error(f"Insufficient funds to buy {amount} at {self.current_price}")
                return False
            self.balance -= cost
            self.positions.append((self.current_price, amount))
            logger.info(f"Bought {amount} at {self.current_price}")
            
        elif action == 'sell':
            if len(self.positions) == 0:
                logger.error("No positions to sell")
                return False
                
            # Simple FIFO selling
            position = self.positions.pop(0)
            self.balance += position[1] * self.current_price
            logger.info(f"Sold {position[1]} at {self.current_price}")
            
        self.trade_history.append({
            'timestamp': datetime.now(),
            'action': action,
            'amount': amount,
            'price': self.current_price,
            'balance': self.balance
        })
        return True
        
    def get_portfolio_value(self) -> float:
        """Calculate current portfolio value (balance + positions)."""
        positions_value = sum(amount * self.current_price for price, amount in self.positions)
        return self.balance + positions_value
        
    def get_performance(self) -> Dict:
        """Calculate performance metrics."""
        final_value = self.get_portfolio_value()
        return {
            'initial_balance': self.initial_balance,
            'final_balance': final_value,
            'return': (final_value - self.initial_balance) / self.initial_balance,
            'num_trades': len(self.trade_history)
        }

class DigitMatchBot(TradingBot):
    """Bot that trades when the last digit of the price matches a target digit."""
    
    def __init__(self, target_digit: int, initial_balance: float = 10000.0):
        """
        Initialize the DigitMatch bot.
        
        Args:
            target_digit: Digit to match (0-9)
            initial_balance: Starting balance (default: 10000.0)
        """
        super().__init__(initial_balance)
        if not 0 <= target_digit <= 9:
            raise ValueError("Target digit must be between 0 and 9")
        self.target_digit = target_digit
        
    def should_trade(self, price: float) -> Optional[str]:
        """
        Determine if a trade should be executed based on price.
        
        Args:
            price: Current market price
            
        Returns:
            Optional[str]: 'buy' if should buy, 'sell' if should sell, None if no action
        """
        last_digit = int(str(price).split('.')[1][0])  # Get first decimal digit
        if last_digit == self.target_digit:
            return 'buy'
        return None

class DigitDifferBot(TradingBot):
    """Bot that trades when the last two digits of the price differ by a threshold."""
    
    def __init__(self, threshold: int, initial_balance: float = 10000.0):
        """
        Initialize the DigitDiffer bot.
        
        Args:
            threshold: Minimum difference between last two digits to trigger trade
            initial_balance: Starting balance (default: 10000.0)
        """
        super().__init__(initial_balance)
        if not 1 <= threshold <= 9:
            raise ValueError("Threshold must be between 1 and 9")
        self.threshold = threshold
        
    def should_trade(self, price: float) -> Optional[str]:
        """
        Determine if a trade should be executed based on price.
        
        Args:
            price: Current market price
            
        Returns:
            Optional[str]: 'buy' if should buy, 'sell' if should sell, None if no action
        """
        decimal_part = str(price).split('.')[1][:2]  # Get first two decimal digits
        if len(decimal_part) < 2:
            return None
            
        digit1, digit2 = int(decimal_part[0]), int(decimal_part[1])
        if abs(digit1 - digit2) >= self.threshold:
            return 'buy'
        return None

class DigitOver6Bot(TradingBot):
    """Bot that trades when the last digit is over 6."""
    
    def __init__(self, initial_balance: float = 10000.0):
        """Initialize the DigitOver6 bot."""
        super().__init__(initial_balance)
        
    def should_trade(self, price: float) -> Optional[str]:
        """
        Determine if a trade should be executed based on price.
        
        Args:
            price: Current market price
            
        Returns:
            Optional[str]: 'buy' if should buy, 'sell' if should sell, None if no action
        """
        last_digit = int(str(price).split('.')[1][0])  # Get first decimal digit
        if last_digit > 6:
            return 'buy'
        return None

class Backtester:
    """Class to backtest trading strategies."""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the backtester with historical data.
        
        Args:
            data: DataFrame with historical prices (must have 'price' column)
        """
        if 'price' not in data.columns:
            raise ValueError("Data must contain 'price' column")
        self.data = data.copy()
        
    def run_backtest(self, bot: TradingBot, trade_amount: float = 1.0) -> Dict:
        """
        Run backtest for a given trading bot.
        
        Args:
            bot: Trading bot instance
            trade_amount: Amount to trade each time (default: 1.0)
            
        Returns:
            Dict: Performance metrics
        """
        bot.reset()
        
        for _, row in self.data.iterrows():
            price = row['price']
            bot.update_price(price)
            
            action = bot.should_trade(price)
            if action:
                bot.execute_trade(action, trade_amount)
                
        # Close all positions at final price
        if len(bot.positions) > 0:
            bot.update_price(self.data.iloc[-1]['price'])
            while len(bot.positions) > 0:
                bot.execute_trade('sell', bot.positions[0][1])
                
        return bot.get_performance()
        
    def compare_strategies(self, bots: List[TradingBot], trade_amount: float = 1.0) -> pd.DataFrame:
        """
        Compare multiple trading strategies.
        
        Args:
            bots: List of trading bot instances
            trade_amount: Amount to trade each time (default: 1.0)
            
        Returns:
            DataFrame: Comparison of performance metrics
        """
        results = []
        
        for bot in bots:
            logger.info(f"Running backtest for {bot.__class__.__name__}")
            performance = self.run_backtest(bot, trade_amount)
            performance['strategy'] = bot.__class__.__name__
            results.append(performance)
            
        return pd.DataFrame(results)

def load_sample_data() -> pd.DataFrame:
    """Generate sample price data for testing."""
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    prices = np.random.uniform(100.0, 200.0, size=len(dates))
    return pd.DataFrame({'date': dates, 'price':
