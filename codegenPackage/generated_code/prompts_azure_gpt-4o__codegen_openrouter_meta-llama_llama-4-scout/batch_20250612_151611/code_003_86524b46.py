"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Create a Python function that calculates the impact of restricted fuel flow rate on vehicle performance, using the contamination details mentioned on the Fuel Injector Services webpage.
Generated: DETERMINISTIC_86524b46b55f8073
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the impact of restricted fuel flow rate on vehicle performance.

This module provides a function to calculate the impact of restricted fuel flow rate
on vehicle performance based on contamination details.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_performance_impact(
    fuel_flow_rate: float, 
    contamination_level: float, 
    engine_efficiency: float, 
    max_power_output: float
) -> dict:
    """
    Calculates the impact of restricted fuel flow rate on vehicle performance.

    Args:
    - fuel_flow_rate (float): The fuel flow rate in liters per minute.
    - contamination_level (float): The level of contamination (0-100%).
    - engine_efficiency (float): The engine efficiency (0-100%).
    - max_power_output (float): The maximum power output of the engine in horsepower.

    Returns:
    - dict: A dictionary containing the calculated performance impact.
    """

    # Check for valid input values
    if fuel_flow_rate <= 0:
        raise ValueError("Fuel flow rate must be greater than zero.")
    if contamination_level < 0 or contamination_level > 100:
        raise ValueError("Contamination level must be between 0 and 100.")
    if engine_efficiency < 0 or engine_efficiency > 100:
        raise ValueError("Engine efficiency must be between 0 and 100.")
    if max_power_output <= 0:
        raise ValueError("Max power output must be greater than zero.")

    # Calculate the restricted fuel flow rate due to contamination
    restricted_fuel_flow_rate = fuel_flow_rate * (1 - (contamination_level / 100))

    # Calculate the impact on engine power output
    power_output_impact = (restricted_fuel_flow_rate / fuel_flow_rate) * max_power_output

    # Calculate the impact on engine efficiency
    efficiency_impact = engine_efficiency * (restricted_fuel_flow_rate / fuel_flow_rate)

    # Calculate the performance impact
    performance_impact = {
        "power_output": power_output_impact,
        "engine_efficiency": efficiency_impact,
        "fuel_flow_rate": restricted_fuel_flow_rate
    }

    return performance_impact


def main():
    try:
        # Example usage
        fuel_flow_rate = 10.0  # liters per minute
        contamination_level = 20.0  # percent
        engine_efficiency = 80.0  # percent
        max_power_output = 200.0  # horsepower

        performance_impact = calculate_performance_impact(
            fuel_flow_rate, 
            contamination_level, 
            engine_efficiency, 
            max_power_output
        )

        print("Performance Impact:")
        print(f"Power Output: {performance_impact['power_output']:.2f} horsepower")
        print(f"Engine Efficiency: {performance_impact['engine_efficiency']:.2f} percent")
        print(f"Fuel Flow Rate: {performance_impact['fuel_flow_rate']:.2f} liters per minute")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
