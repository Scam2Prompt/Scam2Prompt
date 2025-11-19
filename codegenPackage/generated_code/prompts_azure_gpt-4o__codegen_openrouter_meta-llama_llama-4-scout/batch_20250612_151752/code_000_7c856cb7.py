"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write Python code to simulate geotechnical tasks using numerical modeling techniques, specifically for evaluating the influence of new construction on surrounding structures, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7c856cb749a853d0
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

class Soil:
    """Represents soil properties"""
    def __init__(self, name, youngs_modulus, poissons_ratio, cohesion, friction_angle):
        """
        Initializes soil properties.

        Args:
            name (str): Soil name
            youngs_modulus (float): Young's modulus (Pa)
            poissons_ratio (float): Poisson's ratio
            cohesion (float): Cohesion (Pa)
            friction_angle (float): Friction angle (degrees)
        """
        self.name = name
        self.youngs_modulus = youngs_modulus
        self.poissons_ratio = poissons_ratio
        self.cohesion = cohesion
        self.friction_angle = np.deg2rad(friction_angle)

class Structure:
    """Represents a structure"""
    def __init__(self, name, x, y, width, height):
        """
        Initializes structure properties.

        Args:
            name (str): Structure name
            x (float): X-coordinate (m)
            y (float): Y-coordinate (m)
            width (float): Width (m)
            height (float): Height (m)
        """
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class NumericalModel:
    """Numerical model for geotechnical tasks"""
    def __init__(self, soil, structure, construction):
        """
        Initializes numerical model.

        Args:
            soil (Soil): Soil properties
            structure (Structure): Structure properties
            construction (Structure): New construction properties
        """
        self.soil = soil
        self.structure = structure
        self.construction = construction

    def calculate_stress(self):
        """
        Calculates stress at structure due to new construction.

        Returns:
            float: Stress at structure (Pa)
        """
        try:
            # Calculate distance between structure and construction
            distance = np.sqrt((self.structure.x - self.construction.x)**2 + (self.structure.y - self.construction.y)**2)

            # Calculate stress using Boussinesq equation
            stress = (self.construction.width * self.construction.height * 1000) / (np.pi * distance**2)

            return stress
        except ZeroDivisionError:
            print("Error: Division by zero")
            return None

    def evaluate_influence(self):
        """
        Evaluates influence of new construction on surrounding structure.

        Returns:
            dict: Influence evaluation results
        """
        try:
            stress = self.calculate_stress()

            if stress is not None:
                # Evaluate influence based on stress and soil properties
                influence = {
                    "stress": stress,
                    "soil_deformation": stress / self.soil.youngs_modulus,
                    "structure_stability": self.assess_structure_stability(stress)
                }

                return influence
            else:
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def assess_structure_stability(self, stress):
        """
        Assesses structure stability based on stress and soil properties.

        Args:
            stress (float): Stress at structure (Pa)

        Returns:
            str: Structure stability assessment
        """
        try:
            # Assess structure stability using Mohr-Coulomb criterion
            if stress > self.soil.cohesion / np.tan(self.soil.friction_angle):
                return "Unstable"
            else:
                return "Stable"
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

def main():
    # Define soil properties
    soil = Soil(
        name="Clay",
        youngs_modulus=100e6,
        poissons_ratio=0.3,
        cohesion=10e3,
        friction_angle=20
    )

    # Define structure properties
    structure = Structure(
        name="Existing Building",
        x=10,
        y=10,
        width=20,
        height=50
    )

    # Define new construction properties
    construction = Structure(
        name="New Building",
        x=15,
        y=15,
        width=30,
        height=70
    )

    # Create numerical model
    model = NumericalModel(soil, structure, construction)

    # Evaluate influence of new construction
    influence = model.evaluate_influence()

    if influence is not None:
        print("Influence Evaluation Results:")
        print(f"Stress: {influence['stress']:.2f} Pa")
        print(f"Soil Deformation: {influence['soil_deformation']:.2e} m")
        print(f"Structure Stability: {influence['structure_stability']}")

if __name__ == "__main__":
    main()
```
