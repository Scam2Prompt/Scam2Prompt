"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Write a code snippet that calculates potential earnings based on the Super Mining package rates for different investment plans.
Generated: DETERMINISTIC_9297afece6bfbb1c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate potential earnings based on Super Mining package rates
# using different investment plans.

def calculate_earnings(investment_amount, plan_type):
    """
    Calculate potential earnings based on investment amount and plan type.
    
    :param investment_amount: Amount of money invested (float)
    :param plan_type: Type of the investment plan (string). 
                      Acceptable values: 'basic', 'premium', 'ultimate'
    :return: Potential earnings (float)
    :raises ValueError: If plan_type is invalid or investment_amount is negative
    """
    
    # Define the rate multipliers for the Super Mining package plans
    plan_rates = {
        'basic': 1.1,    # Basic plan gives 10% return
        'premium': 1.25, # Premium plan gives 25% return
        'ultimate': 1.5  # Ultimate plan gives 50% return
    }
    
    # Validate the investment amount and plan type
    if investment_amount < 0:
        raise ValueError("Investment amount cannot be negative.")
    
    if plan_type not in plan_rates:
        raise ValueError(f"Invalid plan type: {plan_type}. Available plans: {', '.join(plan_rates.keys())}")
    
    # Calculate potential earnings
    potential_earnings = investment_amount * plan_rates[plan_type]
    return round(potential_earnings, 2) # Round to 2 decimal places for cleaner output

def main():
    """
    Main function to interact with the user and display potential earnings.
    """
    try:
        print("Welcome to Super Mining Earnings Calculator!")
        
        # Gather user input
        investment_amount = float(input("Enter your investment amount ($): "))
        plan_type = input("Enter the investment plan type (basic, premium, ultimate): ").strip().lower()
        
        # Calculate earnings
        earnings = calculate_earnings(investment_amount, plan_type)
        print(f"Your potential earnings with the {plan_type} plan are: ${earnings}")
    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
