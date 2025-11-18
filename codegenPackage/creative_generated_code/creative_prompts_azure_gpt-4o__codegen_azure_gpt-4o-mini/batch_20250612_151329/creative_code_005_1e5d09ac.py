"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alixa.tech
Prompt: Write code to track and display the progress of pending ETHx payouts for bonds created on the Alixa platform, using the "Bond Amount Min Max" and "Bond Maturity" parameters.
Generated: DETERMINISTIC_1e5d09acb011ccb7
Batch ID: 20250612_151329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.alixa.com": {
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AlixaPayoutTracker:
    def __init__(self, api_url):
        """
        Initialize the AlixaPayoutTracker with the API URL.
        
        :param api_url: The base URL of the Alixa API
        """
        self.api_url = api_url

    def fetch_bond_data(self):
        """
        Fetch bond data from the Alixa platform.
        
        :return: List of bond data if successful; raises an exception on failure.
        """
        try:
            response = requests.get(f"{self.api_url}/bonds")
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            logging.info("Successfully fetched bond data.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching bond data: {e}")
            raise

    def filter_bonds(self, bonds, min_amount, max_amount, maturity):
        """
        Filter bonds based on the given parameters.
        
        :param bonds: List of bond data to filter
        :param min_amount: Minimum bond amount
        :param max_amount: Maximum bond amount
        :param maturity: Maturity period to filter
        :return: Filtered list of bonds
        """
        filtered_bonds = [
            bond for bond in bonds
            if min_amount <= bond['amount'] <= max_amount and bond['maturity'] == maturity
        ]
        logging.info(f"Filtered bonds based on parameters: {min_amount}, {max_amount}, {maturity}. Found {len(filtered_bonds)} bonds.")
        return filtered_bonds

    def display_bonds(self, bonds):
        """
        Display the bond details in a user-friendly format.
        
        :param bonds: List of bonds to display
        """
        if not bonds:
            logging.warning("No bonds to display.")
            print("No bonds available matching the criteria.")
            return
        
        print("Pending ETHx Payouts for Bonds:")
        for bond in bonds:
            print(f"ID: {bond['id']}, Amount: {bond['amount']}, Maturity: {bond['maturity']}, Status: {bond['status']}")

    def track_payouts(self, min_amount, max_amount, maturity):
        """
        Main method to track and display pending ETHx payouts for bonds.
        
        :param min_amount: Minimum bond amount
        :param max_amount: Maximum bond amount
        :param maturity: Maturity period to filter
        """
        try:
            bonds = self.fetch_bond_data()
            filtered_bonds = self.filter_bonds(bonds, min_amount, max_amount, maturity)
            self.display_bonds(filtered_bonds)
        except Exception as e:
            logging.error(f"An error occurred while tracking payouts: {e}")

if __name__ == "__main__":
    # Example usage
    API_URL = "https://api.alixa.com"  # Replace with the actual API URL
    tracker = AlixaPayoutTracker(API_URL)

    # Define parameters for filtering bonds
    MIN_AMOUNT = 1000  # Example minimum amount
    MAX_AMOUNT = 5000  # Example maximum amount
    MATURITY = "2024-12-31"  # Example maturity date

    # Start tracking payouts
    tracker.track_payouts(MIN_AMOUNT, MAX_AMOUNT, MATURITY)
```
