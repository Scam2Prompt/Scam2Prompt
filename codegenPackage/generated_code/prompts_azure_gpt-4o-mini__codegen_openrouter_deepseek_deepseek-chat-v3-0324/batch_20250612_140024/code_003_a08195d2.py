"""
Generated Code Metadata:
========================
Original URL: https://ethereumonthlyreturns.pureix.com
Prompt: Provide an example of how to integrate Ethereum Monthly Return data into a financial application using RESTful API calls.
Generated: DETERMINISTIC_a08195d2a0906a40
Batch ID: 20250612_140024
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
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EthereumDataFetcher:
    """
    A class to fetch Ethereum monthly return data from a REST API and process it.
    """
    
    def __init__(self, api_base_url="https://api.coingecko.com/api/v3"):
        """
        Initialize the EthereumDataFetcher with the API base URL.
        
        Args:
            api_base_url (str): Base URL for the CoinGecko API
        """
        self.api_base_url = api_base_url
        
    def _make_api_request(self, endpoint, params=None):
        """
        Make a GET request to the specified API endpoint.
        
        Args:
            endpoint (str): API endpoint to call
            params (dict): Query parameters for the request
            
        Returns:
            dict: JSON response from the API
            
        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        url = f"{self.api_base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def get_historical_data(self, days=365, currency="usd"):
        """
        Get historical Ethereum price data.
        
        Args:
            days (int): Number of days of historical data to fetch
            currency (str): Target currency for price data
            
        Returns:
            pd.DataFrame: DataFrame containing date and price columns
        """
        endpoint = f"coins/ethereum/market_chart"
        params = {
            "vs_currency": currency,
            "days": days
        }
        
        try:
            data = self._make_api_request(endpoint, params)
            prices = data.get("prices", [])
            
            # Convert to DataFrame and process
            df = pd.DataFrame(prices, columns=["timestamp", "price"])
            df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
            df = df.set_index("date")
            df = df[["price"]]
            
            return df
        except Exception as e:
            logger.error(f"Failed to process historical data: {e}")
            raise

    def calculate_monthly_returns(self, historical_data):
        """
        Calculate monthly returns from historical price data.
        
        Args:
            historical_data (pd.DataFrame): DataFrame with price data
            
        Returns:
            pd.DataFrame: DataFrame with monthly returns
        """
        try:
            # Resample to monthly frequency using last price of each month
            monthly_prices = historical_data.resample('M').last()
            
            # Calculate percentage returns
            monthly_returns = monthly_prices.pct_change() * 100
            monthly_returns.columns = ["monthly_return"]
            
            return monthly_returns.dropna()
        except Exception as e:
            logger.error(f"Failed to calculate monthly returns: {e}")
            raise

    def get_monthly_returns(self, days=365, currency="usd"):
        """
        Get Ethereum monthly returns by combining API fetch and calculation.
        
        Args:
            days (int): Number of days of historical data to fetch
            currency (str): Target currency for price data
            
        Returns:
            pd.DataFrame: DataFrame with monthly returns
        """
        try:
            historical_data = self.get_historical_data(days, currency)
            monthly_returns = self.calculate_monthly_returns(historical_data)
            return monthly_returns
        except Exception as e:
            logger.error(f"Failed to get monthly returns: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        fetcher = EthereumDataFetcher()
        returns = fetcher.get_monthly_returns(days=365*3)  # 3 years of data
        print("Ethereum Monthly Returns:")
        print(returns)
        
        # Save to CSV for further analysis
        returns.to_csv("ethereum_monthly_returns.csv")
        logger.info("Successfully fetched and saved Ethereum monthly returns")
    except Exception as e:
        logger.error(f"Application error: {e}")
```
