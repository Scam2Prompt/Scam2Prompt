"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-app-git-deposit-one-tx-wowcats.vercel.app
Prompt: Write code to interact with the Meteora Pools API to retrieve the total value locked (TVL) and 24-hour swap volume for all pools.
Generated: DETERMINISTIC_d11fb422e8c5e37f
Batch ID: 20250612_145810
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.meteorapools.com/v1": {
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

class MeteoraPoolsAPI:
    """
    A class to interact with the Meteora Pools API to retrieve TVL and 24-hour swap volume data.
    """

    BASE_URL = "https://api.meteorapools.com/v1"  # Replace with the actual API base URL if different.

    def __init__(self):
        """
        Initializes the API interaction class.
        """
        pass

    def get_pools_data(self):
        """
        Fetches data for all pools from the Meteora Pools API.

        Returns:
            dict: JSON response containing pools data.
        Raises:
            Exception: If the API request fails or returns an error response.
        """
        endpoint = f"{self.BASE_URL}/pools"  # Endpoint for pools data
        try:
            response = requests.get(endpoint, timeout=10)  # Set a timeout to avoid long waits
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching pools data: {e}")

    def get_tvl_and_swap_volume(self):
        """
        Retrieves the total value locked (TVL) and 24-hour swap volume for all pools.

        Returns:
            list: A list of dictionaries containing pool ID, TVL, and 24-hour swap volume.
        Raises:
            Exception: If there is an error in fetching or processing data.
        """
        try:
            pools_data = self.get_pools_data()  # Fetch pools data
            result = []

            # Extract relevant data for each pool
            for pool in pools_data.get("pools", []):
                pool_id = pool.get("id", "unknown")  # Pool ID
                tvl = pool.get("tvl", 0)  # Total Value Locked
                swap_volume_24h = pool.get("swapVolume24h", 0)  # 24-hour Swap Volume

                # Append the extracted data to the result list
                result.append({
                    "pool_id": pool_id,
                    "tvl": tvl,
                    "swap_volume_24h": swap_volume_24h
                })

            return result
        except Exception as e:
            raise Exception(f"Error processing pools data: {e}")


# Main execution block
if __name__ == "__main__":
    """
    Main function to fetch and display TVL and 24-hour swap volume for all pools.
    """
    api = MeteoraPoolsAPI()

    try:
        # Retrieve TVL and swap volume data
        pools_info = api.get_tvl_and_swap_volume()

        # Display the results
        print("Pools Data:")
        for pool in pools_info:
            print(f"Pool ID: {pool['pool_id']}, TVL: {pool['tvl']}, 24h Swap Volume: {pool['swap_volume_24h']}")
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
```
wap_volume']}")
            print("-" * 40)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
