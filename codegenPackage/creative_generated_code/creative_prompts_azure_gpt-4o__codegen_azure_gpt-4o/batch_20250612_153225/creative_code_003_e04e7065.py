"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innovarenting.com
Prompt: Provide a code example to implement a feature that calculates cost savings for businesses using renting solutions compared to owning a fleet, as highlighted by Innova Renting.
Generated: DETERMINISTIC_e04e70650e9f6bab
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: cost_savings_calculator.py

"""
This script calculates cost savings for businesses using renting solutions
compared to owning a fleet. The calculation is based on user-provided input
about costs associated with owning vs renting.
"""

def calculate_cost_savings(ownership_costs: float, renting_costs: float) -> float:
    """
    Calculate the cost savings for businesses using renting solutions
    compared to owning a fleet.
    
    Args:
        ownership_costs (float): Total annual cost of owning a fleet.
        renting_costs (float): Total annual cost of renting a fleet.
        
    Returns:
        float: The calculated cost savings.
    """
    try:
        # Ensure valid inputs
        if ownership_costs < 0 or renting_costs < 0:
            raise ValueError("Costs must be non-negative.")

        # Calculate savings
        savings = ownership_costs - renting_costs
        return savings
    except ValueError as e:
        print(f"Error: {e}")
        return 0.0  # Return 0 in case of invalid input
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0  # Return 0 for other unexpected errors


def main():
    """
    Main program function. Collects user input and calculates cost savings.
    """
    try:
        # Prompt user for total annual ownership costs
        ownership_costs = float(input("Enter total annual ownership costs (€): "))

        # Prompt user for total annual renting costs
        renting_costs = float(input("Enter total annual renting costs (€): "))

        # Calculate savings
        savings = calculate_cost_savings(ownership_costs, renting_costs)

        # Output the result
        if savings >= 0:
            print(f"Cost savings by renting instead of owning: €{savings:.2f}")
        else:
            print(f"Renting is more expensive by €{-savings:.2f}.")
    except ValueError:
        print("Invalid input. Please enter numeric values for costs.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Entry point of the program
    print("Welcome to the Cost Savings Calculator!")
    print("Compare owning a fleet vs renting to determine potential savings.\n")
    main()
```

This code is production-ready and adheres to the requested guidelines. Save this script as `cost_savings_calculator.py`, and it can be executed in a Python environment.
