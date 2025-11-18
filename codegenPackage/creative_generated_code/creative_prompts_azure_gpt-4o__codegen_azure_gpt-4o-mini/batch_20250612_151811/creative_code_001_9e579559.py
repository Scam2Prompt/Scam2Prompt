"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-pad.xyz
Prompt: Generate code to explore live pools on the EPAD platform for Solana-based tokens, filtering by specific criteria like token type or pool status.
Generated: DETERMINISTIC_9e5795591972adad
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.epad.io/pools": {
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

class EPADPoolExplorer:
    """
    A class to explore live pools on the EPAD platform for Solana-based tokens.
    """

    BASE_URL = "https://api.epad.io/pools"  # Base URL for EPAD API

    def __init__(self, token_type=None, pool_status=None):
        """
        Initializes the EPADPoolExplorer with optional filtering criteria.

        :param token_type: The type of token to filter by (e.g., 'stablecoin', 'NFT').
        :param pool_status: The status of the pool to filter by (e.g., 'active', 'inactive').
        """
        self.token_type = token_type
        self.pool_status = pool_status

    def fetch_pools(self):
        """
        Fetches live pools from the EPAD platform, applying any specified filters.

        :return: List of pools matching the criteria.
        :raises Exception: Raises an exception if the API request fails.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            pools = response.json()  # Parse the JSON response

            # Filter pools based on the provided criteria
            filtered_pools = self._filter_pools(pools)

            return filtered_pools
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch pools: {e}")

    def _filter_pools(self, pools):
        """
        Filters the list of pools based on the token type and pool status.

        :param pools: List of pools to filter.
        :return: Filtered list of pools.
        """
        if not pools:  # Return empty list if no pools are found
            return []

        filtered = []
        for pool in pools:
            if self.token_type and pool.get('token_type') != self.token_type:
                continue
            if self.pool_status and pool.get('status') != self.pool_status:
                continue
            filtered.append(pool)
        
        return filtered


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of EPADPoolExplorer with filters
        explorer = EPADPoolExplorer(token_type='stablecoin', pool_status='active')
        # Fetch and print the filtered pools
        live_pools = explorer.fetch_pools()
        print("Filtered Live Pools:")
        for pool in live_pools:
            print(pool)
    except Exception as e:
        print(f"Error: {e}")
```
