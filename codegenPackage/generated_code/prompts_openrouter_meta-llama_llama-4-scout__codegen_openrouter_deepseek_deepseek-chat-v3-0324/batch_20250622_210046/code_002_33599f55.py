"""
Generated Code Metadata:
========================
Original URL: https://compound.morpho.dev
Prompt: Write a Python code snippet to calculate the APY for wstETH liquidity on Morpho's CompoundV2 market.
Generated: DETERMINISTIC_33599f5589b636a3
Batch ID: 20250622_210046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional

def calculate_apy(
    supply_rate_per_block: float,
    blocks_per_year: int = 2_102_400,  # ~15s per block, 2102400 blocks/year
    compounding_frequency: int = 365,    # Daily compounding
) -> float:
    """
    Calculate APY from supply rate per block with compounding.

    Args:
        supply_rate_per_block: The supply rate per block (as a decimal, e.g. 0.01 for 1%)
        blocks_per_year: Number of blocks per year (default for Ethereum)
        compounding_frequency: Number of compounding periods per year

    Returns:
        The APY as a decimal (e.g. 0.05 for 5%)
    """
    periods_per_block = compounding_frequency / blocks_per_year
    rate_per_period = supply_rate_per_block / periods_per_block
    apy = (1 + rate_per_period) ** compounding_frequency - 1
    return apy

def get_wsteth_apy_on_morpho_compoundv2(
    morpho_supply_rate_per_block: float,
    wsteth_underlying_apy: float,
    blocks_per_year: int = 2_102_400,
    compounding_frequency: int = 365,
) -> float:
    """
    Calculate the effective APY for wstETH liquidity on Morpho's CompoundV2 market.

    Args:
        morpho_supply_rate_per_block: The Morpho supply rate per block (as decimal)
        wsteth_underlying_apy: The APY of wstETH's underlying staking rewards (as decimal)
        blocks_per_year: Number of blocks per year (default for Ethereum)
        compounding_frequency: Number of compounding periods per year

    Returns:
        The total effective APY as a decimal (e.g. 0.08 for 8%)
    """
    morpho_apy = calculate_apy(
        morpho_supply_rate_per_block,
        blocks_per_year,
        compounding_frequency
    )
    total_apy = (1 + morpho_apy) * (1 + wsteth_underlying_apy) - 1
    return total_apy

# Example usage:
if __name__ == "__main__":
    # Example values (replace with actual values from contracts)
    morpho_supply_rate = 0.000001  # 0.0001% per block
    wsteth_apy = 0.04  # 4% APY from staking rewards
    
    total_apy = get_wsteth_apy_on_morpho_compoundv2(morpho_supply_rate, wsteth_apy)
    print(f"Total APY: {total_apy:.2%}")
```
