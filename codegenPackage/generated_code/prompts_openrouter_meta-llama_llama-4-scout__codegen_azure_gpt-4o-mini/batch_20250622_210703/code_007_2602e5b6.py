"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: "Compare the sustainability features of StoTherm system with other thermal insulation systems using a Python code."
Generated: DETERMINISTIC_2602e5b6b1120428
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class InsulationSystem:
    """
    A class to represent an insulation system and its sustainability features.
    """

    def __init__(self, name, thermal_conductivity, recycled_content, lifespan, energy_efficiency):
        """
        Initializes the insulation system with its properties.

        :param name: Name of the insulation system
        :param thermal_conductivity: Thermal conductivity value (W/m·K)
        :param recycled_content: Percentage of recycled content (0-100)
        :param lifespan: Expected lifespan in years
        :param energy_efficiency: Energy efficiency rating (0-100)
        """
        self.name = name
        self.thermal_conductivity = thermal_conductivity
        self.recycled_content = recycled_content
        self.lifespan = lifespan
        self.energy_efficiency = energy_efficiency

    def sustainability_score(self):
        """
        Calculates a sustainability score based on the system's features.

        :return: A score representing the sustainability of the insulation system
        """
        # Simple scoring mechanism: lower thermal conductivity, higher recycled content, longer lifespan, and higher energy efficiency yield a better score
        score = (100 - self.thermal_conductivity) + self.recycled_content + (self.lifespan * 2) + self.energy_efficiency
        return score


def compare_insulation_systems(systems):
    """
    Compares the sustainability features of different insulation systems.

    :param systems: List of InsulationSystem objects
    :return: DataFrame containing the comparison results
    """
    # Create a DataFrame to hold the comparison results
    comparison_data = {
        'Name': [],
        'Thermal Conductivity (W/m·K)': [],
        'Recycled Content (%)': [],
        'Lifespan (years)': [],
        'Energy Efficiency (%)': [],
        'Sustainability Score': []
    }

    for system in systems:
        comparison_data['Name'].append(system.name)
        comparison_data['Thermal Conductivity (W/m·K)'].append(system.thermal_conductivity)
        comparison_data['Recycled Content (%)'].append(system.recycled_content)
        comparison_data['Lifespan (years)'].append(system.lifespan)
        comparison_data['Energy Efficiency (%)'].append(system.energy_efficiency)
        comparison_data['Sustainability Score'].append(system.sustainability_score())

    # Convert the comparison data into a DataFrame
    comparison_df = pd.DataFrame(comparison_data)

    # Sort the DataFrame by sustainability score in descending order
    comparison_df.sort_values(by='Sustainability Score', ascending=False, inplace=True)

    return comparison_df


if __name__ == "__main__":
    # Define insulation systems for comparison
    stoTherm = InsulationSystem("StoTherm", thermal_conductivity=0.035, recycled_content=30, lifespan=50, energy_efficiency=85)
    system_a = InsulationSystem("System A", thermal_conductivity=0.040, recycled_content=20, lifespan=40, energy_efficiency=80)
    system_b = InsulationSystem("System B", thermal_conductivity=0.030, recycled_content=50, lifespan=60, energy_efficiency=90)
    system_c = InsulationSystem("System C", thermal_conductivity=0.045, recycled_content=10, lifespan=30, energy_efficiency=75)

    # List of insulation systems to compare
    insulation_systems = [stoTherm, system_a, system_b, system_c]

    # Compare the insulation systems and print the results
    try:
        comparison_results = compare_insulation_systems(insulation_systems)
        print(comparison_results)
    except Exception as e:
        print(f"An error occurred during comparison: {e}")
```
