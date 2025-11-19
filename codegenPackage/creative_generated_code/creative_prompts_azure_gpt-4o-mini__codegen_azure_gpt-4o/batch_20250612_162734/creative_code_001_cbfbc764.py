"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python function that simulates the operation of a "turbina ferramental" in a manufacturing process, incorporating safety checks.
Generated: DETERMINISTIC_cbfbc76418e08618
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class TurbineError(Exception):
    """Custom exception for turbine-related errors."""
    pass

def simulate_turbina_ferramental(operational_speed, max_speed, min_speed, duration):
    """
    Simulates the operation of a 'turbina ferramental' in a manufacturing process.

    Args:
        operational_speed (float): The desired operational speed of the turbine (RPM).
        max_speed (float): The maximum safe speed of the turbine (RPM).
        min_speed (float): The minimum safe speed of the turbine (RPM).
        duration (int): The duration to run the turbine in seconds.

    Returns:
        str: A message indicating the turbine's operation status.
    
    Raises:
        TurbineError: If the operational speed is outside the safety limits.
        ValueError: If inputs are invalid (negative numbers, nonsensical duration, etc.).
    """
    # Input validation
    if operational_speed < 0 or max_speed < 0 or min_speed < 0 or duration < 0:
        raise ValueError("All parameters must be non-negative.")
    if min_speed >= max_speed:
        raise ValueError("`min_speed` must be less than `max_speed`.")

    # Safety checks
    if operational_speed > max_speed:
        raise TurbineError(f"Operational speed {operational_speed} exceeds the max safe limit of {max_speed}.")
    if operational_speed < min_speed:
        raise TurbineError(f"Operational speed {operational_speed} is below the minimum safe limit of {min_speed}.")

    # Simulate turbine operation
    print("Starting turbine operation...")
    try:
        for second in range(duration):
            print(f"Turbine running at {operational_speed} RPM - {second + 1}s elapsed.")
            time.sleep(1)  # Simulate time passing

        print("Turbine operation completed successfully.")
        return "Turbine operation completed successfully."
    except KeyboardInterrupt:
        print("Turbine operation interrupted by user.")
        return "Turbine operation interrupted by user."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise TurbineError("Unexpected error during turbine operation.") from e

# Example Usage (uncomment to test):
# result = simulate_turbina_ferramental(500, 1000, 100, 5)
# print(result)
```
