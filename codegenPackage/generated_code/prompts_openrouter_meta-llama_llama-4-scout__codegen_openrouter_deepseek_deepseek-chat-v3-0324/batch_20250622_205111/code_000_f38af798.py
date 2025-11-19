"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: "Write a Python code snippet to calculate the interest share for a Spiko user with over 6 months of history, assuming an investment of $10,000 in the USTBL Treasury Bills with a 5.11% APY."
Generated: DETERMINISTIC_f38af7981ddd65d9
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from decimal import Decimal, getcontext

def calculate_interest(
    principal: Decimal,
    apy: Decimal,
    start_date: datetime.date,
    end_date: datetime.date
) -> Decimal:
    """
    Calculate the interest earned on an investment based on APY and time period.
    
    Args:
        principal: Initial investment amount (Decimal)
        apy: Annual Percentage Yield (Decimal)
        start_date: Investment start date (datetime.date)
        end_date: Investment end date (datetime.date)
    
    Returns:
        Decimal: Calculated interest amount
    """
    # Set precision for Decimal calculations
    getcontext().prec = 6
    
    # Calculate days in the investment period
    days_in_period = (end_date - start_date).days
    
    # Calculate daily interest rate (compounded daily)
    daily_rate = (1 + apy) ** (Decimal('1') / Decimal('365')) - 1
    
    # Calculate final amount with compound interest
    final_amount = principal * (1 + daily_rate) ** days_in_period
    
    # Calculate interest earned
    interest = final_amount - principal
    
    return interest.quantize(Decimal('0.01'))

# Example usage for Spiko user with 6+ months history
if __name__ == "__main__":
    try:
        principal = Decimal('10000')  # $10,000 investment
        apy = Decimal('0.0511')      # 5.11% APY
        
        # Calculate dates (6 months from today)
        start_date = datetime.date.today() - datetime.timedelta(days=180)
        end_date = datetime.date.today()
        
        interest = calculate_interest(principal, apy, start_date, end_date)
        
        print(f"Interest earned after 6 months: ${interest}")
    except Exception as e:
        print(f"Error calculating interest: {e}")
```
