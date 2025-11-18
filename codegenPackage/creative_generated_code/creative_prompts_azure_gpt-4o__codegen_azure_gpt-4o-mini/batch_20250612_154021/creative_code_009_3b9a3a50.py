"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterde.com
Prompt: Create a tutorial-style code example for building a portfolio tracker using Aster's API, displaying user trading statistics like total trading volume, open interest, and symbols traded.
Generated: DETERMINISTIC_3b9a3a506fa46c43
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.io/v1": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class PortfolioTracker:
    """
    A class to represent a portfolio tracker using Aster's API.

    Attributes
    ----------
    api_key : str
        The API key for authenticating with Aster's API
    base_url : str
        The base URL for Aster's API
    user_id : str
        The user's ID for fetching trading statistics

    Methods
    -------
    fetch_user_stats():
        Fetches trading statistics for the user.
    display_stats(stats):
        Displays the trading statistics in a readable format.
    """

    def __init__(self, api_key: str, user_id: str):
        """
        Constructs all the necessary attributes for the PortfolioTracker object.

        Parameters
        ----------
        api_key : str
            The API key for authenticating with Aster's API
        user_id : str
            The user's ID for fetching trading statistics
        """
        self.api_key = api_key
        self.base_url = "https://api.aster.io/v1"
        self.user_id = user_id

    def fetch_user_stats(self):
        """
        Fetches trading statistics for the user from Aster's API.

        Returns
        -------
        dict
            A dictionary containing total trading volume, open interest, and symbols traded.
        """
        try:
            url = f"{self.base_url}/users/{self.user_id}/stats"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error on a bad response

            # Return the stats as a dictionary
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching user stats: {e}")
            return None

    def display_stats(self, stats: dict):
        """
        Displays the trading statistics in a readable format.

        Parameters
        ----------
        stats : dict
            A dictionary containing trading statistics to display.
        """
        if stats:
            logging.info("User Trading Statistics:")
            logging.info(f"Total Trading Volume: {stats.get('total_volume', 'N/A')}")
            logging.info(f"Open Interest: {stats.get('open_interest', 'N/A')}")
            logging.info(f"Symbols Traded: {', '.join(stats.get('symbols_traded', [])) if stats.get('symbols_traded') else 'N/A'}")
        else:
            logging.warning("No statistics to display.")

def main():
    """
    Main function to run the Portfolio Tracker.
    """
    # Replace with your actual Aster API key and user ID
    api_key = "YOUR_ASTER_API_KEY"
    user_id = "YOUR_USER_ID"

    # Create an instance of the PortfolioTracker
    tracker = PortfolioTracker(api_key, user_id)

    # Fetch and display user trading statistics
    stats = tracker.fetch_user_stats()
    tracker.display_stats(stats)

if __name__ == "__main__":
    main()
```
