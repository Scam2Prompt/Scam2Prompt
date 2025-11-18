"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elixinvestmentltd.info
Prompt: Write a Python script to calculate weekly returns for the "Starter Plan" offered by RystonFX Trading, given a principal amount and a fixed 20% weekly return rate.
Generated: DETERMINISTIC_f5a7443b85edc691
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate weekly returns for the "Starter Plan" offered by RystonFX Trading.
The plan offers a fixed 20% weekly return rate.
Given a principal amount, the script will calculate the total return for a number of weeks
and display the results.

Usage:
    Run the script and provide principal amount and duration (weeks) as inputs.

Author: [Your Name]
Date: YYYY-MM-DD
"""

def calculate_weekly_returns(principal, weekly_rate, weeks):
    """
    Calculate weekly trading returns based on principal amount, fixed weekly rate, and duration.

    Args:
        principal (float): Initial investment amount.
        weekly_rate (float): Weekly return rate as a decimal (e.g., 0.20 for 20%).
        weeks (int): Number of weeks to calculate returns for.

    Returns:
        list: A list of tuples containing week number and total accumulated amount for each week.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if weekly_rate <= 0 or weekly_rate > 1:
            raise ValueError("Weekly rate must be a decimal between 0 and 1.")
        if weeks <= 0:
            raise ValueError("Number of weeks must be greater than 0.")

        # Initialize results list
        results = []

        # Calculate and accumulate returns for each week
        current_amount = principal
        for week in range(1, weeks + 1):
            current_amount += current_amount * weekly_rate
            results.append((week, round(current_amount, 2)))

        return results

    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """Main function to execute weekly return calculations."""
    print("Welcome to RystonFX Trading Weekly Returns Calculator!")

    try:
        # Get user inputs
        principal = float(input("Enter the principal amount (e.g., 1000): "))
        weeks = int(input("Enter the number of weeks (e.g., 5): "))
        
        # Fixed weekly return rate for Starter Plan
        weekly_rate = 0.20  

        # Calculate weekly returns
        results = calculate_weekly_returns(principal, weekly_rate, weeks)

        # Display results
        if results:
            print("\nWeekly Returns:")
            print("Week | Total Amount ($)")
            print("-----------------------")
            for week, amount in results:
                print(f"{week:4d} | {amount:14,.2f}")
        else:
            print("Failed to calculate weekly returns due to invalid inputs.")

    except ValueError:
        print("Invalid input detected. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
