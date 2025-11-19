"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-app-git-sam-racx-1186-ui-dynamic-pool-pa-2a19c8-wowcats.vercel.app
Prompt: Can you provide an example of how to sort pools by total value locked (TVL) using the Meteora API?
Generated: DETERMINISTIC_9b147153c9daee7f
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.meteora.com/v1/pools": {
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

def fetch_pools_data(api_url):
    """
    Fetch the pools data from the Meteora API.

    :param api_url: The URL of the Meteora API endpoint.
    :return: A list of pools data if successful, else None.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pools data: {e}")
        return None


def sort_pools_by_tvl(pools):
    """
    Sort the pools by Total Value Locked (TVL) in descending order.

    :param pools: A list of pool dictionaries containing 'tvl' as a key.
    :return: A sorted list of pools by TVL in descending order.
    """
    try:
        # Sort pools by TVL (descending order)
        return sorted(pools, key=lambda pool: pool.get('tvl', 0), reverse=True)
    except TypeError as e:
        print(f"Error sorting pools by TVL: {e}")
        return None


def main():
    """
    Main function to fetch and sort pools by TVL.
    """
    # Meteora API endpoint URL (replace with the actual endpoint URL)
    api_url = "https://api.meteora.com/v1/pools"

    # Fetch pools data from the API
    pools_data = fetch_pools_data(api_url)

    if pools_data is None:
        print("Failed to fetch pools data.")
        return

    # Sort pools by TVL
    sorted_pools = sort_pools_by_tvl(pools_data)

    if sorted_pools is None:
        print("Failed to sort pools by TVL.")
        return

    # Output the sorted pools
    print("Pools sorted by TVL (descending order):")
    for pool in sorted_pools:
        print(f"Pool Name: {pool.get('name', 'Unknown')} | TVL: {pool.get('tvl', 'Unknown')}")


if __name__ == "__main__":
    main()
```
