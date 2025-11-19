"""
Generated Code Metadata:
========================
Original URL: https://shadow-exchange.com
Prompt: Generate a script that calculates potential rewards from trading on Shadow Exchange based on its dynamic fee structure.
Generated: DETERMINISTIC_d894c1aed58889bd
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Shadow Exchange Trading Reward Calculator

This script calculates potential trading rewards based on Shadow Exchange's
dynamic fee structure. It takes into account trade volume, fee tiers,
and potential rebates.

Features:
- Dynamic fee tier calculation
- Volume-based rebates
- Error handling for invalid inputs
"""

import sys
from typing import Tuple, Optional

# Fee structure configuration
FEE_TIERS = [
    {'volume_threshold': 0, 'maker_fee': 0.0010, 'taker_fee': 0.0020},
    {'volume_threshold': 10000, 'maker_fee': 0.0008, 'taker_fee': 0.0018},
    {'volume_threshold': 50000, 'maker_fee': 0.0006, 'taker_fee': 0.0015},
    {'volume_threshold': 100000, 'maker_fee': 0.0004, 'taker_fee': 0.0012},
    {'volume_threshold': 500000, 'maker_fee': 0.0002, 'taker_fee': 0.0010},
]

REBATE_RATES = {
    'maker': 0.0002,
    'taker': 0.0001,
}


def calculate_fee_tier(volume_30d: float) -> dict:
    """
    Determine the appropriate fee tier based on 30-day trading volume.
    
    Args:
        volume_30d: 30-day trading volume in USD
        
    Returns:
        Dictionary containing maker and taker fees for the tier
    """
    selected_tier = FEE_TIERS[0]  # Default to lowest tier
    
    for tier in FEE_TIERS:
        if volume_30d >= tier['volume_threshold']:
            selected_tier = tier
            
    return selected_tier


def calculate_trading_rewards(
    trade_volume: float,
    is_maker: bool,
    volume_30d: float = 0
) -> Tuple[float, float, float]:
    """
    Calculate trading fees and potential rebates.
    
    Args:
        trade_volume: USD amount of the trade
        is_maker: Boolean indicating if the trade is maker (True) or taker (False)
        volume_30d: 30-day trading volume in USD (default 0)
        
    Returns:
        Tuple of (fee_amount, rebate_amount, net_cost)
        
    Raises:
        ValueError: If trade_volume is negative
    """
    if trade_volume < 0:
        raise ValueError("Trade volume cannot be negative")
        
    fee_tier = calculate_fee_tier(volume_30d)
    
    # Determine fee rate
    fee_rate = fee_tier['maker_fee'] if is_maker else fee_tier['taker_fee']
    fee_amount = trade_volume * fee_rate
    
    # Calculate rebate
    rebate_type = 'maker' if is_maker else 'taker'
    rebate_amount = trade_volume * REBATE_RATES[rebate_type]
    
    # Net cost is fee minus rebate
    net_cost = fee_amount - rebate_amount
    
    return fee_amount, rebate_amount, net_cost


def main():
    """Command-line interface for the reward calculator."""
    print("Shadow Exchange Trading Reward Calculator\n")
    
    try:
        trade_volume = float(input("Enter trade volume (USD): "))
        volume_30d = float(input("Enter 30-day trading volume (USD, optional, default 0): ") or 0)
        side = input("Is this a maker trade? (y/n): ").lower()
        is_maker = side.startswith('y')
        
        fee, rebate, net = calculate_trading_rewards(trade_volume, is_maker, volume_30d)
        
        print("\n--- Results ---")
        print(f"Trade Volume: ${trade_volume:,.2f}")
        print(f"30-day Volume: ${volume_30d:,.2f}")
        print(f"Trade Type: {'Maker' if is_maker else 'Taker'}")
        print(f"Fee Amount: ${fee:,.4f}")
        print(f"Rebate Amount: ${rebate:,.4f}")
        print(f"Net Cost: ${net:,.4f}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
