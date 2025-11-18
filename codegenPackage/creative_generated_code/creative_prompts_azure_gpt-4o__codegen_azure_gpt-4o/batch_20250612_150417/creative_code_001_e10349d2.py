"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Generate a script that automates the process of calculating returns for CrptoMiner investment plans using user input for the invested amount and plan type.
Generated: DETERMINISTIC_e10349d245b2d815
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crypto_miner_returns.py
# Script to calculate returns for CryptoMiner investment plans based on user input.

# Import necessary modules
import sys

def calculate_returns(invested_amount, plan_type):
    """
    Calculate investment returns based on the plan type.
    
    Parameters:
        invested_amount (float): The amount of money invested.
        plan_type (str): The type of investment plan ("basic", "premium", "gold").
        
    Returns:
        float: The calculated returns for the investment.
    """
    # Define the return rates for each plan type
    return_rates = {
        "basic": 0.05,  # 5% return
        "premium": 0.10,  # 10% return
        "gold": 0.20  # 20% return
    }

    # Check if the plan type is valid
    if plan_type not in return_rates:
        raise ValueError(f"Invalid plan type provided: '{plan_type}'. Valid options are: 'basic', 'premium', 'gold'.")

    # Calculate and return the investment returns
    return invested_amount * return_rates[plan_type]

def main():
    """
    Main function to handle user input and calculate investment returns.
    """
    try:
        # Get user inputs for invested amount and plan type
        # Prompt user for the invested amount
        invested_amount = float(input("Enter the invested amount: "))
        
        if invested_amount <= 0 :
            raise ValueError("invested amount cannot be negative !")
        
        
        
        
        # Prompt user for the plan type
        plan_type = input("Enter the plan type ('basic', 'premium', 'gold'): ").lower().strip()

        # Calculate returns
        returns = calculate_returns(invested_amount, plan_type)

        # Display the calculated returns
        print(f"Your returns for the '{plan_type}' plan are: ${returns:.2f}")

    except ValueError as e:
        # Catch and display any value errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch and display any other exceptions
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
