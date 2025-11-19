"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a script to calculate the total number of ALIEN tokens available for a given ETH investment, considering the presale rates and total supply of 100,000,000 ALIEN.
Generated: DETERMINISTIC_826bc8af0cc43c4c
Batch ID: 20250622_205836
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
ALIEN Token Calculator

Calculates the number of ALIEN tokens available for a given ETH investment
considering presale rates and total supply constraints.

Usage:
    python alien_token_calculator.py <eth_amount> [--presale-stage <stage>]

Arguments:
    eth_amount       Amount of ETH to invest
    --presale-stage  Presale stage (1-3). Defaults to 1 if not specified.
"""

import argparse
from decimal import Decimal, getcontext

# Configure decimal precision
getcontext().prec = 8

# Presale token rates (ALIEN per ETH) for each stage
PRESALE_RATES = {
    1: Decimal('5000'),  # Stage 1: 5000 ALIEN per ETH
    2: Decimal('4000'),  # Stage 2: 4000 ALIEN per ETH
    3: Decimal('3000'),  # Stage 3: 3000 ALIEN per ETH
}

TOTAL_SUPPLY = Decimal('100000000')  # Total ALIEN token supply

def calculate_tokens(eth_amount: Decimal, presale_stage: int) -> Decimal:
    """
    Calculate ALIEN tokens for given ETH amount at specified presale stage.
    
    Args:
        eth_amount: ETH investment amount
        presale_stage: Presale stage (1-3)
    
    Returns:
        Number of ALIEN tokens
    
    Raises:
        ValueError: If presale stage is invalid or ETH amount is negative
    """
    if presale_stage not in PRESALE_RATES:
        raise ValueError(f"Invalid presale stage. Must be 1-3, got {presale_stage}")
    
    if eth_amount < Decimal('0'):
        raise ValueError("ETH amount cannot be negative")
    
    rate = PRESALE_RATES[presale_stage]
    tokens = eth_amount * rate
    
    # Ensure we don't exceed total supply (though unlikely in presale)
    if tokens > TOTAL_SUPPLY:
        tokens = TOTAL_SUPPLY
    
    return tokens.quantize(Decimal('0.00000001'))

def main():
    parser = argparse.ArgumentParser(description="Calculate ALIEN tokens for ETH investment")
    parser.add_argument('eth_amount', type=Decimal, help='Amount of ETH to invest')
    parser.add_argument('--presale-stage', type=int, choices=[1, 2, 3], default=1,
                       help='Presale stage (1-3). Defaults to 1.')
    
    args = parser.parse_args()
    
    try:
        tokens = calculate_tokens(args.eth_amount, args.presale_stage)
        print(f"{args.eth_amount} ETH at stage {args.presale_stage} = {tokens} ALIEN tokens")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
