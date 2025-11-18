"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama2.llamao.fi
Prompt: Write a program to compare the yield farming returns across different chains (e.g., Ethereum, Binance Smart Chain) using DefiLlama's API.
Generated: DETERMINISTIC_7949b84e86c9475f
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/v1/yields": {
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

class DefiYieldFarmComparer:
    """
    A class to compare yield farming returns across different blockchain networks
    using the DefiLlama API.
    """

    API_URL = "https://api.defillama.com/v1/yields"

    def __init__(self):
        """
        Initializes the DefiYieldFarmComparer instance.
        """
        self.data = {}

    def fetch_yield_data(self):
        """
        Fetches yield farming data from the DefiLlama API.
        
        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")

    def compare_yields(self, chain_name):
        """
        Compares yield farming returns for a specified blockchain network.

        Args:
            chain_name (str): The name of the blockchain network to compare yields for.

        Returns:
            dict: A dictionary containing the yield farming data for the specified chain.

        Raises:
            ValueError: If the chain name is not found in the fetched data.
        """
        if not self.data:
            raise Exception("Yield data not fetched. Please fetch data first.")

        # Normalize the chain name for comparison
        chain_name = chain_name.lower()
        yield_data = {}

        for item in self.data:
            if item['chain'].lower() == chain_name:
                yield_data[item['project']] = item['apy']

        if not yield_data:
            raise ValueError(f"No yield data found for the chain: {chain_name}")

        return yield_data

    def display_yields(self, yields):
        """
        Displays the yield farming returns in a formatted manner.

        Args:
            yields (dict): A dictionary of yields to be displayed.
        """
        print(f"Yield farming returns on the specified chain:")
        for project, apy in yields.items():
            print(f"{project}: {apy:.2f}% APY")

if __name__ == "__main__":
    comparer = DefiYieldFarmComparer()

    try:
        # Fetch yield data from the API
        comparer.fetch_yield_data()

        # Specify the chain to compare yields for
        chain_name = input("Enter the blockchain network (e.g., Ethereum, Binance Smart Chain): ")

        # Compare yields and display results
        yields = comparer.compare_yields(chain_name)
        comparer.display_yields(yields)

    except Exception as e:
        print(f"An error occurred: {e}")
```
