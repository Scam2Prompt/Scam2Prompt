"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Create a script to calculate the potential income from dividend-paying stocks or rental properties, aligning with the income generation strategies on Investolazlo.
Generated: DETERMINISTIC_03507fcf00853342
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate potential income from dividend-paying stocks or rental properties
# Author: Expert Programmer
# Date: YYYY-MM-DD
# This script aligns with income generation strategies outlined on Investolazlo.

# Import necessary libraries
import sys

def calculate_dividend_income(stock_price, dividend_yield, shares_owned):
    """
    Calculate annual income from dividend-paying stocks.
    
    Parameters:
        stock_price (float): The price of a single stock.
        dividend_yield (float): The annual dividend yield as a percentage (e.g., 5 for 5%).
        shares_owned (int): The number of shares owned.
    
    Returns:
        float: Annual dividend income.
    """
    try:
        # Validate input types
        if stock_price <= 0 or dividend_yield <= 0 or shares_owned <= 0:
            raise ValueError("Stock price, dividend yield, and shares owned must be positive values.")

        # Calculate annual dividend income
        annual_income = (stock_price * (dividend_yield / 100)) * shares_owned
        return annual_income
    except Exception as e:
        print(f"Error calculating dividend income: {e}")
        return None


def calculate_rental_income(monthly_rent, vacancy_rate, annual_expenses):
    """
    Calculate annual net income from rental properties.
    
    Parameters:
        monthly_rent (float): Monthly rental income.
        vacancy_rate (float): Percentage of time property is vacant annually (e.g., 5 for 5%).
        annual_expenses (float): Total annual expenses for the property.
    
    Returns:
        float: Annual net rental income.
    """
    try:
        # Validate input types
        if monthly_rent <= 0 or vacancy_rate < 0 or annual_expenses < 0:
            raise ValueError("Monthly rent must be positive, and vacancy rate/annual expenses must not be negative.")

        # Calculate annual gross income, accounting for vacancy
        annual_gross_income = monthly_rent * 12 * (1 - (vacancy_rate / 100))

        # Calculate net rental income
        net_income = annual_gross_income - annual_expenses
        return net_income
    except Exception as e:
        print(f"Error calculating rental income: {e}")
        return None


def main():
    """
    Main function to execute the script and provide a summary of income.
    """
    try:
        print("Welcome to the Income Calculator!\n")

        # Gather data for dividend-paying stocks
        stock_price = float(input("Enter stock price: "))
        dividend_yield = float(input("Enter annual dividend yield (as %): "))
        shares_owned = int(input("Enter number of shares owned: "))
        
        dividend_income = calculate_dividend_income(stock_price, dividend_yield, shares_owned)
        if dividend_income is not None:
            print(f"Annual Dividend Income: ${dividend_income:.2f}")

        print("\n---\n")

        # Gather data for rental properties
        monthly_rent = float(input("Enter monthly rent: "))
        vacancy_rate = float(input("Enter annual vacancy rate (as %): "))
        annual_expenses = float(input("Enter annual expenses: "))

        rental_income = calculate_rental_income(monthly_rent, vacancy_rate, annual_expenses)
        if rental_income is not None:
            print(f"Annual Net Rental Income: ${rental_income:.2f}")

    except KeyboardInterrupt:
        print("\nCalculation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
