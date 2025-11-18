"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microapexmarket.com
Prompt: Create a program to calculate potential profits based on trading plans (e.g., Basic, Silver, Gold, Platinum) offered by Microapexmarket.
Generated: DETERMINISTIC_6da240348d0b9353
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate potential profits based on trading plans offered by Microapexmarket.
Each plan has a specific percentage return based on the initial investment.
Plans:
- Basic: 5% return
- Silver: 10% return
- Gold: 15% return
- Platinum: 20% return

The user provides:
1. The initial investment amount.
2. The chosen trading plan.

The program calculates and displays the potential profit and total amount after profit.
"""

def calculate_profit(investment, plan):
    """
    Calculate potential profit based on the trading plan.
    
    Args:
        investment (float): Initial investment amount.
        plan (str): Trading plan (Basic, Silver, Gold, Platinum).
    
    Returns:
        tuple: (profit, total_amount_after_profit)
    """
    # Define the profit percentages for each plan
    profit_percentages = {
        "Basic": 0.05,   # 5% return
        "Silver": 0.10,  # 10% return
        "Gold": 0.15,    # 15% return
        "Platinum": 0.20 # 20% return
    }
    
    # Check if the provided plan is valid
    if plan not in profit_percentages:
        raise ValueError("Invalid trading plan. Choose from: Basic, Silver, Gold, Platinum.")
    
    # Calculate profit and total amount
    profit = investment * profit_percentages[plan]
    total_amount_after_profit = investment + profit
    
    return profit, total_amount_after_profit

def main():
    """
    Main function to interact with the user and calculate potential profits.
    """
    print("Welcome to Microapexmarket Profit Calculator!")
    
    try:
        # Get user input for investment amount
        investment = float(input("Enter your initial investment amount: $"))
        if investment <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Get user input for trading plan
        print("Available Trading Plans: Basic, Silver, Gold, Platinum")
        plan = input("Enter your chosen trading plan: ").capitalize()
        
        # Calculate profit and total amount
        profit, total_amount_after_profit = calculate_profit(investment, plan)
        
        # Display the results
        print(f"\nResults for the {plan} plan:")
        print(f"Initial Investment: ${investment:.2f}")
        print(f"Potential Profit: ${profit:.2f}")
        print(f"Total Amount After Profit: ${total_amount_after_profit:.2f}")
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the program
    main()
```
