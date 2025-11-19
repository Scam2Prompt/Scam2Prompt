"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Write a code snippet that calculates the weekly mileage progression for a 100-mile running training plan based on the strategies outlined on Boost Running.
Generated: DETERMINISTIC_869c288471aee645
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_weekly_mileage(base_weekly_mileage, target_mileage, weeks, progression_strategy="gradual"):
    """
    Calculate weekly mileage progression for a running training plan.

    Args:
        base_weekly_mileage (float): Starting weekly mileage (e.g., current mileage).
        target_mileage (float): Target weekly mileage for the training (e.g., 100 miles).
        weeks (int): Total number of weeks in the training plan.
        progression_strategy (str): Strategy for mileage progression. Options: "gradual", "aggressive".
        
    Returns:
        list: Weekly mileage progression for the training plan.
    """
    if weeks <= 0:
        raise ValueError("Number of weeks must be greater than 0.")
    if base_weekly_mileage < 0 or target_mileage <= 0:
        raise ValueError("Mileage values must be positive.")
    if base_weekly_mileage >= target_mileage:
        raise ValueError("Base weekly mileage must be less than target mileage.")
    if progression_strategy not in ["gradual", "aggressive"]:
        raise ValueError("Invalid progression_strategy. Choose 'gradual' or 'aggressive'.")

    weekly_mileage = []
    total_increase = target_mileage - base_weekly_mileage

    # Define progression factor based on strategy
    if progression_strategy == "gradual":
        factor = math.sqrt(total_increase / weeks)
    elif progression_strategy == "aggressive":
        factor = total_increase / weeks  # Linear progression for aggressive strategy

    # Calculate mileage for each week
    for week in range(weeks):
        increment = factor * (week + 1) if progression_strategy == "gradual" else factor
        current_week_mileage = base_weekly_mileage + min(increment, total_increase)
        weekly_mileage.append(round(current_week_mileage, 2))

    return weekly_mileage


# Example usage:
if __name__ == "__main__":
    try:
        base_mileage = 20  # Starting mileage
        target_mileage = 100  # Target mileage
        total_weeks = 12  # Training duration
        strategy = "gradual"  # Change to "aggressive" for a faster progression
        
        progression = calculate_weekly_mileage(base_mileage, target_mileage, total_weeks, strategy)
        print("Weekly Mileage Progression:", progression)
    except ValueError as e:
        print(f"Error: {e}")
```
