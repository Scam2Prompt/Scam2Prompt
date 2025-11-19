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
from typing import Tuple

def calculate_zapper_session_duration(
    work_intervals: int,
    work_duration: int = 7,
    rest_duration: int = 20
) -> Tuple[datetime.timedelta, datetime.timedelta]:
    """
    Calculate the total duration of a Zapper session including work and rest periods.
    
    Args:
        work_intervals: Number of work intervals in the session
        work_duration: Duration of each work interval in minutes (default: 7)
        rest_duration: Duration of each rest period in minutes (default: 20)
    
    Returns:
        Tuple containing:
        - Total session duration as timedelta
        - Total active work duration as timedelta
    
    Raises:
        ValueError: If work_intervals is not a positive integer
    """
    if not isinstance(work_intervals, int) or work_intervals <= 0:
        raise ValueError("work_intervals must be a positive integer")
    
    # Calculate total work time
    total_work = datetime.timedelta(minutes=work_intervals * work_duration)
    
    # Calculate total rest time (one less rest than work intervals)
    total_rest = datetime.timedelta(minutes=max(0, (work_intervals - 1) * rest_duration))
    
    total_duration = total_work + total_rest
    return total_duration, total_work

def format_timedelta(duration: datetime.timedelta) -> str:
    """
    Format a timedelta into a human-readable string (HH:MM:SS).
    
    Args:
        duration: timedelta object to format
    
    Returns:
        Formatted string in HH:MM:SS format
    """
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    """Main function to demonstrate the Zapper session duration calculation."""
    try:
        print("Zapper Session Duration Calculator")
        print("----------------------------------")
        
        work_intervals = int(input("Enter number of work intervals: "))
        
        total_duration, total_work = calculate_zapper_session_duration(work_intervals)
        
        print(f"\nTotal session duration: {format_timedelta(total_duration)}")
        print(f"Total active work time: {format_timedelta(total_work)}")
        print(f"Number of rest periods: {work_intervals - 1}")
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter a valid positive integer for work intervals.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
