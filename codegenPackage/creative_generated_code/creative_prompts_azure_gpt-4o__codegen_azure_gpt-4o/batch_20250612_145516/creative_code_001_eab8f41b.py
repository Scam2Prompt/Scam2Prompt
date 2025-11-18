"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Create a function in Python that calculates portfolio allocation based on the quarterly percentages provided by SUI Strategies, and outputs the total value of each asset given an initial investment amount.
Generated: DETERMINISTIC_eab8f41b051dbc4f
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_portfolio_allocation(initial_investment, allocation_percentages):
    """
    Calculate portfolio allocation based on quarterly percentages.
    
    Parameters:
    initial_investment (float): The total initial investment amount.
    allocation_percentages (dict): A dictionary where keys are asset names and values are their allocation percentages (0-100).
    
    Returns:
    dict: A dictionary where keys are asset names and values are the total value allocated to each asset.
    """
    try:
        # Validate inputs
        if not isinstance(initial_investment, (int, float)) or initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")
        
        if not isinstance(allocation_percentages, dict) or not allocation_percentages:
            raise ValueError("Allocation percentages must be a non-empty dictionary.")

        if sum(allocation_percentages.values()) != 100:
            raise ValueError("The total allocation percentages must sum up to 100.")

        # Calculate allocation for each asset
        portfolio_allocation = {}
        for asset, percentage in allocation_percentages.items():
            if not isinstance(percentage, (int, float)) or percentage < 0:
                raise ValueError(f"Allocation percentage for {asset} must be a non-negative number.")
            portfolio_allocation[asset] = round(initial_investment * (percentage / 100), 2)
        
        return portfolio_allocation

    except Exception as e:
        # Print error message and exit program
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Define initial investment and allocation percentages
    initial_investment = 100000  # Example: $100,000 initial investment
    allocation_percentages = {
        "Stocks": 50,
        "Bonds": 30,
        "Real Estate": 20,
    }

    # Calculate portfolio allocation
    result = calculate_portfolio_allocation(initial_investment, allocation_percentages)

    # Print the result
    print("Portfolio Allocation:")
    for asset, value in result.items():
        print(f"{asset}: ${value}")
```
