"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Write Python code to calculate compound interest for an investment plan that offers "100.00% hourly returns for a lifetime" as described on the 10x Investment platform.
Generated: DETERMINISTIC_531f36b6cfe5ce48
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_compound_interest(principal, rate, time):
    """
    Calculate compound interest for an investment.

    Args:
        principal (float): Initial investment amount.
        rate (float): Hourly interest rate (as a percentage).
        time (int): Number of hours the investment is held for.

    Returns:
        float: Final investment value after compound interest.
    """
    try:
        # Validate input
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if rate <= 0:
            raise ValueError("Interest rate must be greater than zero.")
        if time < 0:
            raise ValueError("Time must be a non-negative value.")
        
        # Convert rate from percentage to decimal
        hourly_rate = rate / 100
        
        # Calculate compound interest
        final_amount = principal * (1 + hourly_rate) ** time
        
        return final_amount
    
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Example input
        principal = float(input("Enter the principal amount (e.g., 1000): "))
        rate = float(input("Enter the hourly interest rate as a percentage (e.g., 100.0): "))
        time = int(input("Enter the number of hours the investment is held (e.g., 10): "))

        # Calculate and display the result
        result = calculate_compound_interest(principal, rate, time)
        if result is not None:
            print(f"Final investment value after {time} hours: ${result:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, rate, and time.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
