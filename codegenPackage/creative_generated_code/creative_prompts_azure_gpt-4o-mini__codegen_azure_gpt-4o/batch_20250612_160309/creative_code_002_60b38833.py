"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: Generate a code snippet that calculates potential profits based on the investment plans offered by MaxProfit, such as the Bronze, Silver, and Gold plans.
Generated: DETERMINISTIC_60b388337a03b66e
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Define constants for investment plan rates
BRONZE_RATE = 0.05  # Bronze plan offers 5% monthly profit
SILVER_RATE = 0.07  # Silver plan offers 7% monthly profit
GOLD_RATE = 0.10    # Gold plan offers 10% monthly profit

def calculate_profit(investment_amount, months, plan):
    """
    Calculate potential profits based on investment amount, plan rate, and duration.

    :param investment_amount: The amount invested (float)
    :param months: Number of months the investment will be held (int)
    :param plan: Investment plan type ('Bronze', 'Silver', or 'Gold') (str)
    :return: Total profit after the specified duration (float)
    :raises ValueError: If an invalid plan is provided or input is invalid
    """
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than 0.")
    if months <= 0:
        raise ValueError("Number of months must be greater than 0.")
    
    # Determine the rate based on the investment plan
    if plan == 'Bronze':
        rate = BRONZE_RATE
    elif plan == 'Silver':
        rate = SILVER_RATE
    elif plan == 'Gold':
        rate = GOLD_RATE
    else:
        raise ValueError("Invalid plan type. Choose 'Bronze', 'Silver', or 'Gold'.")
    
    # Calculate profit
    profit = investment_amount * rate * months
    return profit

def main():
    """
    Main function to get user input and calculate profit.
    """
    try:
        # Prompt user for input
        investment_amount = float(input("Enter the investment amount ($): "))
        months = int(input("Enter the number of months: "))
        plan = input("Enter the plan type ('Bronze', 'Silver', 'Gold'): ").capitalize()
        
        # Calculate and display profit
        total_profit = calculate_profit(investment_amount, months, plan)
        print(f"Potential profit after {months} months with the {plan} plan: ${total_profit:.2f}")
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unforeseen errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
