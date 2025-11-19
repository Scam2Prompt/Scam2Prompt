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
# Import necessary modules
from typing import Optional

def calculate_effective_hourly_wage(
    hourly_wage: float,
    hours_worked_per_week: int,
    work_life_balance_score: Optional[float] = None,
    positive_environment_score: Optional[float] = None
) -> float:
    """
    Calculate the effective hourly wage of a part-time job, factoring in non-monetary benefits.

    Parameters:
        hourly_wage (float): The base hourly wage in monetary terms.
        hours_worked_per_week (int): The number of hours worked per week.
        work_life_balance_score (Optional[float]): A score between 0 and 1 representing work-life balance benefits.
        positive_environment_score (Optional[float]): A score between 0 and 1 representing the positive work environment.

    Returns:
        float: The effective hourly wage, adjusted for non-monetary benefits.

    Raises:
        ValueError: If hourly_wage is negative or hours_worked_per_week is not positive.
        ValueError: If work_life_balance_score or positive_environment_score is not between 0 and 1.
    """
    # Validate inputs
    if hourly_wage < 0:
        raise ValueError("Hourly wage must be non-negative.")
    if hours_worked_per_week <= 0:
        raise ValueError("Hours worked per week must be positive.")
    if work_life_balance_score is not None and not (0 <= work_life_balance_score <= 1):
        raise ValueError("Work-life balance score must be between 0 and 1.")
    if positive_environment_score is not None and not (0 <= positive_environment_score <= 1):
        raise ValueError("Positive environment score must be between 0 and 1.")

    # Base effective hourly wage starts with the monetary hourly wage
    effective_hourly_wage = hourly_wage

    # Adjust for work-life balance score if provided
    if work_life_balance_score is not None:
        effective_hourly_wage += hourly_wage * work_life_balance_score

    # Adjust for positive work environment score if provided
    if positive_environment_score is not None:
        effective_hourly_wage += hourly_wage * positive_environment_score

    return effective_hourly_wage


# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        hourly_wage = 20.0  # $20 per hour
        hours_worked_per_week = 25  # 25 hours per week
        work_life_balance_score = 0.8  # 80% satisfaction with work-life balance
        positive_environment_score = 0.7  # 70% satisfaction with work environment

        # Calculate effective hourly wage
        result = calculate_effective_hourly_wage(
            hourly_wage,
            hours_worked_per_week,
            work_life_balance_score,
            positive_environment_score
        )

        # Output the result
        print(f"Effective Hourly Wage: ${result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
