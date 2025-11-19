"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate code in Python to calculate tunnel stability using geotechnical parameters such as rock density, stress distribution, and excavation depth, which align with the underground construction services offered by URANPRES.
Generated: DETERMINISTIC_f5f5bb70f657fbb2
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

class TunnelStabilityCalculator:
    """
    Calculates tunnel stability using geotechnical parameters.

    Attributes:
        rock_density (float): Density of the rock in kg/m^3.
        stress_distribution (float): Stress distribution factor (unitless).
        excavation_depth (float): Depth of excavation in meters.
        tunnel_radius (float): Radius of the tunnel in meters.
    """

    def __init__(self, rock_density, stress_distribution, excavation_depth, tunnel_radius):
        """
        Initializes the TunnelStabilityCalculator.

        Args:
            rock_density (float): Density of the rock in kg/m^3.
            stress_distribution (float): Stress distribution factor (unitless).
            excavation_depth (float): Depth of excavation in meters.
            tunnel_radius (float): Radius of the tunnel in meters.

        Raises:
            ValueError: If any input value is negative.
        """
        if rock_density < 0 or stress_distribution < 0 or excavation_depth < 0 or tunnel_radius < 0:
            raise ValueError("All input values must be non-negative.")

        self.rock_density = rock_density
        self.stress_distribution = stress_distribution
        self.excavation_depth = excavation_depth
        self.tunnel_radius = tunnel_radius

    def calculate_vertical_stress(self):
        """
        Calculates the vertical stress at the tunnel depth.

        Returns:
            float: Vertical stress in Pascals.
        """
        # Assuming gravity acceleration as 9.81 m/s^2
        gravity = 9.81
        vertical_stress = self.rock_density * gravity * self.excavation_depth
        return vertical_stress

    def calculate_tunnel_stability(self):
        """
        Calculates the tunnel stability factor.

        Returns:
            float: Tunnel stability factor (unitless).
        """
        vertical_stress = self.calculate_vertical_stress()
        # Using a simple Mohr-Coulomb failure criterion for demonstration purposes
        # In practice, use a more complex and accurate model
        tunnel_stability = (vertical_stress / (self.stress_distribution * self.rock_density * 9.81)) * (self.tunnel_radius / self.excavation_depth)
        return tunnel_stability

    def assess_stability(self):
        """
        Assesses the tunnel stability based on the stability factor.

        Returns:
            str: Stability assessment.
        """
        stability_factor = self.calculate_tunnel_stability()
        if stability_factor > 2.5:
            return "Stable"
        elif stability_factor > 1.5:
            return "Moderately stable"
        else:
            return "Unstable"


def main():
    try:
        rock_density = 2500  # kg/m^3
        stress_distribution = 0.5  # unitless
        excavation_depth = 50  # meters
        tunnel_radius = 5  # meters

        calculator = TunnelStabilityCalculator(rock_density, stress_distribution, excavation_depth, tunnel_radius)
        stability_assessment = calculator.assess_stability()
        print(f"Tunnel stability assessment: {stability_assessment}")
        print(f"Tunnel stability factor: {calculator.calculate_tunnel_stability():.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
