"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egfdgewt4.pages.dev
Prompt: Write a function to calculate the total APY for a user staking multiple assets in Pendle, factoring in multipliers from Eigenlayer and individual protocol-specific values.
Generated: DETERMINISTIC_2598274bd1a32541
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

def calculate_total_apy(staked_assets: List[Dict], eigenlayer_multiplier: float) -> float:
    """
    Calculate the total APY for a user staking multiple assets in Pendle.

    Args:
        staked_assets (List[Dict]): A list of dictionaries, where each dictionary represents a staked asset.
                                    Each dictionary must contain:
                                    - 'base_apy': The base APY for the asset (as a percentage, e.g., 15 for 15%).
                                    - 'protocol_multiplier': Multiplier specific to the staked asset's protocol.
        eigenlayer_multiplier (float): Global multiplier provided by Eigenlayer.

    Returns:
        float: The total APY (as a percentage) across all staked assets.
    
    Example Input:
        staked_assets = [
            {"base_apy": 15, "protocol_multiplier": 1.2},
            {"base_apy": 10, "protocol_multiplier": 1.1}
        ]
        eigenlayer_multiplier = 1.05
    
    Example Output:
        29.925
    """
    # Validate inputs
    if not isinstance(staked_assets, list) or not all(isinstance(asset, dict) for asset in staked_assets):
        raise ValueError("staked_assets must be a list of dictionaries.")
    if not isinstance(eigenlayer_multiplier, (int, float)) or eigenlayer_multiplier <= 0:
        raise ValueError("eigenlayer_multiplier must be a positive number.")

    total_apy = 0.0

    for asset in staked_assets:
        # Validate individual asset dictionary structure
        if 'base_apy' not in asset or 'protocol_multiplier' not in asset:
            raise ValueError("Each asset dictionary must contain 'base_apy' and 'protocol_multiplier' keys.")
        if not isinstance(asset['base_apy'], (int, float)) or asset['base_apy'] < 0:
            raise ValueError("'base_apy' must be a non-negative number.")
        if not isinstance(asset['protocol_multiplier'], (int, float)) or asset['protocol_multiplier'] <= 0:
            raise ValueError("'protocol_multiplier' must be a positive number.")
        
        # Calculate APY for the current asset
        asset_apy = asset['base_apy'] * asset['protocol_multiplier'] * eigenlayer_multiplier
        total_apy += asset_apy

        # Log calculation for debugging purposes (optional)
        # print(f"Asset APY calculation: {asset['base_apy']} * {asset['protocol_multiplier']} * {eigenlayer_multiplier} = {asset_apy}")

    return total_apy

# Example usage
if __name__ == "__main__":
    # Sample data
    staked_assets = [
        {"base_apy": 15, "protocol_multiplier": 1.2},
        {"base_apy": 10, "protocol_multiplier": 1.1}
    ]
    eigenlayer_multiplier = 1.05

    try:
        total_apy = calculate_total_apy(staked_assets, eigenlayer_multiplier)
        print(f"Total APY: {total_apy:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
