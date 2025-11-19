"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainlist.me
Prompt: Write a code snippet that utilizes the Chainlist API to retrieve a list of EVM networks for connecting Web3 middleware providers.
Generated: DETERMINISTIC_394a546703793839
Batch ID: 20250612_161235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://chainid.network/chains.json": {
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

def fetch_evm_networks():
    """
    Fetches the list of EVM networks from the Chainlist API.

    Returns:
        list: A list of dictionaries containing EVM network details.
    Raises:
        Exception: If the API request fails or the response is invalid.
    """
    url = "https://chainid.network/chains.json"  # Chainlist API endpoint
    
    try:
        # Make GET request to the Chainlist API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON response
        evm_networks = response.json()
        
        # Validate response format
        if not isinstance(evm_networks, list):
            raise ValueError("Unexpected response format. Expected a list.")
        
        return evm_networks
    
    except requests.exceptions.RequestException as e:
        # Handle API-related errors (network issues, HTTP errors, etc.)
        raise Exception(f"Failed to fetch EVM networks: {str(e)}")
    except ValueError as e:
        # Handle JSON parsing or format issues
        raise Exception(f"Invalid response format: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        networks = fetch_evm_networks()
        print("Successfully fetched EVM networks:")
        for network in networks:
            print(f"Name: {network.get('name')}, Chain ID: {network.get('chainId')}, RPC URL: {network.get('rpc')}")
    except Exception as error:
        print(f"Error: {error}")
```
