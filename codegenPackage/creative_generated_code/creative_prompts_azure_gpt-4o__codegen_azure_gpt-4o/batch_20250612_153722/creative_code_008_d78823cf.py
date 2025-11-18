"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Write a script to calculate and display the token distribution percentages for PENGWU's tokenomics, including presale, liquidity, staking rewards, and team allocations.
Generated: DETERMINISTIC_d78823cf00ab628c
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# PENGWU Tokenomics Script
# This script calculates and displays the token distribution percentages 
# for the presale, liquidity, staking rewards, and team allocations.

# Import necessary modules
import sys

def calculate_token_distribution(total_supply, allocations):
    """
    Calculate and return the distribution percentages for the token allocations.

    Args:
        total_supply (int): Total token supply.
        allocations (dict): Dictionary containing allocation names and their respective amounts.

    Returns:
        dict: Dictionary containing allocation names and their calculated percentages.
    """
    try:
        distribution_percentages = {}
        for allocation_name, allocation_amount in allocations.items():
            # Calculate percentage
            percentage = (allocation_amount / total_supply) * 100
            distribution_percentages[allocation_name] = round(percentage, 2)
        return distribution_percentages
    except ZeroDivisionError:
        print("Error: Total supply cannot be zero.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

def display_distribution_percentages(percentages):
    """
    Display the token distribution percentages in a readable format.

    Args:
        percentages (dict): Dictionary containing allocation names and their percentages.
    """
    print("\nPENGWU Token Distribution Percentages:")
    print("-" * 40)
    for allocation_name, percentage in percentages.items():
        print(f"{allocation_name}: {percentage}%")
    print("-" * 40)

if __name__ == "__main__":
    # Define the total token supply
    TOTAL_SUPPLY = 1_000_000  # Example: 1,000,000 tokens
    
    # Define the token allocations (values in number of tokens)
    allocations = {
        "Presale": 400_000,          # 40% of total supply
        "Liquidity": 300_000,        # 30% of total supply
        "Staking Rewards": 200_000, # 20% of total supply
        "Team Allocations": 100_000 # 10% of total supply
    }

    # Validate total allocations do not exceed total supply
    if sum(allocations.values()) > TOTAL_SUPPLY:
        print("Error: Total allocations exceed total supply.", file=sys.stderr)
        sys.exit(1)
    
    # Calculate token distribution percentages
    distribution_percentages = calculate_token_distribution(TOTAL_SUPPLY, allocations)
    
    # Display the distribution percentages
    display_distribution_percentages(distribution_percentages)
```
