"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheelee.pages.dev
Prompt: Create a function that calculates the total earnings in LEE based on daily usage rates (e.g., 0.16 - 0.29 LEE/day for 20 minutes/day) and usage duration.
Generated: DETERMINISTIC_df0b846405e861d3
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(daily_rate: float, usage_duration_days: int) -> float:
    """
    Calculate the total earnings in LEE based on daily usage rates and usage duration.

    Parameters:
    daily_rate (float): The daily usage rate in LEE (should be between 0.16 and 0.29).
    usage_duration_days (int): The number of days of usage.

    Returns:
    float: The total earnings in LEE for the given usage duration.

    Raises:
    ValueError: If the daily_rate is not within the valid range or if usage_duration_days is negative.
    """

    # Validate inputs
    if not (0.16 <= daily_rate <= 0.29):
        raise ValueError("Daily rate must be between 0.16 and 0.29 LEE.")
    
    if usage_duration_days < 0:
        raise ValueError("Usage duration days cannot be negative.")

    # Calculate total earnings
    total_earnings = daily_rate * usage_duration_days

    return total_earnings


# Example usage
if __name__ == "__main__":
    try:
        # Example values for daily rate and duration
        daily_rate_example = 0.20  # Example daily rate in LEE
        usage_days_example = 30     # Example duration in days

        earnings = calculate_total_earnings(daily_rate_example, usage_days_example)
        print(f"Total earnings in LEE for {usage_days_example} days: {earnings:.2f} LEE")
    
    except ValueError as e:
        print(f"Error: {e}")
```
