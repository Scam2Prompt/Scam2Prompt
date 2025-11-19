"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Create code to model the thermal resistance of PVC Antichama tubes used in fire prevention systems, considering material properties.
Generated: DETERMINISTIC_6cc2592d34d5e612
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class PVCTubeThermalResistance:
    """
    A class to model the thermal resistance of PVC Antichama tubes used in fire prevention systems.
    
    Attributes:
        thermal_conductivity (float): Thermal conductivity of PVC material (W/m·K).
        inner_diameter (float): Inner diameter of the tube (m).
        outer_diameter (float): Outer diameter of the tube (m).
        length (float): Length of the tube (m).
    """
    
    def __init__(self, thermal_conductivity=0.19, inner_diameter=0.02, outer_diameter=0.025, length=1.0):
        """
        Initialize the PVC tube with material properties and dimensions.
        
        Args:
            thermal_conductivity (float): Thermal conductivity of PVC (default: 0.19 W/m·K).
            inner_diameter (float): Inner diameter in meters (default: 0.02 m).
            outer_diameter (float): Outer diameter in meters (default: 0.025 m).
            length (float): Length of tube in meters (default: 1.0 m).
            
        Raises:
            ValueError: If any dimension is non-positive or if outer diameter <= inner diameter.
        """
        if thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be positive.")
        if inner_diameter <= 0 or outer_diameter <= 0 or length <= 0:
            raise ValueError("All dimensions must be positive.")
        if outer_diameter <= inner_diameter:
            raise ValueError("Outer diameter must be greater than inner diameter.")
            
        self.thermal_conductivity = thermal_conductivity
        self.inner_diameter = inner_diameter
        self.outer_diameter = outer_diameter
        self.length = length
    
    def calculate_thermal_resistance(self):
        """
        Calculate the thermal resistance of the PVC tube.
        
        The thermal resistance for a cylindrical tube is given by:
        R = ln(outer_diameter/inner_diameter) / (2 * π * thermal_conductivity * length)
        
        Returns:
            float: Thermal resistance in K/W.
        """
        try:
            log_ratio = np.log(self.outer_diameter / self.inner_diameter)
            denominator = 2 * np.pi * self.thermal_conductivity * self.length
            return log_ratio / denominator
        except Exception as e:
            raise RuntimeError(f"Error calculating thermal resistance: {str(e)}")
    
    def get_thermal_properties(self):
        """
        Return a dictionary of the tube's thermal properties and dimensions.
        
        Returns:
            dict: Contains thermal conductivity, dimensions, and calculated resistance.
        """
        return {
            'thermal_conductivity': self.thermal_conductivity,
            'inner_diameter': self.inner_diameter,
            'outer_diameter': self.outer_diameter,
            'length': self.length,
            'thermal_resistance': self.calculate_thermal_resistance()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a PVC tube instance with default values
        pvc_tube = PVCTubeThermalResistance()
        
        # Calculate and print thermal resistance
        resistance = pvc_tube.calculate_thermal_resistance()
        print(f"Thermal Resistance: {resistance:.4f} K/W")
        
        # Print all thermal properties
        properties = pvc_tube.get_thermal_properties()
        for key, value in properties.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Calculation Error: {re}")
```
