"""
Generated Code Metadata:
========================
Original URL: https://miden.cloud
Prompt: Write a Python script to query and analyze data from the Miden ecosystem's high-frequency oracle (Pragma) for real-time trading insights.
Generated: DETERMINISTIC_f3159a8bd5d283c4
Batch ID: 20250612_153821
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dev.pragma.build": {
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
from datetime import datetime
import time
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PragmaOracleAnalyzer:
    """
    A class to query and analyze data from Pragma's high-frequency oracle.
    Provides real-time trading insights based on oracle data.
    """
    
    def __init__(self, base_url: str = "https://api.dev.pragma.build"):
        """
        Initialize the PragmaOracleAnalyzer with the API base URL.
        
        Args:
            base_url (str): Base URL for the Pragma API
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'PragmaOracleAnalyzer/1.0'
        })
        
    def get_oracle_data(self, pair: str, timeframe: str = "1m", limit: int = 100) -> Optional[pd.DataFrame]:
        """
        Fetch oracle data for a specific trading pair and timeframe.
        
        Args:
            pair (str): Trading pair (e.g., "BTC-USD")
            timeframe (str): Timeframe for data (e.g., "1m", "5m", "1h")
            limit (int): Number of data points to fetch
            
        Returns:
            pd.DataFrame: DataFrame containing oracle data, or None if request fails
        """
        endpoint = f"/oracle/{pair}?timeframe={timeframe}&limit={limit}"
        url = self.base_url + endpoint
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if not data or 'prices' not in data:
                logger.warning(f"No price data found for pair {pair}")
                return None
                
            df = pd.DataFrame(data['prices'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            
            return df
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching oracle data: {e}")
            return None
            
    def calculate_metrics(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate trading metrics from oracle data.
        
        Args:
            df (pd.DataFrame): DataFrame containing oracle data
            
        Returns:
            Dict[str, float]: Dictionary of calculated metrics
        """
        if df is None or df.empty:
            return {}
            
        metrics = {
            'current_price': df['price'].iloc[-1],
            '24h_high': df['price'].max(),
            '24h_low': df['price'].min(),
            '24h_volatility': (df['price'].max() - df['price'].min()) / df['price'].mean(),
            '24h_volume': df['volume'].sum(),
            'last_updated': df.index[-1].isoformat()
        }
        
        return metrics
        
    def detect_anomalies(self, df: pd.DataFrame, threshold: float = 3.0) -> List[Dict]:
        """
        Detect price anomalies using standard deviation.
        
        Args:
            df (pd.DataFrame): DataFrame containing oracle data
            threshold (float): Number of standard deviations to consider as anomaly
            
        Returns:
            List[Dict]: List of detected anomalies with details
        """
        if df is None or df.empty:
            return []
            
        anomalies = []
        mean = df['price'].mean()
        std = df['price'].std()
        
        for idx, row in df.iterrows():
            z_score = (row['price'] - mean) / std
            if abs(z_score) > threshold:
                anomalies.append({
                    'timestamp': idx.isoformat(),
                    'price': row['price'],
                    'z_score': z_score,
                    'volume': row.get('volume', 0)
                })
                
        return anomalies
        
    def generate_trading_signal(self, df: pd.DataFrame) -> Dict:
        """
        Generate simple trading signals based on price momentum.
        
        Args:
            df (pd.DataFrame): DataFrame containing oracle data
            
        Returns:
            Dict: Trading signal with details
        """
        if df is None or len(df) < 2:
            return {'signal': 'neutral', 'confidence': 0}
            
        last_price = df['price'].iloc[-1]
        prev_price = df['price'].iloc[-2]
        
        if last_price > prev_price * 1.01:  # 1% increase
            return {'signal': 'buy', 'confidence': min(1.0, (last_price - prev_price) / prev_price)}
        elif last_price < prev_price * 0.99:  # 1% decrease
            return {'signal': 'sell', 'confidence': min(1.0, (prev_price - last_price) / prev_price)}
        else:
            return {'signal': 'hold', 'confidence': 0}
            
    def monitor_pair(self, pair: str, interval: int = 60) -> None:
        """
        Continuously monitor a trading pair and log insights.
        
        Args:
            pair (str): Trading pair to monitor
            interval (int): Monitoring interval in seconds
        """
        logger.info(f"Starting monitoring for {pair} (interval: {interval}s)")
        
        try:
            while True:
                df = self.get_oracle_data(pair)
                
                if df is not None:
                    metrics = self.calculate_metrics(df)
                    anomalies = self.detect_anomalies(df)
                    signal = self.generate_trading_signal(df)
                    
                    logger.info(f"\nMetrics for {pair}:\n{metrics}")
                    
                    if anomalies:
                        logger.warning(f"Detected {len(anomalies)} price anomalies!")
                        for anomaly in anomalies[:3]:  # Log first 3 anomalies
                            logger.warning(f"Anomaly: {anomaly}")
                    
                    logger.info(f"Trading signal: {signal['signal']} (confidence: {signal['confidence']:.2f})")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
            
    def close(self):
        """Close the HTTP session."""
        self.session.close()

# Example usage
if __name__ == "__main__":
    analyzer = PragmaOracleAnalyzer()
    
    try:
        # Get data for BTC-USD pair
        btc_data = analyzer.get_oracle_data("BTC-USD")
        
        if btc_data is not None:
            print("Latest BTC-USD data:")
            print(btc_data.tail())
            
            metrics = analyzer.calculate_metrics(btc_data)
            print("\nMetrics:")
            for k, v in metrics.items():
                print(f"{k}: {v}")
                
            # Start monitoring (Ctrl+C to stop)
            analyzer.monitor_pair("BTC-USD")
            
    finally:
        analyzer.close()
```
