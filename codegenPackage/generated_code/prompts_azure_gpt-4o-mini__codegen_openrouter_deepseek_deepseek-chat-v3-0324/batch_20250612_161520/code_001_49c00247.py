"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Write a code snippet that calculates the thermal resistance of different types of refractory bricks provided by Aprisacv, including high alumina and silico-aluminous options.
Generated: DETERMINISTIC_49c002474074f53d
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RefractoryBrick:
    """
    A class to represent a refractory brick and calculate its thermal resistance.
    """
    
    def __init__(self, name: str, thermal_conductivity: float, thickness: float):
        """
        Initialize the refractory brick with its properties.
        
        Args:
            name (str): Name of the brick type (e.g., "High Alumina", "Silico-Aluminous")
            thermal_conductivity (float): Thermal conductivity of the brick (W/m·K)
            thickness (float): Thickness of the brick (meters)
        """
        self.name = name
        self.thermal_conductivity = thermal_conductivity
        self.thickness = thickness
        
    def calculate_thermal_resistance(self) -> float:
        """
        Calculate the thermal resistance of the brick.
        
        Returns:
            float: Thermal resistance in m²·K/W
            
        Raises:
            ValueError: If thermal_conductivity or thickness is non-positive.
        """
        if self.thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be positive.")
        if self.thickness <= 0:
            raise ValueError("Thickness must be positive.")
            
        return self.thickness / self.thermal_conductivity


def main():
    # Example usage with Aprisacv brick types
    bricks = [
        RefractoryBrick("High Alumina", 1.5, 0.1),  # Example values
        RefractoryBrick("Silico-Aluminous", 1.2, 0.1)  # Example values
    ]
    
    for brick in bricks:
        try:
            resistance = brick.calculate_thermal_resistance()
            print(f"{brick.name} brick - Thermal Resistance: {resistance:.4f} m²·K/W")
        except ValueError as e:
            print(f"Error calculating for {brick.name}: {e}")


if __name__ == "__main__":
    main()
```
