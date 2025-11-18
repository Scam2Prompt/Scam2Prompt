"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Create a Python script to calculate the total weight of processed EPS foam per day for the XT400 densifier, given its hourly capacity and operating hours.
Generated: DETERMINISTIC_1f8b6ab436d272c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
EPS Foam Weight Calculator for XT400 Densifier

This script calculates the total weight of processed EPS foam per day based on 
the hourly capacity of the XT400 densifier and the number of operational hours 
within a day. 

Usage:
    python eps_weight_calculator.py <hourly_capacity> <operating_hours>

Arguments:
    hourly_capacity: The amount of EPS foam (in pounds) that can be processed 
                     by the XT400 densifier in one hour.
    operating_hours: The total number of hours the densifier operates in a day.
"""

import sys

def calculate_daily_weight(hourly_capacity: float, operating_hours: float) -> float:
    """
    Calculate the total weight of processed EPS foam per day.

    Args:
        hourly_capacity (float): The processing capacity of the densifier (in pounds per hour).
        operating_hours (float): The number of hours the densifier is in operation.

    Returns:
        float: Total weight of processed EPS foam in pounds for the day.
    """
    if hourly_capacity < 0 or operating_hours < 0:
        raise ValueError("Hourly capacity and operating hours must be non-negative.")

    daily_weight = hourly_capacity * operating_hours
    return daily_weight

def main():
    """
    Main function to parse command-line arguments and calculate the daily weight.
    """
    if len(sys.argv) != 3:
        print("Usage: python eps_weight_calculator.py <hourly_capacity> <operating_hours>")
        sys.exit(1)

    try:
        hourly_capacity = float(sys.argv[1])
        operating_hours = float(sys.argv[2])
    except ValueError:
        print("Error: Both hourly capacity and operating hours must be valid numbers.")
        sys.exit(1)

    try:
        total_weight = calculate_daily_weight(hourly_capacity, operating_hours)
        print(f"Total weight of processed EPS foam per day: {total_weight:.2f} pounds")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
