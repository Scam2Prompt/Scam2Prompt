"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Write a script to calculate the liquidity percentage for a presale, ensuring that less than 51% of raised funds are allocated to liquidity, as described in the Baby Maga project.
Generated: DETERMINISTIC_19babb37067cd10e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# liquidity_calculator.py

# Import necessary modules
import sys

def calculate_liquidity_percentage(raised_funds, liquidity_allocation):
    """
    Calculate the liquidity percentage for a presale.

    Parameters:
    raised_funds (float): Total funds raised during the presale.
    liquidity_allocation (float): Amount of funds allocated to liquidity.

    Returns:
    float: Liquidity percentage of total raised funds.
    """
    if raised_funds <= 0:
        raise ValueError("Raised funds must be greater than zero.")
    if liquidity_allocation < 0:
        raise ValueError("Liquidity allocation cannot be negative.")
    
    liquidity_percentage = (liquidity_allocation / raised_funds) * 100
    return liquidity_percentage


def main():
    """
    Main function to execute the liquidity percentage calculation.
    Takes user input for raised funds and liquidity allocation.
    Ensures liquidity allocation is less than 51% of raised funds.
    """
    try:
        # Prompt user for input
        raised_funds = float(input("Enter the total raised funds ($): "))
        liquidity_allocation = float(input("Enter the liquidity allocation ($): "))

        # Calculate liquidity percentage
        liquidity_percentage = calculate_liquidity_percentage(raised_funds, liquidity_allocation)

        # Check if liquidity allocation exceeds 51% of raised funds
        if liquidity_percentage >= 51:
            print("Error: Liquidity allocation exceeds 51% of raised funds. Please adjust the allocation.")
        else:
            print(f"Liquidity Percentage: {liquidity_percentage:.2f}%")
            print("Liquidity allocation is within the permissible range.")

    except ValueError as e:
        # Handle invalid numeric inputs
        print(f"Input Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```
