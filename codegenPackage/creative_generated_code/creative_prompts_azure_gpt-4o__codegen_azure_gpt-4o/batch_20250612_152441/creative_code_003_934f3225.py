"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Generate code to calculate the inflation rate of CNK tokens over time, considering the steadily decreasing inflation rate mentioned in the Crypto N' Kafe documentation.
Generated: DETERMINISTIC_934f32255b5c4ee5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module to calculate the inflation rate of CNK tokens over time.

This script uses the steadily decreasing inflation rate model mentioned in the Crypto N' Kafe documentation.
The inflation rate decreases every year based on predefined constants.

Assumptions:
- The initial supply of CNK tokens and initial inflation rate are known.
- The inflation rate decreases by a fixed percentage annually as per the documentation.

Production-ready, with appropriate error handling included.
"""

def calculate_inflation_rate(initial_supply: float, initial_inflation_rate: float, annual_rate_decay: float, years: int) -> float:
    """
    Calculate the inflation-adjusted total token supply after a given number of years.

    :param initial_supply: The initial supply of CNK tokens (e.g., 1000000)
    :param initial_inflation_rate: The starting inflation rate as a percentage (e.g., 10%)
    :param annual_rate_decay: The percentage by which the inflation rate reduces annually (e.g., 2%)
    :param years: The number of years over which to calculate inflation (e.g., 10)
    :return: The total CNK token supply after the specified years
    """
    # Validate inputs
    if initial_supply <= 0 or initial_inflation_rate <= 0 or annual_rate_decay < 0 or years < 0:
        raise ValueError("Invalid input values. Ensure all inputs are positive, and years/decay rate are non-negative.")

    current_supply = initial_supply
    current_inflation_rate = initial_inflation_rate

    for year in range(1, years + 1):
        # Calculate the tokens added due to inflation for this year
        tokens_added = current_supply * (current_inflation_rate / 100)
        # Update the total supply
        current_supply += tokens_added
        # Decrease the inflation rate by the annual rate decay
        current_inflation_rate = max(0, current_inflation_rate - annual_rate_decay)  # Ensure inflation rate doesn't drop below zero

    return current_supply


def main():
    """
    Main function to demonstrate the inflation rate calculation for CNK tokens.
    """
    try:
        # Example values (these should ideally come from the Crypto N' Kafe documentation or user input)
        initial_supply = 1000000  # Initial supply of CNK tokens
        initial_inflation_rate = 10  # Starting inflation rate as a percentage
        annual_rate_decay = 2  # Inflation rate decreases by 2% each year
        years = 10  # Calculate inflation over 10 years

        final_supply = calculate_inflation_rate(initial_supply, initial_inflation_rate, annual_rate_decay, years)

        print(f"After {years} years, the total CNK token supply will be: {final_supply:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
