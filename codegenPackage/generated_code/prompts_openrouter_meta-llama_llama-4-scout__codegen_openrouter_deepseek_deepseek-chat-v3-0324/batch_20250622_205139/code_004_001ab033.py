"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write a code snippet to simulate the installation of OpenSeam devices in a factory, assuming a quick installation time of under 1 minute per sewing workstation, and calculate the total installation time for a given number of workstations.
Generated: DETERMINISTIC_001ab0336203c5d1
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

def simulate_installation(num_workstations):
    """
    Simulates the installation of OpenSeam devices in a factory.
    
    Args:
        num_workstations (int): Number of sewing workstations to install devices on.
        
    Returns:
        tuple: (total_time_seconds, total_time_minutes) - Total installation time in seconds and minutes.
    """
    if not isinstance(num_workstations, int) or num_workstations < 1:
        raise ValueError("Number of workstations must be a positive integer")
    
    total_time_seconds = 0
    
    for workstation in range(1, num_workstations + 1):
        # Random installation time between 30-60 seconds per workstation
        install_time = random.uniform(30, 60)
        total_time_seconds += install_time
        
        # Simulate installation delay
        time.sleep(install_time)
        
        print(f"Installed device on workstation {workstation}/{num_workstations} "
              f"(took {install_time:.2f} seconds)")
    
    total_time_minutes = total_time_seconds / 60
    
    return total_time_seconds, total_time_minutes

if __name__ == "__main__":
    try:
        num_workstations = int(input("Enter number of workstations: "))
        seconds, minutes = simulate_installation(num_workstations)
        print(f"\nTotal installation time: {seconds:.2f} seconds ({minutes:.2f} minutes)")
    except ValueError as e:
        print(f"Error: {e}")
```
