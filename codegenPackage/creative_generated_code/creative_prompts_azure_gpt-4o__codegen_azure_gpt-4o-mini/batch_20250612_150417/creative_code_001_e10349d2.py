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
# CryptoMiner Investment Return Calculator

def calculate_return(investment_amount, plan_type):
    """
    Calculate the expected return based on the investment amount and plan type.

    Parameters:
    investment_amount (float): The amount of money invested in the plan.
    plan_type (str): The type of investment plan (e.g., 'basic', 'premium', 'pro').

    Returns:
    float: The expected return from the investment.
    
    Raises:
    ValueError: If the plan type is not recognized or if the investment amount is negative.
    """
    # Define the return rates for each plan type
    plan_rates = {
        'basic': 0.1,   # 10% return
        'premium': 0.15,  # 15% return
        'pro': 0.2      # 20% return
    }

    # Error handling for invalid investment amount
    if investment_amount < 0:
        raise ValueError("Investment amount cannot be negative.")

    # Error handling for invalid plan type
    if plan_type not in plan_rates:
        raise ValueError(f"Invalid plan type. Available types are: {', '.join(plan_rates.keys())}")

    # Calculate expected return
    return investment_amount * plan_rates[plan_type]

def main():
    # Main function to run the investment return calculator
    try:
        # Get user input for investment amount
        investment_amount = float(input("Enter the investment amount: "))
        # Get user input for the plan type
        plan_type = input("Enter the investment plan type (basic, premium, pro): ").strip().lower()

        # Calculate the return
        expected_return = calculate_return(investment_amount, plan_type)

        # Output the expected return
        print(f"Expected return for your investment: ${expected_return:.2f}")

    except ValueError as e:
        # Handle errors in a user-friendly manner
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for any unforeseen errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
