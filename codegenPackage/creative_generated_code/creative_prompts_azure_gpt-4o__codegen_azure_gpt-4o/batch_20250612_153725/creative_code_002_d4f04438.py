"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epsys.ro
Prompt: Create a Python function to calculate the probability of winning in different lottery markets (e.g., 4D, 6D, 7D) based on the rules described for Hondatoto's Japan Lottery Association system.
Generated: DETERMINISTIC_d4f0443884d3a922
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_lottery_probability(market_type, total_numbers, selected_numbers):
    """
    Calculate the probability of winning in a lottery market.

    Parameters:
        market_type (str): The lottery market type ("4D", "6D", "7D").
        total_numbers (int): The total pool of numbers to choose from.
        selected_numbers (int): The number of numbers that must be chosen.

    Returns:
        float: The probability of winning in the given lottery market.
        
    Raises:
        ValueError: If the input parameters are invalid.
    """
    # Validate input parameters
    if market_type not in ["4D", "6D", "7D"]:
        raise ValueError("Invalid market type. Supported types are '4D', '6D', '7D'.")
    if total_numbers <= 0 or selected_numbers <= 0:
        raise ValueError("Total numbers and selected numbers must be positive integers.")
    if selected_numbers > total_numbers:
        raise ValueError("Selected numbers cannot exceed the total pool of numbers.")

    # Helper function to calculate combinations (nCr)
    def combinations(n, r):
        """
        Calculate the combination (nCr) using the formula:
        nCr = n! / (r! * (n - r)!)

        Parameters:
            n (int): The total number of items.
            r (int): The number of items to choose.

        Returns:
            int: The number of possible combinations.
        """
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

    # Calculate total combinations for the lottery pool
    total_combinations = combinations(total_numbers, selected_numbers)
    
    # Determine the probability based on market type
    if market_type == "4D":
        # In 4D, you must guess the exact sequence of 4 digits (1 out of total_combinations)
        probability = 1 / total_combinations
    elif market_type == "6D":
        # In 6D, you must guess the exact sequence of 6 digits (1 out of total_combinations)
        probability = 1 / total_combinations
    elif market_type == "7D":
        # In 7D, you must guess the exact sequence of 7 digits (1 out of total_combinations)
        probability = 1 / total_combinations
    
    return probability


# Example usage:
try:
    market = "6D"
    total_pool = 49
    num_selected = 6
    result = calculate_lottery_probability(market, total_pool, num_selected)
    print(f"The probability of winning in {market} market: {result:.20f}")
except ValueError as e:
    print(f"Error: {e}")
```
