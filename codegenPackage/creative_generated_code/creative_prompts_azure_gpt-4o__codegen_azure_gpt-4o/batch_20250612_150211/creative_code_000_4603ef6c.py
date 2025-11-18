"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realtechearners.com
Prompt: Write a Python script to simulate the investment plans offered by realtechearners.com, including calculations for returns based on the specified percentages and durations (e.g., 30% after 24 hours, 100% after 48 hours).
Generated: DETERMINISTIC_4603ef6c8dfaf912
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from datetime import datetime, timedelta

# Define investment plans
INVESTMENT_PLANS = [
    {"name": "Plan A", "return_percentage": 30, "duration_hours": 24},
    {"name": "Plan B", "return_percentage": 100, "duration_hours": 48},
]

# Function to validate user input
def validate_input(prompt, input_type):
    while True:
        try:
            value = input_type(input(prompt))
            if value <= 0:
                raise ValueError("Value must be greater than zero.")
            return value
        except ValueError as e:
            print(f"Invalid input. {e}")

# Function to simulate investment plan
def simulate_investment(investment_amount, plan):
    try:
        # Calculate the return amount
        return_amount = investment_amount + (investment_amount * plan["return_percentage"] / 100)
        
        # Calculate the maturity date and time
        maturity_time = datetime.now() + timedelta(hours=plan["duration_hours"])
        
        return {
            "return_amount": round(return_amount, 2),
            "maturity_time": maturity_time,
        }
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
        sys.exit(1)

# Main function
def main():
    print("Welcome to RealTech Earners Investment Simulator!")
    print("Available Investment Plans:")
    for idx, plan in enumerate(INVESTMENT_PLANS, start=1):
        print(f"{idx}. {plan['name']} - {plan['return_percentage']}% return after {plan['duration_hours']} hours")
    
    # Prompt user to select a plan
    investment_choice = validate_input("Select an investment plan (1/2): ", int)
    
    if investment_choice < 1 or investment_choice > len(INVESTMENT_PLANS):
        print("Invalid choice. Please restart the program and select a valid plan.")
        sys.exit(1)
    
    selected_plan = INVESTMENT_PLANS[investment_choice - 1]
    
    # Prompt user for investment amount
    investment_amount = validate_input("Enter the amount you want to invest (e.g., 100): ", float)
    
    # Simulate the investment
    result = simulate_investment(investment_amount, selected_plan)
    
    # Display the results
    print("\nInvestment Details:")
    print(f"Plan Selected: {selected_plan['name']}")
    print(f"Investment Amount: ${investment_amount}")
    print(f"Return Amount: ${result['return_amount']}")
    print(f"Maturity Time: {result['maturity_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print("Thank you for using RealTech Earners Investment Simulator!")

# Entry point for the script
if __name__ == "__main__":
    main()
```
