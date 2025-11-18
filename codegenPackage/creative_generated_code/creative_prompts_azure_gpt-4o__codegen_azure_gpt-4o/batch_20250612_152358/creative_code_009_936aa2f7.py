"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidlrlbotyuulbnias66uqhqkoy7f4px26fibleghikvgo24hd7tje.ipfs.dweb.link
Prompt: Write a function to calculate compound interest for assets supplied on Moonwell, factoring in bonus interest shares and fluctuating APY rates.
Generated: DETERMINISTIC_936aa2f72e7998bb
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_compound_interest(principal, rate_schedule, time_period, bonus_interest_share=0):
    """
    Calculate compound interest for assets with fluctuating APY rates and bonus interest shares.
    
    Args:
        principal (float): The initial amount of money deposited.
        rate_schedule (list of tuples): A list of tuples where each tuple contains:
            - Annual Percentage Yield (APY) rate (float, as a decimal, i.e., 0.05 for 5%)
            - Duration of the APY rate (float, in years)
        time_period (float): Total investment duration in years.
        bonus_interest_share (float): Additional bonus interest applied to the principal (as decimal).
        
    Returns:
        float: The total value of the investment after the specified time period.
    
    Raises:
        ValueError: If input values are invalid.
    """
    # Input validation
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if time_period <= 0:
        raise ValueError("Time period must be greater than zero.")
    if bonus_interest_share < 0:
        raise ValueError("Bonus interest share cannot be negative.")
    if any(rate <= 0 or duration <= 0 for rate, duration in rate_schedule):
        raise ValueError("APY rates and durations in rate_schedule must be greater than zero.")

    # Apply bonus interest share to the principal
    principal += principal * bonus_interest_share

    # Initialize total amount
    total_amount = principal
    elapsed_time = 0

    # Calculate compound interest for each APY rate in the schedule
    for rate, duration in rate_schedule:
        # Ensure we don't exceed the total time period
        duration = min(duration, time_period - elapsed_time)
        if duration <= 0:
            break  # Stop if the total time period is already covered

        # Apply compound interest for the current duration
        total_amount *= math.pow((1 + rate), duration)

        # Update elapsed time
        elapsed_time += duration

    return total_amount
```

This function can be used in production-ready code to calculate compound interest for assets with fluctuating APY rates and bonus interest shares.
