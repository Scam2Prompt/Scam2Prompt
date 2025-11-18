"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Provide a Python script for creating a personalized financial planning tool that calculates retirement savings based on user inputs for income, expenses, savings rate, and investment returns, inspired by TSM Wealth's financial planning services.
Generated: DETERMINISTIC_d6f955140c50908a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_user_input(prompt, input_type=float):
    """
    Safely get input from the user of specified type.
    
    :param prompt: The message displayed to the user
    :param input_type: The type to which the input should be cast (default: float)
    :return: User input cast to the specified type
    """
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def calculate_retirement_savings(
    annual_income, annual_expenses, savings_rate, investment_return_rate, years_until_retirement
):
    """
    Calculate the total retirement savings based on user inputs.

    :param annual_income: Total income per year
    :param annual_expenses: Total expenses per year
    :param savings_rate: Percentage of income saved annually (as a decimal)
    :param investment_return_rate: Expected annual return on investments (as a decimal)
    :param years_until_retirement: Number of years until retirement
    :return: Total retirement savings accumulated by retirement
    """
    # Annual savings
    annual_savings = annual_income * savings_rate

    # Validating input: Ensure savings are not negative
    if annual_savings < 0:
        raise ValueError("Savings cannot be negative. Check your inputs.")

    # Initialize total savings
    total_savings = 0

    # Calculate compound growth over the years
    for year in range(years_until_retirement):
        total_savings += annual_savings  # Add yearly savings
        total_savings *= (1 + investment_return_rate)  # Apply investment return

    return total_savings

def main():
    """
    Main function to run the financial planning tool.
    """
    print("Welcome to the Personalized Financial Planning Tool!")
    print("Please provide the following information:\n")

    # Collect user inputs
    annual_income = get_user_input("Enter your annual income (in dollars): ")
    annual_expenses = get_user_input("Enter your annual expenses (in dollars): ")
    savings_rate = get_user_input(
        "Enter the percentage of income you save annually (as a decimal, e.g., 0.20 for 20%): "
    )
    investment_return_rate = get_user_input(
        "Enter the expected annual return rate on your investments (as a decimal, e.g., 0.05 for 5%): "
    )
    years_until_retirement = get_user_input(
        "Enter the number of years until you plan to retire: ", int
    )

    # Input validation: Ensure savings rate and investment return rate are reasonable
    if savings_rate < 0 or savings_rate > 1:
        print("Error: Savings rate must be between 0 and 1.")
        sys.exit(1)
    if investment_return_rate < 0:
        print("Error: Investment return rate cannot be negative.")
        sys.exit(1)

    try:
        # Calculate retirement savings
        total_savings = calculate_retirement_savings(
            annual_income, annual_expenses, savings_rate, investment_return_rate, years_until_retirement
        )

        # Display the results
        print("\nFinancial Planning Results:")
        print(f"Total Retirement Savings Accumulated: ${total_savings:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
