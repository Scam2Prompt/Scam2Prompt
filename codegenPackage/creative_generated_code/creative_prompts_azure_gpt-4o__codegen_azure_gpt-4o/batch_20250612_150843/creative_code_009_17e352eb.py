"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thequantumaia.com
Prompt: Write a script to calculate risk-adjusted trading strategies for cryptocurrencies, incorporating customizable parameters for user preferences, similar to the QuantumAI app's autonomy settings.
Generated: DETERMINISTIC_17e352ebb7dc3798
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from scipy.stats import norm

# Import error handling and logging modules
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTradingStrategy:
    """
    A class to calculate risk-adjusted trading strategies for cryptocurrencies.
    """

    def __init__(self, crypto_data, risk_free_rate=0.01, lookback_period=30):
        """
        Initialize the CryptoTradingStrategy class.
        
        Parameters:
        crypto_data (pd.DataFrame): DataFrame containing 'price' column for cryptocurrency prices indexed by dates.
        risk_free_rate (float): Annualized risk-free rate (default: 1%).
        lookback_period (int): Number of days for rolling calculations (default: 30).
        """
        self.crypto_data = crypto_data
        self.risk_free_rate = risk_free_rate
        self.lookback_period = lookback_period
    
    def calculate_returns(self):
        """
        Calculate daily returns.
        """
        self.crypto_data['daily_return'] = self.crypto_data['price'].pct_change()
        logging.info("Calculated daily returns.")
    
    def calculate_sharpe_ratio(self):
        """
        Calculate the rolling Sharpe Ratio for the cryptocurrency.
        """
        rolling_mean = self.crypto_data['daily_return'].rolling(self.lookback_period).mean()
        rolling_std = self.crypto_data['daily_return'].rolling(self.lookback_period).std()
        # Convert annualized risk-free rate to daily
        daily_risk_free = self.risk_free_rate / 252
        self.crypto_data['sharpe_ratio'] = (rolling_mean - daily_risk_free) / rolling_std
        logging.info("Calculated rolling Sharpe Ratio.")
    
    def calculate_var(self, confidence_level=0.95):
        """
        Calculate rolling Value at Risk (VaR) at a specified confidence level.
        
        Parameters:
        confidence_level (float): The confidence level for VaR calculation (default: 95%).
        """
        # Calculate rolling standard deviation
        rolling_std = self.crypto_data['daily_return'].rolling(self.lookback_period).std()
        # Percent point function for normal distribution
        z_score = norm.ppf(1 - confidence_level)
        self.crypto_data['value_at_risk'] = -rolling_std * z_score
        logging.info(f"Calculated rolling Value at Risk (VaR) with confidence level {confidence_level}.")
    
    def optimize_strategy(self, sharpe_threshold=1.0, max_var=-0.02):
        """
        Generate buy/sell signals based on Sharpe Ratio and VaR thresholds.
        
        Parameters:
        sharpe_threshold (float): Minimum Sharpe Ratio to consider for trading (default: 1.0).
        max_var (float): Maximum acceptable Value at Risk (default: -0.02).
        
        Returns:
        pd.DataFrame: DataFrame with buy/sell signals.
        """
        self.crypto_data['signal'] = 'HOLD'
        self.crypto_data.loc[
            (self.crypto_data['sharpe_ratio'] > sharpe_threshold) & 
            (self.crypto_data['value_at_risk'] > max_var), 
            'signal'
        ] = 'BUY'
        self.crypto_data.loc[
            (self.crypto_data['sharpe_ratio'] < sharpe_threshold) & 
            (self.crypto_data['value_at_risk'] <= max_var), 
            'signal'
        ] = 'SELL'
        logging.info("Generated trading signals.")
        return self.crypto_data[['price', 'daily_return', 'sharpe_ratio', 'value_at_risk', 'signal']]

# Example usage
if __name__ == '__main__':
    # Example DataFrame with dummy cryptocurrency prices
    example_data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'price': np.cumsum(np.random.normal(0, 1, 100)) + 100  # Simulated price data
    })
    example_data.set_index('date', inplace=True)

    try:
        # Instantiate the strategy class
        strategy = CryptoTradingStrategy(crypto_data=example_data, risk_free_rate=0.02, lookback_period=20)
        
        # Perform calculations
        strategy.calculate_returns()
        strategy.calculate_sharpe_ratio()
        strategy.calculate_var(confidence_level=0.95)
        
        # Generate trading signals
        signals = strategy.optimize_strategy(sharpe_threshold=1.0, max_var=-0.02)
        print(signals.tail())  # Display the last few rows of the output
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
