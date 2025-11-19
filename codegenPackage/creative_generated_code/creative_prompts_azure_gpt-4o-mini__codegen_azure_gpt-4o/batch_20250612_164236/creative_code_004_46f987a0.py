"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket-bot.vercel.app
Prompt: How do I implement a feature in my Polymarket bot to track previous market statuses using the API?
Generated: DETERMINISTIC_46f987a08677f9e6
Batch ID: 20250612_164236
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/markets": {
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
from datetime import datetime
import logging

# Configure logging to track bot activity and errors
logging.basicConfig(
    filename='polymarket_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PolymarketBot:
    def __init__(self, api_url: str):
        """
        Initializes the PolymarketBot with the API URL and an empty market status history.
        :param api_url: The base URL for the Polymarket API.
        """
        self.api_url = api_url
        self.market_status_history = {}

    def fetch_market_data(self):
        """
        Fetches the current market data from the Polymarket API.
        :return: JSON response containing market data or None if an error occurs.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            logging.info("Market data fetched successfully.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching market data: {e}")
            return None

    def update_market_status_history(self, market_data: dict):
        """
        Updates the market status history with new market data.
        This method tracks the changes over time for each market.
        :param market_data: The market data fetched from the Polymarket API.
        """
        try:
            timestamp = datetime.utcnow().isoformat()  # Use UTC timestamp for consistency
            for market in market_data.get('markets', []):
                market_id = market.get('id')
                market_status = market.get('status')

                if market_id not in self.market_status_history:
                    # If market is not tracked, initialize its history
                    self.market_status_history[market_id] = []

                # Append the new status with the timestamp
                self.market_status_history[market_id].append({
                    'timestamp': timestamp,
                    'status': market_status
                })

            logging.info("Market status history updated.")
        except Exception as e:
            logging.error(f"Error updating market status history: {e}")

    def display_market_status_history(self):
        """
        Displays the tracked history of market statuses.
        """
        for market_id, history in self.market_status_history.items():
            print(f"Market ID: {market_id}")
            for record in history:
                print(f"  Time: {record['timestamp']}, Status: {record['status']}")

    def run(self):
        """
        Main method to run the bot. Fetches market data and updates the status history.
        """
        market_data = self.fetch_market_data()
        if market_data:
            self.update_market_status_history(market_data)
            self.display_market_status_history()


if __name__ == "__main__":
    # Replace 'https://api.polymarket.com/markets' with the actual Polymarket API URL
    API_URL = "https://api.polymarket.com/markets"
    
    bot = PolymarketBot(api_url=API_URL)
    bot.run()
```
