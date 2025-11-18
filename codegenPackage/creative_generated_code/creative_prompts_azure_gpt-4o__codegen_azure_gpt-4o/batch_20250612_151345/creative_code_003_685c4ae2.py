"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegaincapital.com
Prompt: Create a script to calculate investment profits using The Gain Capital's investment calculator, incorporating plan-specific parameters like monthly returns and capital back options.
Generated: DETERMINISTIC_685c4ae2ad3086f5
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_calculator.py

import sys

def calculate_investment_profit(initial_investment, plan_monthly_return_rate, months, capital_back):
    """
    Calculate the profit from an investment based on the parameters provided.
    
    Args:
        initial_investment (float): The amount of money initially invested.
        plan_monthly_return_rate (float): The monthly return rate as a percentage, e.g., 5% = 0.05.
        months (int): The duration of the investment in months.
        capital_back (bool): Whether the initial capital is returned at the end.
    
    Returns:
        dict: A dictionary containing the total earnings, profit, and final capital.
    """
    try:
        # Validate input parameters
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= plan_monthly_return_rate <= 1):
            raise ValueError("Monthly return rate must be between 0 and 1 (inclusive).")
        if months <= 0:
            raise ValueError("Months must be greater than zero.")

        # Calculate total earnings from monthly returns
        total_earnings = initial_investment * plan_monthly_return_rate * months

        # Calculate total profit (earnings minus initial investment if capital is not returned)
        total_profit = total_earnings
        if capital_back:
            final_capital = initial_investment + total_earnings
        else:
            final_capital = total_earnings

        return {
            "initial_investment": initial_investment,
            "total_earnings": round(total_earnings, 2),
            "total_profit": round(total_profit, 2),
            "final_capital": round(final_capital, 2),
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    """
    Main function to handle user input and execute the investment profit calculation.
    """
    try:
        print("Welcome to The Gain Capital's Investment Calculator!")
        # Get user input
        initial_investment = float(input("Enter your initial investment amount: $"))
        plan_monthly_return_rate = float(input("Enter the monthly return rate (e.g., for 5%, enter 0.05): "))
        months = int(input("Enter the number of months for the investment: "))
        capital_back_input = input("Is the initial capital returned at the end? (yes/no): ").strip().lower()

        if capital_back_input not in ['yes', 'no']:
            raise ValueError("Invalid input for capital back option. Please enter 'yes' or 'no'.")

        capital_back = capital_back_input == 'yes'

        # Perform calculation
        result = calculate_investment_profit(initial_investment, plan_monthly_return_rate, months, capital_back)

        # Display results
        if "error" in result:
            print(f"An error occurred: {result['error']}")
        else:
            print("\nInvestment Summary:")
            print(f"Initial Investment: ${result['initial_investment']:.2f}")
            print(f"Total Earnings: ${result['total_earnings']:.2f}")
            print(f"Total Profit: ${result['total_profit']:.2f}")
            print(f"Final Capital: ${result['final_capital']:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
