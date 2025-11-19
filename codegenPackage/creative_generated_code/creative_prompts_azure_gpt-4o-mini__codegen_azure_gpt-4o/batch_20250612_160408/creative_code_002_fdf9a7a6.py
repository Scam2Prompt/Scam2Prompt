"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama2.llamao.fi
Prompt: Create a query to access the DefiLlama API that compares the TVL of Ethereum and Solana chains, and explain how to interpret the results.
Generated: DETERMINISTIC_fdf9a7a69a59fe53
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi/chains": {
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

def fetch_tvl_data():
    """
    Fetches Total Value Locked (TVL) data for Ethereum and Solana from the DefiLlama API.

    Returns:
        dict: Contains TVL data for Ethereum and Solana.
    """
    try:
        # Base URL for the DefiLlama API
        base_url = "https://api.llama.fi/chains"

        # Send GET request to the API
        response = requests.get(base_url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse JSON response
        chains_data = response.json()

        # Extract TVL for Ethereum and Solana
        tvl_data = {chain['name']: chain['tvl'] for chain in chains_data if chain['name'] in ['Ethereum', 'Solana']}

        return tvl_data

    except requests.exceptions.RequestException as e:
        # Handle potential errors (network issues, invalid response, etc.)
        print(f"Error fetching TVL data from DefiLlama API: {e}")
        return None
    except KeyError as e:
        # Handle errors related to missing keys in the JSON response
        print(f"Unexpected data format received: {e}")
        return None


def compare_tvl(tvl_data):
    """
    Compares TVL between Ethereum and Solana.

    Args:
        tvl_data (dict): TVL data for Ethereum and Solana.

    Returns:
        str: A comparison summary between Ethereum and Solana TVL.
    """
    if not tvl_data or 'Ethereum' not in tvl_data or 'Solana' not in tvl_data:
        return "TVL data is incomplete or unavailable."

    eth_tvl = tvl_data['Ethereum']
    sol_tvl = tvl_data['Solana']

    if eth_tvl > sol_tvl:
        return f"Ethereum has a higher TVL (${eth_tvl:,.2f}) than Solana (${sol_tvl:,.2f})."
    elif eth_tvl < sol_tvl:
        return f"Solana has a higher TVL (${sol_tvl:,.2f}) than Ethereum (${eth_tvl:,.2f})."
    else:
        return f"Ethereum and Solana have the same TVL (${eth_tvl:,.2f})."


if __name__ == "__main__":
    # Fetch TVL data
    tvl_data = fetch_tvl_data()

    # Compare TVL between Ethereum and Solana
    result = compare_tvl(tvl_data)

    # Print the result
    print(result)
```

### How to interpret the results:
- The script fetches Total Value Locked (TVL) data for Ethereum and Solana from the DefiLlama API.
- TVL values are compared, and the script outputs which chain has a higher TVL or if they are equal. The output includes the TVL amounts formatted for readability.
