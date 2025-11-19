"""
Generated Code Metadata:
========================
Original URL: https://7364500043.pages.dev
Prompt: Create a function to analyze on-chain data for Bitcoin, similar to the insights shared in Journal Du Coin's "Bitcoin: L'arme secrète pour démasquer la cupidité des investisseurs."
Generated: DETERMINISTIC_ff5f1548e6516039
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain.info": {
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
from typing import Dict, List, Optional, Tuple

class BitcoinOnChainAnalyzer:
    """
    A class to analyze Bitcoin on-chain data to uncover investor behavior patterns.
    Uses Blockchain.com API for data retrieval.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the analyzer with optional API key.
        
        Args:
            api_key (str, optional): API key for Blockchain.com. Defaults to None.
        """
        self.base_url = "https://api.blockchain.info"
        self.api_key = api_key
        self.headers = {'User-Agent': 'BitcoinOnChainAnalyzer/1.0'}
        
    def _make_api_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a request to the Blockchain.com API.
        
        Args:
            endpoint (str): API endpoint
            params (dict, optional): Query parameters. Defaults to None.
            
        Returns:
            dict: JSON response from API
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(
                url,
                params=params,
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def get_historical_price(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Get historical Bitcoin price data.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame with date and price columns
        """
        endpoint = "/charts/market-price"
        params = {
            'timespan': '1day',
            'start': start_date,
            'end': end_date,
            'format': 'json',
            'sampled': 'true'
        }
        
        if self.api_key:
            params['api_key'] = self.api_key
            
        data = self._make_api_request(endpoint, params)
        df = pd.DataFrame(data['values'])
        df['x'] = pd.to_datetime(df['x'], unit='ms')
        df.rename(columns={'x': 'date', 'y': 'price'}, inplace=True)
        return df
    
    def get_network_value_to_transaction_ratio(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Get Network Value to Transaction (NVT) ratio data.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame with date and NVT ratio columns
        """
        endpoint = "/charts/nvt"
        params = {
            'timespan': '1day',
            'start': start_date,
            'end': end_date,
            'format': 'json',
            'sampled': 'true'
        }
        
        if self.api_key:
            params['api_key'] = self.api_key
            
        data = self._make_api_request(endpoint, params)
        df = pd.DataFrame(data['values'])
        df['x'] = pd.to_datetime(df['x'], unit='ms')
        df.rename(columns={'x': 'date', 'y': 'nvt_ratio'}, inplace=True)
        return df
    
    def get_market_value_to_realized_value(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Get Market Value to Realized Value (MVRV) ratio data.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame with date and MVRV ratio columns
        """
        endpoint = "/charts/mvrv"
        params = {
            'timespan': '1day',
            'start': start_date,
            'end': end_date,
            'format': 'json',
            'sampled': 'true'
        }
        
        if self.api_key:
            params['api_key'] = self.api_key
            
        data = self._make_api_request(endpoint, params)
        df = pd.DataFrame(data['values'])
        df['x'] = pd.to_datetime(df['x'], unit='ms')
        df.rename(columns={'x': 'date', 'y': 'mvrv_ratio'}, inplace=True)
        return df
    
    def get_exchange_flows(self, days: int = 30) -> pd.DataFrame:
        """
        Get exchange inflow/outflow data.
        
        Args:
            days (int): Number of days to retrieve data for. Defaults to 30.
            
        Returns:
            pd.DataFrame: DataFrame with date, inflow, and outflow columns
        """
        endpoint = "/charts/transfers-volume"
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        params = {
            'timespan': '1day',
            'start': start_date.strftime('%Y-%m-%d'),
            'end': end_date.strftime('%Y-%m-%d'),
            'format': 'json',
            'sampled': 'true'
        }
        
        if self.api_key:
            params['api_key'] = self.api_key
            
        data = self._make_api_request(endpoint, params)
        df = pd.DataFrame(data['values'])
        df['x'] = pd.to_datetime(df['x'], unit='ms')
        df.rename(columns={'x': 'date', 'y': 'volume'}, inplace=True)
        return df
    
    def calculate_greed_fear_index(self, price_df: pd.DataFrame, mvrv_df: pd.DataFrame, nvt_df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate a composite greed/fear index based on multiple metrics.
        
        Args:
            price_df (pd.DataFrame): DataFrame with price data
            mvrv_df (pd.DataFrame): DataFrame with MVRV data
            nvt_df (pd.DataFrame): DataFrame with NVT data
            
        Returns:
            pd.DataFrame: DataFrame with date and greed_fear_index columns
        """
        # Merge all dataframes on date
        merged = price_df.merge(mvrv_df, on='date').merge(nvt_df, on='date')
        
        # Normalize metrics
        merged['price_norm'] = (merged['price'] - merged['price'].min()) / (merged['price'].max() - merged['price'].min())
        merged['mvrv_norm'] = (merged['mvrv_ratio'] - merged['mvrv_ratio'].min()) / (merged['mvrv_ratio'].max() - merged['mvrv_ratio'].min())
        merged['nvt_norm'] = (merged['nvt_ratio'] - merged['nvt_ratio'].min()) / (merged['nvt_ratio'].max() - merged['nvt_ratio'].min())
        
        # Calculate composite index (weighted average)
        merged['greed_fear_index'] = (
            0.4 * merged['price_norm'] + 
            0.4 * merged['mvrv_norm'] + 
            0.2 * merged['nvt_norm']
        ) * 100  # Scale to 0-100
        
        return merged[['date', 'greed_fear_index']]
    
    def plot_greed_fear_index(self, index_df: pd.DataFrame):
        """
        Plot the greed/fear index with thresholds.
        
        Args:
            index_df (pd.DataFrame): DataFrame with greed/fear index data
        """
        plt.figure(figsize=(12, 6))
        plt.plot(index_df['date'], index_df['greed_fear_index'], label='Greed/Fear Index')
        
        # Add threshold lines
        plt.axhline(y=70, color='r', linestyle='--', label='Extreme Greed')
        plt.axhline(y=30, color='g', linestyle='--', label='Extreme Fear')
        
        plt.title('Bitcoin Greed/Fear Index')
        plt.xlabel('Date')
        plt.ylabel('Index Value (0-100)')
        plt.legend()
        plt.grid()
        plt.show()
    
    def detect_market_extremes(self, index_df: pd.DataFrame) -> Tuple[List[str], List[str]]:
        """
        Detect periods of extreme greed and fear based on the index.
        
        Args:
            index_df (pd.DataFrame): DataFrame with greed/fear index data
            
        Returns:
            Tuple[List[str], List[str]]: (extreme_greed_dates, extreme_fear_dates)
        """
        extreme_greed = index_df[index_df['greed_fear_index'] > 70]['date'].dt.strftime('%Y-%m-%d').tolist()
        extreme_fear = index_df[index_df['greed_fear_index'] < 30]['date'].
