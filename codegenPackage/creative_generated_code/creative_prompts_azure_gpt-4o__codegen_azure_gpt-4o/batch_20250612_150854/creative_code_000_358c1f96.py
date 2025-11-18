"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: Write Python code to calculate compound interest using the formula and concepts described on the Arbiquant platform, including variables for time, rate, initial investment, and compounding frequency.
Generated: DETERMINISTIC_358c1f962d21ff64
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math

def calculate_compound_interest(principal, rate, time, compounding_frequency):
    """
    Calculate compound interest.

    Args:
        principal (float): The initial investment amount.
        rate (float): Annual interest rate (as a decimal, e.g., 0.05 for 5%).
        time (float): Time in years the investment is held.
        compounding_frequency (int): Number of times the interest is compounded per year.

    Returns:
        float: The final amount after compound interest is applied.
    """
    try:
        # Validate inputs
        if principal <= 0 or rate <= 0 or time <= 0 or compounding_frequency <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Compound interest formula
        final_amount = principal * math.pow((1 + rate / compounding_frequency), compounding_frequency * time)
        return final_amount

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example Usage
    try:
        # Input variables
        principal = float(input("Enter the principal amount (initial investment): "))
        rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
        time = float(input("Enter the time in years: "))
        compounding_frequency = int(input("Enter the compounding frequency per year (e.g., 12 for monthly): "))
        
        # Calculate compound interest
        final_amount = calculate_compound_interest(principal, rate, time, compounding_frequency)
        
        if final_amount is not None:
            print(f"The final amount after {time} years is: ${final_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
