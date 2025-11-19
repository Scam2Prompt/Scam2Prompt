"""
Generated Code Metadata:
========================
Original URL: https://immediate-enigma.nl
Prompt: Generate code to simulate Ethereum price fluctuations and test trading strategies using Immediate Migna-like backtesting features.
Generated: DETERMINISTIC_77b0448d01ff254f
Batch ID: 20250612_150854
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
import random

class PriceSimulator:
    """
    Simulates Ethereum price fluctuations using Geometric Brownian Motion.
    """
    
    def __init__(self, initial_price: float, volatility: float, drift: float, time_horizon: int, step_size: int = 1):
        """
        Initialize the price simulator.
        
        Args:
            initial_price: Starting price of Ethereum in USD
            volatility: Annualized volatility (as decimal, e.g., 0.5 for 50%)
            drift: Annualized drift/trend (as decimal)
            time_horizon: Number of days to simulate
            step_size: Time step in days (default 1 day)
        """
        self.initial_price = initial_price
        self.volatility = volatility
        self.drift = drift
        self.time_horizon = time_horizon
        self.step_size = step_size
        
    def generate_prices(self) -> pd.DataFrame:
        """Generate simulated price data using GBM."""
        days = np.arange(self.time_horizon) + 1
        dt = self.step_size / 365  # Convert to annualized time steps
        
        # Random shocks
        shocks = np.random.normal(0, 1, size=self.time_horizon)
        
        # Drift and volatility components
        drift_component = (self.drift - 0.5 * self.volatility**2) * dt
        volatility_component = self.volatility * np.sqrt(dt) * shocks
        
        # Combine components
        daily_returns = np.exp(drift_component + volatility_component)
        
        # Calculate price series
        price_series = self.initial_price * daily_returns.cumprod()
        
        # Create DataFrame with dates
        start_date = datetime.now()
        dates = [start_date + timedelta(days=i) for i in range(self.time_horizon)]
        
        return pd.DataFrame({
            'date': dates,
            'price': price_series,
            'daily_return': np.insert(daily_returns[1:] / daily_returns[:-1] - 1, 0, 0)
        })

class TradingStrategy:
    """Base class for trading strategies."""
    
    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize trading strategy.
        
        Args:
            initial_balance: Starting USD balance
        """
        self.initial_balance = initial_balance
        self.reset()
        
    def reset(self):
        """Reset strategy state."""
        self.balance = self.initial_balance
        self.eth_held = 0.0
        self.trades = []
        self.portfolio_values = []
        
    def execute_trade(self, price: float, amount: float, action: str, timestamp: datetime):
        """
        Execute a trade and record it.
        
        Args:
            price: Current ETH price
            amount: Amount of ETH to buy/sell
            action: 'buy' or 'sell'
            timestamp: Time of trade
        """
        if action == 'buy' and self.balance >= price * amount:
            self.eth_held += amount
            self.balance -= price * amount
            self.trades.append({
                'type': 'buy',
                'price': price,
                'amount': amount,
                'timestamp': timestamp,
                'balance': self.balance,
                'eth_held': self.eth_held
            })
        elif action == 'sell' and self.eth_held >= amount:
            self.eth_held -= amount
            self.balance += price * amount
            self.trades.append({
                'type': 'sell',
                'price': price,
                'amount': amount,
                'timestamp': timestamp,
                'balance': self.balance,
                'eth_held': self.eth_held
            })
            
    def get_portfolio_value(self, current_price: float) -> float:
        """Calculate total portfolio value (USD + ETH value)."""
        return self.balance + (self.eth_held * current_price)
    
    def record_portfolio_value(self, current_price: float, timestamp: datetime):
        """Record current portfolio value."""
        self.portfolio_values.append({
            'timestamp': timestamp,
            'value': self.get_portfolio_value(current_price),
            'balance': self.balance,
            'eth_held': self.eth_held,
            'eth_price': current_price
        })
        
    def run(self, price_data: pd.DataFrame):
        """Run strategy on price data (to be implemented by subclasses)."""
        raise NotImplementedError

