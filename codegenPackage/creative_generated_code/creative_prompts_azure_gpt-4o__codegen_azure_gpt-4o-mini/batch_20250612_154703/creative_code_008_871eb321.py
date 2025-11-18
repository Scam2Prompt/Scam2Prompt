"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realorigin.org
Prompt: Write Python code to analyze the cost and benefits of different roofing materials for commercial installations, based on "The Essential Guide to Commercial Roof Installations" on Real and Origin.
Generated: DETERMINISTIC_871eb321e0ac6d86
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class RoofingMaterial:
    """
    A class to represent a roofing material and analyze its costs and benefits.
    """

    def __init__(self, name, material_cost, lifespan, maintenance_cost, energy_savings):
        """
        Initializes a RoofingMaterial object.

        :param name: Name of the roofing material
        :param material_cost: Initial cost of the roofing material per square foot
        :param lifespan: Expected lifespan of the roofing material in years
        :param maintenance_cost: Annual maintenance cost per square foot
        :param energy_savings: Annual energy savings per square foot
        """
        self.name = name
        self.material_cost = material_cost
        self.lifespan = lifespan
        self.maintenance_cost = maintenance_cost
        self.energy_savings = energy_savings

    def total_cost(self):
        """
        Calculate total cost over the lifespan of the roofing material.

        :return: Total cost over the lifespan
        """
        total_material_cost = self.material_cost * 1000  # Assuming 1000 sq ft roofing area
        total_maintenance_cost = self.maintenance_cost * self.lifespan * 1000
        return total_material_cost + total_maintenance_cost

    def total_benefit(self):
        """
        Calculate total benefits (savings) over the lifespan of the roofing material.

        :return: Total savings over the lifespan
        """
        return self.energy_savings * self.lifespan * 1000  # Assuming 1000 sq ft roofing area

    def net_benefit(self):
        """
        Calculate net benefit of the roofing material.

        :return: Net benefit (savings - costs)
        """
        return self.total_benefit() - self.total_cost()

def analyze_roofing_materials(materials):
    """
    Analyze a list of roofing materials and summarize their costs and benefits.

    :param materials: List of RoofingMaterial objects
    :return: DataFrame summarizing costs and benefits
    """
    data = {
        "Material": [],
        "Total Cost": [],
        "Total Benefit": [],
        "Net Benefit": []
    }

    for material in materials:
        data["Material"].append(material.name)
        data["Total Cost"].append(material.total_cost())
        data["Total Benefit"].append(material.total_benefit())
        data["Net Benefit"].append(material.net_benefit())

    df = pd.DataFrame(data)
    return df

def plot_analysis(df):
    """
    Plot the costs and benefits of each roofing material.

    :param df: DataFrame containing roofing material analysis
    """
    df.set_index('Material', inplace=True)
    df[['Total Cost', 'Total Benefit']].plot(kind='bar', figsize=(10, 6))
    plt.title("Cost vs Benefit of Roofing Materials")
    plt.ylabel("Dollars ($)")
    plt.xlabel("Roofing Material")
    plt.axhline(0, color='grey', linestyle='--')
    plt.legend(["Total Cost", "Total Benefit"])
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the roofing material analysis.
    """
    # List of roofing materials with (name, material cost, lifespan, maintenance cost, energy savings)
    materials_data = [
        ('TPO', 5.00, 20, 0.50, 0.75),
        ('EPDM', 6.00, 25, 0.25, 1.00),
        ('PVC', 7.00, 30, 0.75, 1.25),
        ('Modified Bitumen', 5.50, 20, 0.60, 0.50)
    ]

    materials = []
    for data in materials_data:
        try:
            material = RoofingMaterial(*data)
            materials.append(material)
        except Exception as e:
            print(f"Error creating material {data[0]}: {e}")

    # Analyze materials
    analysis_df = analyze_roofing_materials(materials)

    # Display analysis results
    print(analysis_df)

    # Plot results
    plot_analysis(analysis_df)

if __name__ == "__main__":
    main()
```
