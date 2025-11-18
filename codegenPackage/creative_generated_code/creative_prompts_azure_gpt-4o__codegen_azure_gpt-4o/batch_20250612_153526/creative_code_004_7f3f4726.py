"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft20-git-arbitrum-toraverse.vercel.app
Prompt: Write a program to calculate gas savings using Tegro's trade roll-ups feature compared to other decentralized exchanges. Include API calls for retrieving testnet stats.
Generated: DETERMINISTIC_7f3f47262bed8f41
Batch ID: 20250612_153526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.otherdex.com/testnet/stats": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.tegro.com/testnet/stats": {
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
import requests  # For making API calls
import json  # For parsing JSON responses

# Constants
TEGRO_API_URL = "https://api.tegro.com/testnet/stats"  # Example API URL for Tegro's testnet stats
OTHER_DEX_API_URL = "https://api.otherdex.com/testnet/stats"  # Example API URL for other DEX's testnet stats

def get_api_data(url):
    """
    Makes an API call to the given URL and returns the JSON response.
    Includes error handling for failed requests.
    
    Args:
        url (str): The API endpoint URL.
    
    Returns:
        dict: JSON data from the API response.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def calculate_gas_savings(tegro_data, other_dex_data):
    """
    Calculates and compares gas savings between Tegro's trade roll-ups feature
    and another decentralized exchange.
    
    Args:
        tegro_data (dict): JSON data from Tegro's API.
        other_dex_data (dict): JSON data from another DEX's API.
    
    Returns:
        float: Gas savings percentage.
    """
    try:
        # Extract relevant data (assuming 'average_gas' is a key in the API response)
        tegro_avg_gas = tegro_data.get("average_gas", None)
        other_dex_avg_gas = other_dex_data.get("average_gas", None)

        # Validate the data
        if tegro_avg_gas is None or other_dex_avg_gas is None:
            raise ValueError("Missing 'average_gas' data from one or both APIs.")

        # Calculate savings percentage
        savings = ((other_dex_avg_gas - tegro_avg_gas) / other_dex_avg_gas) * 100
        return savings

    except ValueError as ve:
        print(f"Validation error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error during calculation: {e}")
        return None


def main():
    """
    Main driver function for the program.
    """
    print("Fetching data from APIs...")
    tegro_data = get_api_data(TEGRO_API_URL)
    other_dex_data = get_api_data(OTHER_DEX_API_URL)

    # Check if data was successfully retrieved
    if tegro_data is None or other_dex_data is None:
        print("Failed to fetch data from one or both APIs. Exiting...")
        return

    print("Calculating gas savings...")
    savings = calculate_gas_savings(tegro_data, other_dex_data)

    if savings is not None:
        print(f"Gas savings using Tegro's trade roll-ups: {savings:.2f}%")
    else:
        print("Failed to calculate gas savings.")


if __name__ == "__main__":
    main()
```
