"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-redstone.com
Prompt: Create a script to parse and display the ranking data of RedStone miners, including wallet addresses, usernames, and their respective scores.
Generated: DETERMINISTIC_b3132dd58e61a413
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/redstone/miners/rankings": {
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
import json
import requests
from typing import List, Dict

class MinerRanking:
    def __init__(self, api_url: str):
        """
        Initializes the MinerRanking with the given API URL.

        Args:
            api_url (str): The URL of the API that provides the ranking data.
        """
        self.api_url = api_url

    def fetch_ranking_data(self) -> List[Dict[str, str]]:
        """
        Fetches the ranking data from the API.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing miner data.
        
        Raises:
            Exception: If there is an error fetching the data from the API.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            ranking_data = response.json()
            return ranking_data  # Return the JSON data as a Python list of dictionaries
        except requests.RequestException as e:
            raise Exception(f"Error fetching ranking data: {e}")

    def display_rankings(self, rankings: List[Dict[str, str]]) -> None:
        """
        Displays the ranking data in a formatted manner.

        Args:
            rankings (List[Dict[str, str]]): The ranking data to display.
        """
        print(f"{'Rank':<5} {'Username':<30} {'Wallet Address':<50} {'Score':<10}")
        print("=" * 100)

        for rank, miner in enumerate(rankings, start=1):
            username = miner.get('username', 'N/A')
            wallet_address = miner.get('wallet_address', 'N/A')
            score = miner.get('score', 0)
            print(f"{rank:<5} {username:<30} {wallet_address:<50} {score:<10}")

    def run(self) -> None:
        """
        Main method to fetch and display miner rankings.
        """
        try:
            rankings = self.fetch_ranking_data()
            self.display_rankings(rankings)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the actual API endpoint for RedStone miners ranking
    API_URL = "https://api.example.com/redstone/miners/rankings"
    miner_ranking = MinerRanking(api_url=API_URL)
    miner_ranking.run()
```
