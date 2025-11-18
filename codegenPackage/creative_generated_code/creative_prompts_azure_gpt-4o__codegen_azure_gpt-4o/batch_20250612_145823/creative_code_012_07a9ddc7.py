"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Write a Python script to query MDEX's API for the TVL (Total Value Locked) of liquidity mining pools on HECO and BSC.
Generated: DETERMINISTIC_07a9ddc7d6c4a5bb
Batch ID: 20250612_145823
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com/{chain}/api/v1/tvl": {
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

def fetch_tvl(chain: str) -> dict:
    """
    Fetch the Total Value Locked (TVL) for liquidity mining pools in MDEX on a specified chain.

    Args:
        chain (str): The blockchain network to query ('heco' or 'bsc').

    Returns:
        dict: A dictionary containing TVL data.

    Raises:
        ValueError: If the provided chain is not supported.
        requests.RequestException: If the API call fails.
    """
    # Supported chains
    supported_chains = {'heco', 'bsc'}
    
    # Validate the provided chain
    if chain.lower() not in supported_chains:
        raise ValueError(f"Unsupported chain '{chain}'. Supported chains are: {supported_chains}")
    
    # API endpoint for querying TVL
    api_url = f"https://api.mdex.com/{chain}/api/v1/tvl"
    
    try:
        # Making the GET request to MDEX API
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        
        # Parse JSON data
        tvl_data = response.json()
        
        # Validate the API response structure
        if "total" not in tvl_data:
            raise ValueError("Unexpected API response structure. 'total' key not found.")
        
        return tvl_data
    
    except requests.RequestException as e:
        # Handle network-related errors
        raise RuntimeError(f"Failed to fetch TVL data from {api_url}: {str(e)}") from e


if __name__ == "__main__":
    # Example usage of the script
    try:
        # Chain options: 'heco' or 'bsc'
        chain = "heco"
        
        # Fetch TVL data
        tvl_info = fetch_tvl(chain)
        
        # Display the TVL data
        print(f"TVL for MDEX on {chain.upper()} Chain:")
        print(f"Total Value Locked: {tvl_info['total']}")
    
    except ValueError as ve:
        # Handle validation errors
        print(f"Error: {ve}")
    except RuntimeError as re:
        # Handle runtime errors during API call
        print(f"Error: {re}")
    except Exception as ex:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {ex}")
```
