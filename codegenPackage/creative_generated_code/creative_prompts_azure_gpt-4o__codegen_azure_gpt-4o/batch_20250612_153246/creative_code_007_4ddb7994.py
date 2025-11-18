"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agdbank.com.br
Prompt: Create a script to calculate the cost of agricultural financing for producers, incorporating AGDbank's focus on advantageous and accessible conditions.
Generated: DETERMINISTIC_4ddb799467808c09
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_input(prompt: str, cast_to: type):
    """
    Helper function to safely get user input and cast it to the required type.
    Args:
        prompt (str): Input prompt for the user.
        cast_to (type): Type to cast the input value to.
    Returns:
        casted_value (type): User input casted to the specified type.
    """
    while True:
        try:
            value = cast_to(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {cast_to.__name__}.")

def calculate_financing_cost(principal: float, rate: float, years: int) -> float:
    """
    Calculates the total cost of agricultural financing.
    Args:
        principal (float): Loan amount in dollars.
        rate (float): Annual interest rate as a percentage.
        years (int): Loan term in years.
    Returns:
        total_cost (float): Total cost including principal and interest.
    """
    # Simple interest formula: Total Cost = Principal + (Principal * Rate * Years)
    total_cost = principal + (principal * (rate / 100) * years)
    return total_cost

def main():
    """
    Main function to interact with users and calculate agricultural financing cost.
    """
    print("Welcome to AGDbank Agricultural Financing Calculator!")
    
    # Step 1: Gather input from user
    print("\nPlease provide the following details:")
    principal = get_input("Enter the loan principal amount (in USD): ", float)
    rate = get_input("Enter the annual interest rate (in %): ", float)
    years = get_input("Enter the loan term (in years): ", int)
    
    # Step 2: Validate input values
    if principal <= 0 or rate <= 0 or years <= 0:
        print("Error: All inputs must be positive values.")
        sys.exit(1)
    
    # Step 3: Perform calculation
    total_cost = calculate_financing_cost(principal, rate, years)
    
    # Step 4: Display the result
    print("\nAgricultural Financing Details:")
    print(f"Principal Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {rate:.2f}%")
    print(f"Loan Term: {years} year(s)")
    print(f"Total Cost (Principal + Interest): ${total_cost:,.2f}")
    print("\nThank you for using AGDbank's Financing Calculator!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
