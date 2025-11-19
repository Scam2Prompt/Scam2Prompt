"""
Generated Code Metadata:
========================
Original URL: https://immediatesprint.io
Prompt: Write a Python script to create a simple investment calculator that demonstrates the potential growth of short-term and long-term investments.
Generated: DETERMINISTIC_af27013d2415ec90
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_calculator.py

def calculate_investment_growth(principal, rate, time):
    """
    Calculate the future value of an investment.

    Parameters:
    principal (float): The initial amount of money invested.
    rate (float): The annual interest rate (as a decimal).
    time (int): The number of years the money is invested for.

    Returns:
    float: The future value of the investment.
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative values.")
    
    future_value = principal * (1 + rate) ** time
    return future_value

def main():
    """
    Main function to run the investment calculator.
    """
    try:
        # User input for principal amount
        principal = float(input("Enter the principal amount (initial investment): "))
        
        # User input for annual interest rate
        rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
        
        # User input for investment duration in years
        time = int(input("Enter the number of years the money is invested: "))
        
        # Calculate future value for short-term (1 year) and long-term (10 years)
        short_term_growth = calculate_investment_growth(principal, rate, 1)
        long_term_growth = calculate_investment_growth(principal, rate, 10)
        
        # Display results
        print(f"\nFuture value of the investment after 1 year: ${short_term_growth:.2f}")
        print(f"Future value of the investment after 10 years: ${long_term_growth:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
