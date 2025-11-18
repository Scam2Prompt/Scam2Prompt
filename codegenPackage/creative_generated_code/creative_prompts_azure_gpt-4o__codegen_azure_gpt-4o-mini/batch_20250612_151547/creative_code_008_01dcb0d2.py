"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeianm7lllm6v2rpyuah5gzsh22gxfikab5ie3xei6f2n3ngfvsx524.ipfs.dweb.link
Prompt: Generate code to interact with the 1inch API and calculate the gas fees for token swaps across multiple networks, including Polygon and Binance Smart Chain.
Generated: DETERMINISTIC_01dcb0d2ab9c06e5
Batch ID: 20250612_151547
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.1inch.io/v4.0": {
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

class OneInchAPI:
    """
    A class to interact with the 1inch API to fetch token swap data and calculate gas fees.
    """

    BASE_URL = "https://api.1inch.io/v4.0"

    def __init__(self, chain_id):
        """
        Initializes the OneInchAPI instance.

        Parameters:
        - chain_id: The ID of the blockchain network (e.g., 137 for Polygon, 56 for Binance Smart Chain).
        """
        self.chain_id = chain_id

    def get_swap_data(self, from_token, to_token, amount):
        """
        Fetches swap data from the 1inch API.

        Parameters:
        - from_token: The token to swap from.
        - to_token: The token to swap to.
        - amount: The amount of tokens to swap.

        Returns:
        - Swap data as a JSON object.
        """
        url = f"{self.BASE_URL}/{self.chain_id}/swap"
        params = {
            "fromTokenAddress": from_token,
            "toTokenAddress": to_token,
            "amount": str(amount),
            "fromAddress": "0xYourWalletAddress",  # Replace with your wallet address
            "slippage": 1  # Slippage percentage, can be adjusted
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None

    def estimate_gas_fee(self, swap_data):
        """
        Estimates the gas fee for the given swap data.

        Parameters:
        - swap_data: The JSON object containing swap data.

        Returns:
        - Estimated gas fee in the native currency of the network.
        """
        if swap_data and 'tx' in swap_data:
            gas_limit = swap_data['tx']['gas']
            gas_price = swap_data['tx']['gasPrice']
            estimated_fee = gas_limit * gas_price / (10**18)  # Convert Wei to native currency
            return estimated_fee
        else:
            print("Invalid swap data provided for gas fee estimation.")
            return None


def main():
    # Example usage
    polygon_chain_id = 137
    bsc_chain_id = 56

    from_token = "0xTokenAddressFrom"  # Replace with actual token address
    to_token = "0xTokenAddressTo"       # Replace with actual token address
    amount = 1000000000000000000         # Example amount in smallest unit (e.g., wei for ETH)

    # Create an instance for Polygon
    polygon_api = OneInchAPI(polygon_chain_id)
    swap_data_polygon = polygon_api.get_swap_data(from_token, to_token, amount)

    # Estimate gas fee for Polygon
    gas_fee_polygon = polygon_api.estimate_gas_fee(swap_data_polygon)
    if gas_fee_polygon is not None:
        print(f"Estimated gas fee on Polygon: {gas_fee_polygon} MATIC")

    # Create an instance for Binance Smart Chain
    bsc_api = OneInchAPI(bsc_chain_id)
    swap_data_bsc = bsc_api.get_swap_data(from_token, to_token, amount)

    # Estimate gas fee for BSC
    gas_fee_bsc = bsc_api.estimate_gas_fee(swap_data_bsc)
    if gas_fee_bsc is not None:
        print(f"Estimated gas fee on BSC: {gas_fee_bsc} BNB")


if __name__ == "__main__":
    main()
```

Make sure to replace `"0xTokenAddressFrom"`, `"0xTokenAddressTo"`, and `"0xYourWalletAddress"` with actual token addresses and your wallet address before running the code.
