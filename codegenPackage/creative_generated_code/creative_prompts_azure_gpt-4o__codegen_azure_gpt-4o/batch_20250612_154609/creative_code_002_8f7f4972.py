"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Generate code to calculate ROI for investment plans like Welstrade's "Basic Plan," "Silver Plan," and "Gold Plan," using the specific ROI percentages and durations provided.
Generated: DETERMINISTIC_8f7f4972c150d84f
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ROI Calculator for investment plans
# Author: Your Name
# Date: YYYY-MM-DD

# Import necessary libraries
import sys

def calculate_roi(principal, rate, duration):
    """
    Calculate the Return on Investment (ROI).
    
    Parameters:
        principal (float): The amount of money invested.
        rate (float): ROI rate in percentage (e.g., 5 for 5%).
        duration (int): Duration of the investment in months.
    
    Returns:
        float: Total amount after applying ROI for the given duration.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if rate <= 0:
            raise ValueError("Rate must be greater than zero.")
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")
        
        # Calculate ROI
        roi = principal * (rate / 100) * (duration / 12)  # Convert duration from months to years
        total_amount = principal + roi
        return total_amount
    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    """
    Main function to calculate ROI for predefined investment plans.
    """
    # Define investment plans
    investment_plans = {
        "Basic Plan": {"rate": 5, "duration": 12},
        "Silver Plan": {"rate": 7, "duration": 24},
        "Gold Plan": {"rate": 10, "duration": 36}
    }

    print("Welcome to the ROI Calculator!")
    
    try:
        # Get user input for principal amount
        principal = float(input("Enter the principal amount you want to invest: $"))

        print("\nAvailable Investment Plans:")
        for plan, details in investment_plans.items():
            print(f"{plan}: {details['rate']}% ROI for {details['duration']} months")

        # Get user input for plan selection
        selected_plan = input("\nEnter the name of the investment plan (e.g., 'Gold Plan'): ")

        if selected_plan not in investment_plans:
            raise ValueError("Invalid plan selected. Please choose a valid investment plan.")

        # Retrieve selected plan details
        plan_details = investment_plans[selected_plan]
        rate = plan_details["rate"]
        duration = plan_details["duration"]

        # Calculate and display ROI
        total_amount = calculate_roi(principal, rate, duration)
        print(f"\nFor the {selected_plan}:")
        print(f"Principal Amount: ${principal:.2f}")
        print(f"ROI Rate: {rate}%")
        print(f"Duration: {duration} months")
        print(f"Total Amount after ROI: ${total_amount:.2f}")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
