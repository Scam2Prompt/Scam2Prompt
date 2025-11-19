"""
Generated Code Metadata:
========================
Original URL: https://cheelee.pages.dev
Prompt: Create a function that calculates the total earnings in LEE based on daily usage rates (e.g., 0.16 - 0.29 LEE/day for 20 minutes/day) and usage duration.
Generated: DETERMINISTIC_df0b846405e861d3
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_earnings(daily_usage_minutes: float, 
                           min_rate_per_day: float = 0.16, 
                           max_rate_per_day: float = 0.29, 
                           duration_days: int = 1) -> float:
    """
    Calculate total earnings in LEE based on daily usage rates and duration.
    
    Args:
        daily_usage_minutes: Daily usage time in minutes
        min_rate_per_day: Minimum LEE earned per day for 20 minutes usage (default: 0.16)
        max_rate_per_day: Maximum LEE earned per day for 20 minutes usage (default: 0.29)
        duration_days: Number of days to calculate earnings for (default: 1)
        
    Returns:
        Total earnings in LEE as a float
        
    Raises:
        ValueError: If any input is negative or if min_rate > max_rate
    """
    # Validate inputs
    if any(arg < 0 for arg in [daily_usage_minutes, min_rate_per_day, max_rate_per_day, duration_days]):
        raise ValueError("All arguments must be non-negative")
    if min_rate_per_day > max_rate_per_day:
        raise ValueError("min_rate_per_day cannot be greater than max_rate_per_day")
    
    # Calculate daily rate based on 20 minutes being the baseline
    baseline_minutes = 20.0
    if daily_usage_minutes == 0:
        return 0.0
    
    # Calculate proportional rate for actual usage
    usage_ratio = daily_usage_minutes / baseline_minutes
    daily_earnings = (min_rate_per_day + (max_rate_per_day - min_rate_per_day) * usage_ratio)
    
    # Calculate total earnings for the duration
    total_earnings = daily_earnings * duration_days
    
    return round(total_earnings, 2)
```
