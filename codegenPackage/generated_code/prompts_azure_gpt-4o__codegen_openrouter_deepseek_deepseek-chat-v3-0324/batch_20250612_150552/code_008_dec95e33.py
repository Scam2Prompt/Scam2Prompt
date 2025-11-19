"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Python script to calculate the allocation percentages of OMEME tokens for presale, staking rewards, liquidity, marketing, development, and community funds based on the tokenomics provided.
Generated: DETERMINISTIC_dec95e33f5a3590f
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OMEME Token Allocation Calculator

This script calculates the allocation percentages of OMEME tokens for various purposes
including presale, staking rewards, liquidity, marketing, development, and community funds.
"""

def calculate_token_allocation(total_supply):
    """
    Calculate token allocation percentages based on the given total supply.
    
    Args:
        total_supply (int): The total supply of OMEME tokens.
        
    Returns:
        dict: A dictionary containing allocation names and their respective amounts and percentages.
    """
    allocations = {
        'Presale': {
            'percentage': 30,
            'description': 'Tokens allocated for presale investors'
        },
        'Staking Rewards': {
            'percentage': 25,
            'description': 'Tokens allocated for staking rewards'
        },
        'Liquidity': {
            'percentage': 20,
            'description': 'Tokens allocated for exchange liquidity'
        },
        'Marketing': {
            'percentage': 10,
            'description': 'Tokens allocated for marketing efforts'
        },
        'Development': {
            'percentage': 10,
            'description': 'Tokens allocated for development team'
        },
        'Community Fund': {
            'percentage': 5,
            'description': 'Tokens allocated for community initiatives'
        }
    }
    
    # Validate total supply
    if not isinstance(total_supply, (int, float)) or total_supply <= 0:
        raise ValueError("Total supply must be a positive number")
    
    # Calculate token amounts for each allocation
    for allocation in allocations.values():
        allocation['amount'] = total_supply * allocation['percentage'] / 100
    
    return allocations

def print_allocation_report(allocations, total_supply):
    """
    Print a formatted report of token allocations.
    
    Args:
        allocations (dict): The allocations dictionary from calculate_token_allocation
        total_supply (int): The total supply of tokens
    """
    print("\nOMEME Token Allocation Report")
    print("=" * 40)
    print(f"Total Supply: {total_supply:,} OMEME\n")
    
    print("{:<20} {:<15} {:<10} {:<30}".format(
        "Allocation", "Percentage", "Amount", "Description"))
    print("-" * 75)
    
    for name, data in allocations.items():
        print("{:<20} {:<15} {:<10,.0f} {:<30}".format(
            name,
            f"{data['percentage']}%",
            data['amount'],
            data['description']
        ))

def main():
    """Main function to execute the token allocation calculation."""
    try:
        # Get total supply from user
        total_supply = float(input("Enter the total supply of OMEME tokens: "))
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0")
        
        # Calculate allocations
        allocations = calculate_token_allocation(total_supply)
        
        # Print report
        print_allocation_report(allocations, total_supply)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
