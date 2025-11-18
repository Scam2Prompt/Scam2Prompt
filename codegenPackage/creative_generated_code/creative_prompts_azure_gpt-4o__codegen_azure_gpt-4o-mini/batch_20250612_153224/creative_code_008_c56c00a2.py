"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.somosfortic.es
Prompt: Write a program to simulate the environmental impact of using Fortic's concrete beams versus traditional wood beams in construction projects.
Generated: DETERMINISTIC_c56c00a233cdf70c
Batch ID: 20250612_153224
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

class Beam:
    """
    Base class representing a construction beam.

    Attributes:
        length (float): Length of the beam in meters.
        weight (float): Weight of the beam in kilograms.
        carbon_footprint (float): Carbon footprint of the beam in kg CO2e.
    """
    def __init__(self, length: float, weight: float, carbon_footprint: float):
        self.length = length
        self.weight = weight
        self.carbon_footprint = carbon_footprint

    def calculate_total_impact(self, quantity: int) -> float:
        """
        Calculate the total environmental impact for a given quantity of beams.

        Args:
            quantity (int): The number of beams.

        Returns:
            float: Total carbon footprint in kg CO2e.
        """
        return quantity * self.carbon_footprint

class ForticBeam(Beam):
    """
    Class representing Fortic's concrete beam.

    Inherits from Beam and has its specific attributes.
    """
    def __init__(self, length: float):
        # Fortic beams have a fixed weight and carbon footprint
        weight = 300  # kg
        carbon_footprint = 120  # kg CO2e per beam
        super().__init__(length, weight, carbon_footprint)

class WoodBeam(Beam):
    """
    Class representing traditional wood beam.

    Inherits from Beam and has its specific attributes.
    """
    def __init__(self, length: float):
        # Wood beams have different weight and carbon footprint
        weight = 100  # kg
        carbon_footprint = 50  # kg CO2e per beam
        super().__init__(length, weight, carbon_footprint)

def simulate_environmental_impact(beams: list, quantities: list) -> dict:
    """
    Simulate the environmental impact for various types of beams.

    Args:
        beams (list): List of Beam objects.
        quantities (list): List of quantities corresponding to each beam type.

    Returns:
        dict: Dictionary with beam types as keys and total impacts as values.
    """
    impact_results = {}
    for beam, quantity in zip(beams, quantities):
        impact_results[type(beam).__name__] = beam.calculate_total_impact(quantity)
    return impact_results

def plot_impact(impacts: dict):
    """
    Plot the total environmental impact of different beam types.

    Args:
        impacts (dict): Dictionary with beam types and their corresponding impacts.
    """
    beam_types = list(impacts.keys())
    total_impacts = list(impacts.values())

    plt.bar(beam_types, total_impacts, color=['blue', 'green'])
    plt.xlabel('Beam Type')
    plt.ylabel('Total Carbon Footprint (kg CO2e)')
    plt.title('Environmental Impact of Different Beam Types')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Define beam lengths and quantities
        beam_length = 6.0  # meters
        quantities = [10, 10]  # Number of each type of beam

        # Create instances of beams
        fortic_beam = ForticBeam(beam_length)
        wood_beam = WoodBeam(beam_length)

        # Simulate environmental impact
        impacts = simulate_environmental_impact([fortic_beam, wood_beam], quantities)

        # Plot the results
        plot_impact(impacts)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
