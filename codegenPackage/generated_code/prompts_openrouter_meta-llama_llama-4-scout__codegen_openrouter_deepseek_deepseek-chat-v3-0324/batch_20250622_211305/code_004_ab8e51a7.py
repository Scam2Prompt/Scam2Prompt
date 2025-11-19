"""
Generated Code Metadata:
========================
Original URL: https://theimmediateifexai.com
Prompt: Develop a demo account trading strategy using Immediate Ifex Ai's platform, focusing on optimizing trading parameters and validating trading modes.
Generated: DETERMINISTIC_ab8e51a7f9d5b369
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from datetime import datetime
import logging
from typing import Dict, Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TradingStrategy:
    """
    A demo trading strategy for Immediate Ifex Ai's platform.
    Optimizes trading parameters and validates trading modes.
    """
    
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the trading strategy with default parameters.
        
        Args:
            initial_balance (float): Starting account balance. Defaults to 10000.0.
        """
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.positions = {}  # Tracks open positions
        self.trade_history = []  # Records all trades
        self.optimization_params = {
            'take_profit': 0.02,  # 2% take profit
            'stop_loss': 0.01,    # 1% stop loss
            'trade_size': 0.1,    # 10% of balance per trade
            'max_trades': 5       # Max concurrent trades
        }
        
    def validate_trading_mode(self, mode: str) -> bool:
        """
        Validate the trading mode.
        
        Args:
            mode (str): Trading mode to validate (e.g., 'live', 'demo', 'backtest')
            
        Returns:
            bool: True if mode is valid, False otherwise
        """
        valid_modes = ['live', 'demo', 'backtest']
        return mode.lower() in valid_modes
    
    def optimize_parameters(self, historical_data: pd.DataFrame) -> Dict:
        """
        Optimize trading parameters based on historical data.
        
        Args:
            historical_data (pd.DataFrame): Historical market data for optimization
            
        Returns:
            Dict: Optimized trading parameters
        """
        try:
            # Simple optimization logic (can be replaced with more sophisticated methods)
            volatility = historical_data['close'].pct_change().std()
            
            optimized_params = {
                'take_profit': max(0.01, min(0.05, volatility * 5)),
                'stop_loss': max(0.005, min(0.03, volatility * 3)),
                'trade_size': 0.1,  # Fixed for demo purposes
                'max_trades': 5     # Fixed for demo purposes
            }
            
            logger.info("Optimized parameters: %s", optimized_params)
            return optimized_params
            
        except Exception as e:
            logger.error("Error optimizing parameters: %s", str(e))
            return self.optimization_params
    
    def execute_trade(self, symbol: str, price: float, action: str, size: Optional[float] = None) -> bool:
        """
        Execute a trade with proper risk management.
        
        Args:
            symbol (str): Trading symbol
            price (float): Current price
            action (str): 'buy' or 'sell'
            size (float, optional): Trade size. Defaults to optimized trade_size.
            
        Returns:
            bool: True if trade executed successfully, False otherwise
        """
        try:
            if not size:
                size = self.optimization_params['trade_size']
                
            trade_amount = self.current_balance * size
            
            if action.lower() not in ['buy', 'sell']:
                logger.error("Invalid trade action: %s", action)
                return False
                
            if len(self.positions) >= self.optimization_params['max_trades']:
                logger.warning("Max trades reached. Cannot execute new trade.")
                return False
                
            if trade_amount > self.current_balance:
                logger.warning("Insufficient balance for trade.")
                return False
                
            # Record the trade
            trade_id = f"{symbol}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            self.positions[trade_id] = {
                'symbol': symbol,
                'price': price,
                'action': action,
                'size': trade_amount,
                'timestamp': datetime.now(),
                'take_profit': price * (1 + self.optimization_params['take_profit'] 
                                      if action == 'buy' 
                                      else 1 - self.optimization_params['take_profit']),
                'stop_loss': price * (1 - self.optimization_params['stop_loss'] 
                                    if action == 'buy' 
                                    else 1 + self.optimization_params['stop_loss'])
            }
            
            self.current_balance -= trade_amount
            self.trade_history.append({
                'trade_id': trade_id,
                **self.positions[trade_id],
                'status': 'open'
            })
            
            logger.info("Executed %s trade for %s: %f @ %f", action, symbol, trade_amount, price)
            return True
            
        except Exception as e:
            logger.error("Error executing trade: %s", str(e))
            return False
    
    def check_positions(self, current_prices: Dict[str, float]) -> None:
        """
        Check open positions and close if TP/SL is hit.
        
        Args:
            current_prices (Dict[str, float]): Current prices for all symbols with open positions
        """
        try:
            for trade_id, position in list(self.positions.items()):
                symbol = position['symbol']
                current_price = current_prices.get(symbol)
                
                if current_price is None:
                    logger.warning("No price data for %s", symbol)
                    continue
                    
                # Check take profit and stop loss
                if (position['action'] == 'buy' and 
                    (current_price >= position['take_profit'] or 
                     current_price <= position['stop_loss'])):
                    
                    profit_loss = (current_price - position['price']) * position['size'] / position['price']
                    self.current_balance += position['size'] + profit_loss
                    
                    # Update trade history
                    for trade in self.trade_history:
                        if trade['trade_id'] == trade_id:
                            trade.update({
                                'close_price': current_price,
                                'close_time': datetime.now(),
                                'status': 'closed',
                                'profit_loss': profit_loss
                            })
                            break
                    
                    del self.positions[trade_id]
                    logger.info("Closed position %s: PnL = %f", trade_id, profit_loss)
                    
                elif (position['action'] == 'sell' and 
                      (current_price <= position['take_profit'] or 
                       current_price >= position['stop_loss'])):
                    
                    profit_loss = (position['price'] - current_price) * position['size'] / position['price']
                    self.current_balance += position['size'] + profit_loss
                    
                    # Update trade history
                    for trade in self.trade_history:
                        if trade['trade_id'] == trade_id:
                            trade.update({
                                'close_price': current_price,
                                'close_time': datetime.now(),
                                'status': 'closed',
                                'profit_loss': profit_loss
                            })
                            break
                    
                    del self.positions[trade_id]
                    logger.info("Closed position %s: PnL = %f", trade_id, profit_loss)
                    
        except Exception as e:
            logger.error("Error checking positions: %s", str(e))
    
    def get_performance_metrics(self) -> Dict:
        """
        Calculate and return performance metrics.
        
        Returns:
            Dict: Performance metrics including ROI, win rate, etc.
        """
        try:
            if not self.trade_history:
                return {}
                
            closed_trades = [t for t in self.trade_history if t['status'] == 'closed']
            if not closed_trades:
                return {}
                
            total_trades = len(closed_trades)
            winning_trades = len([t for t in closed_trades if t['profit_loss'] > 0])
            total_profit = sum(t['profit_loss'] for t in closed_trades)
            roi = (self.current_balance - self.initial_balance) / self.initial_balance * 100
            
            return {
                'initial_balance': self.initial_balance,
                'current_balance': self.current_balance,
                'roi_percent': roi,
                'total_trades': total_trades,
                'winning_trades': winning_trades,
                'win_rate': winning_trades / total_trades * 100,
                'total_profit': total_profit,
                'open_positions': len(self.positions)
            }
            
        except Exception as e:
            logger.error("Error calculating performance metrics: %s", str(e))
            return {}

# Example usage
if __name__ == "__main__":
    # Initialize strategy
    strategy = TradingStrategy()
    
    # Validate trading mode
    if strategy.validate_trading_mode('demo'):
        logger.info("Trading mode validated")
    
    # Simulate historical data for optimization
    dates = pd.date_range(start="2023-01-01", end="2023-06-01")
    prices = np.cumsum(np.random.randn(len
