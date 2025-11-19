"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitesrock.fi
Prompt: Write a Python script to calculate the potential interest earned on USDX over 40 years based on monthly contributions and initial investment.
Generated: DETERMINISTIC_11b20c42aa9c64eb
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_interest(initial_investment, monthly_contribution, annual_interest_rate, years):
    """
    Calculates the total value of an investment including interest earned over a period of time.

    Parameters:
        initial_investment (float): The starting amount of money invested.
        monthly_contribution (float): The amount contributed each month to the investment.
        annual_interest_rate (float): The annual interest rate in percentage (e.g., 5 for 5%).
        years (int): The total number of years to calculate the investment growth.

    Returns:
        float: The total amount after the given number of years including compounded interest.
    """
    try:
        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = annual_interest_rate / 100 / 12
        
        # Total number of months
        months = years * 12
        
        # Initialize total amount with the initial investment
        total_amount = initial_investment
        
        for _ in range(months):
            # Add monthly contribution
            total_amount += monthly_contribution
            
            # Apply monthly interest
            total_amount *= (1 + monthly_interest_rate)
        
        return round(total_amount, 2)
    except Exception as e:
        print(f"An error occurred during calculation: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and perform the calculation.
    """
    try:
        # Get user input for initial investment, monthly contribution, interest rate, and years
        initial_investment = float(input("Enter the initial investment amount (USD): "))
        monthly_contribution = float(input("Enter the monthly contribution amount (USD): "))
        annual_interest_rate = float(input("Enter the annual interest rate (percentage): "))
        years = int(input("Enter the number of years for the investment: "))
        
        if initial_investment < 0 or monthly_contribution < 0 or annual_interest_rate < 0 or years <= 0:
            print("All values must be positive and years must be greater than zero.", file=sys.stderr)
            return
        
        # Calculate the total amount with interest
        total_amount = calculate_interest(initial_investment, monthly_contribution, annual_interest_rate, years)
        
        if total_amount is not None:
            print(f"\nAfter {years} years, the total value of the investment will be: ${total_amount}")
    except ValueError:
        print("Invalid input. Please ensure all values are entered correctly.", file=sys.stderr)


if __name__ == "__main__":
    main()
```
