"""
Generated Code Metadata:
========================
Original URL: https://dequodss.web.app
Prompt: Write a Python script to calculate the daily earnings of $DUST tokens by staking DeGods and DeadGods, considering the 1.25 $DUST per day and 3.75 $DUST per day staking rates.
Generated: DETERMINISTIC_6ef6ccb9f1ba3297
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
from typing import Union

def calculate_daily_dust(
    degods_count: Union[int, float],
    deadgods_count: Union[int, float]
) -> float:
    """
    Calculate daily $DUST earnings from staking DeGods and DeadGods NFTs.
    
    Args:
        degods_count: Number of DeGods NFTs staked (1.25 $DUST/day each)
        deadgods_count: Number of DeadGods NFTs staked (3.75 $DUST/day each)
    
    Returns:
        Total daily $DUST earnings
    """
    DUST_PER_DEGOD = 1.25
    DUST_PER_DEADGOD = 3.75
    
    if degods_count < 0 or deadgods_count < 0:
        raise ValueError("NFT counts cannot be negative")
    
    total_dust = (degods_count * DUST_PER_DEGOD) + (deadgods_count * DUST_PER_DEADGOD)
    return total_dust

def main():
    parser = argparse.ArgumentParser(
        description="Calculate daily $DUST earnings from staking DeGods and DeadGods NFTs"
    )
    parser.add_argument(
        "--degods",
        type=float,
        required=True,
        help="Number of DeGods NFTs staked (1.25 $DUST/day each)"
    )
    parser.add_argument(
        "--deadgods",
        type=float,
        required=True,
        help="Number of DeadGods NFTs staked (3.75 $DUST/day each)"
    )
    
    args = parser.parse_args()
    
    try:
        daily_dust = calculate_daily_dust(args.degods, args.deadgods)
        print(f"Daily $DUST earnings: {daily_dust}")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
