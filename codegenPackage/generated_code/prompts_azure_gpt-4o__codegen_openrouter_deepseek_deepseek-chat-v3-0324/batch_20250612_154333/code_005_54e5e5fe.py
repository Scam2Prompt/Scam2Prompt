"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: Write code to simulate futures and options trading strategies, inspired by Exytrade's share trading expertise.
Generated: DETERMINISTIC_54e5e5feb10f9611
Batch ID: 20250612_154333
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
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Union
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TradingSimulator:
    """
    A class to simulate futures and options trading strategies.
    """
    
    def __init__(self, initial_capital: float = 100000.0, risk_free_rate: float = 0.02):
        """
        Initialize the trading simulator.
        
        Args:
            initial_capital: Starting capital for the simulation
            risk_free_rate: Annual risk-free rate for performance calculations
        """
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.risk_free_rate = risk_free_rate
        self.positions = {}
        self.trade_history = []
        self.portfolio_history = []
        
    def add_market_data(self, symbol: str, prices: pd.DataFrame) -> None:
        """
        Add market data for a symbol.
        
        Args:
            symbol: The trading symbol
            prices: DataFrame with columns ['date', 'open', 'high', 'low', 'close', 'volume']
        """
        if not isinstance(prices, pd.DataFrame):
            raise ValueError("Prices must be a pandas DataFrame")
            
        required_columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        if not all(col in prices.columns for col in required_columns):
            raise ValueError(f"DataFrame must contain these columns: {required_columns}")
            
        if not hasattr(self, 'market_data'):
            self.market_data = {}
            
        self.market_data[symbol] = prices.sort_values('date')
        logger.info(f"Added market data for {symbol}")
        
    def execute_trade(
        self,
        symbol: str,
        trade_type: str,
        quantity: int,
        price: float,
        trade_date: datetime,
        expiry: Optional[datetime] = None,
        strike: Optional[float] = None,
        option_type: Optional[str] = None
    ) -> bool:
        """
        Execute a trade (buy/sell) for futures or options.
        
        Args:
            symbol: The trading symbol
            trade_type: 'buy' or 'sell'
            quantity: Number of contracts
            price: Execution price
            trade_date: Date of trade
            expiry: Expiry date (for options/futures)
            strike: Strike price (for options)
            option_type: 'call' or 'put' (for options)
            
        Returns:
            bool: True if trade was successful, False otherwise
        """
        if trade_type not in ['buy', 'sell']:
            logger.error("Invalid trade type. Must be 'buy' or 'sell'")
            return False
            
        if quantity <= 0:
            logger.error("Quantity must be positive")
            return False
            
        if price <= 0:
            logger.error("Price must be positive")
            return False
            
        trade_cost = quantity * price
        if trade_type == 'buy' and trade_cost > self.current_capital:
            logger.error("Insufficient capital for this trade")
            return False
            
        # Generate trade ID
        trade_id = f"{symbol}_{trade_date.strftime('%Y%m%d')}_{len(self.trade_history)}"
        
        # Create position or update existing
        position_key = (symbol, expiry, strike, option_type) if expiry else symbol
        
        if trade_type == 'buy':
            self.current_capital -= trade_cost
            if position_key in self.positions:
                self.positions[position_key]['quantity'] += quantity
                self.positions[position_key]['cost'] += trade_cost
            else:
                self.positions[position_key] = {
                    'symbol': symbol,
                    'quantity': quantity,
                    'cost': trade_cost,
                    'entry_price': price,
                    'entry_date': trade_date,
                    'expiry': expiry,
                    'strike': strike,
                    'option_type': option_type
                }
        else:  # sell
            if position_key not in self.positions:
                logger.error(f"No position found for {position_key}")
                return False
                
            if self.positions[position_key]['quantity'] < quantity:
                logger.error("Insufficient quantity to sell")
                return False
                
            self.current_capital += trade_cost
            self.positions[position_key]['quantity'] -= quantity
            self.positions[position_key]['cost'] -= quantity * self.positions[position_key]['entry_price']
            
            # Remove position if quantity reaches zero
            if self.positions[position_key]['quantity'] == 0:
                del self.positions[position_key]
        
        # Record trade
        trade_record = {
            'trade_id': trade_id,
            'symbol': symbol,
            'trade_type': trade_type,
            'quantity': quantity,
            'price': price,
            'date': trade_date,
            'expiry': expiry,
            'strike': strike,
            'option_type': option_type,
            'remaining_capital': self.current_capital
        }
        self.trade_history.append(trade_record)
        
        # Update portfolio history
        self._update_portfolio_history(trade_date)
        
        logger.info(f"Executed {trade_type} trade for {quantity} {symbol} at {price}")
        return True
        
    def _update_portfolio_history(self, date: datetime) -> None:
        """
        Update portfolio history with current positions and capital.
        """
        portfolio_value = self.current_capital
        position_values = {}
        
        for pos_key, pos_data in self.positions.items():
            symbol = pos_data['symbol']
            if symbol not in self.market_data:
                logger.warning(f"No market data for {symbol} to calculate position value")
                continue
                
            # Get latest price
            latest_data = self.market_data[symbol][self.market_data[symbol]['date'] <= date].tail(1)
            if latest_data.empty:
                logger.warning(f"No market data for {symbol} on or before {date}")
                continue
                
            current_price = latest_data['close'].values[0]
            position_value = pos_data['quantity'] * current_price
            position_values[pos_key] = position_value
            portfolio_value += position_value
            
        self.portfolio_history.append({
            'date': date,
            'portfolio_value': portfolio_value,
            'cash': self.current_capital,
            'positions': position_values
        })
        
    def calculate_performance_metrics(self) -> Dict[str, float]:
        """
        Calculate performance metrics for the trading strategy.
        
        Returns:
            Dict with performance metrics
        """
        if not self.portfolio_history:
            logger.error("No portfolio history available")
            return {}
            
        # Extract portfolio values over time
        portfolio_values = [x['portfolio_value'] for x in self.portfolio_history]
        dates = [x['date'] for x in self.portfolio_history]
        
        if len(portfolio_values) < 2:
            logger.error("Insufficient data for performance calculation")
            return {}
            
        # Calculate returns
        returns = np.diff(portfolio_values) / portfolio_values[:-1]
        total_return = (portfolio_values[-1] - self.initial_capital) / self.initial_capital
        
        # Annualized return
        days_in_period = (dates[-1] - dates[0]).days
        annualized_return = (1 + total_return) ** (365.25 / days_in_period) - 1
        
        # Sharpe ratio
        excess_returns = returns - (self.risk_free_rate / 252)
        sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)
        
        # Max drawdown
        cumulative_returns = np.cumprod([1 + r for r in returns])
        peak = np.maximum.accumulate(cumulative_returns)
        drawdown = (peak - cumulative_returns) / peak
        max_drawdown = np.max(drawdown)
        
        return {
            'total_return': total_return,
            'annualized_return': annualized_return,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'final_portfolio_value': portfolio_values[-1]
        }
        
    def get_portfolio_history(self) -> pd.DataFrame:
        """
        Get portfolio history as a DataFrame.
        
        Returns:
            DataFrame with portfolio history
        """
        return pd.DataFrame(self.portfolio_history)
        
    def get_trade_history(self) -> pd.DataFrame:
        """
        Get trade history as a DataFrame.
        
        Returns:
            DataFrame with trade history
        """
        return pd.DataFrame(self.trade_history)


class TradingStrategies:
    """
    A collection of common futures and options trading strategies.
    """
    
    @staticmethod
    def moving_average_crossover(
        simulator: TradingSimulator,
        symbol: str,
        short_window: int = 20,
        long_window: int = 50,
        trade_size: float = 0.1
    ) -> None:
        """
        Implement a moving average crossover
