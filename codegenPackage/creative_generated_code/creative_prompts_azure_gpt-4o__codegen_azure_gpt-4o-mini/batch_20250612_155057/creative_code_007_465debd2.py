"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate the "Yerçekimsiz Deneyler" in Stellar Crop, modeling crop growth in zero-gravity conditions with adjustable parameters for environmental factors.
Generated: DETERMINISTIC_465debd28bd1ffeb
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import math
import matplotlib.pyplot as plt

class Crop:
    """
    Class representing a crop with attributes affecting its growth.
    """
    def __init__(self, name, growth_rate, water_needs, nutrient_needs):
        """
        Initializes a new Crop instance.

        :param name: str - Name of the crop
        :param growth_rate: float - Base growth rate of the crop per time unit
        :param water_needs: float - Amount of water needed for optimal growth
        :param nutrient_needs: float - Amount of nutrients needed for optimal growth
        """
        self.name = name
        self.growth_rate = growth_rate
        self.water_needs = water_needs
        self.nutrient_needs = nutrient_needs
        self.height = 0.0  # Initial height of the crop

    def grow(self, water_available, nutrients_available):
        """
        Simulates the growth of the crop based on available resources.

        :param water_available: float - Amount of water available
        :param nutrients_available: float - Amount of nutrients available
        """
        # Calculate growth factor based on available resources
        water_factor = min(water_available / self.water_needs, 1)
        nutrient_factor = min(nutrients_available / self.nutrient_needs, 1)

        # Growth is affected by both water and nutrients
        growth_factor = water_factor * nutrient_factor
        self.height += self.growth_rate * growth_factor
        self.height = max(self.height, 0)  # Prevent negative height


class Environment:
    """
    Class representing the growing environment for crops.
    """
    def __init__(self, water_supply, nutrient_supply):
        """
        Initializes a new Environment instance.

        :param water_supply: float - Total water supply available
        :param nutrient_supply: float - Total nutrient supply available
        """
        self.water_supply = water_supply
        self.nutrient_supply = nutrient_supply

    def simulate_growth(self, crop, time_units):
        """
        Simulates the growth of a crop over a specified time.

        :param crop: Crop - The crop to simulate growth for
        :param time_units: int - Number of time units for growth simulation
        """
        heights = []

        for _ in range(time_units):
            # Randomly determine available water and nutrients for this time unit
            water_available = random.uniform(0, self.water_supply)
            nutrients_available = random.uniform(0, self.nutrient_supply)

            crop.grow(water_available, nutrients_available)
            heights.append(crop.height)

        return heights


def plot_growth(heights, crop_name):
    """
    Plots the growth of the crop over time.

    :param heights: list - List of heights over time
    :param crop_name: str - Name of the crop for labeling the plot
    """
    plt.plot(heights)
    plt.title(f'Growth of {crop_name} in Zero-Gravity Conditions')
    plt.xlabel('Time Units')
    plt.ylabel('Height (cm)')
    plt.grid()
    plt.show()


def main():
    """
    Main function to simulate crop growth in zero-gravity conditions.
    """
    try:
        # Create a crop with specified parameters
        crop = Crop(name="Wheat", growth_rate=0.5, water_needs=5, nutrient_needs=3)

        # Set environment conditions
        environment = Environment(water_supply=50, nutrient_supply=30)

        # Simulate growth over a specified time
        time_units = 20
        heights = environment.simulate_growth(crop, time_units)

        # Plot the growth results
        plot_growth(heights, crop.name)

    except Exception as e:
        print(f"An error occurred during simulation: {e}")


if __name__ == "__main__":
    main()
```
