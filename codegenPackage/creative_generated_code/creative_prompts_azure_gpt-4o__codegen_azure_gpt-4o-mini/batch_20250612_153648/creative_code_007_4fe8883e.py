"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-9e9.pages.dev
Prompt: Develop a script to display $BONK token statistics, including exchange listings and integration counts, using data from the Bonk Coin website.
Generated: DETERMINISTIC_4fe8883e023623ba
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bonkcoin.com": {
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

class BonkTokenStats:
    """
    A class to fetch and display statistics for the $BONK token.
    
    Attributes:
        base_url (str): The base URL of the Bonk Coin API.
    """

    def __init__(self):
        self.base_url = "https://api.bonkcoin.com"  # Base API URL

    def fetch_token_stats(self):
        """
        Fetch token statistics from the Bonk Coin API.

        Returns:
            dict: A dictionary containing token statistics.
        """
        try:
            response = requests.get(f"{self.base_url}/token/stats")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response as a dictionary
        except requests.exceptions.RequestException as e:
            print(f"Error fetching token statistics: {e}")
            return None  # Return None if an error occurs

    def display_stats(self, stats):
        """
        Display the token statistics in a user-friendly format.

        Args:
            stats (dict): The token statistics to display.
        """
        if stats:
            print("=== $BONK Token Statistics ===")
            print(f"Total Supply: {stats.get('total_supply', 'N/A')}")
            print(f"Market Cap: {stats.get('market_cap', 'N/A')}")
            print(f"Exchange Listings: {len(stats.get('exchanges', []))}")
            print(f"Integration Counts: {stats.get('integration_count', 'N/A')}")
        else:
            print("No statistics available to display.")

def main():
    """
    Main function to execute the script.
    """
    bonk_stats = BonkTokenStats()
    stats = bonk_stats.fetch_token_stats()
    bonk_stats.display_stats(stats)

if __name__ == "__main__":
    main()
```
