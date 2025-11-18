"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camp-dmb.pages.dev
Prompt: Provide a Python example for calculating the profit margin for the "Top Earners Plan," which offers a 30% return after 12 days, using user-defined deposit amounts.
Generated: DETERMINISTIC_fb80d58c65eba71e
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_profit_margin(deposit_amount: float) -> float:
    """
    Calculate the profit margin for the "Top Earners Plan."

    Args:
        deposit_amount (float): The amount of money deposited by the user.

    Returns:
        float: The profit margin achieved after 12 days.
    
    Raises:
        ValueError: If the deposit_amount is negative.
    """
    # Validate the input
    if deposit_amount < 0:
        raise ValueError("Deposit amount must be a non-negative value.")

    # Define the return rate for the Top Earners Plan
    return_rate = 0.30  # 30% return

    # Calculate the total profit gained after 12 days
    profit = deposit_amount * return_rate

    # Calculate the total amount after profit
    total_amount = deposit_amount + profit

    # Calculate the profit margin
    profit_margin = profit / total_amount

    return profit_margin


def main():
    """
    Main function to run the profit margin calculation.
    """
    try:
        # User input for deposit amount
        deposit = float(input("Enter the deposit amount for the Top Earners Plan: "))
        
        # Calculate profit margin
        margin = calculate_profit_margin(deposit)
        
        # Display the result
        print(f"The profit margin for a deposit of {deposit:.2f} is: {margin:.2%}")
    
    except ValueError as e:
        print(f"Error: {e}")  # Handle input errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle unexpected errors


if __name__ == "__main__":
    main()
```
