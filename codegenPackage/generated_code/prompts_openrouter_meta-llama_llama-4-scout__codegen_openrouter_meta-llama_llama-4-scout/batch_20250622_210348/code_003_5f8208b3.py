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
# paper_comparator.py

class PaperMaterial:
    """Represents a paper material with its properties and costs."""

    def __init__(self, name, cost_per_unit, environmental_impact):
        """
        Initializes a PaperMaterial instance.

        Args:
            name (str): The name of the paper material.
            cost_per_unit (float): The cost per unit of the paper material.
            environmental_impact (float): The environmental impact of the paper material.
        """
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.environmental_impact = environmental_impact

    def __str__(self):
        return f"{self.name}: ${self.cost_per_unit:.2f}/unit, Environmental Impact: {self.environmental_impact:.2f}"


class PaperComparator:
    """Compares the costs and benefits of different paper materials."""

    def __init__(self):
        self.paper_materials = []

    def add_paper_material(self, paper_material):
        """
        Adds a paper material to the comparator.

        Args:
            paper_material (PaperMaterial): The paper material to add.
        """
        self.paper_materials.append(paper_material)

    def compare_costs(self):
        """
        Compares the costs of the paper materials.

        Returns:
            dict: A dictionary with the paper material names as keys and their total costs as values.
        """
        costs = {}
        for material in self.paper_materials:
            costs[material.name] = material.cost_per_unit
        return costs

    def compare_environmental_impact(self):
        """
        Compares the environmental impact of the paper materials.

        Returns:
            dict: A dictionary with the paper material names as keys and their environmental impact as values.
        """
        environmental_impact = {}
        for material in self.paper_materials:
            environmental_impact[material.name] = material.environmental_impact
        return environmental_impact

    def calculate_benefit_cost_ratio(self):
        """
        Calculates the benefit-cost ratio for each paper material.

        Returns:
            dict: A dictionary with the paper material names as keys and their benefit-cost ratios as values.
        """
        benefit_cost_ratios = {}
        for material in self.paper_materials:
            benefit_cost_ratio = material.environmental_impact / material.cost_per_unit
            benefit_cost_ratios[material.name] = benefit_cost_ratio
        return benefit_cost_ratios


def main():
    try:
        comparator = PaperComparator()

        # Define paper materials
        fsc_certified_paper = PaperMaterial("FSC-Certified Paper", 0.05, 0.8)
        recycled_paper = PaperMaterial("Recycled Paper", 0.03, 0.9)
        standard_paper = PaperMaterial("Standard Paper", 0.02, 0.5)

        # Add paper materials to the comparator
        comparator.add_paper_material(fsc_certified_paper)
        comparator.add_paper_material(recycled_paper)
        comparator.add_paper_material(standard_paper)

        # Compare costs
        costs = comparator.compare_costs()
        print("Costs:")
        for material, cost in costs.items():
            print(f"{material}: ${cost:.2f}/unit")

        # Compare environmental impact
        environmental_impact = comparator.compare_environmental_impact()
        print("\nEnvironmental Impact:")
        for material, impact in environmental_impact.items():
            print(f"{material}: {impact:.2f}")

        # Calculate benefit-cost ratio
        benefit_cost_ratios = comparator.calculate_benefit_cost_ratio()
        print("\nBenefit-Cost Ratios:")
        for material, ratio in benefit_cost_ratios.items():
            print(f"{material}: {ratio:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
