"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxonex.com
Prompt: Write a script to calculate the APY earned on cash and positions held in Moxonex prediction markets over a specified period.
Generated: DETERMINISTIC_6047f7942e7d7343
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_apy(initial_balance, final_balance, start_date, end_date):
    """
    Calculate the Annual Percentage Yield (APY) based on the change in balance
    over a specified period.

    Args:
        initial_balance (float): The starting balance of cash and positions.
        final_balance (float): The ending balance of cash and positions.
        start_date (str): The start date in the format 'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
        float: The APY as a percentage.
    """
    try:
        # Parse dates
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        
        # Calculate the number of days between the start and end dates
        days_held = (end_date - start_date).days
        if days_held <= 0:
            raise ValueError("End date must be after start date.")
        
        # Ensure inputs are valid
        if initial_balance <= 0 or final_balance <= 0:
            raise ValueError("Balances must be greater than 0.")
        
        # Calculate the rate of return
        rate_of_return = final_balance / initial_balance

        # APY formula: ((final_balance / initial_balance)^(365/days_held) - 1) * 100
        apy = (pow(rate_of_return, 365 / days_held) - 1) * 100

        return apy

    except ValueError as ve:
        # Handle invalid input errors
        print(f"ValueError: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # Example usage
    try:
        initial_balance = float(input("Enter initial balance: "))
        final_balance = float(input("Enter final balance: "))
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        apy = calculate_apy(initial_balance, final_balance, start_date, end_date)
        if apy is not None:
            print(f"The APY earned is: {apy:.2f}%")
    except Exception:
        print("An error occurred while calculating the APY.")
```
