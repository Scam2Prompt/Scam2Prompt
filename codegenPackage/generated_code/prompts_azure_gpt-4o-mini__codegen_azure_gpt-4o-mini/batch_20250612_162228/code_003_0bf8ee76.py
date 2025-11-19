"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: What are the unique features of Pyth's price feeds compared to other blockchain oracles for DeFi applications?
Generated: DETERMINISTIC_0bf8ee76fd9e14fe
Batch ID: 20250612_162228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1": {
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
from typing import Dict, Any, List

class PriceFeedError(Exception):
    """Custom exception for price feed errors."""
    pass

class PythPriceFeed:
    """Class to interact with Pyth's price feeds for DeFi applications."""

    BASE_URL = "https://api.pyth.network/v1"

    def __init__(self):
        """Initialize the PythPriceFeed class."""
        self.price_data = {}

    def fetch_price_data(self) -> None:
        """Fetch price data from Pyth's API and store it in the instance."""
        try:
            response = requests.get(f"{self.BASE_URL}/prices")
            response.raise_for_status()  # Raise an error for bad responses
            self.price_data = response.json()
        except requests.RequestException as e:
            raise PriceFeedError(f"Failed to fetch price data: {e}")

    def get_price(self, symbol: str) -> Dict[str, Any]:
        """Get the price for a specific symbol.

        Args:
            symbol (str): The symbol for which to fetch the price.

        Returns:
            Dict[str, Any]: A dictionary containing price information.

        Raises:
            PriceFeedError: If the symbol is not found in the price data.
        """
        if not self.price_data:
            raise PriceFeedError("Price data not fetched. Call fetch_price_data() first.")

        for price_info in self.price_data.get("data", []):
            if price_info.get("symbol") == symbol:
                return price_info
        
        raise PriceFeedError(f"Price data for symbol '{symbol}' not found.")

    def get_all_prices(self) -> List[Dict[str, Any]]:
        """Get all available price data.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing all price information.
        """
        if not self.price_data:
            raise PriceFeedError("Price data not fetched. Call fetch_price_data() first.")
        
        return self.price_data.get("data", [])

# Example usage
if __name__ == "__main__":
    pyth_feed = PythPriceFeed()
    try:
        pyth_feed.fetch_price_data()
        price_info = pyth_feed.get_price("BTC/USD")
        print("BTC/USD Price Info:", price_info)
    except PriceFeedError as e:
        print("Error:", e)
```