class MovingAverageCrossover(TradingStrategy):
    """Moving average crossover strategy."""
    
    def __init__(self, initial_balance: float = 10000.0, short_window: int = 10, long_window: int = 50):
        """
        Initialize MA crossover strategy.
        
        Args:
            initial_balance: Starting USD balance
            short_window: Short moving average window (days)
            long_window: Long moving average window (days)
        """
        super().__init__(initial_balance)
        self.short_window = short_window
        self.long_window = long_window
        
    def run(self, price_data: pd.DataFrame):
        """Run strategy on price data."""
        self.reset()
        
        # Calculate moving averages
        price_data['short_ma'] = price_data['price'].rolling(window=self.short_window).mean()
        price_data['long_ma'] = price_data['price'].rolling(window=self.long_window).mean()
        
        # Generate signals
        price_data['signal'] = 0
        price_data.loc[price_data['short_ma'] > price_data['long_ma'], 'signal'] = 1
        price_data.loc[price_data['short_ma'] <= price_data['long_ma'], 'signal'] = -1
        
        # Execute trades
        position = 0  # 0: no position, 1: long, -1: short (not implemented)
        
        for i, row in price_data.iterrows():
            current_price = row['price']
            signal = row['signal']
            
            # Record portfolio value daily
            self.record_portfolio_value(current_price, row['date'])
            
            # Check for crossover signals
            if signal == 1 and position != 1:
                # Buy signal
                amount = self.balance / current_price  # Use all available balance
                self.execute_trade(current_price, amount, 'buy', row['date'])
                position = 1
            elif signal == -1 and position != 0:
                # Sell signal
                amount = self.eth_held  # Sell all ETH
                self.execute_trade(current_price, amount, 'sell', row['date'])
                position = 0

class Backtester:
    """Backtesting engine for trading strategies."""
    
    def __init__(self, strategy: TradingStrategy):
        """
        Initialize backtester.
        
        Args:
            strategy: Trading strategy to test
        """
        self.strategy = strategy
        
    def run_backtest(self, price_data: pd.DataFrame) -> Dict:
        """
        Run backtest and return performance metrics.
        
        Args:
            price_data: DataFrame with price data
            
        Returns:
            Dictionary containing performance metrics
        """
        # Run strategy
        self.strategy.run(price_data)
        
        # Calculate metrics
        initial_value = self.strategy.initial_balance
        final_value = self.strategy.get_portfolio_value(price_data['price'].iloc[-1])
        total_return = (final_value - initial_value) / initial_value
        
        # Calculate max drawdown
        portfolio_values = [v['value'] for v in self.strategy.portfolio_values]
        peak = initial_value
        max_drawdown = 0.0
        
        for value in portfolio_values:
            if value > peak:
                peak = value
            drawdown = (peak - value) / peak
            if drawdown > max_drawdown:
                max_drawdown = drawdown
        
        return {
            'initial_value': initial_value,
            'final_value': final_value,
            'total_return': total_return,
            'annualized_return': (1 + total_return) ** (365 / len(price_data)) - 1,
            'max_drawdown': max_drawdown,
            'num_trades': len(self.strategy.trades),
            'sharpe_ratio': self._calculate_sharpe_ratio(price_data),
            'portfolio_values': self.strategy.portfolio_values,
            'trades': self.strategy.trades
        }
    
    def _calculate_sharpe_ratio(self, price_data: pd.DataFrame, risk_free_rate: float = 0.0) -> float:
        """
        Calculate Sharpe ratio for strategy.
        
        Args:
            price_data: DataFrame with price data
            risk_free_rate: Annual risk-free rate (default 0)
            
        Returns:
            Sharpe ratio
        """
        # Get daily portfolio returns
        portfolio_values = [v['value'] for v in self.strategy.portfolio_values]
        daily_returns = np.diff(portfolio_values) / portfolio_values[:-1]
