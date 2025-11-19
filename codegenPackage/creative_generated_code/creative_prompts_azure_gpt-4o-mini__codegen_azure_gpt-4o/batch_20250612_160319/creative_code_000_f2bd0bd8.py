"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Steadfast Asset Innovation, including Basic, Silver, Gold, and Dynamic plans.
Generated: DETERMINISTIC_f2bd0bd840facd13
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Calculate Potential Investment Returns Based on Steadfast Asset Innovation Plans.

Plans:
1. Basic: Fixed annual return of 5%.
2. Silver: Fixed annual return of 7%.
3. Gold: Fixed annual return of 10%.
4. Dynamic: Variable annual return rate based on user input.
"""

# Import necessary libraries
import sys

def calculate_returns(principal_amount, years, plan, dynamic_rate=None):
    """
    Calculate potential investment returns based on the selected plan.

    :param principal_amount: Initial amount of investment (float)
    :param years: Investment duration in years (int)
    :param plan: Investment plan chosen (string: 'Basic', 'Silver', 'Gold', 'Dynamic')
    :param dynamic_rate: Annual return rate for Dynamic plan (float, optional)
    :return: Total returns after specified years (float)
    """
    try:
        if principal_amount <= 0 or years <= 0:
            raise ValueError("Principal amount and years must be greater than 0.")
        
        if plan not in ['Basic', 'Silver', 'Gold', 'Dynamic']:
            raise ValueError("Invalid investment plan. Choose 'Basic', 'Silver', 'Gold', or 'Dynamic'.")
        
        if plan == 'Dynamic':
            if dynamic_rate is None or dynamic_rate <= 0:
                raise ValueError("Dynamic rate must be provided and greater than 0.")
            annual_rate = dynamic_rate / 100
        elif plan == 'Basic':
            annual_rate = 0.05
        elif plan == 'Silver':
            annual_rate = 0.07
        elif plan == 'Gold':
            annual_rate = 0.10
        
        # Calculate final returns using compound interest formula
        total_returns = principal_amount * (1 + annual_rate) ** years
        return total_returns

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate investment returns.
    """
    print("Welcome to Steadfast Asset Innovation - Investment Returns Calculator")

    try:
        # Get user input
        principal_amount = float(input("Enter the principal amount (investment): "))
        years = int(input("Enter the number of years: "))
        plan = input("Choose an investment plan (Basic/Silver/Gold/Dynamic): ").strip()

        dynamic_rate = None
        if plan == 'Dynamic':
            dynamic_rate = float(input("Enter the annual return rate for Dynamic plan (percentage): "))

        # Calculate returns
        total_returns = calculate_returns(principal_amount, years, plan, dynamic_rate)
        print(f"\nBased on your inputs, the total returns after {years} years will be: ${total_returns:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal amount, years, and dynamic rate.")

if __name__ == "__main__":
    main()
```
