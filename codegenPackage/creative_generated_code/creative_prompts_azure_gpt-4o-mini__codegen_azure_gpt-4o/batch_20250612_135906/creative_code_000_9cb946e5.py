"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liberty-miners.ltd
Prompt: Generate a Python script that calculates potential profits from the different trading plans offered by liberty-miners.ltd, including Regular, Standard, Veteran, and Premium Trading.
Generated: DETERMINISTIC_9cb946e5b3f1a3c4
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to calculate potential profits for different trading plans
offered by liberty-miners.ltd: Regular, Standard, Veteran, and Premium Trading.

Assumptions:
1. Each trading plan has a fixed ROI (Return on Investment) percentage.
2. The user provides the invested amount and selects a trading plan.
3. Proper error handling is implemented for invalid inputs.
"""

def calculate_profit(investment_amount, roi_percentage):
    """
    Calculates the potential profit based on the investment amount and ROI percentage.

    Parameters:
        investment_amount (float): The amount invested.
        roi_percentage (float): The ROI percentage offered by the trading plan.

    Returns:
        float: The calculated profit.
    """
    return investment_amount * (roi_percentage / 100)

def display_trading_plans():
    """
    Displays the available trading plans and their respective ROI percentages.
    """
    print("\nAvailable Trading Plans:")
    print("1. Regular Trading - ROI: 5%")
    print("2. Standard Trading - ROI: 10%")
    print("3. Veteran Trading - ROI: 15%")
    print("4. Premium Trading - ROI: 20%")

def get_roi_percentage(plan_choice):
    """
    Returns the ROI percentage based on the user's chosen trading plan.

    Parameters:
        plan_choice (int): The trading plan selected by the user.

    Returns:
        float: The ROI percentage for the selected plan.
    """
    roi_map = {
        1: 5,   # Regular Trading
        2: 10,  # Standard Trading
        3: 15,  # Veteran Trading
        4: 20   # Premium Trading
    }
    return roi_map.get(plan_choice, None)  # Return None if plan_choice is invalid

def main():
    """
    Main function to handle user input, calculate profit, and display the results.
    """
    print("Welcome to Liberty Miners Trading Profit Calculator!")
    display_trading_plans()

    try:
        # Get user's choice of trading plan
        plan_choice = int(input("\nEnter the number corresponding to your trading plan (1-4): "))
        
        # Validate user's plan choice
        roi_percentage = get_roi_percentage(plan_choice)
        if roi_percentage is None:
            print("Error: Invalid trading plan selected. Please enter a number between 1 and 4.")
            return
        
        # Get investment amount from the user
        investment_amount = float(input("Enter your investment amount (e.g., 1000): "))
        if investment_amount <= 0:
            print("Error: Investment amount must be greater than zero.")
            return

        # Calculate potential profit
        potential_profit = calculate_profit(investment_amount, roi_percentage)

        # Display results
        print("\n--- Calculation Results ---")
        print(f"Trading Plan: {plan_choice}")
        print(f"ROI Percentage: {roi_percentage}%")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Potential Profit: ${potential_profit:.2f}")
        print("---------------------------")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
```
