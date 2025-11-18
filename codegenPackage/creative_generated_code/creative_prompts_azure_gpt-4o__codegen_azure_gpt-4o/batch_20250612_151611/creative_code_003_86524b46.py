"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Create a Python function that calculates the impact of restricted fuel flow rate on vehicle performance, using the contamination details mentioned on the Fuel Injector Services webpage.
Generated: DETERMINISTIC_86524b46b55f8073
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_vehicle_performance(fuel_flow_rate, contamination_level, engine_efficiency, max_power_output):
    """
    Calculate the impact of restricted fuel flow rate on vehicle performance.

    Parameters:
        fuel_flow_rate (float): The current fuel flow rate in liters per minute.
        contamination_level (float): The contamination level (percentage) affecting the fuel injectors (e.g., 0.2 for 20%).
        engine_efficiency (float): Efficiency of the engine as a decimal (e.g., 0.85 for 85% efficiency).
        max_power_output (float): Maximum power output of the vehicle in horsepower.

    Returns:
        dict: A dictionary containing:
            - adjusted_flow_rate (float): The reduced fuel flow rate due to contamination.
            - power_output (float): The adjusted power output in horsepower.
            - efficiency_loss (float): Efficiency loss due to contamination (percentage).
    """
    try:
        # Validate inputs
        if not (0 <= contamination_level <= 1):
            raise ValueError("Contamination level must be between 0 and 1 (inclusive).")
        if not (0 < engine_efficiency <= 1):
            raise ValueError("Engine efficiency must be greater than 0 and less than or equal to 1.")
        if fuel_flow_rate <= 0 or max_power_output <= 0:
            raise ValueError("Fuel flow rate and max power output must be positive values.")

        # Calculate the adjusted fuel flow rate based on contamination
        adjusted_flow_rate = fuel_flow_rate * (1 - contamination_level)

        # Calculate efficiency loss caused by contamination
        efficiency_loss = contamination_level * 100  # Convert to percentage

        # Calculate the adjusted power output
        power_output = max_power_output * (adjusted_flow_rate / fuel_flow_rate) * engine_efficiency

        return {
            "adjusted_flow_rate": adjusted_flow_rate,
            "power_output": round(power_output, 2),
            "efficiency_loss": round(efficiency_loss, 2)
        }

    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # Example test values
    fuel_flow_rate = 50.0  # liters per minute
    contamination_level = 0.15  # 15% contamination
    engine_efficiency = 0.85  # 85% efficient
    max_power_output = 300.0  # horsepower

    result = calculate_vehicle_performance(fuel_flow_rate, contamination_level, engine_efficiency, max_power_output)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Performance Impact Results:")
        print(f"Adjusted Fuel Flow Rate: {result['adjusted_flow_rate']} L/min")
        print(f"Adjusted Power Output: {result['power_output']} HP")
        print(f"Efficiency Loss: {result['efficiency_loss']}%")
```
