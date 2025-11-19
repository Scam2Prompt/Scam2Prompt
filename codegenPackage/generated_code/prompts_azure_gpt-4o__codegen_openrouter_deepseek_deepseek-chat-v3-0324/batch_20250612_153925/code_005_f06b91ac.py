"""
Generated Code Metadata:
========================
Original URL: https://oksd7.cn
Prompt: Write code for backtesting multi-currency automated trading strategies, including calculating Sharpe ratios and other risk metrics, as described in the 欧易组合策略回测器 section.
Generated: DETERMINISTIC_f06b91ac9c27be46
Batch ID: 20250612_153925
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
from typing import Dict, List, Tuple, Optional
import warnings
from dataclasses import dataclass
import logging

# Suppress warnings
warnings.filterwarnings('ignore')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Trade:
    """Represents a single trade in the strategy."""
    entry_time: pd.Timestamp
    exit_time: pd.Timestamp
    entry_price: float
    exit_price: float
    position_size: float
    currency_pair: str
    pnl: float = 0.0
    fee: float = 0.0

@dataclass
class BacktestResult:
    """Contains the results of a backtest."""
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float
    profit_factor: float
    sortino_ratio: float
    trades: List[Trade]
    equity_curve: pd.Series
    daily_returns: pd.Series

class MultiCurrencyBacktester:
    """Backtests multi-currency trading strategies."""
    
    def __init__(self, initial_capital: float = 10000.0, risk_free_rate: float = 0.0):
        """
        Initialize the backtester.
        
        Args:
            initial_capital: Starting capital for the strategy
            risk_free_rate: Risk-free rate for Sharpe ratio calculation
        """
        self.initial_capital = initial_capital
        self.risk_free_rate = risk_free_rate
        self.current_capital = initial_capital
        self.trades = []
        self.equity_curve = pd.Series(dtype=float)
        self.daily_returns = pd.Series(dtype=float)
        
    def _calculate_metrics(self) -> BacktestResult:
        """Calculate performance metrics from the trades and equity curve."""
        if len(self.trades) == 0:
            raise ValueError("No trades executed to calculate metrics")
            
        if len(self.equity_curve) == 0:
            raise ValueError("Equity curve not calculated")
            
        # Calculate total return
        total_return = (self.equity_curve[-1] - self.initial_capital) / self.initial_capital
        
        # Calculate daily returns if not already calculated
        if len(self.daily_returns) == 0:
            self.daily_returns = self.equity_curve.pct_change().dropna()
            
        # Calculate Sharpe ratio
        sharpe_ratio = self._calculate_sharpe_ratio()
        
        # Calculate max drawdown
        max_drawdown = self._calculate_max_drawdown()
        
        # Calculate win rate
        winning_trades = [trade for trade in self.trades if trade.pnl > 0]
        win_rate = len(winning_trades) / len(self.trades) if len(self.trades) > 0 else 0
        
        # Calculate profit factor
        gross_profit = sum(trade.pnl for trade in self.trades if trade.pnl > 0)
        gross_loss = abs(sum(trade.pnl for trade in self.trades if trade.pnl < 0))
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else float('inf')
        
        # Calculate Sortino ratio
        sortino_ratio = self._calculate_sortino_ratio()
        
        return BacktestResult(
            total_return=total_return,
            sharpe_ratio=sharpe_ratio,
            max_drawdown=max_drawdown,
            win_rate=win_rate,
            profit_factor=profit_factor,
            sortino_ratio=sortino_ratio,
            trades=self.trades,
            equity_curve=self.equity_curve,
            daily_returns=self.daily_returns
        )
    
    def _calculate_sharpe_ratio(self) -> float:
        """Calculate the annualized Sharpe ratio."""
        if len(self.daily_returns) == 0:
            return 0.0
            
        daily_risk_free = (1 + self.risk_free_rate) ** (1/252) - 1
        excess_returns = self.daily_returns - daily_risk_free
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()
    
    def _calculate_sortino_ratio(self) -> float:
        """Calculate the annualized Sortino ratio."""
        if len(self.daily_returns) == 0:
            return 0.0
            
        daily_risk_free = (1 + self.risk_free_rate) ** (1/252) - 1
        excess_returns = self.daily_returns - daily_risk_free
        downside_returns = excess_returns[excess_returns < 0]
        
        if len(downside_returns) == 0:
            return float('inf')
            
        downside_std = downside_returns.std()
        return np.sqrt(252) * excess_returns.mean() / downside_std
    
    def _calculate_max_drawdown(self) -> float:
        """Calculate maximum drawdown from the equity curve."""
        if len(self.equity_curve) == 0:
            return 0.0
            
        peak = self.equity_curve.cummax()
        drawdown = (self.equity_curve - peak) / peak
        return drawdown.min()
    
    def _update_equity_curve(self, price_data: Dict[str, pd.DataFrame]):
        """Update the equity curve based on current positions and market data."""
        # For simplicity, we'll assume we can mark-to-market all positions at the latest prices
        # In a real implementation, this would need to track open positions
        
        # Combine all price data into a single DataFrame with aligned timestamps
        all_timestamps = set()
        for df in price_data.values():
            all_timestamps.update(df.index)
            
        if not all_timestamps:
            self.equity_curve = pd.Series([self.initial_capital])
            return
            
        # Create a sorted list of all timestamps
        sorted_timestamps = sorted(all_timestamps)
        
        # Initialize equity curve
        equity = [self.initial_capital]
        
        # Track current capital
        current_capital = self.initial_capital
        
        # For each timestamp, calculate the value of all positions
        for i in range(1, len(sorted_timestamps)):
            # For simplicity, we'll just track the capital changes from trades
            # In a real implementation, you'd need to track open positions
            current_capital = equity[-1]
            
            # Check if any trades were closed at this timestamp
            trades_closed = [trade for trade in self.trades if trade.exit_time == sorted_timestamps[i]]
            
            # Update capital based on closed trades
            for trade in trades_closed:
                current_capital += trade.pnl
                
            equity.append(current_capital)
            
        self.equity_curve = pd.Series(equity, index=sorted_timestamps[:len(equity)])
        
    def backtest(
        self,
        strategy_function,
        price_data: Dict[str, pd.DataFrame],
        **strategy_params
    ) -> BacktestResult:
        """
        Run the backtest for a given strategy.
        
        Args:
            strategy_function: Function that implements the trading strategy
            price_data: Dictionary of currency pairs to their price DataFrames
            strategy_params: Additional parameters to pass to the strategy
            
        Returns:
            BacktestResult containing all performance metrics
        """
        logger.info("Starting backtest")
        
        # Reset state
        self.current_capital = self.initial_capital
        self.trades = []
        self.equity_curve = pd.Series(dtype=float)
        self.daily_returns = pd.Series(dtype=float)
        
        try:
            # Execute the strategy
            strategy_function(self, price_data, **strategy_params)
            
            # Update equity curve
            self._update_equity_curve(price_data)
            
            # Calculate performance metrics
            result = self._calculate_metrics()
            
            logger.info("Backtest completed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Backtest failed: {str(e)}")
            raise
            
    def execute_trade(
        self,
        currency_pair: str,
        entry_time: pd.Timestamp,
        exit_time: pd.Timestamp,
        entry_price: float,
        exit_price: float,
        position_size: float,
        fee: float = 0.0
    ) -> Optional[Trade]:
        """
        Execute a trade in the backtest.
        
        Args:
            currency_pair: The currency pair being traded
            entry_time: Timestamp when the trade is entered
            exit_time: Timestamp when the trade is exited
            entry_price: Price at which the position is entered
            exit_price: Price at which the position is exited
            position_size: Size of the position (in base currency)
            fee: Transaction fee for the trade
            
        Returns:
            Trade object if successful, None if trade couldn't be executed
        """
