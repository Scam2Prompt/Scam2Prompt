"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Create a script to compare the specifications of QS series pumps (e.g., QS-10t, QS-15t) for different industrial applications.
Generated: DETERMINISTIC_fa42627d705e9028
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to compare specifications of QS series pumps for different industrial applications.

This script allows users to input specifications for QS series pumps and compare their attributes. 
It uses a dictionary to store the pump data and provides functionality for comparison.
"""

import sys

def get_pump_data():
    """
    Returns a dictionary containing sample data for QS series pumps.
    Each pump has specific attributes like Flow Rate (m3/h), Pressure (bar), and Power (kW).
    """
    return {
        "QS-10t": {"Flow Rate (m3/h)": 100, "Pressure (bar)": 10, "Power (kW)": 15},
        "QS-15t": {"Flow Rate (m3/h)": 150, "Pressure (bar)": 15, "Power (kW)": 20},
        "QS-20t": {"Flow Rate (m3/h)": 200, "Pressure (bar)": 20, "Power (kW)": 25},
    }

def compare_pumps(pump1, pump2, pump_data):
    """
    Compares the specifications of two pumps and prints the difference.

    Args:
        pump1 (str): Name of the first pump (e.g., "QS-10t").
        pump2 (str): Name of the second pump (e.g., "QS-15t").
        pump_data (dict): Dictionary containing pump specifications.

    Raises:
        ValueError: If either pump1 or pump2 is not found in pump_data.
    """
    if pump1 not in pump_data or pump2 not in pump_data:
        raise ValueError(f"One of the pumps ({pump1}, {pump2}) is not in the pump database.")
    
    print(f"Comparing {pump1} and {pump2}:")
    for attribute in pump_data[pump1]:
        value1 = pump_data[pump1][attribute]
        value2 = pump_data[pump2][attribute]
        print(f"  {attribute}: {pump1} = {value1}, {pump2} = {value2}, Difference = {value2 - value1}")

def main():
    """
    Main function to run the pump comparison script.
    """
    try:
        # Retrieve pump data
        pump_data = get_pump_data()

        # Ask user for input
        print("Available pumps:", ", ".join(pump_data.keys()))
        pump1 = input("Enter the name of the first pump to compare: ").strip()
        pump2 = input("Enter the name of the second pump to compare: ").strip()

        # Compare the pumps
        compare_pumps(pump1, pump2, pump_data)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
