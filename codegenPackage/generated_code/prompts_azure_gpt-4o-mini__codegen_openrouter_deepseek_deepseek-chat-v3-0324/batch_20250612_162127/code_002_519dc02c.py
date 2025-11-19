"""
Generated Code Metadata:
========================
Original URL: https://paybackclaimltd.com
Prompt: Create a function that analyzes transaction data to identify potential cryptocurrency fraud, as discussed in the Payback Claim Ltd. services.
Generated: DETERMINISTIC_519dc02c5f4dadf3
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

class CryptocurrencyFraudAnalyzer:
    """
    A class to analyze cryptocurrency transaction data for potential fraud indicators.
    """
    
    def __init__(self, transaction_data: pd.DataFrame):
        """
        Initialize the analyzer with transaction data.
        
        Args:
            transaction_data (pd.DataFrame): DataFrame containing transaction records with columns:
                - timestamp: datetime of transaction
                - sender: sender wallet address
                - receiver: receiver wallet address
                - amount: transaction amount in cryptocurrency
                - currency: cryptocurrency type (e.g., BTC, ETH)
                - transaction_hash: unique hash for the transaction
        """
        self.data = transaction_data.copy()
        self._validate_data()
        self._preprocess_data()
        
    def _validate_data(self) -> None:
        """
        Validate the input data structure and content.
        Raises ValueError if data doesn't meet requirements.
        """
        required_columns = {'timestamp', 'sender', 'receiver', 'amount', 'currency', 'transaction_hash'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if self.data.isnull().values.any():
            raise ValueError("Data contains null values")
            
    def _preprocess_data(self) -> None:
        """
        Preprocess the transaction data for analysis.
        """
        # Convert timestamp to datetime if it's not already
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
        
        # Sort by timestamp
        self.data.sort_values('timestamp', inplace=True)
        
        # Add day column for time-based analysis
        self.data['day'] = self.data['timestamp'].dt.date
        
    def detect_high_frequency_transactions(self, threshold: int = 10) -> pd.DataFrame:
        """
        Detect wallets with unusually high transaction frequency.
        
        Args:
            threshold (int): Minimum number of transactions per hour to flag as suspicious
            
        Returns:
            pd.DataFrame: Suspicious transactions with frequency counts
        """
        # Group by sender and hour
        freq_df = self.data.copy()
        freq_df['hour'] = freq_df['timestamp'].dt.floor('H')
        
        # Count transactions per sender per hour
        counts = freq_df.groupby(['sender', 'hour']).size().reset_index(name='count')
        
        # Filter for suspicious activity
        suspicious = counts[counts['count'] >= threshold]
        
        # Merge with original data to get full transaction details
        result = pd.merge(
            suspicious,
            self.data,
            on='sender',
            how='left'
        )
        
        # Filter to only include transactions in the same hour
        result = result[result['timestamp'].dt.floor('H') == result['hour']]
        
        return result
    
    def detect_pump_and_dump(self, window_hours: int = 24, volume_change_threshold: float = 2.0) -> Optional[Dict]:
        """
        Detect potential pump-and-dump patterns for a cryptocurrency.
        
        Args:
            window_hours (int): Time window to analyze for volume spikes
            volume_change_threshold (float): Minimum volume increase factor to consider suspicious
            
        Returns:
            Optional[Dict]: Dictionary with pump details if detected, None otherwise
        """
        if len(self.data['currency'].unique()) > 1:
            raise ValueError("This analysis requires data for a single cryptocurrency")
            
        # Calculate hourly transaction volume
        volume = self.data.resample('H', on='timestamp')['amount'].sum()
        
        if len(volume) < window_hours:
            return None
            
        # Find the maximum volume spike
        max_volume = volume.rolling(window=window_hours).max()
        current_volume = volume.iloc[-1]
        
        if current_volume >= volume_change_threshold * max_volume:
            return {
                'currency': self.data['currency'].iloc[0],
                'volume_increase': current_volume / max_volume,
                'peak_volume': current_volume,
                'time_window': f'{window_hours} hours'
            }
        return None
        
    def detect_self_transfers(self) -> pd.DataFrame:
        """
        Detect transactions where sender and receiver are the same wallet.
        
        Returns:
            pd.DataFrame: Transactions where sender == receiver
        """
        return self.data[self.data['sender'] == self.data['receiver']]
    
    def detect_unusual_amounts(self, z_score_threshold: float = 3.0) -> pd.DataFrame:
        """
        Detect transactions with unusually large amounts using z-score.
        
        Args:
            z_score_threshold (float): Minimum z-score to consider unusual
            
        Returns:
            pd.DataFrame: Transactions with amounts exceeding the z-score threshold
        """
        amounts = self.data['amount']
        mean = amounts.mean()
        std = amounts.std()
        
        if std == 0:  # All amounts are identical
            return pd.DataFrame(columns=self.data.columns)
            
        self.data['z_score'] = (amounts - mean) / std
        return self.data[self.data['z_score'].abs() >= z_score_threshold]
    
    def detect_micro_transactions(self, threshold: float = 0.0001) -> pd.DataFrame:
        """
        Detect very small transactions that could be test transactions.
        
        Args:
            threshold (float): Maximum amount to consider as micro-transaction
            
        Returns:
            pd.DataFrame: Transactions with amounts below the threshold
        """
        return self.data[self.data['amount'] <= threshold]
    
    def analyze_all(self) -> Dict:
        """
        Run all fraud detection methods and return combined results.
        
        Returns:
            Dict: Dictionary containing all detected potential fraud indicators
        """
        results = {
            'high_frequency': self.detect_high_frequency_transactions(),
            'self_transfers': self.detect_self_transfers(),
            'unusual_amounts': self.detect_unusual_amounts(),
            'micro_transactions': self.detect_micro_transactions(),
            'pump_and_dump': self.detect_pump_and_dump()
        }
        return results

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='min'),
        'sender': ['wallet1'] * 50 + ['wallet2'] * 50,
        'receiver': ['wallet2'] * 50 + ['wallet1'] * 50,
        'amount': [0.1] * 50 + [1000] * 50,
        'currency': ['BTC'] * 100,
        'transaction_hash': [f'tx{i}' for i in range(100)]
    })
    
    analyzer = CryptocurrencyFraudAnalyzer(sample_data)
    fraud_indicators = analyzer.analyze_all()
    
    for indicator, data in fraud_indicators.items():
        print(f"\n{indicator.replace('_', ' ').title()}:\n")
        print(data if not data.empty else "No suspicious activity detected")
```
