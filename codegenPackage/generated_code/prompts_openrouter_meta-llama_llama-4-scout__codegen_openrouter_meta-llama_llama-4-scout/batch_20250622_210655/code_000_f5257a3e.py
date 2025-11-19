"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Write a Python code snippet to calculate the amount of DEF required for a BS-VI diesel engine vehicle equipped with SCR technology.
Generated: DETERMINISTIC_f5257a3ebdf7ac0c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_def_consumption(vehicle_type: str, engine_capacity: float, 
                             annual_mileage: float, def_consumption_rate: float = 0.05) -> float:
    """
    Calculate the amount of DEF (Diesel Exhaust Fluid) required for a BS-VI diesel engine vehicle equipped with SCR technology.

    Args:
    - vehicle_type (str): Type of vehicle (e.g., truck, bus, etc.)
    - engine_capacity (float): Engine capacity in liters
    - annual_mileage (float): Annual mileage in kilometers
    - def_consumption_rate (float, optional): DEF consumption rate in liters per kilometer. Defaults to 0.05.

    Returns:
    - float: Annual DEF consumption in liters
    """

    # Validate input parameters
    if not isinstance(vehicle_type, str) or not vehicle_type.strip():
        raise ValueError("Invalid vehicle type")
    if not isinstance(engine_capacity, (int, float)) or engine_capacity <= 0:
        raise ValueError("Invalid engine capacity")
    if not isinstance(annual_mileage, (int, float)) or annual_mileage < 0:
        raise ValueError("Invalid annual mileage")
    if not isinstance(def_consumption_rate, (int, float)) or def_consumption_rate < 0:
        raise ValueError("Invalid DEF consumption rate")

    # Calculate DEF consumption
    try:
        def_consumption = annual_mileage * def_consumption_rate
        return def_consumption
    except Exception as e:
        # Log and re-raise the exception
        print(f"An error occurred: {str(e)}")
        raise


def main():
    vehicle_type = "Truck"
    engine_capacity = 10.0  # liters
    annual_mileage = 100000.0  # kilometers

    try:
        def_required = calculate_def_consumption(vehicle_type, engine_capacity, annual_mileage)
        print(f"The annual DEF consumption for a {vehicle_type} with {engine_capacity}L engine is: {def_required:.2f} liters")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
