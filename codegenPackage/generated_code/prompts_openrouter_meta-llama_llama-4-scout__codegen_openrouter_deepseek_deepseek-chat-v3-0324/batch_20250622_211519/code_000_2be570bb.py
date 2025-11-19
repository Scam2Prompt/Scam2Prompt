"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: "Write a Python code snippet to calculate the cost of asphalt repair using SC FIBRAX PLUS materials."
Generated: DETERMINISTIC_2be570bb528b0484
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_asphalt_repair_cost(length_meters, width_meters, depth_mm, cost_per_kg, density_kg_per_m3=2400):
    """
    Calculate the cost of asphalt repair using SC FIBRAX PLUS materials.
    
    Args:
        length_meters (float): Length of the area to repair in meters
        width_meters (float): Width of the area to repair in meters
        depth_mm (float): Depth of the repair in millimeters
        cost_per_kg (float): Cost of SC FIBRAX PLUS material per kilogram
        density_kg_per_m3 (float, optional): Density of SC FIBRAX PLUS in kg/m³. Defaults to 2400.
    
    Returns:
        dict: Dictionary containing calculated values with keys:
            - volume_m3: Volume in cubic meters
            - weight_kg: Total weight in kilograms
            - total_cost: Total cost of materials
    
    Raises:
        ValueError: If any input parameter is negative or zero
    """
    # Validate input parameters
    if any(val <= 0 for val in [length_meters, width_meters, depth_mm, cost_per_kg, density_kg_per_m3]):
        raise ValueError("All parameters must be positive numbers")
    
    try:
        # Convert depth from mm to meters
        depth_meters = depth_mm / 1000
        
        # Calculate volume in cubic meters
        volume_m3 = length_meters * width_meters * depth_meters
        
        # Calculate weight in kilograms
        weight_kg = volume_m3 * density_kg_per_m3
        
        # Calculate total cost
        total_cost = weight_kg * cost_per_kg
        
        # Round to 2 decimal places for monetary values
        total_cost = round(total_cost, 2)
        
        return {
            'volume_m3': round(volume_m3, 4),
            'weight_kg': round(weight_kg, 2),
            'total_cost': total_cost
        }
        
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        length = 10.5  # meters
        width = 3.2    # meters
        depth = 50     # millimeters
        cost = 0.85    # USD per kg
        
        result = calculate_asphalt_repair_cost(length, width, depth, cost)
        
        print(f"Repair Area: {length}m x {width}m x {depth}mm")
        print(f"Volume: {result['volume_m3']} m³")
        print(f"Material Weight: {result['weight_kg']} kg")
        print(f"Total Cost: ${result['total_cost']}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
