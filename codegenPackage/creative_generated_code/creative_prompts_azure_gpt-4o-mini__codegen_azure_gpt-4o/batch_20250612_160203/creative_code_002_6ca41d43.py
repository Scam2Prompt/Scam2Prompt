"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Generate a code snippet that simulates the growth of capital in an investment account based on the investment plans provided by epiccoin-miners.ltd, including calculations for different deposit amounts.
Generated: DETERMINISTIC_6ca41d43065be841
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def simulate_investment_growth(deposit_amount, annual_rate, years):
    """
    Simulates the growth of capital in an investment account.

    Args:
        deposit_amount (float): The initial deposit amount in USD.
        annual_rate (float): Annual interest rate (as a percentage).
        years (int): Number of years to simulate.

    Returns:
        float: The final amount after the specified number of years.
    """
    try:
        # Input validation
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        if annual_rate <= 0:
            raise ValueError("Annual rate must be greater than 0.")
        if years <= 0:
            raise ValueError("Years must be greater than 0.")

        # Convert percentage rate to decimal
        rate_decimal = annual_rate / 100

        # Compound interest formula: A = P(1 + r)^t
        final_amount = deposit_amount * (1 + rate_decimal) ** years

        return round(final_amount, 2)
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    """
    Main function to simulate investment growth based on user input.
    """
    try:
        print("Welcome to Epiccoin Miners Investment Simulator!")
        
        # Gather user inputs
        deposit_amount = float(input("Enter the initial deposit amount (USD): "))
        annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
        years = int(input("Enter the number of years to simulate: "))

        # Simulate growth
        final_amount = simulate_investment_growth(deposit_amount, annual_rate, years)

        # Display result
        print(f"\nAfter {years} years at an annual rate of {annual_rate}%, your investment will grow to: ${final_amount}")

    except ValueError:
        print("Invalid input. Please provide numeric values for deposit, rate, and years.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
