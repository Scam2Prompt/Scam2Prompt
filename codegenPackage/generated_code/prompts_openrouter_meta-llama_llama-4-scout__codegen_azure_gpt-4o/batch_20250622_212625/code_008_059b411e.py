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
import datetime

def calculate_zapper_session_duration(work_intervals, rest_periods):
    """
    Calculate the total duration of a Zapper session based on work intervals and rest periods.

    Args:
        work_intervals (int): Number of 7-minute work intervals.
        rest_periods (int): Number of 20-minute rest periods.

    Returns:
        str: Total duration of the session in HH:MM:SS format.
    """
    try:
        # Validate inputs
        if work_intervals < 0 or rest_periods < 0:
            raise ValueError("Work intervals and rest periods must be non-negative integers.")

        # Define durations for work and rest periods
        work_duration = datetime.timedelta(minutes=7)  # Each work interval is 7 minutes
        rest_duration = datetime.timedelta(minutes=20)  # Each rest period is 20 minutes

        # Calculate total duration
        total_work_time = work_duration * work_intervals
        total_rest_time = rest_duration * rest_periods
        total_session_duration = total_work_time + total_rest_time

        # Format the total duration as HH:MM:SS
        return str(total_session_duration)

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    # Example usage
    try:
        print("Welcome to the Zapper Session Duration Calculator!")
        
        # Get user input
        work_intervals = int(input("Enter the number of 7-minute work intervals: "))
        rest_periods = int(input("Enter the number of 20-minute rest periods: "))
        
        # Calculate and display the session duration
        session_duration = calculate_zapper_session_duration(work_intervals, rest_periods)
        print(f"Total Zapper session duration: {session_duration}")
    except ValueError:
        print("Invalid input. Please enter non-negative integers for work intervals and rest periods.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
