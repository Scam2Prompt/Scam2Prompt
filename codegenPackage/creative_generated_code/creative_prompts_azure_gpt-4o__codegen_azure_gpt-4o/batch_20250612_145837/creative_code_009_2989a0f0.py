"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidu6kbqouz735lxf6vunpgmtdvgzngf7qxfqbfzvpxqisqb3er7we.ipfs.dweb.link
Prompt: Write a script to automate token deployment across multiple chains like Avalanche, Base, BSC, Ethereum, and SOL, as supported by Chef.fun.
Generated: DETERMINISTIC_2989a0f0d52d13d2
Batch ID: 20250612_145837
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chef.fun/deploy": {
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
import json

# Constants for supported chains
SUPPORTED_CHAINS = ["Avalanche", "Base", "BSC", "Ethereum", "SOL"]

# Chef.fun API configuration
CHEF_FUN_API_URL = "https://api.chef.fun/deploy"
API_KEY = "your_api_key_here"  # Replace with your API key

def deploy_token(chain, token_details):
    """
    Deploy a token on a specified blockchain using the Chef.fun API.

    Parameters:
        chain (str): The blockchain to deploy the token on. Must be one of SUPPORTED_CHAINS.
        token_details (dict): A dictionary containing details about the token (e.g., name, symbol, etc.).

    Returns:
        dict: The response from the API.
    """
    # Validate the chain input
    if chain not in SUPPORTED_CHAINS:
        raise ValueError(f"Unsupported chain '{chain}'. Supported chains are: {', '.join(SUPPORTED_CHAINS)}")
    
    # Prepare the request payload
    payload = {
        "chain": chain,
        "token_details": token_details
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make the API request to deploy the token
        response = requests.post(CHEF_FUN_API_URL, headers=headers, data=json.dumps(payload))
        
        # Raise an HTTPError if the response contains a failed status code
        response.raise_for_status()
        
        # Return the API response as a Python dictionary
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle HTTP and connection errors
        print(f"Error deploying token on {chain}: {str(e)}")
        return {"success": False, "error": str(e)}

def batch_deploy_tokens(token_details, chains=SUPPORTED_CHAINS):
    """
    Deploy a token across multiple chains.

    Parameters:
        token_details (dict): A dictionary containing details about the token (e.g., name, symbol, etc.).
        chains (list): A list of chains to deploy the token on. Defaults to all supported chains.

    Returns:
        dict: A dictionary containing deployment results for each chain.
    """
    results = {}
    
    for chain in chains:
        print(f"Deploying token on {chain}...")
        results[chain] = deploy_token(chain, token_details)
    
    return results

if __name__ == "__main__":
    # Example token details
    token_details = {
        "name": "MyToken",
        "symbol": "MTK",
        "decimals": 18,
        "initial_supply": 1000000000
    }
    
    print("Starting batch token deployment...")
    deploy_results = batch_deploy_tokens(token_details)
    
    print("\nDeployment Results:")
    for chain, result in deploy_results.items():
        print(f"{chain}: {'Success' if result.get('success') else 'Failed'}")
        if not result.get('success'):
            print(f"Error: {result.get('error')}")
```
