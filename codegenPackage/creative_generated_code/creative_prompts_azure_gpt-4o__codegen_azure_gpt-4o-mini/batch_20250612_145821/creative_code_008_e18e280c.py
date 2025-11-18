"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.eu
Prompt: Write code to calculate gas fees for transactions on the Arbitrum network and compare them to Ethereum mainnet fees.
Generated: DETERMINISTIC_e18e280cb61f7d2b
Batch ID: 20250612_145821
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbitrum.io/fees": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api": {
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

class GasFeeCalculator:
    """A class to calculate gas fees for transactions on the Arbitrum network and compare them to Ethereum mainnet fees."""

    ARBITRUM_GAS_API = "https://api.arbitrum.io/fees"
    ETHEREUM_GAS_API = "https://api.etherscan.io/api"

    def __init__(self, etherscan_api_key):
        """
        Initializes the GasFeeCalculator with the provided Etherscan API key.

        Parameters:
            etherscan_api_key (str): Your Etherscan API key for fetching Ethereum gas fees.
        """
        self.etherscan_api_key = etherscan_api_key

    def get_arbitrum_gas_fees(self):
        """Fetches current gas fees from the Arbitrum network."""
        try:
            response = requests.get(self.ARBITRUM_GAS_API)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['result']['fast']  # Assuming 'fast' is the required fee type
        except requests.RequestException as e:
            print(f"Error fetching Arbitrum gas fees: {e}")
            return None

    def get_ethereum_gas_fees(self):
        """Fetches current gas fees from the Ethereum mainnet."""
        try:
            params = {
                'module': 'proxy',
                'action': 'eth_gasPrice',
                'apikey': self.etherscan_api_key
            }
            response = requests.get(self.ETHEREUM_GAS_API, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return int(data['result'], 16)  # Convert hex gas price to int
        except requests.RequestException as e:
            print(f"Error fetching Ethereum gas fees: {e}")
            return None

    def compare_gas_fees(self):
        """Compares gas fees between Arbitrum and Ethereum."""
        arb_gas_fee = self.get_arbitrum_gas_fees()
        eth_gas_fee = self.get_ethereum_gas_fees()

        if arb_gas_fee is not None and eth_gas_fee is not None:
            print(f"Arbitrum Gas Fee (Gwei): {arb_gas_fee}")
            print(f"Ethereum Gas Fee (Gwei): {eth_gas_fee / 1e9}")  # Convert Wei to Gwei

            if arb_gas_fee < (eth_gas_fee / 1e9):
                print("Arbitrum gas fees are lower than Ethereum.")
            else:
                print("Ethereum gas fees are lower than or equal to Arbitrum.")
        else:
            print("Could not compare gas fees due to an error in fetching data.")

if __name__ == "__main__":
    ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your Etherscan API key
    gas_fee_calculator = GasFeeCalculator(ETHERSCAN_API_KEY)
    gas_fee_calculator.compare_gas_fees()
```
