"""
Generated Code Metadata:
========================
Original URL: https://syncexperttrade.com
Prompt: Write a script to simulate recurrent buying patterns for assets, as described in SyncExpertTrade's trading strategy, using historical price data.
Generated: DETERMINISTIC_cfd6643fae4f44d1
Batch ID: 20250612_154622
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
from typing import List, Dict, Optional, Tuple
import yfinance as yf
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SyncExpertTradeSimulator:
    """
    Simulates recurrent buying patterns for assets based on historical price data.
    Implements SyncExpertTrade's trading strategy logic.
    """
    
    def __init__(self, ticker: str, initial_capital: float = 10000.0):
        """
        Initialize the simulator with a ticker symbol and initial capital.
        
        Args:
            ticker: Stock ticker symbol (e.g., 'AAPL')
            initial_capital: Starting investment amount in dollars
        """
        self.ticker = ticker
        self.initial_capital = initial_capital
        self.data = None
        self.positions = []
        self.cash = initial_capital
        self.portfolio_value = []
        self.trade_history = []
        
    def fetch_historical_data(self, start_date: str, end_date: str) -> None:
        """
        Fetch historical price data from Yahoo Finance.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
        """
        try:
            logger.info(f"Fetching historical data for {self.ticker} from {start_date} to {end_date}")
            data = yf.download(self.ticker, start=start_date, end=end_date)
            if data.empty:
                raise ValueError("No data returned for the given date range")
            
            # Calculate daily returns and moving averages
            data['Daily_Return'] = data['Adj Close'].pct_change()
            data['SMA_20'] = data['Adj Close'].rolling(window=20).mean()
            data['SMA_50'] = data['Adj Close'].rolling(window=50).mean()
            
            self.data = data
            logger.info("Successfully fetched and processed historical data")
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")
            raise
    
    def generate_signals(self) -> None:
        """
        Generate trading signals based on the strategy rules.
        """
        if self.data is None:
            raise ValueError("No historical data available. Fetch data first.")
            
        try:
            logger.info("Generating trading signals")
            # Simple strategy: Buy when 20-day SMA crosses above 50-day SMA
            self.data['Signal'] = 0
            self.data['Signal'] = np.where(
                (self.data['SMA_20'] > self.data['SMA_50']) & 
                (self.data['SMA_20'].shift(1) <= self.data['SMA_50'].shift(1)), 
                1, 0
            )
            logger.info("Trading signals generated successfully")
        except Exception as e:
            logger.error(f"Error generating signals: {e}")
            raise
    
    def simulate_trades(self, position_size: float = 0.1) -> None:
        """
        Simulate trades based on generated signals.
        
        Args:
            position_size: Fraction of capital to invest in each position (0-1)
        """
        if self.data is None or 'Signal' not in self.data.columns:
            raise ValueError("Signals not generated. Generate signals first.")
            
        if not 0 < position_size <= 1:
            raise ValueError("Position size must be between 0 and 1")
            
        try:
            logger.info("Simulating trades")
            self.positions = []
            self.cash = self.initial_capital
            self.portfolio_value = []
            self.trade_history = []
            
            for date, row in self.data.iterrows():
                current_price = row['Adj Close']
                
                # Calculate current portfolio value
                positions_value = sum(shares * current_price for shares, _ in self.positions)
                total_value = self.cash + positions_value
                self.portfolio_value.append((date, total_value))
                
                # Check for buy signal
                if row['Signal'] == 1 and self.cash > 0:
                    # Calculate investment amount
                    investment = min(self.cash * position_size, self.cash)
                    shares = investment / current_price
                    
                    # Execute buy
                    self.positions.append((shares, current_price))
                    self.cash -= investment
                    
                    # Record trade
                    self.trade_history.append({
                        'date': date,
                        'action': 'BUY',
                        'shares': shares,
                        'price': current_price,
                        'investment': investment,
                        'cash_remaining': self.cash,
                        'portfolio_value': total_value
                    })
                    logger.debug(f"Buy order executed on {date}: {shares:.2f} shares at ${current_price:.2f}")
                
                # Check for sell conditions (simple: sell after 20 days)
                positions_to_remove = []
                for i, (shares, buy_price) in enumerate(self.positions):
                    buy_date = None
                    for trade in reversed(self.trade_history):
                        if trade['action'] == 'BUY' and abs(trade['price'] - buy_price) < 0.01:
                            buy_date = trade['date']
                            break
                    
                    if buy_date and (date - buy_date).days >= 20:
                        # Execute sell
                        sale_value = shares * current_price
                        self.cash += sale_value
                        positions_to_remove.append(i)
                        
                        # Record trade
                        self.trade_history.append({
                            'date': date,
                            'action': 'SELL',
                            'shares': shares,
                            'price': current_price,
                            'proceeds': sale_value,
                            'cash_remaining': self.cash,
                            'portfolio_value': total_value,
                            'profit': sale_value - (shares * buy_price)
                        })
                        logger.debug(f"Sell order executed on {date}: {shares:.2f} shares at ${current_price:.2f}")
                
                # Remove sold positions (reverse to avoid index issues)
                for i in sorted(positions_to_remove, reverse=True):
                    if i < len(self.positions):
                        self.positions.pop(i)
            
            logger.info("Trade simulation completed successfully")
        except Exception as e:
            logger.error(f"Error simulating trades: {e}")
            raise
    
    def get_results(self) -> Dict:
        """
        Get simulation results including performance metrics.
        
        Returns:
            Dictionary containing simulation results
        """
        if not self.portfolio_value:
            raise ValueError("No simulation results available. Run simulation first.")
            
        try:
            initial_value = self.initial_capital
            final_value = self.portfolio_value[-1][1]
            total_return = (final_value - initial_value) / initial_value * 100
            
            # Calculate profit from trades
            total_profit = sum(
                trade['profit'] for trade in self.trade_history 
                if trade['action'] == 'SELL' and 'profit' in trade
            )
            
            # Count trades
            buy_trades = sum(1 for trade in self.trade_history if trade['action'] == 'BUY')
            sell_trades = sum(1 for trade in self.trade_history if trade['action'] == 'SELL')
            
            # Calculate win rate
            winning_trades = sum(
                1 for trade in self.trade_history 
                if trade['action'] == 'SELL' and trade.get('profit', 0) > 0
            )
            win_rate = (winning_trades / sell_trades * 100) if sell_trades > 0 else 0
            
            return {
                'ticker': self.ticker,
                'initial_capital': initial_value,
                'final_portfolio_value': final_value,
                'total_return_pct': total_return,
                'total_profit': total_profit,
                'total_trades': buy_trades + sell_trades,
                'buy_trades': buy_trades,
                'sell_trades': sell_trades,
                'win_rate_pct': win_rate,
                'trade_history': self.trade_history,
                'portfolio_value_history': self.portfolio_value
            }
        except Exception as e:
            logger.error(f"Error calculating results: {e}")
            raise

def run_simulation(ticker: str, start_date: str, end_date: str, initial_capital: float = 10000.0) -> Dict:
    """
    Run complete simulation pipeline.
    
    Args:
        ticker: Stock ticker symbol
        start_date: Simulation start date (YYYY-MM-DD)
        end_date: Simulation end date (YYYY-MM-DD)
        initial_capital: Starting investment amount
        
    Returns:
        Simulation results dictionary
    """
    try:
        simulator = SyncExpertTradeSimulator(ticker, initial_capital)
        simulator.fetch_historical_data(start_date, end_date)
        simulator.generate_signals()
        simulator.simulate_trades()
        return simulator.get_results()
    except Exception as e:
        logger.error(f"Simulation failed: {e}")
        raise

# Example usage
if __name__ == "__
