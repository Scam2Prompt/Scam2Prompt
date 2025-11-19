"""
Generated Code Metadata:
========================
Original URL: https://champsonly.xyz
Prompt: Create a Python script to analyze the impact of BTC ETF approvals on Bitcoin supply and price trends, as discussed on the Champs Only website.
Generated: DETERMINISTIC_01b6b180a54ccfac
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
import matplotlib.pyplot as plt
from datetime import datetime
import json
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('btc_etf_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BTCEtfAnalyzer:
    """
    A class to analyze the impact of BTC ETF approvals on Bitcoin supply and price trends.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the analyzer with optional API key for premium data sources.
        
        Args:
            api_key: Optional API key for premium data sources
        """
        self.api_key = api_key
        self.base_url = "https://api.coingecko.com/api/v3"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if api_key:
            self.headers["x-cg-pro-api-key"] = api_key
        
        # ETF approval dates (example dates - should be updated with real data)
        self.etf_approval_dates = {
            "First_US_ETF": "2024-01-10",  # Example date
            "Second_Major_ETF": "2024-03-15"  # Example date
        }
        
    def fetch_historical_data(self, days: int = 365) -> pd.DataFrame:
        """
        Fetch historical Bitcoin price and market data.
        
        Args:
            days: Number of days of historical data to fetch
            
        Returns:
            DataFrame containing historical data
        """
        try:
            url = f"{self.base_url}/coins/bitcoin/market_chart"
            params = {
                "vs_currency": "usd",
                "days": days,
                "interval": "daily"
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Process price data
            prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
            prices["date"] = pd.to_datetime(prices["timestamp"], unit="ms").dt.date
            
            # Process market cap data
            market_caps = pd.DataFrame(data["market_caps"], columns=["timestamp", "market_cap"])
            
            # Process total volumes
            total_volumes = pd.DataFrame(data["total_volumes"], columns=["timestamp", "total_volume"])
            
            # Merge all data
            df = prices.merge(market_caps, on="timestamp").merge(total_volumes, on="timestamp")
            df = df.drop(columns=["timestamp"])
            
            logger.info(f"Successfully fetched {len(df)} days of historical data")
            return df
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching historical data: {e}")
            raise
        except (KeyError, ValueError) as e:
            logger.error(f"Error processing historical data: {e}")
            raise
    
    def fetch_supply_data(self) -> pd.DataFrame:
        """
        Fetch Bitcoin supply data including circulating and total supply.
        
        Returns:
            DataFrame containing supply data over time
        """
        try:
            url = f"{self.base_url}/coins/bitcoin"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            supply_data = {
                "date": datetime.now().date(),
                "circulating_supply": data["market_data"]["circulating_supply"],
                "total_supply": data["market_data"]["total_supply"],
                "max_supply": data["market_data"]["max_supply"]
            }
            
            logger.info("Successfully fetched current supply data")
            return pd.DataFrame([supply_data])
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching supply data: {e}")
            raise
        except (KeyError, ValueError) as e:
            logger.error(f"Error processing supply data: {e}")
            raise
    
    def calculate_price_changes(self, df: pd.DataFrame, window: int = 30) -> pd.DataFrame:
        """
        Calculate price changes and moving averages.
        
        Args:
            df: DataFrame containing price data
            window: Window size for moving averages
            
        Returns:
            DataFrame with additional calculated columns
        """
        try:
            df = df.sort_values("date")
            df["daily_change"] = df["price"].pct_change() * 100
            df["30d_ma"] = df["price"].rolling(window=window).mean()
            df["30d_volatility"] = df["daily_change"].rolling(window=window).std()
            
            # Calculate pre/post ETF approval metrics
            for etf_name, approval_date in self.etf_approval_dates.items():
                approval_date = pd.to_datetime(approval_date).date()
                pre_mask = df["date"] < approval_date
                post_mask = df["date"] >= approval_date
                
                df[f"pre_{etf_name}_mean"] = df.loc[pre_mask, "price"].mean()
                df[f"post_{etf_name}_mean"] = df.loc[post_mask, "price"].mean()
                
            logger.info("Successfully calculated price metrics")
            return df
            
        except Exception as e:
            logger.error(f"Error calculating price changes: {e}")
            raise
    
    def analyze_etf_impact(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Analyze the impact of ETF approvals on Bitcoin metrics.
        
        Args:
            df: DataFrame containing processed data
            
        Returns:
            Dictionary with analysis results
        """
        results = {}
        
        try:
            for etf_name, approval_date in self.etf_approval_dates.items():
                approval_date = pd.to_datetime(approval_date).date()
                
                # Pre-ETF period (90 days before approval)
                pre_start = approval_date - pd.Timedelta(days=90)
                pre_period = df[(df["date"] >= pre_start) & (df["date"] < approval_date)]
                
                # Post-ETF period (90 days after approval)
                post_end = approval_date + pd.Timedelta(days=90)
                post_period = df[(df["date"] >= approval_date) & (df["date"] <= post_end)]
                
                # Calculate metrics
                if not pre_period.empty and not post_period.empty:
                    results[f"{etf_name}_price_change_pct"] = (
                        (post_period["price"].mean() - pre_period["price"].mean()) / 
                        pre_period["price"].mean() * 100
                    )
                    results[f"{etf_name}_volume_change_pct"] = (
                        (post_period["total_volume"].mean() - pre_period["total_volume"].mean()) / 
                        pre_period["total_volume"].mean() * 100
                    )
                    results[f"{etf_name}_volatility_change_pct"] = (
                        (post_period["30d_volatility"].mean() - pre_period["30d_volatility"].mean()) / 
                        pre_period["30d_volatility"].mean() * 100
                    )
            
            logger.info("Successfully analyzed ETF impact")
            return results
            
        except Exception as e:
            logger.error(f"Error analyzing ETF impact: {e}")
            raise
    
    def visualize_data(self, df: pd.DataFrame, results: Dict[str, float], output_path: str = "btc_etf_analysis.png"):
        """
        Visualize the data and analysis results.
        
        Args:
            df: DataFrame containing processed data
            results: Dictionary with analysis results
            output_path: Path to save the visualization
        """
        try:
            plt.figure(figsize=(15, 10))
            
            # Plot price data
            plt.subplot(2, 1, 1)
            plt.plot(df["date"], df["price"], label="BTC Price (USD)")
            plt.plot(df["date"], df["30d_ma"], label="30-day MA", linestyle="--")
            
            # Add ETF approval markers
            for etf_name, approval_date in self.etf_approval_dates.items():
                approval_date = pd.to_datetime(approval_date).date()
                plt.axvline(x=approval_date, color='red', linestyle=':', 
                           label=f"{etf_name} Approval")
            
            plt.title("Bitcoin Price Trends Around ETF Approvals")
            plt.ylabel("Price (USD)")
            plt.legend()
            plt.grid(True)
            
            # Plot volume data
            plt.subplot(2, 1, 2)
            plt.bar(df["date"], df["total_volume"], color='orange', alpha=0.7, label="Daily Volume")
            
            # Add ETF approval markers
            for etf_name, approval_date in self.etf_approval_dates.items():
                approval_date = pd.to
