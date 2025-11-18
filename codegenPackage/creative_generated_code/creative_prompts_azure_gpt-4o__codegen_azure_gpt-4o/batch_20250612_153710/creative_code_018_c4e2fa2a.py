"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Generate a code example to use Chainbase's programmable data intelligence for creating advanced crypto insights.
Generated: DETERMINISTIC_c4e2fa2a6cfd314e
Batch ID: 20250612_153710
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.com/v1": {
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
# This script demonstrates how to use Chainbase's programmable data intelligence
# to create advanced crypto insights using Python.

import requests

# Constants
CHAINBASE_API_URL = "https://api.chainbase.com/v1"  # Base URL for Chainbase API
CHAINBASE_API_KEY = "your_chainbase_api_key"       # Replace with your actual API key

# Function to get crypto transaction insights from Chainbase
def get_crypto_insights(chain_name: str, contract_address: str, start_block: int, end_block: int):
    """
    Fetch advanced crypto insights for a specified chain and contract.

    :param chain_name: Name of the blockchain (e.g., 'ethereum')
    :param contract_address: Address of the smart contract to analyze
    :param start_block: Starting block number for analysis
    :param end_block: Ending block number for analysis
    :return: Parsed JSON response containing insights
    """
    # Endpoint for programmable data intelligence (replace with correct endpoint)
    endpoint = f"{CHAINBASE_API_URL}/data/transactions"

    # API request headers
    headers = {
        "Authorization": f"Bearer {CHAINBASE_API_KEY}",
        "Content-Type": "application/json"
    }

    # API request parameters
    payload = {
        "chain": chain_name,
        "contract": contract_address,
        "start_block": start_block,
        "end_block": end_block
    }

    try:
        # Make the API request
        response = requests.post(endpoint, json=payload, headers=headers)

        # Raise an exception if the request was not successful
        response.raise_for_status()

        # Parse the JSON response
        insights = response.json()
        return insights

    except requests.exceptions.RequestException as e:
        # Handle HTTP and connection errors
        print(f"An error occurred while fetching insights: {e}")
        return None

    except ValueError as e:
        # Handle JSON parsing errors
        print(f"An error occurred while parsing the response: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # User inputs
    chain = "ethereum"
    contract = "0x123456789abcdef123456789abcdef12345678"  # Replace with actual contract address
    start_block = 13000000  # Replace with actual start block
    end_block = 13001000    # Replace with actual end block

    # Fetch insights
    insights = get_crypto_insights(chain, contract, start_block, end_block)

    if insights:
        print("Crypto Insights:")
        print(insights)
    else:
        print("Failed to fetch insights.")
```

Make sure to replace `"your_chainbase_api_key"` and the `contract_address` values with valid ones for your use case.
