"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by swiftgoldcoin.com, including plans with 20%, 40%, and 60% returns.
Generated: DETERMINISTIC_984e347a36c46094
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Returns Calculator

This script calculates potential returns based on the investment plans offered by SwiftGoldCoin.
The plans include:
- 20% return on investment
- 40% return on investment
- 60% return on investment

Users can input their investment amount, and the script will display the returns for each plan.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Function to calculate returns based on percentage
def calculate_returns(investment_amount, return_percentage):
    """
    Calculate the return based on the investment amount and percentage.

    Args:
        investment_amount (float): The amount invested.
        return_percentage (float): The return percentage.

    Returns:
        float: The potential return.
    """
    try:
        # Ensure inputs are valid
        if investment_amount < 0 or return_percentage < 0:
            raise ValueError("Investment amount and return percentage must be positive.")
        # Calculate the return
        return investment_amount * (return_percentage / 100)
    except TypeError:
        raise TypeError("Invalid input type. Expected numbers for investment amount and return percentage.")

# Main function
def main():
    """
    Entry point for the script. Takes user input and calculates returns for different plans.
    """
    print("Welcome to the SwiftGoldCoin Investment Returns Calculator!")
    
    try:
        # Prompt the user for the investment amount
        investment_amount = float(input("Enter your investment amount (in USD): "))
        if investment_amount <= 0:
            print("Investment amount must be greater than zero.")
            return
        
        # Define the return percentages for each plan
        plans = {
            "20% Plan": 20,
            "40% Plan": 40,
            "60% Plan": 60
        }
        
        # Calculate and display the returns for each plan
        print("\nPotential returns based on your investment:")
        for plan_name, return_percentage in plans.items():
            potential_return = calculate_returns(investment_amount, return_percentage)
            print(f"{plan_name}: ${potential_return:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a valid numeric investment amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
