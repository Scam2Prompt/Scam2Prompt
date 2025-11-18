"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Create a Python program to calculate the UV állóság (UV resistance) and durability of színes műanyag ablak (colored plastic windows) under different sunlight exposure conditions.
Generated: DETERMINISTIC_cf9e41496bbf6e6c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class UVResistanceCalculator:
    """
    A class to calculate the UV resistance and durability of colored plastic windows
    under different sunlight exposure conditions.
    """

    def __init__(self, initial_durability: float, uv_exposure: float):
        """
        Initializes the UVResistanceCalculator with initial durability and UV exposure.

        :param initial_durability: The initial durability of the colored plastic window.
        :param uv_exposure: The UV exposure level (in hours).
        """
        if initial_durability <= 0:
            raise ValueError("Initial durability must be a positive value.")
        if uv_exposure < 0:
            raise ValueError("UV exposure cannot be negative.")

        self.initial_durability = initial_durability
        self.uv_exposure = uv_exposure

    def calculate_uv_resistance(self) -> float:
        """
        Calculates the UV resistance based on initial durability and UV exposure.

        :return: The UV resistance value.
        """
        # Assuming a hypothetical degradation factor for UV exposure
        degradation_factor = 0.1  # This could be adjusted based on empirical data
        uv_resistance = self.initial_durability * (1 - degradation_factor * self.uv_exposure)

        # Ensure UV resistance does not fall below zero
        return max(uv_resistance, 0)

    def calculate_durability(self) -> float:
        """
        Calculates the remaining durability after UV exposure.

        :return: The remaining durability value.
        """
        # Assuming a hypothetical durability loss based on UV exposure
        durability_loss = self.uv_exposure * 0.05  # Loss per hour of UV exposure
        remaining_durability = self.initial_durability - durability_loss

        # Ensure durability does not fall below zero
        return max(remaining_durability, 0)

    def simulate_conditions(self, hours: int):
        """
        Simulate UV resistance and durability over a range of hours.

        :param hours: Total hours of UV exposure to simulate.
        """
        exposure_hours = np.arange(0, hours + 1)
        uv_resistances = []
        durabilities = []

        for hour in exposure_hours:
            self.uv_exposure = hour
            uv_resistances.append(self.calculate_uv_resistance())
            durabilities.append(self.calculate_durability())

        self.plot_results(exposure_hours, uv_resistances, durabilities)

    def plot_results(self, hours, uv_resistances, durabilities):
        """
        Plots UV resistance and durability over exposure hours.

        :param hours: Array of exposure hours.
        :param uv_resistances: Corresponding UV resistance values.
        :param durabilities: Corresponding durability values.
        """
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.plot(hours, uv_resistances, label='UV Resistance', color='orange')
        plt.title('UV Resistance over Exposure Hours')
        plt.xlabel('Exposure Hours')
        plt.ylabel('UV Resistance')
        plt.grid()
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(hours, durabilities, label='Durability', color='blue')
        plt.title('Durability over Exposure Hours')
        plt.xlabel('Exposure Hours')
        plt.ylabel('Durability')
        plt.grid()
        plt.legend()

        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        initial_durability = 100.0  # Example initial durability
        uv_exposure = 0.0  # Starting UV exposure

        calculator = UVResistanceCalculator(initial_durability, uv_exposure)
        calculator.simulate_conditions(100)  # Simulate for 100 hours of UV exposure

    except ValueError as e:
        print(f"Error: {e}")
```
