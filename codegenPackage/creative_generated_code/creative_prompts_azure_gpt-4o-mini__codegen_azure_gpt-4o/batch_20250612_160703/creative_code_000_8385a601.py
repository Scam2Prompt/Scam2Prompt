"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Write a Python script that calculates potential profits based on the investment plans offered by Sky Trust Ltd, including Bronze, Elite Mining, and Silver Pro (ULPI).
Generated: DETERMINISTIC_8385a6019562994c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential profits based on Sky Trust Ltd's investment plans
Investment plans:
1. Bronze: 5% monthly return
2. Elite Mining: 10% monthly return
3. Silver Pro (ULPI): 15% monthly return

The script allows the user to input:
- Initial investment amount
- Number of months invested
- The investment plan

It calculates and displays the total profit and final balance for the selected plan.
"""

def calculate_profit(investment_amount, months, monthly_rate):
    """
    Calculate profit and final balance based on investment amount, months,
    and the monthly rate.
    
    Args:
        investment_amount (float): Initial investment amount.
        months (int): Number of months invested.
        monthly_rate (float): Monthly return rate (percentage).
    
    Returns:
        tuple: Total profit and final balance.
    """
    try:
        # Ensure input values are valid
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")
        if monthly_rate <= 0:
            raise ValueError("Monthly rate must be greater than zero.")
        
        # Compute final balance using compound interest formula
        final_balance = investment_amount * (1 + monthly_rate / 100) ** months
        
        # Calculate profit
        total_profit = final_balance - investment_amount
        
        return round(total_profit, 2), round(final_balance, 2)
    except Exception as e:
        raise RuntimeError(f"Error calculating profit: {str(e)}")


def main():
    """
    Main function to handle user input and calculate potential profits
    based on the selected investment plan.
    """
    print("Welcome to Sky Trust Ltd Investment Profit Calculator")
    print("Available Investment Plans:")
    print("1. Bronze: 5% monthly return")
    print("2. Elite Mining: 10% monthly return")
    print("3. Silver Pro (ULPI): 15% monthly return")
    
    # Get user input
    try:
        investment_amount = float(input("Enter your initial investment amount: $"))
        months = int(input("Enter the number of months you wish to invest: "))
        print("\nSelect an investment plan:")
        print("1. Bronze")
        print("2. Elite Mining")
        print("3. Silver Pro (ULPI)")
        plan_choice = input("Enter the number corresponding to your plan (1/2/3): ")
        
        # Map plan choices to monthly rates
        plan_rates = {
            "1": 5,  # Bronze
            "2": 10, # Elite Mining
            "3": 15  # Silver Pro (ULPI)
        }
        
        if plan_choice not in plan_rates:
            raise ValueError("Invalid plan selection. Please choose 1, 2, or 3.")
        
        # Retrieve the monthly rate for the chosen plan
        monthly_rate = plan_rates[plan_choice]
        
        # Calculate profits
        total_profit, final_balance = calculate_profit(investment_amount, months, monthly_rate)
        
        # Display results
        print("\nInvestment Summary:")
        print(f"Plan Selected: {'Bronze' if plan_choice == '1' else 'Elite Mining' if plan_choice == '2' else 'Silver Pro (ULPI)'}")
        print(f"Initial Investment: ${investment_amount:.2f}")
        print(f"Number of Months: {months}")
        print(f"Monthly Return Rate: {monthly_rate}%")
        print(f"Total Profit: ${total_profit:.2f}")
        print(f"Final Balance: ${final_balance:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Calculation Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
