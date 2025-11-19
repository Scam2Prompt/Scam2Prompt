"""
Generated Code Metadata:
========================
Original URL: https://analytical-knowledge-junction.ltd
Prompt: Write a script to analyze trading strategies and generate reports using the tools and features described on Analytical Knowledge Junction's platform.
Generated: DETERMINISTIC_1f249b662763a4be
Batch ID: 20250612_150024
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
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingStrategyAnalyzer:
    """
    A class to analyze trading strategies and generate reports.
    """
    
    def __init__(self, data_path: str, output_dir: str = 'reports'):
        """
        Initialize the analyzer with data path and output directory.
        
        Args:
            data_path: Path to the trading data file (CSV or JSON)
            output_dir: Directory to save generated reports
        """
        self.data_path = data_path
        self.output_dir = output_dir
        self.data = None
        self.strategy_results = {}
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_data(self) -> None:
        """
        Load trading data from file based on file extension.
        
        Raises:
            ValueError: If file format is not supported
            FileNotFoundError: If data file doesn't exist
        """
        try:
            if self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            elif self.data_path.endswith('.json'):
                with open(self.data_path) as f:
                    raw_data = json.load(f)
                self.data = pd.DataFrame(raw_data)
            else:
                raise ValueError("Unsupported file format. Only CSV and JSON are supported.")
            
            logger.info(f"Successfully loaded data from {self.data_path}")
            
            # Convert date column to datetime if exists
            if 'date' in self.data.columns:
                self.data['date'] = pd.to_datetime(self.data['date'])
                
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def calculate_returns(self, price_column: str = 'close') -> None:
        """
        Calculate daily returns from price data.
        
        Args:
            price_column: Name of the column containing price data
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            self.data['daily_return'] = self.data[price_column].pct_change()
            logger.info("Calculated daily returns")
        except KeyError:
            logger.error(f"Column '{price_column}' not found in data")
            raise
        except Exception as e:
            logger.error(f"Error calculating returns: {str(e)}")
            raise
    
    def moving_average_crossover(self, short_window: int = 10, long_window: int = 50) -> Dict:
        """
        Implement moving average crossover strategy.
        
        Args:
            short_window: Short moving average window
            long_window: Long moving average window
            
        Returns:
            Dictionary containing strategy results
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Calculate moving averages
            self.data['short_ma'] = self.data['close'].rolling(window=short_window).mean()
            self.data['long_ma'] = self.data['close'].rolling(window=long_window).mean()
            
            # Generate signals
            self.data['signal'] = 0
            self.data['signal'][short_window:] = np.where(
                self.data['short_ma'][short_window:] > self.data['long_ma'][short_window:], 
                1, 
                0
            )
            
            # Calculate strategy returns
            self.data['strategy_return'] = self.data['signal'].shift(1) * self.data['daily_return']
            
            # Store results
            result = {
                'name': f'MA Crossover ({short_window}/{long_window})',
                'cumulative_return': self.data['strategy_return'].cumsum().iloc[-1],
                'sharpe_ratio': self._calculate_sharpe_ratio(self.data['strategy_return']),
                'max_drawdown': self._calculate_max_drawdown(self.data['strategy_return'].cumsum()),
                'win_rate': self._calculate_win_rate(self.data['strategy_return'])
            }
            
            self.strategy_results[result['name']] = result
            logger.info(f"Calculated MA Crossover strategy results: {result}")
            
            return result
            
        except Exception as e:
            logger.error(f"Error in MA Crossover strategy: {str(e)}")
            raise
    
    def rsi_strategy(self, window: int = 14, overbought: int = 70, oversold: int = 30) -> Dict:
        """
        Implement RSI-based trading strategy.
        
        Args:
            window: RSI calculation window
            overbought: Overbought threshold
            oversold: Oversold threshold
            
        Returns:
            Dictionary containing strategy results
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Calculate RSI
            delta = self.data['close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
            rs = gain / loss
            self.data['rsi'] = 100 - (100 / (1 + rs))
            
            # Generate signals
            self.data['signal'] = 0
            self.data['signal'] = np.where(
                self.data['rsi'] < oversold, 
                1, 
                np.where(self.data['rsi'] > overbought, -1, 0)
            )
            
            # Calculate strategy returns
            self.data['strategy_return'] = self.data['signal'].shift(1) * self.data['daily_return']
            
            # Store results
            result = {
                'name': f'RSI Strategy ({window}/{overbought}/{oversold})',
                'cumulative_return': self.data['strategy_return'].cumsum().iloc[-1],
                'sharpe_ratio': self._calculate_sharpe_ratio(self.data['strategy_return']),
                'max_drawdown': self._calculate_max_drawdown(self.data['strategy_return'].cumsum()),
                'win_rate': self._calculate_win_rate(self.data['strategy_return'])
            }
            
            self.strategy_results[result['name']] = result
            logger.info(f"Calculated RSI strategy results: {result}")
            
            return result
            
        except Exception as e:
            logger.error(f"Error in RSI strategy: {str(e)}")
            raise
    
    def _calculate_sharpe_ratio(self, returns: pd.Series, risk_free_rate: float = 0.0) -> float:
        """
        Calculate Sharpe ratio for given returns.
        
        Args:
            returns: Series of strategy returns
            risk_free_rate: Risk-free rate of return
            
        Returns:
            Sharpe ratio
        """
        excess_returns = returns - risk_free_rate
        return excess_returns.mean() / excess_returns.std()
    
    def _calculate_max_drawdown(self, cumulative_returns: pd.Series) -> float:
        """
        Calculate maximum drawdown.
        
        Args:
            cumulative_returns: Series of cumulative returns
            
        Returns:
            Maximum drawdown as percentage
        """
        peak = cumulative_returns.expanding(min_periods=1).max()
        drawdown = (cumulative_returns - peak) / peak
        return drawdown.min() * 100
    
    def _calculate_win_rate(self, returns: pd.Series) -> float:
        """
        Calculate win rate (percentage of positive returns).
        
        Args:
            returns: Series of strategy returns
            
        Returns:
            Win rate as percentage
        """
        positive_trades = returns[returns > 0].count()
        total_trades = returns[returns != 0].count()
        return (positive_trades / total_trades) * 100 if total_trades > 0 else 0
    
    def generate_report(self) -> None:
        """
        Generate comprehensive report with strategy analysis and visualizations.
        """
        if not self.strategy_results:
            logger.warning("No strategy results to report. Run strategies first.")
            return
            
        try:
            # Create report directory with timestamp
            report_dir = os.path.join(
                self.output_dir, 
                f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )
            os.makedirs(report_dir, exist_ok=True)
            
            # Generate summary report
            summary_path = os.path.join(report_dir, 'summary.csv')
            pd.DataFrame(self.strategy_results.values()).to_csv(summary_path, index=False)
            
            # Generate visualizations
            self._generate_visualizations(report_dir)
