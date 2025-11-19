"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-lifestyle-pro.com
Prompt: Create a Python script to monitor and analyze trading performance, including metrics like profit/loss and trade accuracy, for a trading software like Bitcoin Lifestyle.
Generated: DETERMINISTIC_f61abf31007d05dd
Batch ID: 20250622_211305
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
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_performance.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingPerformanceAnalyzer:
    """
    A class to monitor and analyze trading performance metrics.
    """
    
    def __init__(self, trades_file=None):
        """
        Initialize the analyzer with optional trades data file.
        
        Args:
            trades_file (str): Path to CSV file containing trades data
        """
        self.trades = pd.DataFrame()
        if trades_file and os.path.exists(trades_file):
            self.load_trades(trades_file)
    
    def load_trades(self, file_path):
        """
        Load trades data from CSV file.
        
        Args:
            file_path (str): Path to CSV file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        try:
            self.trades = pd.read_csv(file_path, parse_dates=['entry_time', 'exit_time'])
            required_columns = {'entry_price', 'exit_price', 'entry_time', 
                               'exit_time', 'position_type', 'size'}
            if not required_columns.issubset(self.trades.columns):
                raise ValueError("CSV file missing required columns")
            logger.info(f"Successfully loaded {len(self.trades)} trades from {file_path}")
        except Exception as e:
            logger.error(f"Error loading trades file: {str(e)}")
            raise
    
    def add_trade(self, entry_price, exit_price, entry_time, exit_time, 
                  position_type, size, fees=0.0, notes=None):
        """
        Add a single trade to the analyzer.
        
        Args:
            entry_price (float): Entry price
            exit_price (float): Exit price
            entry_time (datetime): Entry timestamp
            exit_time (datetime): Exit timestamp
            position_type (str): 'long' or 'short'
            size (float): Position size
            fees (float): Trading fees
            notes (str): Optional trade notes
        """
        try:
            new_trade = {
                'entry_price': entry_price,
                'exit_price': exit_price,
                'entry_time': pd.to_datetime(entry_time),
                'exit_time': pd.to_datetime(exit_time),
                'position_type': position_type.lower(),
                'size': size,
                'fees': fees,
                'notes': notes,
                'profit': self._calculate_profit(entry_price, exit_price, position_type, size, fees)
            }
            
            self.trades = pd.concat([
                self.trades,
                pd.DataFrame([new_trade])
            ], ignore_index=True)
            logger.info("Added new trade successfully")
        except Exception as e:
            logger.error(f"Error adding trade: {str(e)}")
            raise
    
    def _calculate_profit(self, entry_price, exit_price, position_type, size, fees):
        """
        Calculate profit for a single trade.
        
        Args:
            entry_price (float): Entry price
            exit_price (float): Exit price
            position_type (str): 'long' or 'short'
            size (float): Position size
            fees (float): Trading fees
            
        Returns:
            float: Calculated profit
        """
        position_type = position_type.lower()
        if position_type == 'long':
            return (exit_price - entry_price) * size - fees
        elif position_type == 'short':
            return (entry_price - exit_price) * size - fees
        else:
            raise ValueError("position_type must be either 'long' or 'short'")
    
    def calculate_metrics(self):
        """
        Calculate performance metrics for all trades.
        
        Returns:
            dict: Dictionary containing calculated metrics
        """
        if self.trades.empty:
            logger.warning("No trades available to calculate metrics")
            return {}
        
        try:
            metrics = {}
            
            # Basic metrics
            metrics['total_trades'] = len(self.trades)
            metrics['winning_trades'] = len(self.trades[self.trades['profit'] > 0])
            metrics['losing_trades'] = len(self.trades[self.trades['profit'] < 0])
            metrics['breakeven_trades'] = len(self.trades[self.trades['profit'] == 0])
            
            # Profit metrics
            metrics['total_profit'] = self.trades['profit'].sum()
            metrics['average_profit'] = self.trades['profit'].mean()
            metrics['median_profit'] = self.trades['profit'].median()
            metrics['max_profit'] = self.trades['profit'].max()
            metrics['max_loss'] = self.trades['profit'].min()
            
            # Accuracy metrics
            metrics['win_rate'] = metrics['winning_trades'] / metrics['total_trades'] * 100
            metrics['loss_rate'] = metrics['losing_trades'] / metrics['total_trades'] * 100
            
            # Risk/reward metrics
            avg_win = self.trades[self.trades['profit'] > 0]['profit'].mean()
            avg_loss = abs(self.trades[self.trades['profit'] < 0]['profit'].mean())
            metrics['risk_reward_ratio'] = avg_win / avg_loss if avg_loss != 0 else np.inf
            
            # Position metrics
            metrics['long_positions'] = len(self.trades[self.trades['position_type'] == 'long'])
            metrics['short_positions'] = len(self.trades[self.trades['position_type'] == 'short'])
            
            # Duration metrics
            durations = (self.trades['exit_time'] - self.trades['entry_time']).dt.total_seconds()
            metrics['avg_trade_duration_seconds'] = durations.mean()
            
            return metrics
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            raise
    
    def generate_report(self, output_file=None):
        """
        Generate a performance report with metrics.
        
        Args:
            output_file (str): Optional file path to save report
            
        Returns:
            str: Formatted report text
        """
        metrics = self.calculate_metrics()
        if not metrics:
            return "No trades available to generate report"
        
        report_lines = [
            "Trading Performance Report",
            "=========================",
            f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            f"Total Trades: {metrics['total_trades']}",
            f"Winning Trades: {metrics['winning_trades']} ({metrics['win_rate']:.2f}%)",
            f"Losing Trades: {metrics['losing_trades']} ({metrics['loss_rate']:.2f}%)",
            f"Breakeven Trades: {metrics['breakeven_trades']}",
            "",
            "Profit Metrics:",
            f"  Total Profit: {metrics['total_profit']:.2f}",
            f"  Average Profit: {metrics['average_profit']:.2f}",
            f"  Median Profit: {metrics['median_profit']:.2f}",
            f"  Max Profit: {metrics['max_profit']:.2f}",
            f"  Max Loss: {metrics['max_loss']:.2f}",
            "",
            "Position Metrics:",
            f"  Long Positions: {metrics['long_positions']}",
            f"  Short Positions: {metrics['short_positions']}",
            "",
            "Risk/Reward:",
            f"  Risk/Reward Ratio: {metrics['risk_reward_ratio']:.2f}",
            "",
            "Duration Metrics:",
            f"  Average Trade Duration: {metrics['avg_trade_duration_seconds']:.2f} seconds",
        ]
        
        report_text = "\n".join(report_lines)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(report_text)
                logger.info(f"Report saved to {output_file}")
            except Exception as e:
                logger.error(f"Error saving report: {str(e)}")
        
        return report_text
    
    def save_trades(self, file_path):
        """
        Save current trades to CSV file.
        
        Args:
            file_path (str): Path to save CSV file
            
        Raises:
            ValueError: If no trades to save
        """
        if self.trades.empty:
            raise ValueError("No trades to save")
        
        try:
            self.trades.to_csv(file_path, index=False)
            logger.info(f"Saved {len(self.trades)} trades to {file_path}")
        except Exception as e:
            logger.error(f"Error saving trades: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    analyzer = TradingPerformanceAnalyzer()
    
    # Example trades
    analyzer.add_trade(
        entry_price=50000,
        exit_price=
