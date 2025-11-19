"""
Generated Code Metadata:
========================
Original URL: https://financial-justice.com
Prompt: Create a program that flags suspicious trading activity indicative of Forex scams, referencing the details provided by Financial Justice.
Generated: DETERMINISTIC_8b08f5b82910b7cd
Batch ID: 20250612_150446
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
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class ForexScamDetector:
    """
    A class to detect suspicious trading activities in Forex markets that may indicate scams.
    References Financial Justice guidelines for scam indicators.
    """
    
    def __init__(self, data_path=None, df=None):
        """
        Initialize the detector with either a file path or a DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing trading data. Defaults to None.
            df (pd.DataFrame, optional): DataFrame containing trading data. Defaults to None.
        """
        if data_path:
            self.df = pd.read_csv(data_path)
        elif df is not None:
            self.df = df.copy()
        else:
            raise ValueError("Either data_path or df must be provided")
            
        self._preprocess_data()
        
    def _preprocess_data(self):
        """Preprocess the trading data for analysis."""
        # Convert timestamp to datetime
        if 'timestamp' in self.df.columns:
            self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
            self.df.sort_values('timestamp', inplace=True)
            
        # Ensure required columns exist
        required_columns = ['account_id', 'amount', 'profit_loss']
        for col in required_columns:
            if col not in self.df.columns:
                raise ValueError(f"Missing required column: {col}")
    
    def detect_unusual_profits(self, threshold=0.9):
        """
        Flag accounts with unusually high profit rates.
        
        Args:
            threshold (float): Profit threshold (0-1) to consider as suspicious. Defaults to 0.9.
            
        Returns:
            pd.DataFrame: Accounts with suspicious profit rates.
        """
        account_stats = self.df.groupby('account_id')['profit_loss'].agg(['count', 'sum'])
        account_stats['profit_rate'] = account_stats['sum'] / account_stats['count']
        
        suspicious = account_stats[account_stats['profit_rate'] > threshold].reset_index()
        return suspicious
    
    def detect_high_frequency_trading(self, time_window='1H', threshold=100):
        """
        Flag accounts with unusually high trading frequency.
        
        Args:
            time_window (str): Pandas time window string. Defaults to '1H'.
            threshold (int): Minimum trades in window to flag. Defaults to 100.
            
        Returns:
            pd.DataFrame: Accounts with suspicious trading frequency.
        """
        if 'timestamp' not in self.df.columns:
            raise ValueError("Timestamp column required for frequency analysis")
            
        trades_per_window = self.df.groupby([
            'account_id',
            pd.Grouper(key='timestamp', freq=time_window)
        ]).size().reset_index(name='trades')
        
        suspicious = trades_per_window[trades_per_window['trades'] > threshold]
        return suspicious
    
    def detect_large_transactions(self, amount_threshold=10000, count_threshold=5):
        """
        Flag accounts with multiple large transactions.
        
        Args:
            amount_threshold (float): Minimum amount to consider large. Defaults to 10000.
            count_threshold (int): Minimum count of large transactions to flag. Defaults to 5.
            
        Returns:
            pd.DataFrame: Accounts with suspicious large transactions.
        """
        large_txns = self.df[self.df['amount'] > amount_threshold]
        large_txns_count = large_txns.groupby('account_id').size().reset_index(name='count')
        
        suspicious = large_txns_count[large_txns_count['count'] >= count_threshold]
        return suspicious
    
    def detect_pump_and_dump(self, price_change_threshold=0.5, volume_threshold=0.8):
        """
        Detect potential pump-and-dump schemes.
        
        Args:
            price_change_threshold (float): Minimum price change to consider. Defaults to 0.5.
            volume_threshold (float): Minimum volume change to consider. Defaults to 0.8.
            
        Returns:
            pd.DataFrame: Potential pump-and-dump instances.
        """
        if 'price' not in self.df.columns or 'volume' not in self.df.columns:
            raise ValueError("Price and volume columns required for pump-and-dump detection")
            
        self.df['price_change'] = self.df['price'].pct_change()
        self.df['volume_change'] = self.df['volume'].pct_change()
        
        suspicious = self.df[
            (self.df['price_change'] > price_change_threshold) & 
            (self.df['volume_change'] > volume_threshold)
        ]
        return suspicious
    
    def detect_all_scams(self):
        """
        Run all detection methods and return combined results.
        
        Returns:
            dict: Dictionary containing all detection results.
        """
        results = {
            'unusual_profits': self.detect_unusual_profits(),
            'high_frequency': self.detect_high_frequency_trading(),
            'large_transactions': self.detect_large_transactions(),
            'pump_and_dump': self.detect_pump_and_dump()
        }
        return results
    
    def generate_report(self, output_path=None):
        """
        Generate a comprehensive report of suspicious activities.
        
        Args:
            output_path (str, optional): Path to save report. If None, returns report as string.
            
        Returns:
            str or None: Report content if output_path is None, else None.
        """
        results = self.detect_all_scams()
        report_lines = ["Forex Scam Detection Report", "="*30, ""]
        
        for method, df in results.items():
            report_lines.append(f"\n{method.replace('_', ' ').title()}:")
            report_lines.append("-"*len(report_lines[-1]))
            
            if df.empty:
                report_lines.append("No suspicious activity detected")
            else:
                report_lines.append(df.to_string())
        
        report = "\n".join(report_lines)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(report)
        else:
            return report

# Example usage
if __name__ == "__main__":
    # Sample data creation for demonstration
    data = {
        'account_id': np.random.choice(['A100', 'A101', 'A102', 'SCAM001'], 1000),
        'timestamp': pd.date_range(start='2023-01-01', periods=1000, freq='min'),
        'amount': np.random.uniform(10, 1000, 1000),
        'profit_loss': np.random.uniform(-1, 1, 1000),
        'price': np.random.uniform(1, 2, 1000),
        'volume': np.random.uniform(100, 1000, 1000)
    }
    
    # Create some suspicious patterns
    data['profit_loss'][:100] = 0.95  # Unusually high profits for first 100 trades
    data['amount'][-50:] = 15000      # Large transactions at the end
    data['price'][500:510] = data['price'][500:510] * 2  # Pump
    data['volume'][500:510] = data['volume'][500:510] * 2
    
    df = pd.DataFrame(data)
    
    # Initialize detector
    detector = ForexScamDetector(df=df)
    
    # Generate and print report
    print(detector.generate_report())
```
