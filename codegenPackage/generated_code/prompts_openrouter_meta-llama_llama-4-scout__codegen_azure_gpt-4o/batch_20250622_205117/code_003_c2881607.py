"""
Generated Code Metadata:
========================
Original URL: https://cowswap.cc
Prompt: Compare the features of CoW Swap with other decentralized exchanges (DEXs) like Uniswap and SushiSwap, focusing on gas prices and supported tokens.
Generated: DETERMINISTIC_c2881607c83a37c4
Batch ID: 20250622_205117
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cow.fi/mainnet/api/v1/markets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.thegraph.com/subgraphs/name/sushiswap/exchange": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

def fetch_dex_data(dex_name):
    """
    Fetches data from the specified DEX API.
    
    Args:
        dex_name (str): The name of the DEX (e.g., 'CoW Swap', 'Uniswap', 'SushiSwap').
    
    Returns:
        dict: A dictionary containing DEX data such as gas prices and supported tokens.
    """
    dex_apis = {
        "CoW Swap": "https://api.cow.fi/mainnet/api/v1/markets",
        "Uniswap": "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2",
        "SushiSwap": "https://api.thegraph.com/subgraphs/name/sushiswap/exchange"
    }
    
    if dex_name not in dex_apis:
        raise ValueError(f"Unsupported DEX: {dex_name}")
    
    try:
        response = requests.get(dex_apis[dex_name]) if dex_name == "CoW Swap" else requests.post(
            dex_apis[dex_name],
            json={"query": "{ tokens { id symbol name } }"}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch data from {dex_name}: {e}")

def compare_dex_features():
    """
    Compares features of CoW Swap, Uniswap, and SushiSwap focusing on gas prices and supported tokens.
    
    Returns:
        dict: A dictionary containing the comparison results.
    """
    comparison = {}
    
    # Fetch data for each DEX
    for dex in ["CoW Swap", "Uniswap", "SushiSwap"]:
        try:
            data = fetch_dex_data(dex)
            if dex == "CoW Swap":
                # Extract supported tokens and gas price information for CoW Swap
                tokens = [market['baseToken']['symbol'] for market in data.get('markets', [])]
                gas_price = "Gasless (uses meta-transactions)"
            else:
                # Extract supported tokens for Uniswap and SushiSwap
                tokens = [token['symbol'] for token in data['data']['tokens']]
                gas_price = "User pays gas fees directly"
            
            comparison[dex] = {
                "Supported Tokens": tokens,
                "Gas Price": gas_price
            }
        except RuntimeError as e:
            comparison[dex] = {"Error": str(e)}
    
    return comparison

def main():
    """
    Main function to execute the DEX comparison and display the results.
    """
    try:
        comparison_results = compare_dex_features()
        for dex, features in comparison_results.items():
            print(f"DEX: {dex}")
            for key, value in features.items():
                if isinstance(value, list):
                    print(f"  {key}: {', '.join(value[:5])}... ({len(value)} total)")  # Show first 5 tokens for brevity
                else:
                    print(f"  {key}: {value}")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
