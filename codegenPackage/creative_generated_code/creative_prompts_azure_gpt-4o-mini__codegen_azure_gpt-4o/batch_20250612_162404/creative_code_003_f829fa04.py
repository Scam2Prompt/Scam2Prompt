"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-dot-com.pages.dev
Prompt: Explain how to use the Beefy API to access data on total value locked (TVL) and the number of vaults across different chains.
Generated: DETERMINISTIC_f829fa044d43592c
Batch ID: 20250612_162404
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.beefy.finance/vaults": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.beefy.finance/tvl": {
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

def fetch_beefy_data(api_url):
    """
    Fetches data from the Beefy API.

    Args:
        api_url (str): The URL of the Beefy API.

    Returns:
        dict: The JSON response from the API if successful.

    Raises:
        ValueError: If the API response indicates failure.
    """
    try:
        # Make the request to the Beefy API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Parse and return JSON data
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error while fetching Beefy data: {e}")
        raise
    except ValueError:
        # Handle JSON parsing errors
        print("Error parsing JSON response from Beefy API.")
        raise


def get_tvl_and_vaults():
    """
    Fetches Beefy data and extracts Total Value Locked (TVL) and number of vaults
    across different chains.

    Returns:
        dict: A dictionary containing TVL and vault count for each chain.
    """
    api_url = "https://api.beefy.finance/tvl"  # Beefy TVL endpoint
    vaults_url = "https://api.beefy.finance/vaults"  # Beefy vaults endpoint

    try:
        # Fetch TVL data
        tvl_data = fetch_beefy_data(api_url)

        # Fetch vault data
        vaults_data = fetch_beefy_data(vaults_url)

        # Parse TVL and vault counts by chain
        result = {}
        for chain, tvl in tvl_data.items():
            # Count the number of vaults per chain
            chain_vaults = [vault for vault in vaults_data if vault.get("chain") == chain]
            result[chain] = {
                "tvl": tvl,
                "vault_count": len(chain_vaults)
            }

        return result
    except Exception as e:
        print(f"Error while processing Beefy data: {e}")
        return None


if __name__ == "__main__":
    # Entry point for the script
    try:
        # Fetch TVL and vault details
        data = get_tvl_and_vaults()
        if data:
            print("Beefy Data:")
            for chain, details in data.items():
                print(f"Chain: {chain}, TVL: {details['tvl']}, Vaults: {details['vault_count']}")
        else:
            print("Failed to retrieve Beefy data.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
