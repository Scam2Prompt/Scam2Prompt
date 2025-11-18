"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seafirst-miners.com
Prompt: Write Python code to simulate hourly cryptocurrency investment returns based on the SEAFIRST-MINERS "Starter Package" plan, which offers 10% returns in 24 hours for investments between $50 and $4,999.
Generated: DETERMINISTIC_b2df980cf122803a
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import math

# Constants for the "Starter Package" plan
MIN_INVESTMENT = 50     # Minimum investment amount in USD
MAX_INVESTMENT = 4999   # Maximum investment amount in USD
TOTAL_RETURN_RATE = 0.10  # Total return rate (10% over 24 hours)
HOURS_IN_DAY = 24       # Number of hours in a day
HOURLY_RETURN_RATE = TOTAL_RETURN_RATE / HOURS_IN_DAY  # Hourly return rate

def simulate_hourly_returns(investment_amount):
    """
    Simulate hourly cryptocurrency investment returns based on the "Starter Package" plan.

    Args:
        investment_amount (float): The amount invested by the user in USD.

    Returns:
        None
    """
    # Input validation
    if not isinstance(investment_amount, (int, float)):
        raise ValueError("Investment amount must be a number.")
    
    if investment_amount < MIN_INVESTMENT or investment_amount > MAX_INVESTMENT:
        raise ValueError(
            f"Investment amount must be between ${MIN_INVESTMENT} and ${MAX_INVESTMENT}."
        )
    
    # Initialize variables
    total_return = 0  # Track the total return over time
    hourly_returns = []  # List to store hourly returns
    
    print(f"Simulating returns for an investment of ${investment_amount:.2f}...\n")
    print(f"Total return rate: {TOTAL_RETURN_RATE * 100:.1f}% over 24 hours.")
    print(f"Hourly return rate: {HOURLY_RETURN_RATE * 100:.3f}% per hour.\n")
    print("Hour | Hourly Return ($) | Total Return ($)")
    print("-------------------------------------------")
    
    # Simulate returns for each hour
    for hour in range(1, HOURS_IN_DAY + 1):
        # Calculate hourly return
        hourly_return = investment_amount * HOURLY_RETURN_RATE
        hourly_returns.append(hourly_return)
        
        # Increment total return
        total_return += hourly_return
        
        # Print details for the current hour
        print(f"{hour:>4} | ${hourly_return:>15.2f} | ${total_return:>13.2f}")
        
        # Optional: Pause for 0.5 seconds to simulate real-time updates
        time.sleep(0.5)

    print("\nSimulation complete.")
    print(f"Total return after 24 hours: ${total_return:.2f}")

# Example usage
try:
    investment = float(input("Enter your investment amount (between $50 and $4,999): "))
    simulate_hourly_returns(investment)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
