"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.solanary.com
Prompt: Provide an example of how to use the Solanary Multi-Jackpot API to display real-time updates of prize pool amounts and winners.
Generated: DETERMINISTIC_921328f9c27d2ab5
Batch ID: 20250612_150446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solanary.com/multi-jackpot": {
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

class SolanaryAPI:
    """
    A class to interact with the Solanary Multi-Jackpot API.
    """

    BASE_URL = "https://api.solanary.com/multi-jackpot"

    def __init__(self):
        """
        Initializes the SolanaryAPI class.
        """
        self.session = requests.Session()

    def get_jackpot_info(self):
        """
        Fetches the current jackpot information from the Solanary API.

        Returns:
            dict: A dictionary containing jackpot information, including prize pools and winners.
        """
        try:
            response = self.session.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()  # Return the JSON response
        except requests.RequestException as e:
            print(f"Error fetching jackpot information: {e}")
            return None

def display_jackpot_info(jackpot_info):
    """
    Displays the jackpot information including prize pools and winners.

    Args:
        jackpot_info (dict): The jackpot information to display.
    """
    if jackpot_info:
        print("Current Jackpot Information:")
        for jackpot in jackpot_info.get('jackpots', []):
            prize_pool = jackpot.get('prize_pool', 'Unknown')
            winners = jackpot.get('winners', [])
            winner_names = ', '.join(winners) if winners else 'No winners yet'
            print(f"Jackpot ID: {jackpot.get('id')}")
            print(f"Prize Pool: {prize_pool}")
            print(f"Winners: {winner_names}")
            print("-" * 30)
    else:
        print("No jackpot information available.")

def main():
    """
    Main function to fetch and display jackpot information in real-time.
    """
    api = SolanaryAPI()
    
    while True:
        jackpot_info = api.get_jackpot_info()
        display_jackpot_info(jackpot_info)
        time.sleep(30)  # Pause for 30 seconds before refreshing

if __name__ == "__main__":
    main()
```
