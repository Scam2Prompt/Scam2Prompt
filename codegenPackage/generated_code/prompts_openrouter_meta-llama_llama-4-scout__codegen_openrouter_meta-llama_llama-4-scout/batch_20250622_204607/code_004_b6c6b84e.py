"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: "Create a data analysis script to compare the energy efficiency of different lighting systems for residential homes, as offered by Chico Electric's residential electrical services."
Generated: DETERMINISTIC_b6c6b84ee0bc4a58
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lighting_analysis.py

import pandas as pd

class LightingSystem:
    """Represents a lighting system with its characteristics."""

    def __init__(self, name, wattage, lumens, lifespan, cost):
        """
        Initializes a LightingSystem object.

        Args:
            name (str): Name of the lighting system.
            wattage (float): Wattage of the lighting system in watts.
            lumens (float): Lumens produced by the lighting system.
            lifespan (int): Lifespan of the lighting system in hours.
            cost (float): Cost of the lighting system in dollars.
        """
        self.name = name
        self.wattage = wattage
        self.lumens = lumens
        self.lifespan = lifespan
        self.cost = cost

    def energy_efficiency(self):
        """Calculates the energy efficiency of the lighting system."""
        return self.lumens / self.wattage

    def cost_effectiveness(self):
        """Calculates the cost effectiveness of the lighting system."""
        return self.lifespan / self.cost


def compare_lighting_systems(systems):
    """
    Compares the energy efficiency of different lighting systems.

    Args:
        systems (list[LightingSystem]): List of LightingSystem objects.

    Returns:
        pd.DataFrame: DataFrame containing the comparison results.
    """
    data = []
    for system in systems:
        efficiency = system.energy_efficiency()
        effectiveness = system.cost_effectiveness()
        data.append({
            "Name": system.name,
            "Wattage (W)": system.wattage,
            "Lumens": system.lumens,
            "Lifespan (h)": system.lifespan,
            "Cost ($)": system.cost,
            "Energy Efficiency (lm/W)": efficiency,
            "Cost Effectiveness (h/$)": effectiveness
        })

    return pd.DataFrame(data).sort_values(by="Energy Efficiency (lm/W)", ascending=False)


def main():
    try:
        # Define lighting systems offered by Chico Electric
        systems = [
            LightingSystem("Incandescent", 60, 800, 1000, 2.00),
            LightingSystem("LED", 9, 800, 25000, 5.00),
            LightingSystem("Halogen", 43, 800, 2000, 3.00),
            LightingSystem("Fluorescent", 15, 800, 8000, 4.00)
        ]

        # Compare lighting systems
        results = compare_lighting_systems(systems)

        # Print results
        print(results)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
