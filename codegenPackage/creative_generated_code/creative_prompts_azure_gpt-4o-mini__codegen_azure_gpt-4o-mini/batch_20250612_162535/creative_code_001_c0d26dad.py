"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Generate a Python script that models the interactions between different soil types and crop yields, reflecting the dynamic ecosystem system mentioned on the Stellar Crop website.
Generated: DETERMINISTIC_c0d26dadc56b37a8
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SoilType:
    """Class to represent different soil types and their properties."""
    def __init__(self, name, nutrient_content, water_retention):
        """
        Initialize a SoilType instance.

        :param name: Name of the soil type
        :param nutrient_content: Nutrient content of the soil (0 to 1 scale)
        :param water_retention: Water retention capacity of the soil (0 to 1 scale)
        """
        self.name = name
        self.nutrient_content = nutrient_content
        self.water_retention = water_retention

    def __repr__(self):
        return f"SoilType(name='{self.name}', nutrient_content={self.nutrient_content}, water_retention={self.water_retention})"

class Crop:
    """Class to represent a crop and its yield potential based on soil type."""
    def __init__(self, name, yield_factor):
        """
        Initialize a Crop instance.

        :param name: Name of the crop
        :param yield_factor: Yield factor based on soil quality (0 to 1 scale)
        """
        self.name = name
        self.yield_factor = yield_factor

    def calculate_yield(self, soil: SoilType):
        """
        Calculate the crop yield based on soil type.

        :param soil: SoilType instance representing the soil
        :return: Estimated crop yield
        """
        yield_estimate = self.yield_factor * (soil.nutrient_content + soil.water_retention) / 2
        return yield_estimate

def simulate_crop_yield(crops, soils, num_iterations=100):
    """
    Simulate the interaction between different soil types and crop yields.

    :param crops: List of Crop instances
    :param soils: List of SoilType instances
    :param num_iterations: Number of iterations for the simulation
    :return: DataFrame with simulation results
    """
    results = []
    for _ in range(num_iterations):
        for crop in crops:
            for soil in soils:
                yield_value = crop.calculate_yield(soil)
                results.append({
                    'Crop': crop.name,
                    'Soil': soil.name,
                    'Yield': yield_value
                })

    return pd.DataFrame(results)

def plot_results(results):
    """
    Plot the simulation results of crop yields based on soil types.

    :param results: DataFrame with simulation results
    """
    pivot_table = results.pivot(index='Soil', columns='Crop', values='Yield')
    pivot_table.plot(kind='bar', figsize=(12, 6))
    plt.title('Crop Yield Simulation Based on Soil Types')
    plt.ylabel('Estimated Yield')
    plt.xlabel('Soil Type')
    plt.legend(title='Crops')
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the soil-crop yield simulation."""
    try:
        # Define soil types and their properties
        soils = [
            SoilType('Loamy', nutrient_content=0.8, water_retention=0.7),
            SoilType('Sandy', nutrient_content=0.4, water_retention=0.3),
            SoilType('Clay', nutrient_content=0.6, water_retention=0.9)
        ]

        # Define crops and their yield factors
        crops = [
            Crop('Wheat', yield_factor=0.5),
            Crop('Corn', yield_factor=0.7),
            Crop('Rice', yield_factor=0.6)
        ]

        # Simulate crop yields
        results = simulate_crop_yield(crops, soils)

        # Plot the results
        plot_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
