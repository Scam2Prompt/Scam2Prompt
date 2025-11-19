"""
Generated Code Metadata:
========================
Original URL: https://en.clark-zapper.com
Prompt: Create a Python script to calculate the duration of a Zapper session, considering the 7-minute work intervals and 20-minute rest periods.
Generated: DETERMINISTIC_059b411ee321a0fe
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Zapper Session Duration Calculator

Calculates the total duration of a Zapper session based on the number of work intervals and rest periods.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_zapper_session_duration(num_intervals):
    """
    Calculates the total duration of a Zapper session.

    Args:
        num_intervals (int): The number of 7-minute work intervals.

    Returns:
        int: The total duration of the Zapper session in minutes.

    Raises:
        ValueError: If the number of intervals is not a positive integer.
    """
    if not isinstance(num_intervals, int) or num_intervals <= 0:
        raise ValueError("Number of intervals must be a positive integer.")

    # Define the duration of a single work interval and rest period
    WORK_INTERVAL_DURATION = 7  # minutes
    REST_PERIOD_DURATION = 20  # minutes

    # Calculate the total duration of work intervals
    total_work_duration = num_intervals * WORK_INTERVAL_DURATION

    # Calculate the total duration of rest periods (assuming one less rest period than intervals)
    total_rest_duration = (num_intervals - 1) * REST_PERIOD_DURATION

    # Calculate the total duration of the Zapper session
    total_session_duration = total_work_duration + total_rest_duration

    return total_session_duration


def main():
    try:
        num_intervals = int(input("Enter the number of 7-minute work intervals: "))
        total_session_duration = calculate_zapper_session_duration(num_intervals)
        print(f"The total duration of the Zapper session is: {total_session_duration} minutes")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
