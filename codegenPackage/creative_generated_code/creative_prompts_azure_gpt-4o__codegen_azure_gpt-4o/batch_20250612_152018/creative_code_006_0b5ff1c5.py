"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareairdrop.com
Prompt: Develop a Python script to calculate gas fees for transactions on Flare's network, highlighting its cost efficiency compared to other platforms.
Generated: DETERMINISTIC_0b5ff1c5a77b2df3
Batch ID: 20250612_152018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=gastracker&action=gasoracle": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.flare.network/gas-price": {
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

def get_gas_price(network):
    """
    Fetches the current gas price for the specified network.

    Args:
        network (str): The name of the blockchain network (e.g., 'Flare', 'Ethereum').

    Returns:
        float: The current gas price in gwei.

    Raises:
        ValueError: If the network is unsupported or an error occurs during the API call.
    """
    # Dictionary mapping network names to their respective API endpoints
    gas_price_endpoints = {
        "Flare": "https://api.flare.network/gas-price",
        "Ethereum": "https://api.etherscan.io/api?module=gastracker&action=gasoracle",
    }

    if network not in gas_price_endpoints:
        raise ValueError(f"Unsupported network: {network}")

    try:
        response = requests.get(gas_price_endpoints[network])
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Extract gas price from the response based on network
        if network == "Flare":
            return response.json().get("gasPrice", 0)  # Example: {'gasPrice': 0.00001}
        elif network == "Ethereum":
            return float(response.json().get("result", {}).get("SafeGasPrice", 0))
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching gas price for {network}: {e}")


def calculate_transaction_fee(gas_price, gas_limit):
    """
    Calculates the transaction fee based on the gas price and gas limit.

    Args:
        gas_price (float): Current gas price in gwei.
        gas_limit (int): The gas limit for the transaction.

    Returns:
        float: The transaction fee in ETH.
    """
    # Convert gas price from gwei to ETH (1 ETH = 1e9 gwei)
    return (gas_price * gas_limit) / 1e9


def compare_gas_fees(gas_limit):
    """
    Compares the gas fees for a given gas limit between Flare and Ethereum.

    Args:
        gas_limit (int): The gas limit for the transaction.

    Returns:
        dict: A dictionary containing gas fees for Flare and Ethereum.
    """
    try:
        flare_gas_price = get_gas_price("Flare")
        ethereum_gas_price = get_gas_price("Ethereum")
        
        flare_fee = calculate_transaction_fee(flare_gas_price, gas_limit)
        ethereum_fee = calculate_transaction_fee(ethereum_gas_price, gas_limit)

        return {
            "FlareFee_ETH": flare_fee,
            "EthereumFee_ETH": ethereum_fee,
            "CostEfficiency": "Flare" if flare_fee < ethereum_fee else "Ethereum"
        }
    except ValueError as e:
        print(f"Error during comparison: {e}")
        return {}


if __name__ == "__main__":
    """
    Entry point of the script. Demonstrates gas fee comparison for a sample transaction.
    """
    # Example gas limit for a simple transaction
    GAS_LIMIT = 21000

    try:
        fees_comparison = compare_gas_fees(GAS_LIMIT)
        if fees_comparison:
            print(f"Gas Fees Comparison for Gas Limit {GAS_LIMIT}:")
            print(f"Flare Fee (ETH): {fees_comparison['FlareFee_ETH']}")
            print(f"Ethereum Fee (ETH): {fees_comparison['EthereumFee_ETH']}")
            print(f"Cost-Efficient Platform: {fees_comparison['CostEfficiency']}")
        else:
            print("Failed to fetch or compare gas fees.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
