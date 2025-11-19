"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudminingglobal.com
Prompt: Write a script to calculate potential returns on investment using the various plans offered by Cloudminingglobal.
Generated: DETERMINISTIC_88b9e937d579cd75
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

# Function to calculate potential returns on investment
def calculate_roi(investment_amount, annual_rate, duration_years):
    """
    Calculate the potential ROI (Return on Investment).

    Parameters:
        investment_amount (float): The initial investment amount in USD.
        annual_rate (float): The annual interest rate (as a percentage).
        duration_years (int): The duration of the investment in years.

    Returns:
        float: The total potential returns after the specified duration.
    """
    try:
        # Ensure all inputs are positive numbers
        if investment_amount <= 0 or annual_rate <= 0 or duration_years <= 0:
            raise ValueError("Inputs must be positive numbers.")
        
        # Compound interest formula: A = P * (1 + r)^t
        total_returns = investment_amount * ((1 + annual_rate / 100) ** duration_years)
        return total_returns
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

# Main function to display the various investment returns
def main():
    """
    Main function to calculate ROI based on Cloudminingglobal investment plans.
    """
    print("Welcome to Cloudminingglobal Investment ROI Calculator!")

    plans = [
        {"name": "Basic Plan", "annual_rate": 5},      # 5% annual interest
        {"name": "Silver Plan", "annual_rate": 10},    # 10% annual interest
        {"name": "Gold Plan", "annual_rate": 15},      # 15% annual interest
        {"name": "Platinum Plan", "annual_rate": 20},  # 20% annual interest
    ]

    try:
        # Get user input for investment details
        investment_amount = float(input("Enter your investment amount (USD): "))
        duration_years = int(input("Enter the duration of investment (years): "))
        
        if investment_amount <= 0 or duration_years <= 0:
            raise ValueError("Investment amount and duration must be positive numbers.")
        
        print("\nPotential returns based on available plans:")
        print("-" * 60)
        
        # Calculate and display the potential returns for each plan
        for plan in plans:
            total_returns = calculate_roi(investment_amount, plan["annual_rate"], duration_years)
            if total_returns is not None:
                print(f"{plan['name']} ({plan['annual_rate']}% annual rate): ${total_returns:.2f}")
        
        print("-" * 60)
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point for the script
if __name__ == "__main__":
    main()
```
