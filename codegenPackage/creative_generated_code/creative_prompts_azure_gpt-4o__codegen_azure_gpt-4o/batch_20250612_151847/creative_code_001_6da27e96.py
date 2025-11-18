"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Generate code to calculate Bitcoin earnings based on the earning rates provided by SuperMining's investment plans (e.g., Micro, Mega, Giga, Tera), and display daily and minute-based profits.
Generated: DETERMINISTIC_6da27e96a8c7e753
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_earnings(plan, initial_investment):
    """
    Calculate daily and per-minute Bitcoin earnings based on the investment plan.
    
    Args:
        plan (str): The investment plan (e.g., 'Micro', 'Mega', 'Giga', 'Tera').
        initial_investment (float): The initial amount of Bitcoin invested.
    
    Returns:
        dict: A dictionary containing daily and per-minute earnings.
    """
    # Define earning rates for each plan
    earning_rates = {
        'Micro': 0.0015,  # 0.15% daily earning rate
        'Mega': 0.0030,  # 0.30% daily earning rate
        'Giga': 0.0050,  # 0.50% daily earning rate
        'Tera': 0.0080   # 0.80% daily earning rate
    }
    
    # Validate that the plan exists
    if plan not in earning_rates:
        raise ValueError(f"Invalid plan '{plan}'. Valid plans are: {', '.join(earning_rates.keys())}")
    
    # Ensure the initial investment is positive
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than 0.")
    
    # Calculate daily earnings
    daily_earning_rate = earning_rates[plan]
    daily_earnings = initial_investment * daily_earning_rate
    
    # Calculate per-minute earnings (assuming 1440 minutes in a day)
    minute_earnings = daily_earnings / 1440
    
    return {
        'daily_earnings': daily_earnings,
        'minute_earnings': minute_earnings
    }


def display_earnings():
    """
    Prompt the user for inputs and display Bitcoin earnings based on the selected plan.
    """
    try:
        print("Welcome to SuperMining Earnings Calculator!")
        
        # Prompt for the investment plan
        plan = input("Enter your investment plan (Micro, Mega, Giga, Tera): ").strip().capitalize()
        
        # Prompt for the initial investment amount
        initial_investment = float(input("Enter your initial Bitcoin investment amount: "))
        
        # Calculate earnings
        earnings = calculate_earnings(plan, initial_investment)
        
        # Display results
        print("\nEarnings Summary:")
        print(f"Daily Earnings: {earnings['daily_earnings']:.8f} BTC")
        print(f"Per-Minute Earnings: {earnings['minute_earnings']:.8f} BTC")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    display_earnings()
```
