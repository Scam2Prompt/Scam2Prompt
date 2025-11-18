"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama-swap.github.io
Prompt: Write a Python script that uses the Defillama Swap API to retrieve real-time analytics on total value locked (TVL) across multiple DeFi protocols and display the data in a user-friendly format.
Generated: DETERMINISTIC_994e761f348ec486
Batch ID: 20250612_150426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/v1/protocols": {
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

class DeFiAnalytics:
    """Class to interact with the Defillama Swap API to retrieve TVL data."""

    API_URL = "https://api.defillama.com/v1/protocols"

    def __init__(self):
        """Initialize the DeFiAnalytics class."""
        self.protocols_data = []

    def fetch_data(self):
        """Fetch TVL data from the Defillama API.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()  # Raise an error for bad responses
            self.protocols_data = response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def display_data(self):
        """Display the total value locked (TVL) across multiple DeFi protocols in a user-friendly format."""
        if not self.protocols_data:
            print("No data available. Please fetch data first.")
            return

        print(f"{'Protocol':<30} {'TVL (USD)':<15}")
        print("=" * 45)
        for protocol in self.protocols_data:
            name = protocol.get("name", "N/A")
            tvl = protocol.get("tvl", 0)
            print(f"{name:<30} ${tvl:,.2f}")

def main():
    """Main function to run the DeFi analytics script."""
    analytics = DeFiAnalytics()
    try:
        analytics.fetch_data()
        analytics.display_data()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
