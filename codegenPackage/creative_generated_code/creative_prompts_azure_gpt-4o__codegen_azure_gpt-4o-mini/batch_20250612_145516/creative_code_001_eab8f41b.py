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
def calculate_portfolio_allocation(initial_investment, allocation_percentages):
    """
    Calculate the total value of each asset in a portfolio based on 
    quarterly allocation percentages and an initial investment amount.

    Parameters:
        initial_investment (float): The total amount of money to invest.
        allocation_percentages (dict): A dictionary where keys are asset names 
                                       and values are their respective allocation 
                                       percentages (0 to 100).

    Returns:
        dict: A dictionary with asset names as keys and their corresponding 
              total values as values.

    Raises:
        ValueError: If any allocation percentage is not between 0 and 100, 
                    or if the total percentage does not sum to 100.
    """
    
    # Validate input types
    if not isinstance(initial_investment, (int, float)) or initial_investment < 0:
        raise ValueError("Initial investment must be a non-negative number.")
    
    if not isinstance(allocation_percentages, dict):
        raise ValueError("Allocation percentages must be provided as a dictionary.")

    # Calculate total percentage
    total_percentage = sum(allocation_percentages.values())

    # Validate total percentage
    if total_percentage != 100:
        raise ValueError("Total allocation percentages must sum to 100.")

    # Initialize a dictionary to hold the total values for each asset
    asset_values = {}

    # Calculate the total value for each asset based on the provided percentages
    for asset, percentage in allocation_percentages.items():
        if not (0 <= percentage <= 100):
            raise ValueError(f"Allocation percentage for '{asset}' is out of bounds (0-100).")
        
        asset_value = (percentage / 100) * initial_investment
        asset_values[asset] = asset_value

    return asset_values

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 10000  # Example initial investment
        allocation_percentages = {
            'Stocks': 50,
            'Bonds': 30,
            'Real Estate': 20
        }

        result = calculate_portfolio_allocation(initial_investment, allocation_percentages)
        print("Portfolio Allocation:", result)
    except ValueError as e:
        print(f"Error: {e}")
```
