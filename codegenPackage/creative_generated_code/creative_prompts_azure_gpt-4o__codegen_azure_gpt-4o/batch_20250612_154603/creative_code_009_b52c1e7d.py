"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainecotrust.cc
Prompt: Create a script to calculate and display the ROI for each investment plan offered by mainecotrust.cc, including daily profit percentages.
Generated: DETERMINISTIC_b52c1e7d311fd8d9
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_roi(investment_amount, daily_profit_percentage, investment_duration_days):
    """
    Calculate the ROI (Return on Investment) for a given investment plan.

    Parameters:
        investment_amount (float): The initial investment amount.
        daily_profit_percentage (float): The daily profit as a percentage.
        investment_duration_days (int): The duration of the investment in days.

    Returns:
        float: The total ROI for the investment plan.
    """
    try:
        # Convert percentage to decimal
        daily_profit_rate = daily_profit_percentage / 100
        
        # Calculate total profit
        total_profit = investment_amount * daily_profit_rate * investment_duration_days
        
        # Calculate ROI (returning investment + profit)
        roi = investment_amount + total_profit
        
        return roi

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while calculating ROI: {e}")
        sys.exit(1)

def display_investment_rois(investment_plans):
    """
    Display ROI for each investment plan.

    Parameters:
        investment_plans (list): A list of dictionaries containing investment plans.
                                 Each plan should have keys 'name', 'amount', 'daily_profit_percentage', 
                                 and 'duration_days'.
    """
    print(f"{'Investment Plan':<20}{'ROI':<15}")
    print("-" * 35)

    for plan in investment_plans:
        try:
            # Extract details of the investment plan
            name = plan['name']
            amount = plan['amount']
            daily_profit_percentage = plan['daily_profit_percentage']
            duration_days = plan['duration_days']
            
            # Calculate ROI
            roi = calculate_roi(amount, daily_profit_percentage, duration_days)
            
            # Display results
            print(f"{name:<20}${roi:<15.2f}")
        
        except KeyError as e:
            # Handle missing keys in the investment plan dictionary
            print(f"Missing key in investment plan: {e}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred while processing investment plan '{name}': {e}")

# Example usage
if __name__ == "__main__":
    # Define investment plans
    investment_plans = [
        {'name': 'Starter Plan', 'amount': 100, 'daily_profit_percentage': 2.5, 'duration_days': 30},
        {'name': 'Premium Plan', 'amount': 500, 'daily_profit_percentage': 3.0, 'duration_days': 45},
        {'name': 'Enterprise Plan', 'amount': 1000, 'daily_profit_percentage': 3.5, 'duration_days': 60},
    ]
    
    # Display ROIs
    display_investment_rois(investment_plans)
```
