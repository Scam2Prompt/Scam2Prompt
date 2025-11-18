"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Write a function using the deBridge API to fetch real-time analytics of cross-chain flows between Ethereum and Solana.
Generated: DETERMINISTIC_097b025550356e23
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.debridge.finance/v1/": {
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

# Define constants for the deBridge API
DEBRIDGE_API_BASE_URL = "https://api.debridge.finance/v1/"
CROSS_CHAIN_ANALYTICS_ENDPOINT = "analytics/cross-chain-flows"
ETHEREUM_CHAIN_ID = 1  # Ethereum chain ID
SOLANA_CHAIN_ID = 101  # Solana chain ID

# Function to fetch real-time cross-chain analytics between Ethereum and Solana
def fetch_cross_chain_analytics(api_key):
    """
    Fetches real-time analytics of cross-chain flows between Ethereum and Solana using the deBridge API.

    Args:
        api_key (str): API key for authenticating with the deBridge API.

    Returns:
        dict: JSON response containing cross-chain analytics data.

    Raises:
        ValueError: If the API response contains an error.
        Exception: For other unexpected errors.
    """
    # Construct the request URL
    url = f"{DEBRIDGE_API_BASE_URL}{CROSS_CHAIN_ANALYTICS_ENDPOINT}"
    
    # Define query parameters
    params = {
        "fromChainId": ETHEREUM_CHAIN_ID,  # Source chain ID (Ethereum)
        "toChainId": SOLANA_CHAIN_ID      # Destination chain ID (Solana)
    }
    
    # Define request headers
    headers = {
        "Authorization": f"Bearer {api_key}",  # Include the API key for authentication
        "Accept": "application/json"          # Expect JSON response
    }
    
    try:
        # Make the GET request to the deBridge API
        response = requests.get(url, headers=headers, params=params)

        # Check if the response status code is OK (200)
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            # Raise a ValueError for API-specific errors
            raise ValueError(f"Failed to fetch data: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        # Handle any unexpected errors during the HTTP request
        raise Exception(f"An error occurred while fetching cross-chain analytics: {str(e)}")


# Example usage:
if __name__ == "__main__":
    try:
        # Replace 'your_api_key_here' with your actual deBridge API key
        api_key = "your_api_key_here"
        analytics_data = fetch_cross_chain_analytics(api_key)
        print("Cross-chain analytics data:", analytics_data)
    except Exception as e:
        print("Error:", str(e))
```
