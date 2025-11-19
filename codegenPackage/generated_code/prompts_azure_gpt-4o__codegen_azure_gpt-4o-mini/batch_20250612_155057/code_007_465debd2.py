"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate the "Yerçekimsiz Deneyler" in Stellar Crop, modeling crop growth in zero-gravity conditions with adjustable parameters for environmental factors.
Generated: DETERMINISTIC_465debd28bd1ffeb
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt

class Crop:
    """
    A class to represent a crop in a zero-gravity environment.
    """

    def __init__(self, growth_rate, water_needs, nutrient_needs):
        """
        Initialize the crop with its growth parameters.

        :param growth_rate: The rate at which the crop grows (units per time).
        :param water_needs: The amount of water needed for optimal growth.
        :param nutrient_needs: The amount of nutrients needed for optimal growth.
        """
        self.growth_rate = growth_rate
        self.water_needs = water_needs
        self.nutrient_needs = nutrient_needs
        self.height = 0  # Initial height of the crop

    def grow(self, water_available, nutrients_available):
        """
        Simulate the growth of the crop based on available resources.

        :param water_available: The amount of water available.
        :param nutrients_available: The amount of nutrients available.
        """
        if water_available < 0 or nutrients_available < 0:
            raise ValueError("Water and nutrients must be non-negative.")

        # Calculate growth based on available resources
        water_factor = min(water_available / self.water_needs, 1)
        nutrient_factor = min(nutrients_available / self.nutrient_needs, 1)

        growth_factor = (water_factor + nutrient_factor) / 2
        growth = self.growth_rate * growth_factor

        self.height += growth
        return self.height


class Environment:
    """
    A class to represent the environment in which the crops grow.
    """

    def __init__(self, water_supply, nutrient_supply):
        """
        Initialize the environment with its resources.

        :param water_supply: The total amount of water available.
        :param nutrient_supply: The total amount of nutrients available.
        """
        self.water_supply = water_supply
        self.nutrient_supply = nutrient_supply

    def simulate_growth(self, crop, days):
        """
        Simulate the growth of a crop over a number of days.

        :param crop: The crop to be grown.
        :param days: The number of days to simulate growth.
        :return: A list of crop heights over time.
        """
        heights = []
        for day in range(days):
            try:
                # Randomly adjust available resources each day
                water_available = random.uniform(0, self.water_supply)
                nutrients_available = random.uniform(0, self.nutrient_supply)

                # Grow the crop and record its height
                height = crop.grow(water_available, nutrients_available)
                heights.append(height)
            except ValueError as e:
                print(f"Error on day {day}: {e}")
                heights.append(crop.height)  # Keep the height unchanged on error

        return heights


def plot_growth(days, heights):
    """
    Plot the growth of the crop over time.

    :param days: The number of days simulated.
    :param heights: The heights of the crop over time.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(days), heights, marker='o')
    plt.title('Crop Growth in Zero-Gravity Conditions')
    plt.xlabel('Days')
    plt.ylabel('Height (units)')
    plt.grid()
    plt.show()


def main():
    """
    Main function to run the crop growth simulation.
    """
    # Define crop parameters
    growth_rate = 1.0  # units per day
    water_needs = 5.0  # units of water
    nutrient_needs = 3.0  # units of nutrients

    # Create a crop instance
    crop = Crop(growth_rate, water_needs, nutrient_needs)

    # Create an environment instance
    water_supply = 50.0  # total water available
    nutrient_supply = 30.0  # total nutrients available
    environment = Environment(water_supply, nutrient_supply)

    # Simulate growth for a specified number of days
    days = 30
    heights = environment.simulate_growth(crop, days)

    # Plot the results
    plot_growth(days, heights)


if __name__ == "__main__":
    main()
```
