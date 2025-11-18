"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Write a Python script that calculates the allocation of funds raised during the Bulldogito Coin presale into categories like marketing, liquidity, dev team, and B2B Booster, based on the percentages provided.
Generated: DETERMINISTIC_65a4dbeccd70c989
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate fund allocation for Bulldogito Coin presale.
Allocates percentages of the total funds raised into specified categories: 
marketing, liquidity, dev team, and B2B Booster.
"""

# Import necessary libraries
from typing import Dict


def allocate_funds(total_funds: float, allocation_percentages: Dict[str, float]) -> Dict[str, float]:
    """
    Function to calculate the allocation of funds into various categories.

    Args:
        total_funds (float): Total funds raised during the presale.
        allocation_percentages (Dict[str, float]): A dictionary where keys are category names 
                                                   and values are percentages allocated to the category.

    Returns:
        Dict[str, float]: A dictionary containing the allocated amount for each category.
    """
    if total_funds <= 0:
        raise ValueError("Total funds must be greater than zero.")
    
    if not allocation_percentages:
        raise ValueError("Allocation percentages dictionary cannot be empty.")
    
    # Validate percentages sum to 100
    total_percentage = sum(allocation_percentages.values())
    if total_percentage != 100:
        raise ValueError("Allocation percentages must sum to 100.")

    # Calculate allocated funds for each category
    allocation_result = {}
    for category, percentage in allocation_percentages.items():
        allocation_result[category] = round((total_funds * (percentage / 100)), 2)

    return allocation_result


def main():
    """
    Main function to demonstrate fund allocation.
    """
    try:
        # Example input: total funds raised and allocation percentages
        total_funds_raised = 1000000  # Total funds raised in USD
        allocation_percentages = {
            "Marketing": 40,  # 40% for marketing
            "Liquidity": 30,  # 30% for liquidity
            "Dev Team": 20,   # 20% for development team
            "B2B Booster": 10 # 10% for B2B Booster
        }

        # Calculate allocation
        allocations = allocate_funds(total_funds_raised, allocation_percentages)

        # Print results
        print("Fund Allocation:")
        for category, amount in allocations.items():
            print(f"{category}: ${amount:,.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
