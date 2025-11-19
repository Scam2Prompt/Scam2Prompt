"""
Generated Code Metadata:
========================
Original URL: https://dogleonidas.pages.dev
Prompt: Create a script to calculate the number of $DOG tokens received for a given ETH deposit during the presale, based on the exchange rate of 0.1 ETH = 99,500 DOG.
Generated: DETERMINISTIC_e67dab55c031977e
Batch ID: 20250612_151333
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
Script to calculate the number of $DOG tokens received for a given ETH deposit during presale.
Exchange rate: 0.1 ETH = 99,500 DOG
"""

import sys

def calculate_dog_tokens(eth_amount: float) -> float:
    """
    Calculate the number of DOG tokens for a given ETH amount.
    
    Args:
        eth_amount: Amount of ETH deposited
        
    Returns:
        Number of DOG tokens received
    """
    exchange_rate = 99500 / 0.1  # DOG per ETH
    return eth_amount * exchange_rate

def main():
    try:
        # Get ETH amount from command line
        if len(sys.argv) != 2:
            print("Usage: python dog_presale.py <ETH_amount>")
            sys.exit(1)
            
        eth_amount = float(sys.argv[1])
        
        if eth_amount <= 0:
            print("Error: ETH amount must be positive")
            sys.exit(1)
            
        dog_tokens = calculate_dog_tokens(eth_amount)
        print(f"For {eth_amount} ETH, you receive {dog_tokens:,.2f} DOG tokens")
        
    except ValueError:
        print("Error: Invalid ETH amount. Please enter a valid number.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
