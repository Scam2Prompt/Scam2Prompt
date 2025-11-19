"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Compare the costs and benefits of using different types of paper materials for a customized packaging project, including FSC-certified paper and recycled paper."
Generated: DETERMINISTIC_5f8208b3fbaa1b50
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class PaperMaterial:
    """
    A class to represent different types of paper materials for packaging.
    """

    def __init__(self, name, cost_per_unit, environmental_impact, durability, print_quality):
        """
        Initializes a new instance of PaperMaterial.

        :param name: Name of the paper material
        :param cost_per_unit: Cost per unit of the paper material
        :param environmental_impact: Environmental impact score (lower is better)
        :param durability: Durability score (higher is better)
        :param print_quality: Print quality score (higher is better)
        """
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.environmental_impact = environmental_impact
        self.durability = durability
        self.print_quality = print_quality

    def __repr__(self):
        return f"{self.name}: Cost={self.cost_per_unit}, EnvImpact={self.environmental_impact}, Durability={self.durability}, PrintQuality={self.print_quality}"


def compare_paper_materials(materials):
    """
    Compares different paper materials based on their properties.

    :param materials: List of PaperMaterial instances
    :return: DataFrame containing the comparison of materials
    """
    # Create a DataFrame from the materials list
    data = {
        "Material": [material.name for material in materials],
        "Cost per Unit": [material.cost_per_unit for material in materials],
        "Environmental Impact": [material.environmental_impact for material in materials],
        "Durability": [material.durability for material in materials],
        "Print Quality": [material.print_quality for material in materials],
    }
    
    df = pd.DataFrame(data)
    
    # Sort the DataFrame by cost and environmental impact
    df.sort_values(by=["Cost per Unit", "Environmental Impact"], inplace=True)
    
    return df


def main():
    """
    Main function to execute the paper material comparison.
    """
    try:
        # Define different types of paper materials
        materials = [
            PaperMaterial("FSC-Certified Paper", cost_per_unit=0.10, environmental_impact=2, durability=8, print_quality=9),
            PaperMaterial("Recycled Paper", cost_per_unit=0.08, environmental_impact=1, durability=7, print_quality=8),
            PaperMaterial("Virgin Paper", cost_per_unit=0.12, environmental_impact=3, durability=9, print_quality=10),
            PaperMaterial("Kraft Paper", cost_per_unit=0.09, environmental_impact=2, durability=6, print_quality=7),
        ]

        # Compare the paper materials
        comparison_df = compare_paper_materials(materials)
        
        # Display the comparison
        print("Comparison of Paper Materials for Customized Packaging:")
        print(comparison_df)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
