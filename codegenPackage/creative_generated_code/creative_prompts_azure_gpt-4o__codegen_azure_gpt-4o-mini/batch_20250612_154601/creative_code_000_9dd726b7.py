"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-app-git-feat-permissioned-vault-wowcats.vercel.app
Prompt: Write code to interact with the Meteora Pools API to retrieve and display the total value locked (TVL) and 24-hour swap volume for all dynamic pools.
Generated: DETERMINISTIC_9dd726b787bbd2e0
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.meteora.pools": {
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

class MeteoraAPI:
    BASE_URL = "https://api.meteora.pools"

    def __init__(self):
        """Initialize the MeteoraAPI class."""
        pass

    def fetch_dynamic_pools(self):
        """Fetch all dynamic pools from the Meteora Pools API.

        Returns:
            list: A list of dynamic pools if the request is successful, 
                  None otherwise.
        """
        endpoint = f"{self.BASE_URL}/dynamic-pools"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('pools', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching dynamic pools: {e}")
            return None

    def get_tvl_and_swap_volume(self):
        """Retrieve and display the total value locked (TVL) and 
        24-hour swap volume for all dynamic pools.

        Returns:
            None: This function prints the results to stdout.
        """
        pools = self.fetch_dynamic_pools()
        if pools is None:
            print("Failed to retrieve pools.")
            return
        
        total_tvl = 0
        total_swap_volume = 0
        
        # Iterate through each pool to aggregate TVL and swap volume
        for pool in pools:
            tvl = pool.get('totalValueLocked', 0)
            swap_volume = pool.get('swapVolume24h', 0)

            total_tvl += tvl
            total_swap_volume += swap_volume

        # Display the results
        print(f"Total Value Locked (TVL): {total_tvl:.2f}")
        print(f"24-hour Swap Volume: {total_swap_volume:.2f}")


if __name__ == "__main__":
    api = MeteoraAPI()
    api.get_tvl_and_swap_volume()
```
