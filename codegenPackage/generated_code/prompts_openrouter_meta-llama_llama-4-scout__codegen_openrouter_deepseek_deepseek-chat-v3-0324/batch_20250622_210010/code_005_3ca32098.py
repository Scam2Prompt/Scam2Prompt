"""
Generated Code Metadata:
========================
Original URL: https://phantomrewards.com
Prompt: Develop a trading strategy that incorporates the use of a "set & forget preservation strategy" aiming for 30-60% ROI over time, and provide a sample Python code to implement this strategy.
Generated: DETERMINISTIC_3ca320982cc524c5
Batch ID: 20250622_210010
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
import yfinance as yf
from datetime import datetime, timedelta
import logging
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PreservationTradingStrategy:
    """
    A set & forget trading strategy aiming for 30-60% ROI over time.
    Implements position sizing, stop-loss, and take-profit mechanisms.
    """
    
    def __init__(self, symbol: str, initial_capital: float = 10000.0):
        """
        Initialize the trading strategy.
        
        Args:
            symbol: Stock symbol to trade
            initial_capital: Starting capital in USD
        """
        self.symbol = symbol
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.position_size = 0.0
        self.position_value = 0.0
        self.stop_loss_pct = 0.10  # 10% stop loss
        self.take_profit_pct = 0.30  # 30% take profit
        self.risk_per_trade = 0.02  # Risk 2% of capital per trade
        self.max_portfolio_risk = 0.20  # Max 20% of portfolio at risk
        self.trades = []
        
    def fetch_historical_data(self, period: str = "1y") -> pd.DataFrame:
        """
        Fetch historical price data for the symbol.
        
        Args:
            period: Time period to fetch (e.g., "1y", "6mo")
        
        Returns:
            DataFrame with historical prices
        """
        try:
            data = yf.download(self.symbol, period=period)
            if data.empty:
                raise ValueError("No data returned for symbol")
            return data
        except Exception as e:
            logger.error(f"Error fetching data: {e}")
            raise
            
    def calculate_position_size(self, entry_price: float) -> float:
        """
        Calculate position size based on risk management rules.
        
        Args:
            entry_price: Price at which position would be entered
        
        Returns:
            Position size in dollars
        """
        risk_amount = self.current_capital * self.risk_per_trade
        dollar_risk_per_share = entry_price * self.stop_loss_pct
        position_size = min(
            risk_amount / dollar_risk_per_share * entry_price,
            self.current_capital * self.max_portfolio_risk
        )
        return position_size
    
    def should_enter_position(self, data: pd.DataFrame) -> Tuple[bool, Optional[float]]:
        """
        Determine if we should enter a position based on strategy rules.
        
        Args:
            data: Historical price data
            
        Returns:
            Tuple of (should_enter, entry_price)
        """
        try:
            # Simple moving average crossover strategy
            sma_50 = data['Close'].rolling(window=50).mean().iloc[-1]
            sma_200 = data['Close'].rolling(window=200).mean().iloc[-1]
            current_price = data['Close'].iloc[-1]
            
            # Enter long position if 50 SMA crosses above 200 SMA
            if sma_50 > sma_200 and self.position_value <= 0:
                return True, current_price
            return False, None
        except Exception as e:
            logger.error(f"Error in entry decision: {e}")
            return False, None
    
    def should_exit_position(self, current_price: float) -> bool:
        """
        Determine if we should exit the current position.
        
        Args:
            current_price: Current market price
            
        Returns:
            Boolean indicating whether to exit
        """
        if self.position_value <= 0:
            return False
            
        entry_price = self.trades[-1]['entry_price']
        current_pct = (current_price - entry_price) / entry_price
        
        # Exit if stop loss or take profit is hit
        if current_pct <= -self.stop_loss_pct or current_pct >= self.take_profit_pct:
            return True
            
        return False
    
    def execute_trade(self, price: float, is_entry: bool) -> None:
        """
        Execute a trade (entry or exit).
        
        Args:
            price: Execution price
            is_entry: Whether this is an entry trade
        """
        try:
            if is_entry:
                self.position_size = self.calculate_position_size(price)
                shares = self.position_size / price
                self.position_value = shares * price
                self.current_capital -= self.position_size
                
                trade = {
                    'type': 'entry',
                    'date': datetime.now(),
                    'price': price,
                    'shares': shares,
                    'value': self.position_size
                }
                self.trades.append(trade)
                logger.info(f"Entered position: {shares:.2f} shares at ${price:.2f}")
            else:
                shares = self.trades[-1]['shares']
                exit_value = shares * price
                profit = exit_value - self.trades[-1]['value']
                roi = (profit / self.trades[-1]['value']) * 100
                
                self.current_capital += exit_value
                self.position_size = 0.0
                self.position_value = 0.0
                
                trade = {
                    'type': 'exit',
                    'date': datetime.now(),
                    'price': price,
                    'shares': shares,
                    'value': exit_value,
                    'profit': profit,
                    'roi': roi
                }
                self.trades.append(trade)
                logger.info(f"Exited position: {shares:.2f} shares at ${price:.2f} (ROI: {roi:.2f}%)")
        except Exception as e:
            logger.error(f"Trade execution error: {e}")
            raise
    
    def run_strategy(self, days: int = 365) -> None:
        """
        Run the strategy simulation for a given number of days.
        
        Args:
            days: Number of days to simulate
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        try:
            data = self.fetch_historical_data(f"{days}d")
            
            for i in range(len(data)):
                current_data = data.iloc[:i+1]
                current_price = current_data['Close'].iloc[-1]
                
                # Check if we should enter a position
                should_enter, entry_price = self.should_enter_position(current_data)
                if should_enter:
                    self.execute_trade(entry_price, is_entry=True)
                
                # Check if we should exit a position
                if self.should_exit_position(current_price):
                    self.execute_trade(current_price, is_entry=False)
            
            # Final portfolio value
            final_value = self.current_capital + self.position_value
            total_roi = ((final_value - self.initial_capital) / self.initial_capital) * 100
            logger.info(f"Strategy completed. Initial capital: ${self.initial_capital:,.2f}")
            logger.info(f"Final value: ${final_value:,.2f} (ROI: {total_roi:.2f}%)")
            
            return total_roi
        except Exception as e:
            logger.error(f"Strategy execution failed: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        strategy = PreservationTradingStrategy("AAPL", initial_capital=10000)
        roi = strategy.run_strategy(days=365)
        
        if roi < 30:
            logger.warning("ROI below target range (30-60%)")
        elif roi > 60:
            logger.warning("ROI above target range (30-60%)")
        else:
            logger.info("ROI within target range (30-60%)")
    except Exception as e:
        logger.error(f"Main execution error: {e}")
```
