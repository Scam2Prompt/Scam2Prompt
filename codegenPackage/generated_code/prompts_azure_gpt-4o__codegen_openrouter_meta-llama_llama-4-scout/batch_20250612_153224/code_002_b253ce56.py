"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Generate code to simulate the effect of river diversion on local ecosystems, inspired by the campaigns against river exploitation discussed by "Čuvari Šare."
Generated: DETERMINISTIC_b253ce56ea4adb72
Batch ID: 20250612_153224
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

class River:
    def __init__(self, name, flow_rate, sediment_load):
        """
        Initialize a River object.

        Args:
        - name (str): Name of the river.
        - flow_rate (float): Flow rate of the river in m^3/s.
        - sediment_load (float): Sediment load of the river in kg/m^3.
        """
        self.name = name
        self.flow_rate = flow_rate
        self.sediment_load = sediment_load

class Ecosystem:
    def __init__(self, name, biodiversity, water_quality):
        """
        Initialize an Ecosystem object.

        Args:
        - name (str): Name of the ecosystem.
        - biodiversity (float): Biodiversity of the ecosystem (0-1).
        - water_quality (float): Water quality of the ecosystem (0-1).
        """
        self.name = name
        self.biodiversity = biodiversity
        self.water_quality = water_quality

    def simulate_diversion(self, river, diversion_rate):
        """
        Simulate the effect of river diversion on the ecosystem.

        Args:
        - river (River): River object.
        - diversion_rate (float): Rate of river diversion (0-1).

        Returns:
        - New biodiversity and water quality values.
        """
        # Assume a 10% decrease in biodiversity and water quality for every 10% of river diversion
        new_biodiversity = self.biodiversity * (1 - diversion_rate * 0.1)
        new_water_quality = self.water_quality * (1 - diversion_rate * 0.1)

        # Ensure values are within valid range
        new_biodiversity = max(0, min(new_biodiversity, 1))
        new_water_quality = max(0, min(new_water_quality, 1))

        return new_biodiversity, new_water_quality

def simulate_river_diversion(river, ecosystem, diversion_rate):
    """
    Simulate the effect of river diversion on a local ecosystem.

    Args:
    - river (River): River object.
    - ecosystem (Ecosystem): Ecosystem object.
    - diversion_rate (float): Rate of river diversion (0-1).

    Returns:
    - New biodiversity and water quality values.
    """
    try:
        new_biodiversity, new_water_quality = ecosystem.simulate_diversion(river, diversion_rate)
        return new_biodiversity, new_water_quality
    except Exception as e:
        print(f"Error simulating river diversion: {str(e)}")
        return None

def plot_ecosystem_changes(ecosystem, diversion_rates):
    """
    Plot changes in ecosystem biodiversity and water quality due to river diversion.

    Args:
    - ecosystem (Ecosystem): Ecosystem object.
    - diversion_rates (list): List of diversion rates (0-1).
    """
    biodiversities = []
    water_qualities = []

    for diversion_rate in diversion_rates:
        new_biodiversity, new_water_quality = ecosystem.simulate_diversion(river, diversion_rate)
        biodiversities.append(new_biodiversity)
        water_qualities.append(new_water_quality)

    plt.plot(diversion_rates, biodiversities, label='Biodiversity')
    plt.plot(diversion_rates, water_qualities, label='Water Quality')
    plt.xlabel('Diversion Rate')
    plt.ylabel('Value')
    plt.title('Ecosystem Changes due to River Diversion')
    plt.legend()
    plt.show()

# Example usage
river = River("Šare", 10.0, 50.0)
ecosystem = Ecosystem("Local Ecosystem", 0.8, 0.9)
diversion_rate = 0.2

new_biodiversity, new_water_quality = simulate_river_diversion(river, ecosystem, diversion_rate)
print(f"New biodiversity: {new_biodiversity:.2f}, New water quality: {new_water_quality:.2f}")

diversion_rates = np.linspace(0, 1, 11)
plot_ecosystem_changes(ecosystem, diversion_rates)
```
