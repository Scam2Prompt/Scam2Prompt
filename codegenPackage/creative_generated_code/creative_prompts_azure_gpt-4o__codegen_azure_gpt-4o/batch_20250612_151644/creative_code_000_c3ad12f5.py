"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-mh2dokjx4-zapper-fi.vercel.app
Prompt: Write code using Zapper's Beta API to track wallet activity, including NFTs, DAOs, and DeFi transactions, for a specific Ethereum address.
Generated: DETERMINISTIC_c3ad12f51810b448
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.xyz/v2": {
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
from requests.exceptions import HTTPError

# Zapper Beta API base URL
BASE_URL = "https://api.zapper.xyz/v2"

# Replace with your Zapper API key
API_KEY = "your_api_key_here"

# Ethereum wallet address to track
ETHEREUM_ADDRESS = "your_ethereum_address_here"

def fetch_wallet_activity(wallet_address, api_key):
    """
    Fetch wallet activity including NFTs, DAOs, and DeFi transactions from Zapper's Beta API.
    
    Parameters:
        wallet_address (str): Ethereum wallet address to track.
        api_key (str): Zapper API key.
    
    Returns:
        dict: Wallet activity data if successful.
    
    Raises:
        Exception: If there is an error fetching the data from the API.
    """
    url = f"{BASE_URL}/activity"
    params = {
        "addresses[]": wallet_address,  # Wallet address to track
        "api_key": api_key              # API key for authentication
    }

    try:
        # Make GET request to Zapper API
        response = requests.get(url, params=params)

        # Raise HTTPError for non-200 status codes
        response.raise_for_status()

        # Parse and return JSON response
        return response.json()

    except HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
        raise Exception("Failed to fetch wallet activity from Zapper API.") from http_err

    except Exception as err:
        # Handle other exceptions
        print(f"An error occurred: {err}")
        raise Exception("An unexpected error occurred.") from err

def main():
    """
    Main function to track wallet activity using Zapper's Beta API.
    """
    try:
        print(f"Fetching activity for Ethereum address: {ETHEREUM_ADDRESS}")
        wallet_activity = fetch_wallet_activity(ETHEREUM_ADDRESS, API_KEY)

        # Display wallet activity
        print("Wallet Activity:")
        print(wallet_activity)

    except Exception as ex:
        print(f"Error: {ex}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note**:  
- Replace `your_api_key_here` with your actual Zapper API key.  
- Replace `your_ethereum_address_here` with the Ethereum wallet address you want to track.  
- Ensure you adhere to Zapper's API usage limits and authentication requirements.
