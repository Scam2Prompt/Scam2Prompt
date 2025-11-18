"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Suggest best practices for optimizing gas fees in Ethereum transactions using Linea's security approach, and provide example code.
Generated: DETERMINISTIC_dc25bc4d49fed5cf
Batch ID: 20250612_153812
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linea.network": {
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

class EthereumGasOptimizer:
    def __init__(self, api_key: str, endpoint: str = "https://api.linea.network"):
        """
        Initialize the EthereumGasOptimizer with API key and endpoint.

        :param api_key: API key for authentication.
        :param endpoint: API endpoint for Linea's services.
        """
        self.api_key = api_key
        self.endpoint = endpoint

    def get_gas_price(self) -> float:
        """
        Fetch the current gas price from the Linea network.

        :return: Current gas price in Gwei.
        :raises Exception: If the API call fails or returns an error.
        """
        try:
            response = requests.get(f"{self.endpoint}/gas-price", headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for bad responses
            gas_data = response.json()
            return gas_data['gasPrice']
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch gas price: {e}")

    def estimate_gas_limit(self, transaction_data: dict) -> int:
        """
        Estimate the gas limit for a given transaction.

        :param transaction_data: Dictionary containing transaction data.
        :return: Estimated gas limit.
        :raises Exception: If the estimation fails.
        """
        try:
            response = requests.post(f"{self.endpoint}/estimate-gas", json=transaction_data,
                                     headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for bad responses
            gas_limit_data = response.json()
            return gas_limit_data['gasLimit']
        except requests.RequestException as e:
            raise Exception(f"Failed to estimate gas limit: {e}")

    def optimize_transaction(self, transaction_data: dict) -> dict:
        """
        Optimize the transaction by estimating gas limit and fetching gas price.

        :param transaction_data: Dictionary containing transaction data.
        :return: Optimized transaction data with gas price and limit.
        :raises Exception: If any step in the optimization fails.
        """
        try:
            gas_price = self.get_gas_price()  # Get current gas price
            gas_limit = self.estimate_gas_limit(transaction_data)  # Estimate gas limit

            # Optimize transaction data
            transaction_data['gasPrice'] = gas_price
            transaction_data['gasLimit'] = gas_limit

            return transaction_data
        except Exception as e:
            raise Exception(f"Transaction optimization failed: {e}")

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    optimizer = EthereumGasOptimizer(api_key=API_KEY)

    # Example transaction data
    transaction_data = {
        "to": "0xRecipientAddress",
        "value": "0.01",
        "data": "0xYourData"  # Optional
    }

    try:
        optimized_transaction = optimizer.optimize_transaction(transaction_data)
        print("Optimized Transaction:", optimized_transaction)
    except Exception as e:
        print("Error:", str(e))
```
