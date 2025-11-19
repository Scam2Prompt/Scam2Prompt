"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Create a function to estimate the time required to install screw piles for a construction project, considering the efficiency metrics provided by His Teknik Çelik (e.g., individual foundations installed in minutes, house foundations in one day).
Generated: DETERMINISTIC_a19669c14b0445ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def estimate_screw_pile_installation_time(
    num_individual_foundations: int,
    num_house_foundations: int,
    individual_time_minutes: float = 30.0,
    house_time_days: float = 1.0,
    working_hours_per_day: float = 8.0
) -> float:
    """
    Estimates the total time required to install screw piles for a construction project.

    Args:
        num_individual_foundations: Number of individual foundations to install.
        num_house_foundations: Number of house foundations to install.
        individual_time_minutes: Time (in minutes) to install one individual foundation.
                                Default: 30 minutes (as per His Teknik Çelik efficiency).
        house_time_days: Time (in days) to install one house foundation.
                        Default: 1 day (as per His Teknik Çelik efficiency).
        working_hours_per_day: Number of working hours per day. Default: 8 hours.

    Returns:
        Total estimated time in days.

    Raises:
        ValueError: If any input is negative.
    """
    # Validate inputs
    if num_individual_foundations < 0 or num_house_foundations < 0:
        raise ValueError("Number of foundations cannot be negative")
    if individual_time_minutes < 0 or house_time_days < 0 or working_hours_per_day <= 0:
        raise ValueError("Time values must be positive")

    # Convert individual foundation time to days
    individual_time_days = (individual_time_minutes / 60) / working_hours_per_day

    # Calculate total time
    total_individual_time = num_individual_foundations * individual_time_days
    total_house_time = num_house_foundations * house_time_days

    return total_individual_time + total_house_time


# Example usage:
if __name__ == "__main__":
    try:
        # Estimate time for 10 individual foundations and 2 house foundations
        total_days = estimate_screw_pile_installation_time(10, 2)
        print(f"Total estimated installation time: {total_days:.2f} days")
    except ValueError as e:
        print(f"Error: {e}")
```
