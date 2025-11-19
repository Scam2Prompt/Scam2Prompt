"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdexx.com
Prompt: How can I implement cross-chain liquidity aggregation for perpetual contracts using Aster's API?
Generated: DETERMINISTIC_a73bb3a9d030d0ad
Batch ID: 20250612_163133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.finance/v1": {
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
from typing import List, Dict, Union

# Constants
API_BASE_URL = "https://api.aster.finance/v1"
TIMEOUT = 10  # Timeout for API requests in seconds

class CrossChainLiquidityAggregator:
    """
    A class to handle cross-chain liquidity aggregation for perpetual contracts using Aster's API.
    """

    def __init__(self, api_key: str):
        """
        Initialize the aggregator with the API key for authentication.
        
        :param api_key: Your Aster API key for authorization.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def fetch_liquidity_pools(self, chains: List[str]) -> List[Dict[str, Union[str, float]]]:
        """
        Fetch available liquidity pools across multiple chains.
        
        :param chains: List of chains to query liquidity pools from.
        :return: List of liquidity pools with details like name, volume, and chain.
        """
        try:
            url = f"{API_BASE_URL}/liquidity-pools"
            payload = {"chains": chains}
            response = requests.post(url, headers=self.headers, json=payload, timeout=TIMEOUT)

            # Raise an error if the request failed
            response.raise_for_status()

            return response.json().get("pools", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching liquidity pools: {str(e)}")
            return []

    def aggregate_liquidity(self, contract_id: str, liquidity_pools: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[str, float]]:
        """
        Aggregate liquidity across the selected pools for a given perpetual contract.
        
        :param contract_id: The ID of the perpetual contract to aggregate liquidity for.
        :param liquidity_pools: List of liquidity pools with details like name, volume, and chain.
        :return: Aggregated liquidity details.
        """
        try:
            url = f"{API_BASE_URL}/aggregate-liquidity"
            payload = {
                "contract_id": contract_id,
                "pools": liquidity_pools
            }
            response = requests.post(url, headers=self.headers, json=payload, timeout=TIMEOUT)

            # Raise an error if the request failed
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error aggregating liquidity: {str(e)}")
            return {"status": "error", "message": str(e)}

    def execute_liquidity_swap(self, contract_id: str, pool_id: str, amount: float) -> Dict[str, Union[str, float]]:
        """
        Execute a liquidity swap for a perpetual contract using a specific pool.
        
        :param contract_id: The ID of the perpetual contract.
        :param pool_id: The ID of the liquidity pool to execute the swap with.
        :param amount: The amount of liquidity to swap.
        :return: Swap execution result.
        """
        try:
            url = f"{API_BASE_URL}/execute-swap"
            payload = {
                "contract_id": contract_id,
                "pool_id": pool_id,
                "amount": amount
            }
            response = requests.post(url, headers=self.headers, json=payload, timeout=TIMEOUT)

            # Raise an error if the request failed
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error executing liquidity swap: {str(e)}")
            return {"status": "error", "message": str(e)}

def main():
    # Example usage of the CrossChainLiquidityAggregator class
    api_key = "your_api_key_here"  # Replace with your actual Aster API key
    aggregator = CrossChainLiquidityAggregator(api_key)

    # Fetch liquidity pools across chains
    chains = ["ethereum", "polygon", "binance-smart-chain"]
    liquidity_pools = aggregator.fetch_liquidity_pools(chains)

    if liquidity_pools:
        print("Available Liquidity Pools:")
        for pool in liquidity_pools:
            print(pool)

        # Aggregate liquidity for a specific perpetual contract
        contract_id = "example_contract_id"  # Replace with your contract ID
        aggregated_data = aggregator.aggregate_liquidity(contract_id, liquidity_pools)
        print("Aggregated Liquidity Data:", aggregated_data)

        # Execute a liquidity swap (example)
        pool_id = liquidity_pools[0]["id"]  # Choose a pool ID from the fetched pools
        amount = 100.0  # Replace with the desired swap amount
        swap_result = aggregator.execute_liquidity_swap(contract_id, pool_id, amount)
        print("Liquidity Swap Result:", swap_result)
    else:
        print("No liquidity pools available.")

if __name__ == "__main__":
    main()
```
