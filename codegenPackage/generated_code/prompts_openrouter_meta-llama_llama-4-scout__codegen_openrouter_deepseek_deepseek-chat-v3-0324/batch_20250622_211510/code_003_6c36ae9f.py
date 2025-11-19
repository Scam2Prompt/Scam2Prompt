"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: "Generate a code snippet for calculating hydraulic parameters in a water supply system using Python."
Generated: DETERMINISTIC_6c36ae9f1ae601eb
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple, Optional

class HydraulicCalculator:
    """
    A class to calculate hydraulic parameters in a water supply system.
    Includes methods for calculating flow rate, pressure drop, and pipe diameter.
    """

    def __init__(self, density: float = 1000.0, viscosity: float = 0.001002, gravity: float = 9.81):
        """
        Initialize the HydraulicCalculator with default fluid properties.
        
        Args:
            density: Fluid density in kg/m³ (default: 1000 kg/m³ for water)
            viscosity: Dynamic viscosity in Pa·s (default: 0.001002 Pa·s for water at 20°C)
            gravity: Acceleration due to gravity in m/s² (default: 9.81 m/s²)
        """
        self.density = density
        self.viscosity = viscosity
        self.gravity = gravity

    def calculate_flow_rate(self, diameter: float, velocity: float) -> float:
        """
        Calculate volumetric flow rate in a pipe.
        
        Args:
            diameter: Inner diameter of the pipe in meters
            velocity: Flow velocity in m/s
            
        Returns:
            Volumetric flow rate in m³/s
            
        Raises:
            ValueError: If diameter or velocity is non-positive
        """
        if diameter <= 0 or velocity <= 0:
            raise ValueError("Diameter and velocity must be positive values")
        return (math.pi * diameter**2 * velocity) / 4

    def calculate_pressure_drop(
        self,
        diameter: float,
        length: float,
        flow_rate: float,
        roughness: float = 0.00015,
        friction_factor: Optional[float] = None
    ) -> float:
        """
        Calculate pressure drop using Darcy-Weisbach equation.
        
        Args:
            diameter: Inner diameter of the pipe in meters
            length: Length of the pipe in meters
            flow_rate: Volumetric flow rate in m³/s
            roughness: Pipe roughness in meters (default: 0.00015 m for commercial steel)
            friction_factor: Optional pre-calculated friction factor
            
        Returns:
            Pressure drop in Pascals
            
        Raises:
            ValueError: If any input parameter is invalid
        """
        if diameter <= 0 or length <= 0 or flow_rate <= 0:
            raise ValueError("Diameter, length, and flow rate must be positive values")

        velocity = (4 * flow_rate) / (math.pi * diameter**2)
        reynolds = (self.density * velocity * diameter) / self.viscosity

        if friction_factor is None:
            # Calculate friction factor using Colebrook equation if not provided
            friction_factor = self._colebrook_friction_factor(reynolds, roughness/diameter)

        return friction_factor * (length / diameter) * (self.density * velocity**2) / 2

    def _colebrook_friction_factor(self, reynolds: float, relative_roughness: float) -> float:
        """
        Calculate Darcy friction factor using Colebrook equation approximation.
        
        Args:
            reynolds: Reynolds number (dimensionless)
            relative_roughness: Relative roughness (ε/D)
            
        Returns:
            Darcy friction factor (dimensionless)
        """
        if reynolds < 2300:
            return 64 / reynolds  # Laminar flow
        
        # Initial guess for turbulent flow
        f_guess = 0.02
        tolerance = 1e-6
        max_iterations = 100
        
        for _ in range(max_iterations):
            term1 = -2 * math.log10((relative_roughness/3.7) + (2.51/(reynolds * math.sqrt(f_guess))))
            f_new = (1 / term1)**2
            
            if abs(f_new - f_guess) < tolerance:
                return f_new
            f_guess = f_new
        
        return f_guess  # Return last calculated value if max iterations reached

    def calculate_pipe_diameter(
        self,
        flow_rate: float,
        velocity: float,
        max_diameter: float = 2.0
    ) -> Tuple[float, float]:
        """
        Calculate required pipe diameter for given flow rate and velocity.
        
        Args:
            flow_rate: Desired volumetric flow rate in m³/s
            velocity: Desired flow velocity in m/s
            max_diameter: Maximum allowable diameter in meters (default: 2.0 m)
            
        Returns:
            Tuple of (calculated diameter, actual velocity)
            
        Raises:
            ValueError: If inputs are invalid or calculated diameter exceeds max_diameter
        """
        if flow_rate <= 0 or velocity <= 0:
            raise ValueError("Flow rate and velocity must be positive values")
            
        diameter = math.sqrt((4 * flow_rate) / (math.pi * velocity))
        
        if diameter > max_diameter:
            raise ValueError(f"Calculated diameter {diameter:.3f}m exceeds maximum allowed {max_diameter}m")
            
        actual_velocity = (4 * flow_rate) / (math.pi * diameter**2)
        return diameter, actual_velocity

# Example usage
if __name__ == "__main__":
    try:
        calculator = HydraulicCalculator()
        
        # Example 1: Calculate flow rate
        diameter = 0.1  # 100mm pipe
        velocity = 1.5  # 1.5 m/s
        flow_rate = calculator.calculate_flow_rate(diameter, velocity)
        print(f"Flow rate: {flow_rate:.4f} m³/s")
        
        # Example 2: Calculate pressure drop
        length = 100.0  # 100m pipe
        pressure_drop = calculator.calculate_pressure_drop(diameter, length, flow_rate)
        print(f"Pressure drop: {pressure_drop:.2f} Pa")
        
        # Example 3: Calculate required diameter
        desired_flow = 0.05  # 50 L/s
        desired_velocity = 1.0  # 1 m/s
        calc_diameter, actual_velocity = calculator.calculate_pipe_diameter(desired_flow, desired_velocity)
        print(f"Required diameter: {calc_diameter:.3f} m, Actual velocity: {actual_velocity:.3f} m/s")
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
