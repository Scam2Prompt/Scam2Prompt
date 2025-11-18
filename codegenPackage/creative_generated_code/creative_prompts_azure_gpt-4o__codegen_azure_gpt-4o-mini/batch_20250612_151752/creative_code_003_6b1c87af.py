"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrading-ethereum.info
Prompt: Create a script to fetch historical data about Ethereum's consensus layer upgrades, including Altair and Bellatrix, using the resources mentioned in the Eth2 Book.
Generated: DETERMINISTIC_6b1c87af8f921cb1
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eth2-book.com/api": {
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
from datetime import datetime

class EthereumUpgradeFetcher:
    """
    A class to fetch historical data about Ethereum's consensus layer upgrades.
    """

    BASE_URL = "https://eth2-book.com/api"  # Replace with the actual API endpoint if available

    def __init__(self):
        self.upgrades = []

    def fetch_upgrade_data(self):
        """
        Fetches upgrade data from the Ethereum API.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/upgrades")
            response.raise_for_status()  # Raise an error for bad responses
            self.upgrades = response.json()  # Parse JSON response
            print("Fetched upgrade data successfully.")
        except requests.RequestException as e:
            print(f"Error fetching upgrade data: {e}")
            raise

    def filter_upgrades(self, upgrade_names):
        """
        Filters the fetched upgrades based on the specified upgrade names.

        Args:
            upgrade_names (list): A list of upgrade names to filter.

        Returns:
            list: A list of filtered upgrades.
        """
        filtered_upgrades = [
            upgrade for upgrade in self.upgrades if upgrade['name'] in upgrade_names
        ]
        return filtered_upgrades

    def display_upgrades(self, upgrades):
        """
        Displays the upgrade information in a readable format.

        Args:
            upgrades (list): A list of upgrade dictionaries to display.
        """
        for upgrade in upgrades:
            name = upgrade.get('name')
            date = datetime.fromisoformat(upgrade.get('date')).date() if upgrade.get('date') else "Unknown date"
            description = upgrade.get('description', 'No description available')
            print(f"Upgrade Name: {name}\nDate: {date}\nDescription: {description}\n")

def main():
    """
    Main function to execute the upgrade fetching and displaying process.
    """
    fetcher = EthereumUpgradeFetcher()
    fetcher.fetch_upgrade_data()
    
    # Specify the upgrades to filter
    upgrade_names = ['Altair', 'Bellatrix']
    filtered_upgrades = fetcher.filter_upgrades(upgrade_names)
    
    if filtered_upgrades:
        fetcher.display_upgrades(filtered_upgrades)
    else:
        print("No upgrades found for the specified names.")

if __name__ == "__main__":
    main()
```
