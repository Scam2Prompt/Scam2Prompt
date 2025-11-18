"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fund-x.link
Prompt: Create a program that calculates the impact of high bonuses offered by FUND-X LTD on initial investments and potential returns.
Generated: DETERMINISTIC_ba06abce54f4e746
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Fund-X Bonus Impact Calculator
Description: This program calculates the impact of high bonuses offered by FUND-X LTD
             on initial investments and potential returns.
Author: Your Name
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_bonus_adjusted_return(initial_investment, annual_growth_rate, years, bonus_percentage):
    """
    Calculate the adjusted return based on the bonus offered.

    Parameters:
        initial_investment (float): The initial amount invested.
        annual_growth_rate (float): The annual growth rate in percentage.
        years (int): The investment duration in years.
        bonus_percentage (float): The bonus percentage offered by FUND-X LTD.

    Returns:
        dict: A dictionary containing the original return, bonus amount, 
              and adjusted return.
    """
    try:
        # Ensure all inputs are valid
        if initial_investment <= 0 or annual_growth_rate <= 0 or years <= 0 or bonus_percentage < 0:
            raise ValueError("Inputs must be positive numbers. Bonus percentage can be zero.")

        # Calculate original return without the bonus
        original_return = initial_investment * ((1 + annual_growth_rate / 100) ** years)

        # Calculate bonus amount based on initial investment
        bonus_amount = initial_investment * (bonus_percentage / 100)

        # Calculate adjusted return including the bonus
        adjusted_return = original_return + bonus_amount

        # Return the results in a dictionary
        return {
            "original_return": round(original_return, 2),
            "bonus_amount": round(bonus_amount, 2),
            "adjusted_return": round(adjusted_return, 2)
        }

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        return None

def main():
    """
    Main function to drive the program.
    """
    try:
        print("Welcome to the FUND-X Bonus Impact Calculator!")

        # Input collection from the user
        initial_investment = float(input("Enter initial investment amount: "))
        annual_growth_rate = float(input("Enter annual growth rate (in %): "))
        years = int(input("Enter investment duration (in years): "))
        bonus_percentage = float(input("Enter bonus percentage offered by FUND-X LTD: "))

        # Perform calculation
        results = calculate_bonus_adjusted_return(initial_investment, annual_growth_rate, years, bonus_percentage)

        # Display results if calculation was successful
        if results:
            print("\n--- Calculation Results ---")
            print(f"Original Return: ${results['original_return']}")
            print(f"Bonus Amount: ${results['bonus_amount']}")
            print(f"Adjusted Return: ${results['adjusted_return']}")
        else:
            print("Failed to perform calculation due to input error.")

    except ValueError:
        # Handle invalid inputs
        print("Error: Please enter valid numerical inputs.")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the program
    main()
```
