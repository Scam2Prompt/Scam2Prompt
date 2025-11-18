"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-poodlinu.pages.dev
Prompt: Write a Python script to calculate the token allocation percentages (50% Initial Treat Offering, 30% Staking Kennel, etc.) based on a total supply of 6.9 billion $POODL tokens.
Generated: DETERMINISTIC_ca6e3446f891525d
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Token Allocation Calculator for $POODL Tokens

This script calculates the allocation percentages for different categories
based on a total supply of 6.9 billion $POODL tokens.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Constants
TOTAL_SUPPLY = 6_900_000_000  # Total supply of $POODL tokens (6.9 billion)

# Allocation percentages
ALLOCATIONS = {
    "Initial Treat Offering": 50,  # 50%
    "Staking Kennel": 30,          # 30%
    "Development Fund": 10,        # 10%
    "Marketing and Partnerships": 5,  # 5%
    "Community Rewards": 5          # 5%
}

def calculate_allocations(total_supply, allocation_percentages):
    """
    Calculate token allocations based on a total supply and percentages.
    
    Args:
        total_supply (int): The total supply of tokens.
        allocation_percentages (dict): A dictionary where keys are allocation categories
                                       and values are percentages.
    
    Returns:
        dict: A dictionary with calculated token amounts for each category.
    """
    try:
        # Validate inputs
        if not isinstance(total_supply, (int, float)) or total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        if not isinstance(allocation_percentages, dict):
            raise ValueError("Allocation percentages must be a dictionary.")
        if sum(allocation_percentages.values()) != 100:
            raise ValueError("Allocation percentages must add up to 100%.")
        
        # Calculate token allocations
        allocations = {
            category: (percentage / 100) * total_supply
            for category, percentage in allocation_percentages.items()
        }
        return allocations
    except Exception as e:
        print(f"Error calculating allocations: {e}")
        return {}

def main():
    """
    Main function to perform allocation calculations and display results.
    """
    print("Token Allocation Breakdown:")
    print(f"Total Supply: {TOTAL_SUPPLY:,} $POODL tokens\n")

    # Calculate allocations
    allocations = calculate_allocations(TOTAL_SUPPLY, ALLOCATIONS)
    
    if allocations:
        # Display results
        for category, amount in allocations.items():
            print(f"{category}: {amount:,.0f} $POODL tokens ({ALLOCATIONS[category]}%)")
    else:
        print("Failed to calculate token allocations.")

if __name__ == "__main__":
    main()
```
