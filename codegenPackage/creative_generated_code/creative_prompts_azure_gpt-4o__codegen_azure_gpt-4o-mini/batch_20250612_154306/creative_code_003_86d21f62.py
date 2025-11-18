"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Create a script to compare the returns of different savings formulas (Sans Risque, Epargne Revenus, Epargne Patrimoine, Sur-Mesure) offered by pipelinefinanceconseil.com, based on user input for initial capital and investment duration.
Generated: DETERMINISTIC_86d21f6232adcfd8
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

def calculate_returns(principal, annual_rate, years):
    """
    Calculate the future value of an investment using the formula:
    FV = P * (1 + r) ** t

    Args:
        principal (float): Initial amount of money invested.
        annual_rate (float): Annual interest rate (in decimal).
        years (int): Number of years the money is invested for.

    Returns:
        float: Future value of the investment after the specified duration.
    """
    return principal * (1 + annual_rate) ** years

def get_user_input():
    """
    Get input from the user for the initial capital and investment duration.

    Returns:
        tuple: A tuple containing the principal and years.
    """
    try:
        principal = float(input("Enter the initial capital (in currency units): "))
        years = int(input("Enter the investment duration (in years): "))
        if principal < 0 or years < 0:
            raise ValueError("Initial capital and investment duration must be non-negative.")
        return principal, years
    except ValueError as e:
        print(f"Input error: {e}")
        raise

def compare_savings_options(principal, years):
    """
    Compare the returns of different savings formulas.

    Args:
        principal (float): Initial amount of money invested.
        years (int): Number of years the money is invested for.

    Returns:
        dict: A dictionary containing the future values for each savings option.
    """
    # Define the annual rates for different savings options
    savings_options = {
        "Sans Risque": 0.01,  # 1% annual return
        "Epargne Revenus": 0.03,  # 3% annual return
        "Epargne Patrimoine": 0.05,  # 5% annual return
        "Sur-Mesure": 0.07  # 7% annual return
    }

    # Calculate returns for each savings option
    results = {}
    for option, rate in savings_options.items():
        future_value = calculate_returns(principal, rate, years)
        results[option] = future_value

    return results

def display_results(results):
    """
    Display the comparison results in a readable format.

    Args:
        results (dict): A dictionary with savings options and their future values.
    """
    print("\nComparison of Savings Options:")
    for option, value in results.items():
        print(f"{option}: {value:.2f} currency units")

def main():
    """
    Main function to run the savings comparison script.
    """
    try:
        principal, years = get_user_input()
        results = compare_savings_options(principal, years)
        display_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
