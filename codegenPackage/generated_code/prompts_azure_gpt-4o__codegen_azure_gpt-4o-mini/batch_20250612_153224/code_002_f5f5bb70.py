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
class TunnelStabilityCalculator:
    """
    A class to calculate tunnel stability based on geotechnical parameters.
    """

    def __init__(self, rock_density: float, stress_distribution: float, excavation_depth: float):
        """
        Initializes the TunnelStabilityCalculator with the given parameters.

        :param rock_density: Density of the rock (in kg/m^3)
        :param stress_distribution: Stress distribution (in kPa)
        :param excavation_depth: Depth of excavation (in meters)
        """
        self.rock_density = rock_density
        self.stress_distribution = stress_distribution
        self.excavation_depth = excavation_depth

    def calculate_stability_factor(self) -> float:
        """
        Calculates the stability factor of the tunnel.

        :return: Stability factor (dimensionless)
        """
        try:
            # Calculate the weight of the rock per unit area
            weight_of_rock = self.rock_density * self.excavation_depth * 9.81  # in N/m^2

            # Calculate the stability factor
            stability_factor = weight_of_rock / self.stress_distribution

            return stability_factor

        except ZeroDivisionError:
            raise ValueError("Stress distribution cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during stability calculation: {e}")

    def is_stable(self) -> bool:
        """
        Determines if the tunnel is stable based on the stability factor.

        :return: True if stable, False otherwise
        """
        stability_factor = self.calculate_stability_factor()
        return stability_factor > 1.5  # A stability factor greater than 1.5 is considered stable


if __name__ == "__main__":
    # Example parameters for the tunnel stability calculation
    rock_density = 2500.0  # kg/m^3
    stress_distribution = 150.0  # kPa
    excavation_depth = 30.0  # meters

    # Create an instance of the TunnelStabilityCalculator
    calculator = TunnelStabilityCalculator(rock_density, stress_distribution, excavation_depth)

    try:
        stability_factor = calculator.calculate_stability_factor()
        print(f"Stability Factor: {stability_factor:.2f}")
        if calculator.is_stable():
            print("The tunnel is stable.")
        else:
            print("The tunnel is not stable.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
```
