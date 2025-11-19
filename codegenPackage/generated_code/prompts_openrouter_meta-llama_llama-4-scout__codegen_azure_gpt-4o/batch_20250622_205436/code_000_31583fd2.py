"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: "Generate a Python code for numerical modeling of geotechnical tasks as per the services offered by Научно-образовательный центр «Геотехника» им. З.Г. Тер-Мартиросяна."
Generated: DETERMINISTIC_31583fd20855833a
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class GeotechnicalModel:
    """
    A class for numerical modeling of geotechnical tasks.
    This class provides tools for simulating stress-strain behavior in soil mechanics.
    """

    def __init__(self, elastic_modulus, poisson_ratio):
        """
        Initialize the geotechnical model with material properties.

        :param elastic_modulus: Elastic modulus of the material (E) in MPa
        :param poisson_ratio: Poisson's ratio of the material (ν), dimensionless
        """
        if elastic_modulus <= 0:
            raise ValueError("Elastic modulus must be positive.")
        if not (0 <= poisson_ratio < 0.5):
            raise ValueError("Poisson's ratio must be between 0 and 0.5.")

        self.elastic_modulus = elastic_modulus
        self.poisson_ratio = poisson_ratio

    def calculate_stress(self, strain):
        """
        Calculate stress based on strain using Hooke's law.

        :param strain: Strain (ε), dimensionless
        :return: Stress (σ) in MPa
        """
        if strain < 0:
            raise ValueError("Strain must be non-negative.")
        stress = self.elastic_modulus * strain
        return stress

    def calculate_strain_energy(self, strain):
        """
        Calculate strain energy density for the given strain.

        :param strain: Strain (ε), dimensionless
        :return: Strain energy density in MPa
        """
        if strain < 0:
            raise ValueError("Strain must be non-negative.")
        strain_energy = 0.5 * self.elastic_modulus * strain**2
        return strain_energy

    def plot_stress_strain_curve(self, max_strain):
        """
        Plot the stress-strain curve for the material.

        :param max_strain: Maximum strain to plot, dimensionless
        """
        if max_strain <= 0:
            raise ValueError("Maximum strain must be positive.")

        strains = np.linspace(0, max_strain, 100)
        stresses = [self.calculate_stress(strain) for strain in strains]

        plt.figure(figsize=(8, 6))
        plt.plot(strains, stresses, label="Stress-Strain Curve", color="blue")
        plt.xlabel("Strain (ε)")
        plt.ylabel("Stress (σ) [MPa]")
        plt.title("Stress-Strain Curve")
        plt.grid(True)
        plt.legend()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Define material properties
        elastic_modulus = 30  # MPa
        poisson_ratio = 0.3  # Dimensionless

        # Create a geotechnical model instance
        model = GeotechnicalModel(elastic_modulus, poisson_ratio)

        # Calculate stress and strain energy for a given strain
        strain = 0.01  # Example strain
        stress = model.calculate_stress(strain)
        strain_energy = model.calculate_strain_energy(strain)

        print(f"Stress at strain {strain}: {stress} MPa")
        print(f"Strain energy density at strain {strain}: {strain_energy} MPa")

        # Plot the stress-strain curve
        max_strain = 0.05  # Maximum strain for the plot
        model.plot_stress_strain_curve(max_strain)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
