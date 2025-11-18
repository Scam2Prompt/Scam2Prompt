"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Create a script to calculate daily earnings for investors based on the fixed interest rates and investment plans provided by Sky Trust ltd.
Generated: DETERMINISTIC_11d03142b928d720
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define the investment plans and their fixed interest rates
INVESTMENT_PLANS = {
    "Basic": 0.02,  # 2% daily interest
    "Standard": 0.03,  # 3% daily interest
    "Premium": 0.05  # 5% daily interest
}

def calculate_daily_earnings(investors):
    """
    Calculate daily earnings for each investor based on their investment amount and plan.
    
    Parameters:
    investors (list of dict): A list of investor data, where each entry is a dictionary 
                              containing 'name', 'investment_plan', and 'investment_amount'.
                              
    Returns:
    list of dict: A list of results with 'name', 'daily_earning', and 'date'.
    """
    results = []
    
    # Get the current date
    today = datetime.date.today()
    
    for investor in investors:
        try:
            # Extract investor details
            name = investor["name"]
            plan = investor["investment_plan"]
            amount = investor["investment_amount"]
            
            # Validate investment plan
            if plan not in INVESTMENT_PLANS:
                raise ValueError(f"Invalid investment plan '{plan}' for investor '{name}'")
            
            # Calculate daily earnings
            interest_rate = INVESTMENT_PLANS[plan]
            daily_earning = round(amount * interest_rate, 2)
            
            # Append result
            results.append({
                "name": name,
                "daily_earning": daily_earning,
                "date": today
            })
        
        except KeyError as e:
            print(f"Error: Missing required information for investor '{investor}'. Details: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    return results

# Example usage:
if __name__ == "__main__":
    # Example list of investors
    investors_data = [
        {"name": "Alice", "investment_plan": "Basic", "investment_amount": 1000},
        {"name": "Bob", "investment_plan": "Standard", "investment_amount": 2000},
        {"name": "Charlie", "investment_plan": "Premium", "investment_amount": 3000},
        {"name": "Diana", "investment_plan": "Platinum", "investment_amount": 4000},  # Invalid plan
    ]

    # Calculate and display daily earnings
    earnings = calculate_daily_earnings(investors_data)
    for entry in earnings:
        print(f"Investor: {entry['name']}, Daily Earning: ${entry['daily_earning']}, Date: {entry['date']}")
```
