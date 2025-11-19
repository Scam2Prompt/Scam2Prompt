"""
Generated Code Metadata:
========================
Original URL: https://magpiexyz.pages.dev
Prompt: Write a script to interact with the Magpie XYZ API to calculate and display the current TVL (Total Value Locked) for all listed platforms, including Wombat, Pendle, Radiant, PancakeSwap, and EigenLayer.
Generated: DETERMINISTIC_880a0783bddef47a
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.magpie.xyz/v1/tvl": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class MagpieAPI:
    """
    A class to interact with the Magpie XYZ API to fetch Total Value Locked (TVL) data.
    """

    BASE_URL = "https://api.magpie.xyz/v1/tvl"

    def __init__(self):
        """
        Initializes the MagpieAPI class.
        """
        self.platforms = ["Wombat", "Pendle", "Radiant", "PancakeSwap", "EigenLayer"]

    def fetch_tvl_data(self):
        """
        Fetches the TVL data from the Magpie API.

        Returns:
            dict: A dictionary containing TVL data for the specified platforms.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Magpie API: {e}")
            return None

    def calculate_tvl(self, tvl_data):
        """
        Calculates the total value locked for the specified platforms.

        Args:
            tvl_data (dict): The TVL data fetched from the API.

        Returns:
            dict: A dictionary containing the TVL for each platform.
        """
        tvl_results = {}
        for platform in self.platforms:
            tvl_results[platform] = tvl_data.get(platform, 0)
        return tvl_results

    def display_tvl(self, tvl_results):
        """
        Displays the TVL results in a readable format.

        Args:
            tvl_results (dict): A dictionary containing the TVL for each platform.
        """
        print("Total Value Locked (TVL) for Listed Platforms:")
        for platform, tvl in tvl_results.items():
            print(f"{platform}: ${tvl:,.2f}")

def main():
    """
    Main function to execute the TVL calculation and display.
    """
    magpie_api = MagpieAPI()
    tvl_data = magpie_api.fetch_tvl_data()

    if tvl_data is not None:
        tvl_results = magpie_api.calculate_tvl(tvl_data)
        magpie_api.display_tvl(tvl_results)

if __name__ == "__main__":
    main()
```
