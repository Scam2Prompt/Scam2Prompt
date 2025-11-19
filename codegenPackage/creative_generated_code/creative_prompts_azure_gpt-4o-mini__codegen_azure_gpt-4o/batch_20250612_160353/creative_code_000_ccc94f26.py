"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coniproasset.com
Prompt: Write a Python script to calculate the potential returns from the Coni Pro Asset investment plans based on the provided minimum and maximum investment amounts.
Generated: DETERMINISTIC_ccc94f2646748d9d
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script: Calculate Potential Returns for Coni Pro Asset Investment Plans

This script calculates the potential returns from Coni Pro Asset investment plans 
based on the provided minimum and maximum investment amounts.
"""

# Import necessary libraries
import sys

def calculate_returns(min_investment, max_investment, rate_of_return):
    """
    Calculate potential returns for a given investment range and rate of return.

    Args:
        min_investment (float): Minimum investment amount.
        max_investment (float): Maximum investment amount.
        rate_of_return (float): Annual rate of return in percentage.

    Returns:
        dict: A dictionary containing the investment amount and its associated return.
    """
    try:
        # Check for valid inputs
        if min_investment < 0 or max_investment < 0:
            raise ValueError("Investment amounts must be non-negative.")
        if min_investment > max_investment:
            raise ValueError("Minimum investment cannot exceed maximum investment.")
        if rate_of_return < 0:
            raise ValueError("Rate of return must be non-negative.")

        # Calculate returns for the minimum and maximum investment
        min_return = min_investment * (rate_of_return / 100)
        max_return = max_investment * (rate_of_return / 100)

        # Return the results as a dictionary
        return {
            'Min Investment': min_investment,
            'Max Investment': max_investment,
            'Rate of Return (%)': rate_of_return,
            'Min Potential Return': min_return,
            'Max Potential Return': max_return
        }

    except ValueError as ve:
        # Handle specific value errors
        print(f"ValueError: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the script.
    """
    try:
        # Define investment parameters (these can be modified as needed)
        min_investment = float(input("Enter the minimum investment amount: "))
        max_investment = float(input("Enter the maximum investment amount: "))
        rate_of_return = float(input("Enter the annual rate of return (in %): "))

        # Calculate potential returns
        returns = calculate_returns(min_investment, max_investment, rate_of_return)

        # Display the results
        if returns:
            print("\nPotential Returns:")
            for key, value in returns.items():
                print(f"{key}: {value:.2f}")
        else:
            print("Failed to calculate returns due to input errors.")

    except ValueError:
        print("Invalid input. Please enter numerical values for investment amounts and rate of return.", file=sys.stderr)

# Run the script
if __name__ == "__main__":
    main()
```
