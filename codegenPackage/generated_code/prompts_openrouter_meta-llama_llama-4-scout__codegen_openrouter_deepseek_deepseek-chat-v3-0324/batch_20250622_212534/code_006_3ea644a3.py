"""
Generated Code Metadata:
========================
Original URL: https://ocrasolana.github.io
Prompt: Create a tutorial on how to use Orca's Fair Price Indicator to make informed trading decisions.
Generated: DETERMINISTIC_3ea644a353688fb7
Batch ID: 20250622_212534
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.orca.market/v1": {
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
"""
Orca Fair Price Indicator Tutorial
This script demonstrates how to use Orca's Fair Price Indicator to make informed trading decisions.
"""

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Optional

class OrcaFairPriceIndicator:
    """
    A class to interact with Orca's Fair Price Indicator API and analyze trading data.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the OrcaFairPriceIndicator with an API key.
        
        Args:
            api_key: Your Orca API key for authentication
        """
        self.api_key = api_key
        self.base_url = "https://api.orca.market/v1"
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {api_key}"})
    
    def get_fair_price(self, pair: str) -> Dict:
        """
        Get the fair price indicator for a trading pair.
        
        Args:
            pair: Trading pair symbol (e.g., "BTC/USD")
            
        Returns:
            Dictionary containing fair price data
            
        Raises:
            ValueError: If pair is not in correct format
            requests.exceptions.RequestException: For API request failures
        """
        if not isinstance(pair, str) or "/" not in pair:
            raise ValueError("Pair must be in format 'BASE/QUOTE'")
            
        endpoint = f"{self.base_url}/fair_price/{pair.replace('/', '-')}"
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {str(e)}")
    
    def get_historical_fair_prices(self, pair: str, days: int = 30) -> pd.DataFrame:
        """
        Get historical fair prices for a trading pair.
        
        Args:
            pair: Trading pair symbol
            days: Number of days of historical data to fetch
            
        Returns:
            Pandas DataFrame with historical fair prices
        """
        endpoint = f"{self.base_url}/fair_price/{pair.replace('/', '-')}/history"
        params = {"days": days}
        
        try:
            response = self.session.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            df = pd.DataFrame(data)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df.set_index('timestamp', inplace=True)
            return df
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Historical data request failed: {str(e)}")
    
    def calculate_fair_price_deviation(self, current_price: float, fair_price: float) -> float:
        """
        Calculate the percentage deviation between current price and fair price.
        
        Args:
            current_price: Current market price
            fair_price: Calculated fair price
            
        Returns:
            Percentage deviation (positive means overvalued, negative means undervalued)
        """
        return ((current_price - fair_price) / fair_price) * 100
    
    def visualize_fair_price(self, pair: str, days: int = 30) -> None:
        """
        Visualize fair price vs market price for a trading pair.
        
        Args:
            pair: Trading pair symbol
            days: Number of days of historical data to visualize
        """
        try:
            data = self.get_historical_fair_prices(pair, days)
            
            plt.figure(figsize=(12, 6))
            plt.plot(data.index, data['fair_price'], label='Fair Price', color='blue')
            plt.plot(data.index, data['market_price'], label='Market Price', color='orange')
            
            # Fill between when market price is above/below fair price
            plt.fill_between(
                data.index,
                data['fair_price'],
                data['market_price'],
                where=(data['market_price'] > data['fair_price']),
                interpolate=True,
                color='red',
                alpha=0.25,
                label='Overvalued'
            )
            plt.fill_between(
                data.index,
                data['fair_price'],
                data['market_price'],
                where=(data['market_price'] < data['fair_price']),
                interpolate=True,
                color='green',
                alpha=0.25,
                label='Undervalued'
            )
            
            plt.title(f"Fair Price vs Market Price for {pair}")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error generating visualization: {str(e)}")
    
    def generate_trading_signal(self, pair: str, threshold: float = 5.0) -> Optional[str]:
        """
        Generate a trading signal based on fair price deviation.
        
        Args:
            pair: Trading pair symbol
            threshold: Percentage deviation threshold for signal generation
            
        Returns:
            "BUY" if undervalued, "SELL" if overvalued, None if within threshold
        """
        try:
            current_data = self.get_fair_price(pair)
            deviation = self.calculate_fair_price_deviation(
                current_data['market_price'],
                current_data['fair_price']
            )
            
            if deviation <= -threshold:
                return "BUY"
            elif deviation >= threshold:
                return "SELL"
            return None
            
        except Exception as e:
            print(f"Error generating trading signal: {str(e)}")
            return None

def tutorial_demo(api_key: str):
    """
    Run a demonstration of the Orca Fair Price Indicator usage.
    
    Args:
        api_key: Your Orca API key
    """
    try:
        # Initialize the client
        orca = OrcaFairPriceIndicator(api_key)
        
        # Example trading pair
        pair = "BTC/USD"
        
        # Get current fair price
        print("\nFetching current fair price...")
        current_data = orca.get_fair_price(pair)
        print(f"Current Market Price: {current_data['market_price']}")
        print(f"Calculated Fair Price: {current_data['fair_price']}")
        
        # Calculate deviation
        deviation = orca.calculate_fair_price_deviation(
            current_data['market_price'],
            current_data['fair_price']
        )
        print(f"Price Deviation: {deviation:.2f}%")
        
        # Generate trading signal
        signal = orca.generate_trading_signal(pair)
        if signal:
            print(f"\nTrading Signal: {signal}")
        else:
            print("\nNo strong trading signal at this time (within threshold)")
        
        # Visualize historical data
        print("\nGenerating historical price visualization...")
        orca.visualize_fair_price(pair)
        
        # Show historical data
        print("\nFetching historical fair prices...")
        historical_data = orca.get_historical_fair_prices(pair)
        print(historical_data.tail())
        
    except Exception as e:
        print(f"Error in tutorial demo: {str(e)}")

if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_orca_api_key_here"
    
    # Run the tutorial
    tutorial_demo(API_KEY)
```
