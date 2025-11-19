"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Generate a Python script to calculate the number of SHROOM tokens a user can buy based on the amount of ETH they spend, given the presale rates (e.g., 0.1 ETH ~ 99,500 SHROOM).
Generated: DETERMINISTIC_243dafa5faf8fef7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from decimal import Decimal, getcontext

# Constants for SHROOM token presale rates
PRESALE_RATE = Decimal('99500')  # SHROOM per 0.1 ETH
ETH_RATE_BASE = Decimal('0.1')   # ETH amount for the base rate

def calculate_shroom_tokens(eth_amount: Decimal) -> Decimal:
    """
    Calculate the number of SHROOM tokens a user can buy based on ETH spent.
    
    Args:
        eth_amount: Amount of ETH spent (as Decimal for precision)
    
    Returns:
        Decimal: Amount of SHROOM tokens receivable
    
    Raises:
        ValueError: If eth_amount is negative
    """
    if eth_amount < Decimal('0'):
        raise ValueError("ETH amount cannot be negative")
    
    return (eth_amount / ETH_RATE_BASE) * PRESALE_RATE

def main():
    # Set precision for Decimal calculations
    getcontext().prec = 18
    
    try:
        # Get user input
        eth_input = input("Enter the amount of ETH you want to spend: ")
        eth_amount = Decimal(eth_input)
        
        # Calculate SHROOM tokens
        shroom_tokens = calculate_shroom_tokens(eth_amount)
        
        # Display results
        print(f"\nFor {eth_amount} ETH, you will receive:")
        print(f"{shroom_tokens:.0f} SHROOM tokens")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
