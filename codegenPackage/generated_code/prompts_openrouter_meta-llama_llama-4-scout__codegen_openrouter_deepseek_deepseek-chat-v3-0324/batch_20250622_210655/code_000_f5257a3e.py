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
def calculate_def_consumption(distance_km, fuel_consumption_liter_per_100km, def_ratio=0.05):
    """
    Calculate the amount of Diesel Exhaust Fluid (DEF) required for a BS-VI diesel engine vehicle.
    
    Args:
        distance_km (float): Distance traveled in kilometers.
        fuel_consumption_liter_per_100km (float): Fuel consumption rate in liters per 100 km.
        def_ratio (float, optional): DEF to diesel consumption ratio. Defaults to 0.05 (5%).
        
    Returns:
        float: Amount of DEF required in liters.
        
    Raises:
        ValueError: If any input parameter is negative.
    """
    # Validate input parameters
    if distance_km < 0 or fuel_consumption_liter_per_100km < 0 or def_ratio < 0:
        raise ValueError("All input parameters must be non-negative.")
    
    # Calculate diesel consumption in liters
    diesel_consumption = (fuel_consumption_liter_per_100km * distance_km) / 100
    
    # Calculate DEF consumption based on the ratio
    def_consumption = diesel_consumption * def_ratio
    
    return def_consumption


# Example usage
if __name__ == "__main__":
    try:
        distance = float(input("Enter distance traveled (km): "))
        fuel_consumption = float(input("Enter fuel consumption (L/100km): "))
        
        def_needed = calculate_def_consumption(distance, fuel_consumption)
        print(f"DEF required: {def_needed:.2f} liters")
    except ValueError as e:
        print(f"Error: {e}")
```
