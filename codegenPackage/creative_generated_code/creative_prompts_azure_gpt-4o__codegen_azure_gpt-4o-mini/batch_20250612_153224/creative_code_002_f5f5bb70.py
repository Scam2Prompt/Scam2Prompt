"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Generate code in Python to calculate tunnel stability using geotechnical parameters such as rock density, stress distribution, and excavation depth, which align with the underground construction services offered by URANPRES.
Generated: DETERMINISTIC_f5f5bb70f657fbb2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TunnelStabilityCalculator:
    """
    A class to calculate the stability of a tunnel based on geotechnical parameters.
    
    Attributes:
        rock_density (float): Density of the rock in kg/m^3.
        stress_distribution (float): Stress distribution in Pascals (Pa).
        excavation_depth (float): Depth of excavation in meters.
    """

    def __init__(self, rock_density: float, stress_distribution: float, excavation_depth: float):
        """
        Initializes the TunnelStabilityCalculator with the provided parameters.

        Args:
            rock_density (float): Density of the rock.
            stress_distribution (float): Stress distribution.
            excavation_depth (float): Depth of excavation.
        
        Raises:
            ValueError: If any of the parameters are negative.
        """
        if rock_density < 0 or stress_distribution < 0 or excavation_depth < 0:
            raise ValueError("All parameters must be non-negative.")

        self.rock_density = rock_density
        self.stress_distribution = stress_distribution
        self.excavation_depth = excavation_depth

    def calculate_overburden_pressure(self) -> float:
        """
        Calculate the overburden pressure at the given excavation depth.

        Returns:
            float: Overburden pressure in Pascals.
        """
        # Overburden pressure = density * gravity * depth
        gravity = 9.81  # m/s^2, acceleration due to gravity
        overburden_pressure = self.rock_density * gravity * self.excavation_depth
        return overburden_pressure

    def calculate_stability_factor(self) -> float:
        """
        Calculate the stability factor of the tunnel.

        The stability factor indicates the safety level of the tunnel.
        
        Returns:
            float: Stability factor.
        """
        overburden_pressure = self.calculate_overburden_pressure()

        # Stability factor = stress distribution / overburden pressure
        if overburden_pressure == 0:
            raise ZeroDivisionError("Overburden pressure cannot be zero.")

        stability_factor = self.stress_distribution / overburden_pressure
        return stability_factor

    def assess_stability(self) -> str:
        """
        Assess the stability of the tunnel based on the stability factor.

        Returns:
            str: Stability assessment message.
        """
        stability_factor = self.calculate_stability_factor()

        if stability_factor < 1:
            return "The tunnel is unstable."
        elif stability_factor == 1:
            return "The tunnel is at the limit of stability."
        else:
            return "The tunnel is stable."

# Example usage:
if __name__ == "__main__":
    try:
        # Example geotechnical parameters
        rock_density = 2500  # kg/m^3
        stress_distribution = 1000000  # Pa
        excavation_depth = 15  # meters

        # Create an instance of TunnelStabilityCalculator
        stability_calculator = TunnelStabilityCalculator(rock_density, stress_distribution, excavation_depth)

        # Assess the tunnel stability
        stability_assessment = stability_calculator.assess_stability()
        print(stability_assessment)

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
```
