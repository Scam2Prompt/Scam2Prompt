"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lessfeesandgas.web.app
Prompt: Generate code to compare transaction fees between Ethereum and Solana networks using their respective APIs, referencing the "Less Fees & Gas" concept.
Generated: DETERMINISTIC_21abac3dde1a8145
Batch ID: 20250612_152739
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://public-api.solscan.io/v1/fees": {
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

class TransactionFeeComparator:
    """A class to compare transaction fees between Ethereum and Solana networks."""

    ETHEREUM_API_URL = "https://api.etherscan.io/api"
    SOLANA_API_URL = "https://public-api.solscan.io/v1/fees"
    ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your Etherscan API key

    def get_ethereum_fee(self):
        """
        Fetch the current average transaction fee for Ethereum.
        
        Returns:
            float: The average transaction fee in Gwei.
        """
        try:
            params = {
                'module': 'proxy',
                'action': 'eth_gasPrice',
                'apikey': self.ETHERSCAN_API_KEY,
            }
            response = requests.get(self.ETHEREUM_API_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            # Return the gas price in Gwei
            gas_price_wei = int(response.json().get('result', 0))
            gas_price_gwei = gas_price_wei / 1e9
            return gas_price_gwei

        except requests.exceptions.RequestException as e:
            print(f"Error fetching Ethereum fee: {e}")
            return None

    def get_solana_fee(self):
        """
        Fetch the current transaction fee for Solana.
        
        Returns:
            float: The transaction fee in SOL (Solana's native token).
        """
        try:
            response = requests.get(self.SOLANA_API_URL)
            response.raise_for_status()  # Raise an error for bad responses

            # Return the fee value
            return response.json().get('fee', 0)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching Solana fee: {e}")
            return None

    def compare_fees(self):
        """
        Compare transaction fees between Ethereum and Solana.
        
        Returns:
            str: A comparison statement on the fees.
        """
        eth_fee = self.get_ethereum_fee()
        sol_fee = self.get_solana_fee()

        if eth_fee is None or sol_fee is None:
            return "Could not retrieve fee information for comparison."

        comparison = "Ethereum transaction fee: {:.6f} Gwei\n".format(eth_fee)
        comparison += "Solana transaction fee: {:.6f} SOL".format(sol_fee)

        if eth_fee < sol_fee:
            comparison += "\nEthereum has lower fees."
        else:
            comparison += "\nSolana has lower fees."

        return comparison


if __name__ == "__main__":
    comparator = TransactionFeeComparator()
    result = comparator.compare_fees()
    print(result)
``` 

Make sure to replace `"YOUR_ETHERSCAN_API_KEY"` with your actual Etherscan API key to run the code.
