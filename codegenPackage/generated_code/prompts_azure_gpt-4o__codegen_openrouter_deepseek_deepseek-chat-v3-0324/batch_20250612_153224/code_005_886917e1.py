"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Develop a program to calculate the load-bearing capacity of kamnite dekorativne podporne stene (stone decorative retaining walls) based on input parameters like height and material density.
Generated: DETERMINISTIC_886917e1bd9390a5
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

class StoneRetainingWall:
    """
    A class to calculate the load-bearing capacity of stone decorative retaining walls.
    
    Attributes:
        height (float): Height of the wall in meters.
        density (float): Density of the stone material in kg/m³.
        thickness (float): Thickness of the wall in meters.
        gravity (float): Acceleration due to gravity (default: 9.81 m/s²).
        safety_factor (float): Safety factor for load-bearing calculations (default: 2.5).
    """
    
    def __init__(self, height: float, density: float, thickness: float, 
                 gravity: float = 9.81, safety_factor: float = 2.5):
        """
        Initialize the StoneRetainingWall with given parameters.
        
        Args:
            height: Height of the wall in meters.
            density: Density of the stone material in kg/m³.
            thickness: Thickness of the wall in meters.
            gravity: Acceleration due to gravity (default: 9.81 m/s²).
            safety_factor: Safety factor for load-bearing calculations (default: 2.5).
            
        Raises:
            ValueError: If any of the parameters are non-positive.
        """
        if height <= 0 or density <= 0 or thickness <= 0 or gravity <= 0 or safety_factor <= 0:
            raise ValueError("All parameters must be positive values.")
            
        self.height = height
        self.density = density
        self.thickness = thickness
        self.gravity = gravity
        self.safety_factor = safety_factor
    
    def calculate_self_weight(self) -> float:
        """
        Calculate the self-weight of the wall per unit length.
        
        Returns:
            float: Self-weight of the wall in N/m.
        """
        return self.density * self.height * self.thickness * self.gravity
    
    def calculate_lateral_earth_pressure(self, soil_density: float, friction_angle: float) -> float:
        """
        Calculate the lateral earth pressure on the wall.
        
        Args:
            soil_density: Density of the retained soil in kg/m³.
            friction_angle: Angle of internal friction of the soil in degrees.
            
        Returns:
            float: Lateral earth pressure in N/m.
            
        Raises:
            ValueError: If soil_density or friction_angle are non-positive.
        """
        if soil_density <= 0 or friction_angle <= 0:
            raise ValueError("Soil density and friction angle must be positive values.")
            
        # Convert angle to radians and calculate coefficient of active earth pressure
        phi_rad = math.radians(friction_angle)
        ka = (1 - math.sin(phi_rad)) / (1 + math.sin(phi_rad))
        
        # Calculate total lateral force per unit length
        return 0.5 * soil_density * self.gravity * (self.height ** 2) * ka
    
    def calculate_load_bearing_capacity(self, soil_density: float, friction_angle: float) -> float:
        """
        Calculate the load-bearing capacity of the wall considering overturning and sliding.
        
        Args:
            soil_density: Density of the retained soil in kg/m³.
            friction_angle: Angle of internal friction of the soil in degrees.
            
        Returns:
            float: Load-bearing capacity in N/m.
            
        Raises:
            ValueError: If soil_density or friction_angle are non-positive.
        """
        if soil_density <= 0 or friction_angle <= 0:
            raise ValueError("Soil density and friction angle must be positive values.")
            
        # Calculate resisting moment (self-weight * thickness/2)
        self_weight = self.calculate_self_weight()
        resisting_moment = self_weight * (self.thickness / 2)
        
        # Calculate overturning moment (lateral force * height/3)
        lateral_force = self.calculate_lateral_earth_pressure(soil_density, friction_angle)
        overturning_moment = lateral_force * (self.height / 3)
        
        # Factor of safety against overturning
        fos_overturning = resisting_moment / overturning_moment
        
        # Factor of safety against sliding (assuming friction coefficient = tan(friction_angle))
        friction_coeff = math.tan(math.radians(friction_angle))
        fos_sliding = (self_weight * friction_coeff) / lateral_force
        
        # The load-bearing capacity is the minimum of the two safety factors
        min_fos = min(fos_overturning, fos_sliding)
        
        # Return the actual capacity considering the required safety factor
        return min_fos / self.safety_factor
    
    def get_wall_properties(self) -> dict:
        """
        Return a dictionary of the wall's properties.
        
        Returns:
            dict: Dictionary containing wall properties.
        """
        return {
            'height': self.height,
            'density': self.density,
            'thickness': self.thickness,
            'gravity': self.gravity,
            'safety_factor': self.safety_factor
        }


def main():
    """
    Example usage of the StoneRetainingWall class.
    """
    try:
        # Example wall parameters
        wall = StoneRetainingWall(
            height=2.0,       # 2 meters tall
            density=2500,     # 2500 kg/m³ (typical for stone)
            thickness=0.5     # 0.5 meters thick
        )
        
        # Soil parameters
        soil_density = 1800   # 1800 kg/m³
        friction_angle = 30   # 30 degrees
        
        # Calculate and print results
        self_weight = wall.calculate_self_weight()
        lateral_pressure = wall.calculate_lateral_earth_pressure(soil_density, friction_angle)
        capacity = wall.calculate_load_bearing_capacity(soil_density, friction_angle)
        
        print("Wall Properties:")
        for key, value in wall.get_wall_properties().items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nCalculated Values:")
        print(f"Self-weight: {self_weight:.2f} N/m")
        print(f"Lateral Earth Pressure: {lateral_pressure:.2f} N/m")
        print(f"Load-bearing Capacity (FOS={wall.safety_factor}): {capacity:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
