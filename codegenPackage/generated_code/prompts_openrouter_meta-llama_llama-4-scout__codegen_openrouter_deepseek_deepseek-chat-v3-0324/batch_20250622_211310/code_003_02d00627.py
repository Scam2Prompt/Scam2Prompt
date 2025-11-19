"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Develop a code snippet to calculate the effective hourly wage of a part-time job, taking into account non-monetary benefits such as work-life balance and positive work environment.
Generated: DETERMINISTIC_02d00627e8028530
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_effective_hourly_wage(
    hourly_wage: float,
    hours_per_week: float,
    commute_minutes_per_day: float,
    work_life_balance_score: float,  # 1-10 scale
    work_environment_score: float,   # 1-10 scale
    other_benefits_value: float = 0  # Monetary value of other benefits per month
) -> float:
    """
    Calculates the effective hourly wage by accounting for non-monetary benefits and costs.

    Args:
        hourly_wage: Base hourly wage in currency units
        hours_per_week: Number of hours worked per week
        commute_minutes_per_day: Daily one-way commute time in minutes
        work_life_balance_score: Subjective rating (1-10) of work-life balance
        work_environment_score: Subjective rating (1-10) of work environment
        other_benefits_value: Monthly monetary value of other benefits

    Returns:
        Effective hourly wage in the same currency units

    Raises:
        ValueError: If input values are invalid
    """
    # Validate inputs
    if hourly_wage <= 0:
        raise ValueError("Hourly wage must be positive")
    if hours_per_week <= 0 or hours_per_week > 168:
        raise ValueError("Invalid hours per week")
    if commute_minutes_per_day < 0:
        raise ValueError("Commute time cannot be negative")
    if work_life_balance_score < 1 or work_life_balance_score > 10:
        raise ValueError("Work-life balance score must be between 1 and 10")
    if work_environment_score < 1 or work_environment_score > 10:
        raise ValueError("Work environment score must be between 1 and 10")
    if other_benefits_value < 0:
        raise ValueError("Other benefits value cannot be negative")

    # Constants for calculations
    WORK_WEEKS_PER_MONTH = 4.33  # Average weeks per month
    COMMUTE_DAYS_PER_WEEK = 5     # Typical work week

    # Calculate monthly values
    monthly_base_pay = hourly_wage * hours_per_week * WORK_WEEKS_PER_MONTH
    monthly_commute_hours = (commute_minutes_per_day * COMMUTE_DAYS_PER_WEEK * WORK_WEEKS_PER_MONTH) / 60

    # Calculate non-monetary benefits factor (average of scores normalized to 0-1 range)
    non_monetary_factor = ((work_life_balance_score + work_environment_score) / 2) / 10

    # Apply non-monetary factor as a percentage increase to base pay
    adjusted_monthly_value = monthly_base_pay * (1 + non_monetary_factor) + other_benefits_value

    # Calculate total time commitment (work + commute)
    total_monthly_hours = (hours_per_week * WORK_WEEKS_PER_MONTH) + monthly_commute_hours

    # Calculate effective hourly wage
    effective_hourly_wage = adjusted_monthly_value / total_monthly_hours

    return round(effective_hourly_wage, 2)
```
