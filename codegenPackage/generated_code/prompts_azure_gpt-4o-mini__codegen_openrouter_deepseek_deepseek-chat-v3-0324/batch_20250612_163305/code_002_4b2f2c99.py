"""
Generated Code Metadata:
========================
Original URL: https://award-topg.pages.dev
Prompt: Write a script to calculate the amount of TOPG tokens received for different ETH contributions in a presale, based on the rates provided for $TOPG.
Generated: DETERMINISTIC_4b2f2c990368b30f
Batch ID: 20250612_163305
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
TOPG Token Presale Calculator

This script calculates the amount of TOPG tokens received for different ETH contributions
in a presale, based on the provided exchange rates.

Usage:
    python3 topg_presale_calculator.py <ETH_amount> [--rate <rate>]

Arguments:
    ETH_amount    Amount of ETH contributed (in ETH)
    --rate        Optional: Custom exchange rate (TOPG per ETH). Defaults to presale rate.

Example:
    python3 topg_presale_calculator.py 1.5
    python3 topg_presale_calculator.py 2 --rate 50000
"""

import argparse
from decimal import Decimal, getcontext

# Presale configuration
DEFAULT_RATE = 75000  # TOPG per 1 ETH

def calculate_topg(eth_amount: Decimal, rate: int) -> Decimal:
    """
    Calculate TOPG tokens received for a given ETH amount and exchange rate.
    
    Args:
        eth_amount: Amount of ETH contributed (in ETH)
        rate: Exchange rate (TOPG per 1 ETH)
    
    Returns:
        Amount of TOPG tokens received
    """
    return eth_amount * Decimal(rate)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Calculate TOPG tokens for ETH contribution")
    parser.add_argument("eth_amount", type=Decimal, help="Amount of ETH contributed")
    parser.add_argument("--rate", type=int, default=DEFAULT_RATE,
                       help=f"Exchange rate (TOPG per ETH). Default: {DEFAULT_RATE}")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate input
    if args.eth_amount <= 0:
        raise ValueError("ETH amount must be positive")
    if args.rate <= 0:
        raise ValueError("Exchange rate must be positive")
    
    # Set decimal precision
    getcontext().prec = 18
    
    # Calculate and display results
    topg_amount = calculate_topg(args.eth_amount, args.rate)
    print(f"\nPresale Calculation Results:")
    print(f"ETH Contributed: {args.eth_amount:.8f} ETH")
    print(f"Exchange Rate: 1 ETH = {args.rate:,} TOPG")
    print(f"TOPG Received: {topg_amount:,.2f} TOPG")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)
```
