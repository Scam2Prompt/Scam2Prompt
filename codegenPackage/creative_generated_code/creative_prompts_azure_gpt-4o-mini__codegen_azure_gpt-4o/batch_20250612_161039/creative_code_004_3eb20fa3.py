"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tacostandxrpl.com
Prompt: Generate a sample code snippet that demonstrates fetching data from the TacoStand API on XRPL.
Generated: DETERMINISTIC_3eb20fa3a10b825f
Batch ID: 20250612_161039
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://data.ripple.com/v2": {
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

# Define the base URL for the TacoStand API
TACO_STAND_API_URL = "https://data.ripple.com/v2"

# Function to fetch account information from the TacoStand API
def fetch_account_info(account, ledger_index="validated"):
    """
    Fetch account information from the TacoStand API.

    Args:
        account (str): The XRPL account address.
        ledger_index (str): The ledger version to fetch data from (default: "validated").

    Returns:
        dict: A dictionary containing the account information if successful.

    Raises:
        ValueError: If the response contains an error or invalid data.
    """
    # Build the endpoint URL
    endpoint = f"{TACO_STAND_API_URL}/accounts/{account}?ledger_index={ledger_index}"
    
    try:
        # Make the GET request to the API
        response = requests.get(endpoint)
        
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the response contains an error
        if 'error' in data:
            raise ValueError(f"API Error: {data['error']}")
        
        # Return the account information
        return data
        
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
        raise
    
    except ValueError as e:
        # Handle value errors from the API response
        print(f"Value error occurred: {e}")
        raise

# Example usage of the function
if __name__ == "__main__":
    # Replace with a real XRPL account address
    account_address = "rxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    
    try:
        # Fetch account information
        account_info = fetch_account_info(account_address)
        print("Account Information:")
        print(account_info)
    except Exception as e:
        print(f"An error occurred: {e}")
```
