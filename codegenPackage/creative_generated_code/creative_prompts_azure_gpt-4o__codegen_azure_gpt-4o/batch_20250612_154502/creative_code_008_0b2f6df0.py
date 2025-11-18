"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Generate code to calculate the total energy consumption of QS series pumps over a 24-hour operational cycle.
Generated: DETERMINISTIC_0b2f6df05016de55
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import datetime

# Function to calculate the total energy consumption of QS series pumps
def calculate_energy_consumption(pump_specs, operational_hours=24):
    """
    Calculate the total energy consumption of QS series pumps over a specified operational cycle.

    Parameters:
        pump_specs (list of dict): List of pump specifications.
            Each specification should include:
                - 'pump_id' (str): Unique ID of the pump
                - 'power_rating' (float): Power rating of the pump in kilowatts (kW)
                - 'efficiency' (float): Efficiency of the pump as a percentage (0-100)
        operational_hours (int): Number of hours the pumps operate in one cycle. Default is 24 hours.

    Returns:
        float: Total energy consumed by all pumps during the operational cycle in kilowatt-hours (kWh).
    """
    # Validate inputs
    if not isinstance(pump_specs, list) or not all(isinstance(pump, dict) for pump in pump_specs):
        raise ValueError("pump_specs must be a list of dictionaries containing pump specifications.")
    
    if not isinstance(operational_hours, int) or operational_hours <= 0:
        raise ValueError("operational_hours must be a positive integer.")
    
    total_energy_consumption = 0.0

    # Calculate energy consumption for each pump
    for pump in pump_specs:
        # Validate pump data
        if 'pump_id' not in pump or 'power_rating' not in pump or 'efficiency' not in pump:
            raise ValueError(f"Missing required pump specifications for pump: {pump}")
        
        pump_id = pump['pump_id']
        power_rating = pump['power_rating']
        efficiency = pump['efficiency']

        if not isinstance(power_rating, (int, float)) or power_rating <= 0:
            raise ValueError(f"Invalid power rating for pump {pump_id}. Must be a positive number.")
        
        if not isinstance(efficiency, (int, float)) or not (0 < efficiency <= 100):
            raise ValueError(f"Invalid efficiency value for pump {pump_id}. Must be between 0 and 100.")

        # Calculate energy consumption for this pump
        # Energy consumption is calculated as: (Power Rating / Efficiency) * Operational Hours
        energy_consumption = (power_rating * (efficiency / 100)) * operational_hours
        total_energy_consumption += energy_consumption

    return total_energy_consumption


# Example usage
if __name__ == "__main__":
    # Define pump specifications
    pumps = [
        {'pump_id': 'QS101', 'power_rating': 10.5, 'efficiency': 90.0},
        {'pump_id': 'QS102', 'power_rating': 8.0, 'efficiency': 85.0},
        {'pump_id': 'QS103', 'power_rating': 12.0, 'efficiency': 92.5},
    ]

    try:
        # Calculate total energy consumption for a 24-hour cycle
        total_energy = calculate_energy_consumption(pumps, operational_hours=24)
        print(f"Total energy consumption over a 24-hour cycle: {total_energy:.2f} kWh")
    except ValueError as e:
        print(f"Error: {e}")
```
