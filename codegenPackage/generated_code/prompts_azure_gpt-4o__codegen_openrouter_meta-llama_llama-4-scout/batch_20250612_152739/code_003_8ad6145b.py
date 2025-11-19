"""
Generated Code Metadata:
========================
Original URL: https://herramientasharo.shop
Prompt: Create a Python function that simulates the runtime of a Predator generator (e.g., 4550W model from Haro Outlet) based on fuel tank capacity and load percentage.
Generated: DETERMINISTIC_8ad6145bda397bd0
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_predator_runtime(tank_capacity_liters, load_percentage, fuel_efficiency_gph):
    """
    Calculates the runtime of a Predator generator based on fuel tank capacity and load percentage.

    Args:
        tank_capacity_liters (float): The capacity of the fuel tank in liters.
        load_percentage (float): The load percentage of the generator (0-100).
        fuel_efficiency_gph (float): The fuel efficiency of the generator in gallons per hour.

    Returns:
        float: The runtime of the generator in hours.

    Raises:
        ValueError: If tank_capacity_liters, load_percentage, or fuel_efficiency_gph is not a positive number.
    """

    # Validate input values
    if tank_capacity_liters <= 0:
        raise ValueError("Tank capacity must be a positive number.")
    if load_percentage < 0 or load_percentage > 100:
        raise ValueError("Load percentage must be between 0 and 100.")
    if fuel_efficiency_gph <= 0:
        raise ValueError("Fuel efficiency must be a positive number.")

    # Convert tank capacity from liters to gallons (1 gallon = 3.785 liters)
    tank_capacity_gallons = tank_capacity_liters / 3.785

    # Adjust fuel efficiency based on load percentage (assuming linear relationship)
    adjusted_fuel_efficiency_gph = fuel_efficiency_gph * (load_percentage / 100)

    # Calculate runtime
    runtime_hours = tank_capacity_gallons / adjusted_fuel_efficiency_gph

    return runtime_hours


def main():
    try:
        # Example usage
        tank_capacity_liters = 12.7  # 4550W Predator generator tank capacity
        load_percentage = 50  # 50% load
        fuel_efficiency_gph = 0.8  # fuel efficiency at 100% load

        runtime_hours = calculate_predator_runtime(tank_capacity_liters, load_percentage, fuel_efficiency_gph)
        print(f"The runtime of the generator is {runtime_hours:.2f} hours.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
