"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Create a Python function that simulates the runtime of a Predator generator (e.g., 4550W model from Haro Outlet) based on fuel tank capacity and load percentage.
Generated: DETERMINISTIC_8ad6145bda397bd0
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def simulate_generator_runtime(fuel_tank_capacity_liters, load_percentage, fuel_consumption_rate=0.3):
    """
    Simulates the runtime of a generator based on fuel tank capacity and load percentage.
    
    :param fuel_tank_capacity_liters: Capacity of the fuel tank in liters (float).
    :param load_percentage: Load percentage the generator is running at (0 to 100, float).
    :param fuel_consumption_rate: Fuel consumption rate (liters per hour at 100% load, default: 0.3).
    
    :return: Estimated runtime in hours (float).
    
    Raises:
        ValueError: If inputs are out of valid range or invalid types.
    """
    try:
        # Input validation
        if not isinstance(fuel_tank_capacity_liters, (int, float)) or fuel_tank_capacity_liters <= 0:
            raise ValueError("Fuel tank capacity must be a positive number.")
        if not isinstance(load_percentage, (int, float)) or not (0 <= load_percentage <= 100):
            raise ValueError("Load percentage must be a number between 0 and 100.")
        
        # Calculating fuel consumption based on load percentage
        adjusted_fuel_consumption = fuel_consumption_rate * (load_percentage / 100)
        
        # Avoid division by zero
        if adjusted_fuel_consumption <= 0:
            raise ValueError("Adjusted fuel consumption is zero or negative. Check the input values.")
        
        # Calculate runtime
        runtime_hours = fuel_tank_capacity_liters / adjusted_fuel_consumption
        
        # Return rounded runtime to 2 decimal places
        return round(runtime_hours, 2)
    
    except ValueError as ve:
        # Handle specific input validation errors
        raise ve
    
    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")


# Example usage:
# Assuming a generator with a 4550W model running at 75% load and a 12-liter fuel tank.
if __name__ == "__main__":
    try:
        fuel_tank_capacity = 12  # liters
        load_percentage = 75  # percent
        runtime = simulate_generator_runtime(fuel_tank_capacity, load_percentage)
        print(f"Estimated runtime: {runtime} hours")
    except Exception as e:
        print(f"Error: {e}")
```
