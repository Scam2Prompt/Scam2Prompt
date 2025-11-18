"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Create a function to calculate total returns for Sabka Future's "SUPER GOLD" plan, factoring in daily returns and investment duration.
Generated: DETERMINISTIC_bc118c02636d423b
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import timedelta, datetime

def calculate_total_returns(initial_investment, daily_return_rate, start_date, end_date):
    """
    Calculate the total returns for Sabka Future's "SUPER GOLD" plan.
    
    Parameters:
        initial_investment (float): The initial amount invested (in USD or relevant currency).
        daily_return_rate (float): The daily return rate as a percentage (e.g., 0.5 for 0.5% daily return).
        start_date (str): The start date of the investment in 'YYYY-MM-DD' format.
        end_date (str): The end date of the investment in 'YYYY-MM-DD' format.
    
    Returns:
        float: The total returns after the investment duration.
    """
    try:
        # Convert date strings to datetime objects
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Ensure the start date is before the end date
        if start_date_obj >= end_date_obj:
            raise ValueError("Start date must be earlier than end date.")
        
        # Calculate the number of investment days
        total_days = (end_date_obj - start_date_obj).days
        
        # Ensure valid input values
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if daily_return_rate < 0:
            raise ValueError("Daily return rate must be non-negative.")
        
        # Compound the total returns daily
        total_returns = initial_investment * ((1 + daily_return_rate / 100) ** total_days)
        return round(total_returns, 2)  # Round to 2 decimal places for currency representation

    except ValueError as ve:
        # Handle invalid input values
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage (ensure to remove or comment out in production if not needed)
if __name__ == "__main__":
    initial_investment = 1000.0  # Example: $1000
    daily_return_rate = 0.5      # Example: 0.5% daily return
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    
    total_returns = calculate_total_returns(initial_investment, daily_return_rate, start_date, end_date)
    if total_returns is not None:
        print(f"Total returns for the SUPER GOLD plan: ${total_returns}")
```
