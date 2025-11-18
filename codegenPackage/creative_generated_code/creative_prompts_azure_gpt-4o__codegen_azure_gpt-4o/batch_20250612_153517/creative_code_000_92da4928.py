"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-dv6.pages.dev
Prompt: Write a script to interact with the SUN.io API to query the Total Value Locked (TVL) for stablecoin pools, SunSwap pools, and farming pools on the TRON blockchain.
Generated: DETERMINISTIC_92da4928e67172ad
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sun.io/v1": {
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

# Constants for the SUN.io API and endpoints
API_BASE_URL = "https://api.sun.io/v1"
ENDPOINTS = {
    "stablecoin_pools": "/stablecoin-pools",
    "sunswap_pools": "/sunswap-pools",
    "farming_pools": "/farming-pools",
}

def fetch_tvl(endpoint):
    """
    Fetch the Total Value Locked (TVL) for a given endpoint.

    Args:
        endpoint (str): The API endpoint to query.

    Returns:
        dict: Parsed JSON response containing TVL data.

    Raises:
        ValueError: If the response contains an error or is invalid.
    """
    try:
        url = f"{API_BASE_URL}{endpoint}"
        response = requests.get(url, timeout=10)  # Set a timeout for the API request
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        data = response.json()  # Parse the JSON response

        if not data or "data" not in data:
            raise ValueError(f"Invalid response format: {data}")
        
        return data["data"]
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise ValueError(f"An error occurred while making the API request: {e}")
    except ValueError as e:
        # Handle invalid response formats or missing data
        raise ValueError(f"An error occurred while processing the response: {e}")

def main():
    """
    Main function to query TVL data for stablecoin pools, SunSwap pools, and farming pools.
    """
    try:
        print("Fetching TVL data from SUN.io API...\n")

        # Fetch TVL for each pool type
        stablecoin_tvl = fetch_tvl(ENDPOINTS["stablecoin_pools"])
        sunswap_tvl = fetch_tvl(ENDPOINTS["sunswap_pools"])
        farming_tvl = fetch_tvl(ENDPOINTS["farming_pools"])

        # Display the results
        print("Stablecoin Pools TVL:")
        print(stablecoin_tvl, "\n")

        print("SunSwap Pools TVL:")
        print(sunswap_tvl, "\n")

        print("Farming Pools TVL:")
        print(farming_tvl, "\n")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
