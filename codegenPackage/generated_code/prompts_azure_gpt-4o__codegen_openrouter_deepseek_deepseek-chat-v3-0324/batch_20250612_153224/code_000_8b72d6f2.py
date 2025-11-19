"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Write code to calculate the materials needed for constructing an armiranobetonska zaščitna podporna stena (reinforced concrete protective wall), including concrete volume and reinforcement requirements.
Generated: DETERMINISTIC_8b72d6f2dbae1c1a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ReinforcedConcreteWall:
    """
    Class to calculate materials needed for constructing a reinforced concrete protective wall.
    Calculates concrete volume and reinforcement requirements based on wall dimensions and design parameters.
    """
    
    def __init__(self, length, height, thickness, concrete_cover=0.05):
        """
        Initialize wall dimensions and parameters.
        
        Args:
            length (float): Wall length in meters
            height (float): Wall height in meters
            thickness (float): Wall thickness in meters
            concrete_cover (float): Concrete cover for reinforcement in meters (default: 0.05m)
        """
        self.length = length
        self.height = height
        self.thickness = thickness
        self.concrete_cover = concrete_cover
        
        # Validate inputs
        if any(dim <= 0 for dim in [length, height, thickness]):
            raise ValueError("All dimensions must be positive numbers")
        if concrete_cover < 0:
            raise ValueError("Concrete cover cannot be negative")
    
    def calculate_concrete_volume(self):
        """
        Calculate the volume of concrete needed for the wall.
        
        Returns:
            float: Concrete volume in cubic meters
        """
        return self.length * self.height * self.thickness
    
    def calculate_reinforcement(self, vertical_spacing=0.15, horizontal_spacing=0.15, 
                               vertical_bar_diameter=0.012, horizontal_bar_diameter=0.012):
        """
        Calculate reinforcement requirements for the wall.
        
        Args:
            vertical_spacing (float): Spacing between vertical bars in meters (default: 0.15m)
            horizontal_spacing (float): Spacing between horizontal bars in meters (default: 0.15m)
            vertical_bar_diameter (float): Diameter of vertical bars in meters (default: 0.012m)
            horizontal_bar_diameter (float): Diameter of horizontal bars in meters (default: 0.012m)
            
        Returns:
            dict: Dictionary containing:
                - vertical_bars_count: Number of vertical bars
                - horizontal_bars_count: Number of horizontal bars
                - vertical_steel_length: Total length of vertical steel in meters
                - horizontal_steel_length: Total length of horizontal steel in meters
                - vertical_steel_weight: Total weight of vertical steel in kg
                - horizontal_steel_weight: Total weight of horizontal steel in kg
        """
        # Validate inputs
        if any(spacing <= 0 for spacing in [vertical_spacing, horizontal_spacing]):
            raise ValueError("Bar spacing must be positive numbers")
        if any(diameter <= 0 for diameter in [vertical_bar_diameter, horizontal_bar_diameter]):
            raise ValueError("Bar diameters must be positive numbers")
        
        # Calculate number of bars
        vertical_bars = math.ceil(self.length / vertical_spacing) + 1
        horizontal_bars = math.ceil(self.height / horizontal_spacing) + 1
        
        # Calculate total bar lengths
        vertical_length = vertical_bars * self.height
        horizontal_length = horizontal_bars * self.length
        
        # Calculate steel weights (7850 kg/m³ density, πr² cross-section)
        vertical_weight = (math.pi * (vertical_bar_diameter/2)**2) * vertical_length * 7850
        horizontal_weight = (math.pi * (horizontal_bar_diameter/2)**2) * horizontal_length * 7850
        
        return {
            'vertical_bars_count': vertical_bars,
            'horizontal_bars_count': horizontal_bars,
            'vertical_steel_length': vertical_length,
            'horizontal_steel_length': horizontal_length,
            'vertical_steel_weight': vertical_weight,
            'horizontal_steel_weight': horizontal_weight
        }
    
    def generate_materials_report(self):
        """
        Generate a comprehensive report of all materials needed for the wall.
        
        Returns:
            dict: Dictionary containing concrete volume and reinforcement details
        """
        concrete = self.calculate_concrete_volume()
        reinforcement = self.calculate_reinforcement()
        
        return {
            'concrete_volume_m3': concrete,
            'reinforcement': reinforcement
        }


# Example usage
if __name__ == "__main__":
    try:
        wall = ReinforcedConcreteWall(length=10.0, height=3.0, thickness=0.3)
        report = wall.generate_materials_report()
        
        print("Materials Report:")
        print(f"Concrete Volume: {report['concrete_volume_m3']:.2f} m³")
        print("\nReinforcement Details:")
        print(f"Vertical Bars: {report['reinforcement']['vertical_bars_count']} bars")
        print(f"Horizontal Bars: {report['reinforcement']['horizontal_bars_count']} bars")
        print(f"Vertical Steel Length: {report['reinforcement']['vertical_steel_length']:.2f} m")
        print(f"Horizontal Steel Length: {report['reinforcement']['horizontal_steel_length']:.2f} m")
        print(f"Vertical Steel Weight: {report['reinforcement']['vertical_steel_weight']:.2f} kg")
        print(f"Horizontal Steel Weight: {report['reinforcement']['horizontal_steel_weight']:.2f} kg")
    
    except ValueError as e:
        print(f"Error: {e}")
```
