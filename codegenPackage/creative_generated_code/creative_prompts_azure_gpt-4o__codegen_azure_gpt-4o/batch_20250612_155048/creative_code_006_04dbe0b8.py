"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuvius.com
Prompt: Develop a script to simulate the random distribution of vesting start times within a 24-hour window, as described on the Illuvius platform.
Generated: DETERMINISTIC_04dbe0b87e37afc0
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

def generate_vesting_times(n, start_date=None):
    """
    Generate random vesting start times within a 24-hour window.

    Parameters:
        n (int): The number of vesting times to generate.
        start_date (datetime, optional): The base start date. Defaults to the current date and time.

    Returns:
        list: A list of randomized vesting start times as datetime objects.
    """
    if n <= 0:
        raise ValueError("The number of vesting times must be a positive integer.")

    # Use the current date and time if no start_date is provided
    base_date = start_date if start_date else datetime.now()

    vesting_times = []
    for _ in range(n):
        # Generate a random offset (in seconds) within a 24-hour period
        random_seconds = random.randint(0, 24 * 60 * 60 - 1)
        vesting_time = base_date + timedelta(seconds=random_seconds)
        vesting_times.append(vesting_time)

    return vesting_times

def main():
    """
    Main function to execute the vesting time simulation.
    """
    try:
        # Example: Generate 5 random vesting start times
        vesting_start_times = generate_vesting_times(5)

        print("Generated vesting start times:")
        for idx, time in enumerate(vesting_start_times, start=1):
            print(f"{idx}: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
