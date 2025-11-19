"""
Generated Code Metadata:
========================
Original URL: https://vfatio.com
Prompt: Write a Python script to calculate the total value locked (TVL) in a liquidity pool, given the TVL of two assets, such as WETH and superOETHb, with their respective prices.
Generated: DETERMINISTIC_00d1a0c69a3ba179
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional

def calculate_tvl(
    asset1_tvl: float, 
    asset1_price: float, 
    asset2_tvl: float, 
    asset2_price: float
) -> float:
    """
    Calculate the Total Value Locked (TVL) in a liquidity pool.
    
    Args:
        asset1_tvl: TVL of the first asset in its native units
        asset1_price: Price of the first asset in USD
        asset2_tvl: TVL of the second asset in its native units
        asset2_price: Price of the second asset in USD
    
    Returns:
        Total value locked in USD
    
    Raises:
        ValueError: If any of the input values are negative
    """
    # Validate input values
    if any(val < 0 for val in [asset1_tvl, asset1_price, asset2_tvl, asset2_price]):
        raise ValueError("All values must be non-negative")
    
    # Calculate TVL for each asset and sum them
    asset1_value = asset1_tvl * asset1_price
    asset2_value = asset2_tvl * asset2_price
    total_tvl = asset1_value + asset2_value
    
    return total_tvl

def main():
    """
    Main function to demonstrate TVL calculation with example values.
    """
    try:
        # Example values (replace with actual values in production)
        weth_tvl = 1000.0  # TVL in WETH
        weth_price = 3000.0  # Price of WETH in USD
        super_oethb_tvl = 5000.0  # TVL in superOETHb
        super_oethb_price = 1.5  # Price of superOETHb in USD
        
        # Calculate and print TVL
        tvl = calculate_tvl(weth_tvl, weth_price, super_oethb_tvl, super_oethb_price)
        print(f"Total Value Locked (TVL): ${tvl:,.2f}")
        
    except ValueError as e:
        print(f"Error calculating TVL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
