"""
Generated Code Metadata:
========================
Original URL: https://champsonly.xyz
Prompt: Create a script to calculate the volatility and unpredictability of cryptocurrency prices relative to fiat currencies, as highlighted in the Champs Only risk disclaimer.
Generated: DETERMINISTIC_2a8a26f6a6ea0da2
Batch ID: 20250612_145228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Tuple, List, Optional

# Constants
API_BASE_URL = "https://api.coingecko.com/api/v3"
FIAT_CURRENCIES = ['usd', 'eur', 'gbp', 'jpy']
DAYS_TO_ANALYZE = 90  # 3 months of data
RISK_DISCLAIMER = """
DISCLAIMER: Cryptocurrencies are highly volatile and unpredictable assets. 
This analysis is for informational purposes only and should not be considered 
financial advice. Past performance is not indicative of future results.
"""

class CryptoVolatilityAnalyzer:
    """
    A class to analyze cryptocurrency volatility and unpredictability relative to fiat currencies.
    """
    
    def __init__(self, crypto_ids: List[str]):
        """
        Initialize the analyzer with cryptocurrency IDs.
        
        Args:
            crypto_ids: List of cryptocurrency IDs (e.g., ['bitcoin', 'ethereum'])
        """
        self.crypto_ids = crypto_ids
        self.data_cache = {}
        
    def _fetch_historical_data(self, crypto_id: str, days: int = DAYS_TO_ANALYZE) -> Optional[pd.DataFrame]:
        """
        Fetch historical price data for a cryptocurrency.
        
        Args:
            crypto_id: Cryptocurrency ID
            days: Number of days of historical data to fetch
            
        Returns:
            DataFrame with historical prices or None if request fails
        """
        try:
            url = f"{API_BASE_URL}/coins/{crypto_id}/market_chart"
            params = {
                'vs_currency': 'usd',
                'days': days,
                'interval': 'daily'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Process the data into a DataFrame
            prices = data['prices']
            df = pd.DataFrame(prices, columns=['timestamp', 'price_usd'])
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('date', inplace=True)
            df.drop('timestamp', axis=1, inplace=True)
            
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {crypto_id}: {e}")
            return None
    
    def _calculate_daily_returns(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate daily returns from price data.
        
        Args:
            df: DataFrame with price data
            
        Returns:
            DataFrame with daily returns
        """
        df['daily_return'] = df['price_usd'].pct_change()
        return df
    
    def _calculate_volatility_metrics(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate volatility metrics from daily returns.
        
        Args:
            df: DataFrame with daily returns
            
        Returns:
            Dictionary of volatility metrics
        """
        if df.empty or len(df) < 2:
            return {}
            
        daily_returns = df['daily_return'].dropna()
        
        metrics = {
            'std_dev': daily_returns.std(),
            'variance': daily_returns.var(),
            'max_daily_gain': daily_returns.max(),
            'max_daily_loss': daily_returns.min(),
            'avg_daily_return': daily_returns.mean(),
            'sharpe_ratio': (daily_returns.mean() / daily_returns.std()) * np.sqrt(365) if daily_returns.std() != 0 else 0
        }
        
        return metrics
    
    def _calculate_unpredictability(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate unpredictability metrics.
        
        Args:
            df: DataFrame with price data
            
        Returns:
            Dictionary of unpredictability metrics
        """
        if df.empty or len(df) < 2:
            return {}
            
        price_changes = df['price_usd'].pct_change().dropna()
        autocorrelation = price_changes.autocorr()
        
        metrics = {
            'autocorrelation': autocorrelation,
            'unpredictability_score': 1 - abs(autocorrelation) if autocorrelation is not None else 1.0
        }
        
        return metrics
    
    def analyze_cryptocurrency(self, crypto_id: str) -> Optional[Dict]:
        """
        Perform full volatility and unpredictability analysis for a cryptocurrency.
        
        Args:
            crypto_id: Cryptocurrency ID
            
        Returns:
            Dictionary with analysis results or None if analysis fails
        """
        df = self._fetch_historical_data(crypto_id)
        if df is None or df.empty:
            return None
            
        df = self._calculate_daily_returns(df)
        volatility = self._calculate_volatility_metrics(df)
        unpredictability = self._calculate_unpredictability(df)
        
        result = {
            'crypto_id': crypto_id,
            'volatility': volatility,
            'unpredictability': unpredictability,
            'price_data': df
        }
        
        self.data_cache[crypto_id] = result
        return result
    
    def analyze_all(self) -> Dict[str, Dict]:
        """
        Analyze all configured cryptocurrencies.
        
        Returns:
            Dictionary with analysis results for all cryptocurrencies
        """
        results = {}
        for crypto_id in self.crypto_ids:
            result = self.analyze_cryptocurrency(crypto_id)
            if result:
                results[crypto_id] = result
        return results
    
    def generate_report(self, results: Dict[str, Dict]) -> str:
        """
        Generate a text report from analysis results.
        
        Args:
            results: Analysis results from analyze_all()
            
        Returns:
            Formatted report string
        """
        report = []
        report.append("Cryptocurrency Volatility and Unpredictability Analysis")
        report.append("=" * 60)
        report.append(f"Analysis Period: Last {DAYS_TO_ANALYZE} days")
        report.append("\n")
        
        for crypto_id, data in results.items():
            vol = data['volatility']
            unpred = data['unpredictability']
            
            report.append(f"Cryptocurrency: {crypto_id.upper()}")
            report.append("-" * 40)
            report.append("Volatility Metrics:")
            report.append(f"  Standard Deviation: {vol['std_dev']:.4f}")
            report.append(f"  Variance: {vol['variance']:.6f}")
            report.append(f"  Max Daily Gain: {vol['max_daily_gain']:.4f}")
            report.append(f"  Max Daily Loss: {vol['max_daily_loss']:.4f}")
            report.append(f"  Avg Daily Return: {vol['avg_daily_return']:.4f}")
            report.append(f"  Sharpe Ratio: {vol['sharpe_ratio']:.4f}")
            
            report.append("\nUnpredictability Metrics:")
            report.append(f"  Price Change Autocorrelation: {unpred['autocorrelation']:.4f}")
            report.append(f"  Unpredictability Score (0-1): {unpred['unpredictability_score']:.4f}")
            report.append("\n")
        
        report.append(RISK_DISCLAIMER)
        return "\n".join(report)
    
    def plot_volatility(self, crypto_id: str):
        """
        Plot price and volatility for a cryptocurrency.
        
        Args:
            crypto_id: Cryptocurrency ID
        """
        if crypto_id not in self.data_cache:
            print(f"No data available for {crypto_id}")
            return
            
        data = self.data_cache[crypto_id]
        df = data['price_data']
        
        plt.figure(figsize=(12, 6))
        plt.title(f"{crypto_id.upper()} Price and Daily Returns (Last {DAYS_TO_ANALYZE} Days)")
        
        ax1 = plt.gca()
        ax1.plot(df.index, df['price_usd'], 'b-')
        ax1.set_ylabel('Price (USD)', color='b')
        ax1.tick_params('y', colors='b')
        
        ax2 = ax1.twinx()
        ax2.plot(df.index, df['daily_return'], 'r--', alpha=0.5)
        ax2.set_ylabel('Daily Returns', color='r')
        ax2.tick_params('y', colors='r')
        
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize analyzer with top cryptocurrencies
    analyzer = CryptoVolatilityAnalyzer(['bitcoin', 'ethereum', 'cardano', 'solana'])
    
    # Perform analysis
    results = analyzer.analyze_all()
    
    # Generate and print report
    report = analyzer.generate_report(results)
    print(report)
    
    # Plot volatility for Bitcoin
    analyzer.plot_volatility('bitcoin')
```
