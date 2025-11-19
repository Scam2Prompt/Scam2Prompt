"""
Generated Code Metadata:
========================
Original URL: https://illuvius.com
Prompt: Develop a script to simulate the random distribution of vesting start times within a 24-hour window, as described on the Illuvius platform.
Generated: DETERMINISTIC_04dbe0b87e37afc0
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta

def simulate_vesting_start_times(num_simulations: int) -> list:
    """
    Simulates random vesting start times within a 24-hour window.
    
    Args:
        num_simulations (int): Number of start times to generate
        
    Returns:
        list: List of datetime objects representing vesting start times
    """
    if not isinstance(num_simulations, int) or num_simulations <= 0:
        raise ValueError("num_simulations must be a positive integer")
    
    start_times = []
    current_time = datetime.utcnow()
    
    for _ in range(num_simulations):
        # Generate random seconds within 24 hours (86400 seconds)
        random_seconds = random.randint(0, 86400)
        # Calculate the vesting start time
        vesting_time = current_time + timedelta(seconds=random_seconds)
        start_times.append(vesting_time)
    
    return start_times

def format_times_for_display(start_times: list) -> list:
    """
    Formats datetime objects into human-readable strings.
    
    Args:
        start_times (list): List of datetime objects
        
    Returns:
        list: List of formatted time strings
    """
    return [time.strftime("%Y-%m-%d %H:%M:%S UTC") for time in start_times]

def main():
    try:
        num_simulations = 10  # Default number of simulations
        print(f"Simulating {num_simulations} vesting start times...")
        
        start_times = simulate_vesting_start_times(num_simulations)
        formatted_times = format_times_for_display(start_times)
        
        print("\nVesting Start Times:")
        for i, time_str in enumerate(formatted_times, 1):
            print(f"{i}. {time_str}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
