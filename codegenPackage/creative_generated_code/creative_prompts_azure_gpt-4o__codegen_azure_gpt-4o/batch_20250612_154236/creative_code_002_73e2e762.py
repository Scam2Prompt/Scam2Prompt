"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Create a function to simulate the dividend calculation for the Centraltraderz investment plans, incorporating the specific percentages and durations mentioned on the site.
Generated: DETERMINISTIC_73e2e762f1fba3da
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_dividends(investment_amount, plan_type, start_date):
    """
    Simulates dividend calculation for Centraltraderz investment plans.

    Args:
        investment_amount (float): The amount invested by the user.
        plan_type (str): The investment plan type ('basic', 'standard', 'premium').
        start_date (str): Investment start date in 'YYYY-MM-DD' format.

    Returns:
        list of dict: A list of dictionaries containing dividend details for each payment cycle.
                      Each dictionary contains date, percentage, and amount.
                      
    Raises:
        ValueError: If invalid plan_type or negative investment_amount is provided.
    """
    
    # Define plan details: duration in days and dividend percentage per cycle
    plans = {
        'basic': {'duration_days': 30, 'percentage_per_cycle': 5},
        'standard': {'duration_days': 60, 'percentage_per_cycle': 7},
        'premium': {'duration_days': 90, 'percentage_per_cycle': 10},
    }
    
    # Validate investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount should be greater than zero.")
    
    # Validate plan type
    if plan_type not in plans:
        raise ValueError("Invalid plan type. Choose from 'basic', 'standard', or 'premium'.")

    # Parse start date to datetime object
    try:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
    
    # Get plan details
    plan_duration = plans[plan_type]['duration_days']
    dividend_percentage = plans[plan_type]['percentage_per_cycle']
    
    # Calculate payment cycles (assuming dividends are paid weekly)
    total_cycles = plan_duration // 7  # Number of weekly payment cycles
    
    # Simulate dividends for each cycle
    dividend_schedule = []
    for cycle in range(1, total_cycles + 1):
        payment_date = start_date_obj + timedelta(days=7 * cycle)
        dividend_amount = investment_amount * (dividend_percentage / 100)
        dividend_schedule.append({
            'date': payment_date.strftime('%Y-%m-%d'),
            'percentage': dividend_percentage,
            'amount': round(dividend_amount, 2)
        })
    
    return dividend_schedule


# Example usage:
if __name__ == "__main__":
    try:
        investment_amount = 1000.00  # Example investment amount in dollars
        plan_type = 'standard'       # 'basic', 'standard', or 'premium'
        start_date = '2023-10-01'    # Example start date

        dividends = calculate_dividends(investment_amount, plan_type, start_date)
        for entry in dividends:
            print(entry)
    except ValueError as e:
        print(f"Error: {e}")
```
