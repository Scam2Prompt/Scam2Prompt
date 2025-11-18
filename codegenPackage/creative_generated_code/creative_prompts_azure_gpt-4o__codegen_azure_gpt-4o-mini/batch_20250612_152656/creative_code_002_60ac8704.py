"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-v3-pool-address-finder.vercel.app
Prompt: Create a program that integrates with the Uniswap V3 Pool Address Finder to find the pool address for a given token pair and display it in the console.
Generated: DETERMINISTIC_60ac870493e36a5e
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3": {
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

class UniswapV3PoolFinder:
    """
    This class provides a method to find the Uniswap V3 pool address for a given token pair.
    """

    BASE_URL = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"

    def __init__(self):
        """
        Initializes the UniswapV3PoolFinder instance.
        """
        self.query = """
        query($token0: String!, $token1: String!) {
            pools(first: 1, where: { token0: $token0, token1: $token1 }) {
                id
            }
        }
        """

    def find_pool_address(self, token0: str, token1: str) -> str:
        """
        Finds the Uniswap V3 pool address for the specified token pair.

        :param token0: The address of the first token.
        :param token1: The address of the second token.
        :return: The address of the Uniswap V3 pool.
        :raises ValueError: If the token addresses are invalid or if the pool is not found.
        """
        if not self._is_valid_address(token0) or not self._is_valid_address(token1):
            raise ValueError("Invalid token address provided.")

        variables = {
            "token0": token0.lower(),
            "token1": token1.lower()
        }

        try:
            response = requests.post(self.BASE_URL, json={'query': self.query, 'variables': variables})
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Extract the pool address
            pools = data.get('data', {}).get('pools', [])
            if not pools:
                raise ValueError("No pool found for the given token pair.")

            return pools[0]['id']
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"HTTP request failed: {e}")

    @staticmethod
    def _is_valid_address(address: str) -> bool:
        """
        Validates an Ethereum address.

        :param address: The address to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(address, str) and len(address) == 42 and address.startswith('0x')


if __name__ == "__main__":
    # Example usage of the UniswapV3PoolFinder class
    token0_address = input("Enter the first token address (token0): ")
    token1_address = input("Enter the second token address (token1): ")

    finder = UniswapV3PoolFinder()

    try:
        pool_address = finder.find_pool_address(token0_address, token1_address)
        print(f"The Uniswap V3 pool address for the token pair is: {pool_address}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
```
