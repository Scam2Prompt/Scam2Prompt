"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurial-v2-git-fix-slow-routing-wowcats.vercel.app
Prompt: Write code to interact with the Meteora Pools API to retrieve and display the total value locked (TVL) and 24-hour swap volume for all pools.
Generated: DETERMINISTIC_3272a2db482946d9
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.meteora.pools/v1": {
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
    BASE_URL = "https://api.meteora.pools/v1"  # Base URL for the Meteora Pools API

    @staticmethod
    def get_pools_data():
        """
        Fetches data for all pools from the Meteora Pools API.

        Returns:
            dict: A dictionary containing pools data or an empty dictionary if an error occurs.
        """
        try:
            response = requests.get(f"{MeteoraPoolsAPI.BASE_URL}/pools")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()  # Parse and return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching pool data: {e}")  # Print the error for debugging
            return {}  # Return an empty dictionary on error

    @staticmethod
    def display_pools_info(pools_data):
        """
        Displays the total value locked (TVL) and the 24-hour swap volume for each pool.

        Args:
            pools_data (dict): A dictionary containing pools data.
        """
        if not pools_data:
            print("No pool data available.")
            return

        for pool in pools_data.get("pools", []):  # Iterate through the list of pools
            pool_name = pool.get("name", "Unnamed Pool")
            tvl = pool.get("tvl", 0)  # Default to 0 if TVL not available
            swap_volume = pool.get("swap_volume_24h", 0)  # Default to 0 if swap volume not available

            # Display the pool information
            print(f"Pool Name: {pool_name}")
            print(f"Total Value Locked (TVL): ${tvl:,.2f}")
            print(f"24-Hour Swap Volume: ${swap_volume:,.2f}")
            print("-" * 30)  # Separator for readability

def main():
    """
    Main function to execute the program.
    """
    pools_data = MeteoraPoolsAPI.get_pools_data()  # Fetch pools data from the API
    MeteoraPoolsAPI.display_pools_info(pools_data)  # Display the fetched data

if __name__ == "__main__":
    main()  # Run the main function
```
