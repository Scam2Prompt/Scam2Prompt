"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Create a script to calculate the load requirements for EV charging stations with wallboxes, including load balancing features as recommended by Technische Installatiebedrijf van Boxtel.
Generated: DETERMINISTIC_3af840d9f3678d75
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
EV Charging Load Calculator with Load Balancing

This script calculates the load requirements for EV charging stations equipped 
with wallboxes. It includes load balancing to ensure the total power consumption 
does not exceed the maximum available capacity.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import sys

def calculate_load(ev_chargers, max_capacity):
    """
    Calculate the load requirements for EV chargers with load balancing.

    Args:
        ev_chargers (list[dict]): List of EV chargers with their power ratings.
            Each charger should be represented as a dictionary with keys:
            - 'id': Unique identifier for the charger.
            - 'max_power': Maximum power rating of the charger in kW.
        max_capacity (float): Maximum available capacity in kW.

    Returns:
        dict: A dictionary containing load allocation per charger and total load.
    """
    if not ev_chargers or max_capacity <= 0:
        raise ValueError("Invalid input: chargers list cannot be empty and max_capacity must be positive.")

    total_max_power = sum(charger['max_power'] for charger in ev_chargers)
    if total_max_power <= max_capacity:
        # No need for load balancing if total max power is within capacity
        return {
            "load_allocation": {charger['id']: charger['max_power'] for charger in ev_chargers},
            "total_load": total_max_power
        }

    # Load balancing required
    load_allocation = {}
    scaling_factor = max_capacity / total_max_power
    total_load = 0

    for charger in ev_chargers:
        allocated_power = charger['max_power'] * scaling_factor
        load_allocation[charger['id']] = round(allocated_power, 2)  # Round to 2 decimal places
        total_load += allocated_power

    return {
        "load_allocation": load_allocation,
        "total_load": round(total_load, 2)  # Round to 2 decimal places
    }


def main():
    """
    Main function to execute the EV charging load calculator.

    Prompts user for input, calculates load, and displays the results.
    """
    try:
        # Example EV chargers data
        ev_chargers = [
            {"id": "Charger1", "max_power": 22},  # 22 kW charger
            {"id": "Charger2", "max_power": 22},  # 22 kW charger
            {"id": "Charger3", "max_power": 11},  # 11 kW charger
        ]

        # Example maximum available capacity
        max_capacity = float(input("Enter the maximum available capacity in kW (e.g., 40): "))

        result = calculate_load(ev_chargers, max_capacity)

        # Display the results
        print("\nLoad Allocation:")
        for charger_id, load in result["load_allocation"].items():
            print(f"{charger_id}: {load} kW")
        print(f"\nTotal Load: {result['total_load']} kW")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
