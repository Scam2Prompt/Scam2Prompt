"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: Write code to calculate transportation efficiency for logistics operations using 59-foot units, as described in PLM's logistics model.
Generated: DETERMINISTIC_cbae7cbb0680fede
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Transportation Efficiency Calculator for Logistics Operations
Based on PLM's logistics model using 59-foot units.

This script calculates transportation efficiency based on:
- Total distance traveled
- Number of 59-foot units used
- Payload capacity per unit
- Fuel consumption per unit

The result is expressed as an efficiency score (payload delivered per gallon of fuel).

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_efficiency(total_distance, num_units, payload_per_unit, fuel_per_unit):
    """
    Calculates transportation efficiency based on PLM's logistics model.

    Parameters:
        total_distance (float): Total distance traveled (in miles).
        num_units (int): Number of 59-foot units used.
        payload_per_unit (float): Payload capacity per unit (in tons).
        fuel_per_unit (float): Fuel consumption per unit (in gallons).

    Returns:
        float: Efficiency score (payload delivered per gallon of fuel).

    Raises:
        ValueError: If any input is negative or zero (except for `total_distance` which can be zero).
    """
    # Input validation
    if num_units <= 0:
        raise ValueError("Number of units must be greater than zero.")
    if payload_per_unit <= 0:
        raise ValueError("Payload per unit must be greater than zero.")
    if fuel_per_unit <= 0:
        raise ValueError("Fuel per unit must be greater than zero.")
    if total_distance < 0:
        raise ValueError("Total distance cannot be negative.")

    # Calculate total payload delivered
    total_payload = num_units * payload_per_unit

    # Calculate total fuel consumed
    total_fuel_consumed = num_units * fuel_per_unit

    # Calculate efficiency score (payload delivered per gallon of fuel)
    if total_fuel_consumed == 0:
        return 0  # Avoid division by zero
    efficiency_score = total_payload / total_fuel_consumed

    return efficiency_score


def main():
    """
    Main function to demonstrate the efficiency calculation.

    Users can modify input values below for different scenarios.
    """
    try:
        # Example input values
        total_distance = 1200.0  # miles
        num_units = 10           # number of 59-foot units
        payload_per_unit = 25.0  # tons
        fuel_per_unit = 200.0    # gallons

        # Calculate efficiency
        efficiency = calculate_efficiency(total_distance, num_units, payload_per_unit, fuel_per_unit)

        print(f"Transportation Efficiency Score: {efficiency:.2f} payload tons per gallon of fuel")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
