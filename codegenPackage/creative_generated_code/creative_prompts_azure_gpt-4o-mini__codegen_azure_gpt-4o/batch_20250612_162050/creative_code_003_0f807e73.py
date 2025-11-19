"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presales1.pages.dev
Prompt: Develop a script that simulates the purchase of JESSE tokens at various BASE levels and outputs the results.
Generated: DETERMINISTIC_0f807e73b802ceb5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to simulate the purchase of JESSE tokens at various BASE levels
# Author: [Your Name]
# Date: [Insert Date]

import sys

def calculate_tokens(base, amount):
    """
    Calculate the number of JESSE tokens received for a given amount and base level.

    :param base: The base level price of JESSE tokens.
    :param amount: The amount of currency spent.
    :return: The number of JESSE tokens purchased.
    """
    try:
        if base <= 0 or amount <= 0:
            raise ValueError("Base and amount must be positive numbers.")
        return amount / base
    except TypeError:
        raise TypeError("Base and amount must be numeric values.")

def simulate_purchases(base_levels, purchase_amounts):
    """
    Simulate the purchase of JESSE tokens for various base levels and amounts.

    :param base_levels: List of BASE levels.
    :param purchase_amounts: List of purchase amounts.
    :return: Dictionary containing simulation results.
    """
    results = {}
    for base in base_levels:
        results[base] = []
        for amount in purchase_amounts:
            try:
                tokens = calculate_tokens(base, amount)
                results[base].append(tokens)
            except ValueError as ve:
                results[base].append(f"Error: {ve}")
            except TypeError as te:
                results[base].append(f"Error: {te}")
    return results

def print_results(simulation_results):
    """
    Print simulation results in a user-friendly format.

    :param simulation_results: Dictionary containing simulation results.
    """
    print("Simulation Results:")
    print("===================")
    for base, purchases in simulation_results.items():
        print(f"Base Level: {base}")
        for idx, tokens in enumerate(purchases):
            print(f"  Purchase {idx + 1}: {tokens} JESSE tokens")
        print("-------------------")

def main():
    """
    Main function to execute the simulation.
    """
    try:
        # Define BASE levels and purchase amounts
        base_levels = [0.5, 1, 1.5, 2]  # Example BASE levels
        purchase_amounts = [10, 20, 30]  # Example purchase amounts in currency

        # Run simulation
        results = simulate_purchases(base_levels, purchase_amounts)

        # Output results
        print_results(results)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
