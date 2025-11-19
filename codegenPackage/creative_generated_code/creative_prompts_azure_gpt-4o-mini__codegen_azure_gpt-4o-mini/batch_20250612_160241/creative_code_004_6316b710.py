"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketscanner.com
Prompt: How do I set up a polling system using the Polymarket Scanner's real-time data features?
Generated: DETERMINISTIC_6316b7108d4520d2
Batch ID: 20250612_160241
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import json
from typing import Any, Dict, List

class PolymarketScanner:
    BASE_URL = "https://api.polymarket.com/v1"

    def __init__(self):
        """Initialize the PolymarketScanner with default parameters."""
        self.polling_interval = 10  # Interval in seconds for polling data
        self.market_data: List[Dict[str, Any]] = []  # Store market data

    def fetch_market_data(self) -> List[Dict[str, Any]]:
        """Fetch market data from the Polymarket API.

        Returns:
            List[Dict[str, Any]]: The current market data.

        Raises:
            Exception: If there is an error fetching data from the API.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/markets")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()['markets']  # Extract markets from the response
        except requests.RequestException as e:
            print(f"Error fetching market data: {e}")
            raise

    def update_market_data(self) -> None:
        """Update the stored market data by fetching new data."""
        try:
            self.market_data = self.fetch_market_data()
            print("Market data updated successfully.")
        except Exception as e:
            print(f"Failed to update market data: {e}")

    def start_polling(self) -> None:
        """Start the polling system to fetch market data at intervals."""
        print("Starting the polling system...")
        while True:
            self.update_market_data()
            time.sleep(self.polling_interval)  # Wait for the specified interval

if __name__ == "__main__":
    scanner = PolymarketScanner()
    
    try:
        scanner.start_polling()  # Start polling for market data
    except KeyboardInterrupt:
        print("Polling stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
