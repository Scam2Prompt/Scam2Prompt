"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-nfts.pages.dev
Prompt: Write a function to calculate shared yields for lending assets like USDC.e, ETH, XAI, and PENDLE based on Stella's APY percentages and total supply data.
Generated: DETERMINISTIC_7784005dbb4f1a0f
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, List

def calculate_shared_yields(asset_data: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate shared yields for lending assets based on APY percentages and total supply data.

    Parameters:
        asset_data (Dict[str, Dict[str, float]]): A dictionary containing asset information.
            Each asset should have an APY percentage ('apy') and total supply ('total_supply').

            Example:
            {
                "USDC.e": {"apy": 0.05, "total_supply": 100_000},
                "ETH": {"apy": 0.07, "total_supply": 50_000},
                "XAI": {"apy": 0.02, "total_supply": 200_000},
                "PENDLE": {"apy": 0.12, "total_supply": 10_000}
            }

    Returns:
        Dict[str, float]: A dictionary containing the calculated shared yield for each asset.
            Shared yield is calculated as (APY * Total Supply).
    """
    
    # Initialize result dictionary
    shared_yields = {}

    try:
        # Iterate through each asset and calculate its shared yield
        for asset, data in asset_data.items():
            # Validate keys and values
            if 'apy' not in data or 'total_supply' not in data:
                raise KeyError(f"Missing 'apy' or 'total_supply' data for asset '{asset}'")
            if not isinstance(data['apy'], (int, float)) or not isinstance(data['total_supply'], (int, float)):
                raise ValueError(f"'apy' and 'total_supply' must be numeric for asset '{asset}'")
            if data['apy'] < 0 or data['total_supply'] < 0:
                raise ValueError(f"'apy' and 'total_supply' must be non-negative for asset '{asset}'")
            
            # Compute shared yield: APY * Total Supply
            shared_yields[asset] = data['apy'] * data['total_supply']
    
    except Exception as e:
        # Log or handle errors appropriately (depending on production requirements)
        print(f"An error occurred while calculating shared yields: {e}")
        raise  # Rethrow the exception for further handling if needed
    
    return shared_yields


# Example usage:
if __name__ == "__main__":
    # Example asset data
    assets = {
        "USDC.e": {"apy": 0.05, "total_supply": 100_000},
        "ETH": {"apy": 0.07, "total_supply": 50_000},
        "XAI": {"apy": 0.02, "total_supply": 200_000},
        "PENDLE": {"apy": 0.12, "total_supply": 10_000}
    }

    # Calculate shared yields
    result = calculate_shared_yields(assets)

    # Print results
    print("Shared Yields:")
    for asset, yield_value in result.items():
        print(f"{asset}: {yield_value:.2f}")
```
