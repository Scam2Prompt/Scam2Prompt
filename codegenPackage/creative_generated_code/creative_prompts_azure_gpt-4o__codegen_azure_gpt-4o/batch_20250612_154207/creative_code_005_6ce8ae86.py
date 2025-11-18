"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qbt.finance
Prompt: Develop a Python script to calculate the estimated monthly profit for a user on Qubit Finance based on their supply and borrow balances and APR rates.
Generated: DETERMINISTIC_6ce8ae8616f13098
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_monthly_profit(supply_balance, borrow_balance, supply_apr, borrow_apr):
    """
    Calculates the estimated monthly profit based on supply and borrow balances and APR.
    
    Parameters:
    - supply_balance (float): The amount of assets supplied by the user.
    - borrow_balance (float): The amount of assets borrowed by the user.
    - supply_apr (float): Annual Percentage Rate (APR) for supplied assets (in percentage).
    - borrow_apr (float): Annual Percentage Rate (APR) for borrowed assets (in percentage).

    Returns:
    - float: Estimated monthly profit.
    """
    try:
        # Validate inputs
        if supply_balance < 0 or borrow_balance < 0 or supply_apr < 0 or borrow_apr < 0:
            raise ValueError("All input values must be non-negative.")

        # Convert APR from percentage to decimal
        supply_apr_decimal = supply_apr / 100
        borrow_apr_decimal = borrow_apr / 100

        # Calculate annual profit/loss
        annual_profit = (supply_balance * supply_apr_decimal) - (borrow_balance * borrow_apr_decimal)

        # Convert annual profit to monthly profit
        monthly_profit = annual_profit / 12

        return monthly_profit

    except TypeError:
        raise TypeError("All inputs must be numbers.")

    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")


def main():
    """
    Main function to gather user inputs, calculate monthly profit, and display the result.
    """
    try:
        print("Welcome to Qubit Finance Profit Calculator")
        
        # Gather user inputs
        supply_balance = float(input("Enter your supply balance: "))
        borrow_balance = float(input("Enter your borrow balance: "))
        supply_apr = float(input("Enter the supply APR (in %): "))
        borrow_apr = float(input("Enter the borrow APR (in %): "))

        # Calculate monthly profit
        monthly_profit = calculate_monthly_profit(supply_balance, borrow_balance, supply_apr, borrow_apr)

        # Display the result
        print(f"\nEstimated Monthly Profit: ${monthly_profit:.2f}")
        
    except ValueError:
        print("Invalid input: Please ensure all values are numbers and non-negative.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
