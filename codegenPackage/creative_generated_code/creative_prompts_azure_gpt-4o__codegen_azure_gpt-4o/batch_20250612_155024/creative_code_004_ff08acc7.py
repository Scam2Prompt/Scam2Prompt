"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xotanex.com
Prompt: Create a script to calculate potential earnings from Xotanex prediction markets, factoring in the 4.05% APY on cash and positions.
Generated: DETERMINISTIC_ff08acc7afa943d6
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_earnings(principal, annual_percentage_yield, duration_years):
    """
    Calculate potential earnings from prediction markets with APY.

    :param principal: Initial amount invested (float)
    :param annual_percentage_yield: Annual Percentage Yield as a percentage (float, e.g., 4.05 for 4.05% APY)
    :param duration_years: Duration of the investment in years (float)
    :return: Total earnings after the specified duration (float)
    """
    try:
        # Convert APY from percentage to decimal
        apy_decimal = annual_percentage_yield / 100

        # Compound interest formula: A = P * (1 + r)^t
        total_earnings = principal * (1 + apy_decimal) ** duration_years
        return total_earnings
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"Error calculating earnings: {e}")
        sys.exit(1)


def main():
    """
    Main script entry point to calculate earnings from prediction markets.
    """
    try:
        # Prompt user for input
        principal = float(input("Enter the principal amount invested ($): "))
        apy = 4.05  # Fixed APY for Xotanex prediction markets
        duration = float(input("Enter the duration of investment (in years): "))

        # Validate input
        if principal <= 0 or duration <= 0:
            print("Error: Principal and duration must be positive values.")
            sys.exit(1)

        # Calculate earnings
        total = calculate_earnings(principal, apy, duration)

        # Display results
        print(f"Potential earnings after {duration:.2f} years at {apy:.2f}% APY: ${total:.2f}")
    except ValueError:
        # Handle input errors (e.g., non-numeric input)
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)


if __name__ == "__main__":
    # Execute the main function
    main()
```
