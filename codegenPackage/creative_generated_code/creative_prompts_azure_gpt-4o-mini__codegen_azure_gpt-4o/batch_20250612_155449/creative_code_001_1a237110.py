"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Write a function that calculates the percentage allocation of SUI in the investment strategy for each quarter from 2024 to 2026.
Generated: DETERMINISTIC_1a23711000127b24
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_sui_allocation(start_year=2024, end_year=2026, total_investment=100000, investment_strategy=None):
    """
    Calculate the percentage allocation of SUI in the investment strategy for each quarter from the start year to the end year.

    Args:
        start_year (int): The starting year for the calculation.
        end_year (int): The ending year for the calculation.
        total_investment (float): Total investment amount (default $100,000).
        investment_strategy (dict): Dictionary containing SUI allocation per quarter, e.g., {"Q1": 0.25, "Q2": 0.4, "Q3": 0.2, "Q4": 0.15} (percentages in decimals).

    Returns:
        dict: Dictionary with years as keys and quarters as sub-keys containing SUI allocation percentages and amounts.
    """

    # Validate input
    if not isinstance(start_year, int) or not isinstance(end_year, int):
        raise ValueError("start_year and end_year must be integers.")
    if start_year > end_year:
        raise ValueError("start_year must be less than or equal to end_year.")
    if not isinstance(total_investment, (int, float)) or total_investment <= 0:
        raise ValueError("total_investment must be a positive number.")
    if investment_strategy is None:
        investment_strategy = {"Q1": 0.25, "Q2": 0.25, "Q3": 0.25, "Q4": 0.25}  # Default equal allocation
    if not isinstance(investment_strategy, dict):
        raise ValueError("investment_strategy must be a dictionary.")
    if not sum(investment_strategy.values()) == 1.0:
        raise ValueError("The sum of allocation percentages in investment_strategy must equal 1.")

    # Initialize results dictionary
    results = {}

    # Generate data for each year and quarter
    for year in range(start_year, end_year + 1):
        results[year] = {}  # Nested dictionary for quarters
        for quarter, percentage in investment_strategy.items():
            allocation_amount = total_investment * percentage
            results[year][quarter] = {
                "percentage": percentage * 100,  # Convert to percentage (e.g., 25%)
                "allocation_amount": allocation_amount,  # Allocation amount for the quarter
            }
    
    return results


# Example usage of the function
if __name__ == "__main__":
    try:
        # Define custom investment strategy
        custom_strategy = {"Q1": 0.3, "Q2": 0.4, "Q3": 0.2, "Q4": 0.1}
        
        # Calculate SUI allocation from 2024 to 2026
        allocation = calculate_sui_allocation(start_year=2024, end_year=2026, total_investment=150000, investment_strategy=custom_strategy)
        
        # Print the results
        for year, quarters in allocation.items():
            print(f"Year {year}:")
            for quarter, details in quarters.items():
                print(f"  {quarter}: {details['percentage']}% (${details['allocation_amount']:.2f})")
    except Exception as e:
        print(f"Error: {e}")
```
