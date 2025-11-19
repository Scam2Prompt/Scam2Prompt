"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Create a Python script to calculate the total weight of processed EPS foam per day for the XT400 densifier, given its hourly capacity and operating hours.
Generated: DETERMINISTIC_1f8b6ab436d272c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
XT400 Densifier Daily EPS Foam Weight Calculator

Calculates the total weight of processed EPS foam per day for the XT400 densifier.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_daily_weight(hourly_capacity: float, operating_hours: float) -> float:
    """
    Calculates the total weight of processed EPS foam per day.

    Args:
        hourly_capacity (float): The hourly capacity of the XT400 densifier in kg/h.
        operating_hours (float): The number of hours the densifier operates per day.

    Returns:
        float: The total weight of processed EPS foam per day in kg.

    Raises:
        ValueError: If hourly capacity or operating hours are negative.
    """
    if hourly_capacity < 0 or operating_hours < 0:
        raise ValueError("Hourly capacity and operating hours must be non-negative.")

    daily_weight = hourly_capacity * operating_hours
    return daily_weight


def main():
    try:
        # Define the hourly capacity of the XT400 densifier in kg/h
        hourly_capacity = 400  # kg/h

        # Define the operating hours per day
        operating_hours = 8  # hours/day

        # Calculate the daily weight
        daily_weight = calculate_daily_weight(hourly_capacity, operating_hours)

        # Print the result
        print(f"The total weight of processed EPS foam per day is: {daily_weight:.2f} kg")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
