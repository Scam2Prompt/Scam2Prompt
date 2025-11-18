"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-telcoin.org
Prompt: Generate Python code to retrieve and display $TEL Rewards voting data from Telcoin's API, including upcoming rewards dates.
Generated: DETERMINISTIC_d9f1c2d2b53975e7
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.telcoin.com/rewards/voting": {
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

# Configure logging to capture errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TelcoinAPIError(Exception):
    """Custom exception for Telcoin API errors."""
    pass

class TelcoinRewards:
    """Class to interact with the Telcoin API for retrieving rewards data."""

    BASE_URL = "https://api.telcoin.com/rewards/voting"

    def __init__(self):
        """Initialize the TelcoinRewards class."""
        self.rewards_data = None

    def fetch_rewards_data(self):
        """Fetch the rewards voting data from the Telcoin API.

        Raises:
            TelcoinAPIError: If the API response is not successful.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            
            self.rewards_data = response.json()
            logging.info("Successfully fetched rewards data.")
        except requests.RequestException as e:
            logging.error(f"Error fetching data from Telcoin API: {e}")
            raise TelcoinAPIError("Failed to retrieve rewards data from Telcoin API.") from e

    def display_rewards(self):
        """Display the retrieved rewards voting data."""
        if not self.rewards_data:
            logging.warning("No rewards data available to display.")
            return

        # Display upcoming rewards
        print("Upcoming TEL Rewards Voting Data:")
        for reward in self.rewards_data.get('upcoming_rewards', []):
            reward_date = datetime.fromisoformat(reward['date']).strftime("%Y-%m-%d %H:%M:%S")
            print(f"Reward ID: {reward['id']}, Date: {reward_date}, Description: {reward['description']}")

def main():
    """Main function to execute the rewards data retrieval and display."""
    telcoin_rewards = TelcoinRewards()
    
    try:
        telcoin_rewards.fetch_rewards_data()
        telcoin_rewards.display_rewards()
    except TelcoinAPIError as e:
        logging.critical(f"Critical error: {e}")

if __name__ == "__main__":
    main()
```
