"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Generate code to display live updates and statistics for basketball matches, inspired by the match updates provided by "Grad košarke."
Generated: DETERMINISTIC_19d65f940788a4d3
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/live-basketball-matches": {
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
import json
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasketballMatchUpdater:
    """Class to fetch and display live updates and statistics for basketball matches."""

    def __init__(self, api_url):
        """
        Initializes the BasketballMatchUpdater with the API URL.

        Args:
            api_url (str): The URL of the basketball match updates API.
        """
        self.api_url = api_url

    def fetch_live_updates(self):
        """
        Fetches live updates from the specified API URL.

        Returns:
            dict: Parsed JSON response containing match updates.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching live updates: {e}")
            return None

    def display_updates(self, updates):
        """
        Displays the fetched updates in a readable format.

        Args:
            updates (dict): The match updates to display.
        """
        if updates is None:
            logging.warning("No updates to display.")
            return

        # Display match information
        for match in updates.get('matches', []):
            match_time = datetime.fromtimestamp(match['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"Match: {match['home_team']} vs {match['away_team']} at {match_time}")
            logging.info(f"Score: {match['home_score']} - {match['away_score']}")
            logging.info(f"Quarter: {match['quarter']}")

            # Display player statistics
            for player in match.get('players', []):
                logging.info(f"Player: {player['name']} | Points: {player['points']} | Fouls: {player['fouls']}")

            logging.info("-" * 40)

    def run(self, interval=60):
        """
        Continuously fetches and displays live updates at specified intervals.

        Args:
            interval (int): Time in seconds between updates.
        """
        while True:
            updates = self.fetch_live_updates()
            self.display_updates(updates)
            logging.info(f"Waiting for {interval} seconds before fetching updates...")
            time.sleep(interval)

# Example usage
if __name__ == "__main__":
    API_URL = "https://api.example.com/live-basketball-matches"  # Replace with the actual API URL
    updater = BasketballMatchUpdater(API_URL)
    updater.run(interval=30)  # Fetch updates every 30 seconds
```
