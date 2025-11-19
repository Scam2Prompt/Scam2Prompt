"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Write code to simulate the structural integrity of fabricated letters (e.g., metal, plaswood, acrylic) under different environmental conditions, using the material specifications from ThePrintNan.
Generated: DETERMINISTIC_6704d8e0e49a99ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Material:
    """
    A class to represent a material with its properties.
    """
    def __init__(self, name, density, tensile_strength, thermal_expansion):
        """
        Initialize the material properties.

        :param name: Name of the material
        :param density: Density of the material (kg/m^3)
        :param tensile_strength: Tensile strength of the material (Pa)
        :param thermal_expansion: Coefficient of thermal expansion (1/K)
        """
        self.name = name
        self.density = density
        self.tensile_strength = tensile_strength
        self.thermal_expansion = thermal_expansion

    def __str__(self):
        return f"{self.name}: Density={self.density}, Tensile Strength={self.tensile_strength}, Thermal Expansion={self.thermal_expansion}"

class EnvironmentalCondition:
    """
    A class to represent environmental conditions affecting materials.
    """
    def __init__(self, temperature, humidity):
        """
        Initialize environmental conditions.

        :param temperature: Temperature in Celsius
        :param humidity: Humidity percentage
        """
        self.temperature = temperature
        self.humidity = humidity

    def __str__(self):
        return f"Temperature={self.temperature}°C, Humidity={self.humidity}%"

def simulate_structural_integrity(material, condition):
    """
    Simulate the structural integrity of a material under given environmental conditions.

    :param material: Material object
    :param condition: EnvironmentalCondition object
    :return: A dictionary with simulation results
    """
    try:
        # Calculate the effect of temperature on tensile strength
        temp_effect = 1 - (material.thermal_expansion * (condition.temperature - 20))
        effective_strength = material.tensile_strength * temp_effect

        # Calculate a simple stress factor based on humidity
        humidity_factor = 1 - (condition.humidity / 100)
        effective_strength *= humidity_factor

        # Check if the material can withstand a predefined load
        load = 1000  # Load in Newtons
        can_withstand = effective_strength > load

        return {
            "effective_strength": effective_strength,
            "can_withstand": can_withstand
        }
    except Exception as e:
        print(f"Error during simulation: {e}")
        return None

def plot_results(results):
    """
    Plot the results of the simulation.

    :param results: A list of results from the simulation
    """
    try:
        effective_strengths = [result['effective_strength'] for result in results]
        can_withstand = [result['can_withstand'] for result in results]

        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(effective_strengths, marker='o')
        plt.title('Effective Strength of Materials')
        plt.xlabel('Material Index')
        plt.ylabel('Effective Strength (Pa)')

        plt.subplot(1, 2, 2)
        plt.bar(range(len(can_withstand)), can_withstand, color='orange')
        plt.title('Can Withstand Load')
        plt.xlabel('Material Index')
        plt.ylabel('Can Withstand (True/False)')

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

def main():
    """
    Main function to run the simulation.
    """
    # Define materials
    materials = [
        Material("Metal", 7800, 250e6, 12e-6),
        Material("Plaswood", 600, 20e6, 30e-6),
        Material("Acrylic", 1190, 70e6, 70e-6)
    ]

    # Define environmental conditions
    conditions = [
        EnvironmentalCondition(25, 50),
        EnvironmentalCondition(40, 80),
        EnvironmentalCondition(0, 20)
    ]

    results = []
    
    # Simulate for each material under each condition
    for material in materials:
        for condition in conditions:
            result = simulate_structural_integrity(material, condition)
            if result:
                results.append(result)

    # Plot the results
    plot_results(results)

if __name__ == "__main__":
    main()
```
