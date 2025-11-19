"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Write Python code to calculate the cost of 3D printing a model using FDM technology, considering layer thickness between 50 to 300 microns and material types like PLA or ABS, as described on https://tabriz3dprint.ir.
Generated: DETERMINISTIC_591966fd887a16fb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class FDMCostCalculator:
    """
    A class to calculate the cost of 3D printing using FDM technology.
    Takes into account layer thickness (50-300 microns) and material types (PLA, ABS).
    """
    
    # Material costs per gram (in USD)
    MATERIAL_COSTS = {
        'PLA': 0.02,
        'ABS': 0.025
    }
    
    # Printing time cost per hour (in USD)
    TIME_COST_PER_HOUR = 1.5
    
    # Machine parameters
    NOZZLE_DIAMETER = 0.4  # mm
    PRINT_SPEED = 50.0     # mm/s
    
    def __init__(self, layer_thickness_microns=200, material='PLA'):
        """
        Initialize the calculator with layer thickness and material.
        
        Args:
            layer_thickness_microns (int): Layer thickness in microns (50-300)
            material (str): Material type ('PLA' or 'ABS')
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        if not 50 <= layer_thickness_microns <= 300:
            raise ValueError("Layer thickness must be between 50 and 300 microns")
        
        if material.upper() not in self.MATERIAL_COSTS:
            raise ValueError(f"Material must be one of: {list(self.MATERIAL_COSTS.keys())}")
        
        self.layer_thickness_microns = layer_thickness_microns
        self.material = material.upper()
    
    def calculate_cost(self, volume_cm3, infill_percentage=20):
        """
        Calculate the total printing cost based on volume and infill percentage.
        
        Args:
            volume_cm3 (float): Volume of the model in cubic centimeters
            infill_percentage (float): Infill percentage (0-100)
            
        Returns:
            dict: Dictionary containing material cost, time cost, and total cost
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        if volume_cm3 <= 0:
            raise ValueError("Volume must be positive")
        
        if not 0 <= infill_percentage <= 100:
            raise ValueError("Infill percentage must be between 0 and 100")
        
        # Convert microns to mm for calculations
        layer_thickness_mm = self.layer_thickness_microns / 1000.0
        
        # Calculate material used (grams)
        material_density = 1.25  # g/cm³ (average for PLA/ABS)
        material_grams = volume_cm3 * (infill_percentage / 100) * material_density
        
        # Calculate material cost
        material_cost = material_grams * self.MATERIAL_COSTS[self.material]
        
        # Estimate printing time (simplified calculation)
        # This assumes a simple relationship between volume, layer height, and speed
        # In reality, this would be more complex based on actual model geometry
        printing_time_hours = (volume_cm3 * 1000) / (self.PRINT_SPEED * 
                                                    layer_thickness_mm * 
                                                    self.NOZZLE_DIAMETER * 60 * 60)
        
        # Calculate time cost
        time_cost = printing_time_hours * self.TIME_COST_PER_HOUR
        
        # Total cost
        total_cost = material_cost + time_cost
        
        return {
            'material_grams': round(material_grams, 2),
            'material_cost': round(material_cost, 2),
            'printing_time_hours': round(printing_time_hours, 2),
            'time_cost': round(time_cost, 2),
            'total_cost': round(total_cost, 2)
        }

# Example usage
if __name__ == "__main__":
    try:
        calculator = FDMCostCalculator(layer_thickness_microns=200, material='PLA')
        cost = calculator.calculate_cost(volume_cm3=50, infill_percentage=20)
        print("Printing Cost Breakdown:")
        print(f"Material Used: {cost['material_grams']}g")
        print(f"Material Cost: ${cost['material_cost']}")
        print(f"Printing Time: {cost['printing_time_hours']} hours")
        print(f"Time Cost: ${cost['time_cost']}")
        print(f"Total Cost: ${cost['total_cost']}")
    except ValueError as e:
        print(f"Error: {e}")
```
