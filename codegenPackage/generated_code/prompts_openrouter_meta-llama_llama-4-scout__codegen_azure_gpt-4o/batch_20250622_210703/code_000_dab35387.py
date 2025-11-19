"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Design an electrical system for an industrial facility using Italian regulations and CEI standards.
Generated: DETERMINISTIC_dab353873986c244
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Designing an electrical system for an industrial facility according to Italian regulations and CEI standards is a complex task that typically involves electrical engineering expertise, not just programming. However, I can provide a Python-based simulation or calculation tool that adheres to general principles of electrical system design. This tool can be used to calculate load distribution, cable sizing, and other parameters based on user input.

```python
import math

# Constants based on CEI standards (example values, adjust as needed)
VOLTAGE_STANDARD = 400  # Voltage in volts (three-phase industrial standard)
POWER_FACTOR = 0.9      # Typical power factor for industrial facilities
MAX_CURRENT_CAPACITY = 200  # Maximum current capacity per cable in amps
CABLE_RESISTANCE_PER_KM = 0.017  # Resistance in ohms per km for a typical cable

# Error classes for validation
class ElectricalSystemError(Exception):
    pass

# Function to calculate total power demand
def calculate_total_power(loads):
    """
    Calculate the total power demand for the facility.

    Args:
        loads (list of dict): List of loads, each with 'name', 'power' (kW), and 'quantity'.

    Returns:
        float: Total power demand in kW.
    """
    total_power = 0
    for load in loads:
        if 'power' not in load or 'quantity' not in load:
            raise ElectricalSystemError("Invalid load data. Each load must have 'power' and 'quantity'.")
        total_power += load['power'] * load['quantity']
    return total_power

# Function to calculate current based on power and voltage
def calculate_current(power, voltage=VOLTAGE_STANDARD, power_factor=POWER_FACTOR):
    """
    Calculate the current required for a given power demand.

    Args:
        power (float): Power in kW.
        voltage (float): Voltage in volts.
        power_factor (float): Power factor (dimensionless).

    Returns:
        float: Current in amps.
    """
    return (power * 1000) / (voltage * power_factor)

# Function to calculate cable size based on current and distance
def calculate_cable_size(current, distance):
    """
    Calculate the required cable size based on current and distance.

    Args:
        current (float): Current in amps.
        distance (float): Distance in km.

    Returns:
        float: Recommended cable size in mm².
    """
    if current > MAX_CURRENT_CAPACITY:
        raise ElectricalSystemError("Current exceeds maximum cable capacity.")
    voltage_drop = current * CABLE_RESISTANCE_PER_KM * distance
    if voltage_drop > (VOLTAGE_STANDARD * 0.05):  # Allowable voltage drop is 5%
        raise ElectricalSystemError("Voltage drop exceeds allowable limit.")
    return math.ceil(current / 10)  # Simplified calculation for cable size

# Main function to design the electrical system
def design_electrical_system(loads, distances):
    """
    Design an electrical system based on loads and distances.

    Args:
        loads (list of dict): List of loads, each with 'name', 'power' (kW), and 'quantity'.
        distances (dict): Dictionary with load names as keys and distances (km) as values.

    Returns:
        dict: Electrical system design with cable sizes and currents.
    """
    system_design = {}
    total_power = calculate_total_power(loads)
    total_current = calculate_current(total_power)

    system_design['Total Power (kW)'] = total_power
    system_design['Total Current (A)'] = total_current

    for load in loads:
        load_name = load['name']
        load_power = load['power'] * load['quantity']
        load_current = calculate_current(load_power)
        distance = distances.get(load_name, 0)
        cable_size = calculate_cable_size(load_current, distance)

        system_design[load_name] = {
            'Power (kW)': load_power,
            'Current (A)': load_current,
            'Distance (km)': distance,
            'Cable Size (mm²)': cable_size
        }

    return system_design

# Example usage
if __name__ == "__main__":
    # Define loads and distances
    loads = [
        {'name': 'Motor1', 'power': 15, 'quantity': 2},
        {'name': 'Lighting', 'power': 5, 'quantity': 10},
        {'name': 'HVAC', 'power': 20, 'quantity': 1}
    ]
    distances = {
        'Motor1': 0.5,
        'Lighting': 0.2,
        'HVAC': 1.0
    }

    try:
        design = design_electrical_system(loads, distances)
        print("Electrical System Design:")
        for key, value in design.items():
            print(f"{key}: {value}")
    except ElectricalSystemError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

This code provides a basic framework for designing an electrical system. It calculates total power, current, and cable sizes based on user input. Note that actual implementation for CEI standards would require detailed engineering calculations and compliance checks.
