"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orikod.com
Prompt: Generate Python code to interact with the Arbitrum Rollup API for querying transaction history and calculating gas savings.
Generated: DETERMINISTIC_63e2257856d67851
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbitrum.io/rpc": {
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

class ArbitrumAPI:
    """Class to interact with the Arbitrum Rollup API."""

    BASE_URL = "https://api.arbitrum.io/rpc"

    def __init__(self):
        """Initialize the ArbitrumAPI class."""
        self.session = requests.Session()

    def get_transaction_history(self, address, start_block=0, end_block='latest'):
        """
        Retrieve the transaction history for a given Ethereum address on Arbitrum.
        
        :param address: str - The Ethereum address to query.
        :param start_block: int - The starting block number for the query.
        :param end_block: int or str - The ending block number, default is 'latest'.
        :return: list - A list of transaction details for the given address.
        :raises ValueError: If the address is not a valid Ethereum address.
        :raises Exception: For any request-related errors.
        """
        if not self.is_valid_address(address):
            raise ValueError("Invalid Ethereum address provided.")

        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByAddress",
            "params": [address, start_block, end_block],
            "id": 1
        }

        try:
            response = self.session.post(self.BASE_URL, json=payload)
            response.raise_for_status()  # Raise an error for HTTP error codes
            result = response.json().get('result', [])
            return result
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error retrieving transaction history: {str(e)}")

    def calculate_gas_savings(self, transactions):
        """
        Calculate gas savings from a list of Ethereum transactions.

        :param transactions: list - A list of transaction dictionaries.
        :return: float - The total gas savings calculated.
        """
        total_gas_saved = 0.0
        
        for tx in transactions:
            gas_price = int(tx['gasPrice']) if 'gasPrice' in tx else 0
            gas_limit = int(tx['gas']) if 'gas' in tx else 0
            # Assuming a hypothetical gas price on Arbitrum is lower than Ethereum mainnet
            eth_gas_price = gas_price * 1.5  # Example conversion factor
            savings = (eth_gas_price - gas_price) * gas_limit
            total_gas_saved += savings

        return total_gas_saved

    @staticmethod
    def is_valid_address(address):
        """
        Validate an Ethereum address.

        :param address: str - The Ethereum address to validate.
        :return: bool - True if valid, False otherwise.
        """
        return len(address) == 42 and address.startswith("0x")

# Example usage
if __name__ == "__main__":
    address_to_query = "0xYourEthereumAddressHere"
    api = ArbitrumAPI()
    
    try:
        # Fetch transaction history
        transactions = api.get_transaction_history(address_to_query)
        print("Transaction History:", transactions)

        # Calculate gas savings
        gas_savings = api.calculate_gas_savings(transactions)
        print(f"Total Gas Savings: {gas_savings} wei")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

Make sure to replace `"0xYourEthereumAddressHere"` with a valid Ethereum address before running the code.
