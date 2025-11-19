"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Develop a financial calculator that helps young individuals assess their current financial situation and set long-term monetary goals, inspired by the services offered at Australia Wide Wealth.
Generated: DETERMINISTIC_0aaf3521956a09e5
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_float_input(prompt):
    """
    Safely get a float input from the user.
    :param prompt: The message to display to the user.
    :return: A float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_savings_growth(initial_savings, monthly_contribution, annual_interest_rate, years):
    """
    Calculate the future value of savings with monthly contributions and compound interest.
    :param initial_savings: Initial amount of savings.
    :param monthly_contribution: Monthly contribution to savings.
    :param annual_interest_rate: Annual interest rate (in percentage).
    :param years: Number of years to calculate growth for.
    :return: Future value of savings.
    """
    months = years * 12
    monthly_interest_rate = annual_interest_rate / 100 / 12
    future_value = initial_savings

    for _ in range(months):
        future_value += monthly_contribution
        future_value += future_value * monthly_interest_rate

    return future_value

def main():
    """
    Main function to run the financial calculator.
    """
    print("Welcome to the Financial Calculator!")
    print("This tool will help you assess your current financial situation and set long-term monetary goals.\n")

    # Gather user inputs
    initial_savings = get_float_input("Enter your current savings amount ($): ")
    monthly_contribution = get_float_input("Enter your monthly savings contribution ($): ")
    annual_interest_rate = get_float_input("Enter the expected annual interest rate (in %): ")
    years = get_float_input("Enter the number of years you want to save for: ")

    # Validate inputs
    if initial_savings < 0 or monthly_contribution < 0 or annual_interest_rate < 0 or years <= 0:
        print("Error: All inputs must be positive numbers, and years must be greater than zero.")
        sys.exit(1)

    # Calculate future savings
    future_savings = calculate_savings_growth(initial_savings, monthly_contribution, annual_interest_rate, years)

    # Display results
    print("\nFinancial Summary:")
    print(f"Initial Savings: ${initial_savings:,.2f}")
    print(f"Monthly Contribution: ${monthly_contribution:,.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Years to Save: {years}")
    print(f"Future Savings Value: ${future_savings:,.2f}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
