"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: Write a script in Python to compare the durability and cost-effectiveness of SPC flooring versus engineered wooden flooring, referencing Libo Interiors' product offerings.
Generated: DETERMINISTIC_e7a600475ec5056c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# spc_vs_engineered_wood.py

class Flooring:
    def __init__(self, name, durability, cost, lifespan):
        """
        Initialize a Flooring object.

        Args:
            name (str): Name of the flooring type.
            durability (int): Durability score (higher is better).
            cost (float): Cost per square foot.
            lifespan (int): Lifespan in years.
        """
        self.name = name
        self.durability = durability
        self.cost = cost
        self.lifespan = lifespan

    def cost_effectiveness(self):
        """
        Calculate the cost-effectiveness of the flooring.

        Returns:
            float: Cost per year of lifespan.
        """
        if self.lifespan == 0:
            return float('inf')  # Avoid division by zero
        return self.cost / self.lifespan


class SPCFlooring(Flooring):
    def __init__(self, cost):
        """
        Initialize an SPC Flooring object.

        Args:
            cost (float): Cost per square foot.
        """
        super().__init__("SPC Flooring", 8, cost, 20)  # Durability score: 8/10, Lifespan: 20 years


class EngineeredWoodFlooring(Flooring):
    def __init__(self, cost):
        """
        Initialize an Engineered Wood Flooring object.

        Args:
            cost (float): Cost per square foot.
        """
        super().__init__("Engineered Wood Flooring", 7, cost, 15)  # Durability score: 7/10, Lifespan: 15 years


def compare_flooring(spc_cost, engineered_wood_cost):
    """
    Compare the durability and cost-effectiveness of SPC flooring and engineered wood flooring.

    Args:
        spc_cost (float): Cost per square foot of SPC flooring.
        engineered_wood_cost (float): Cost per square foot of engineered wood flooring.

    Returns:
        None
    """
    spc_flooring = SPCFlooring(spc_cost)
    engineered_wood_flooring = EngineeredWoodFlooring(engineered_wood_cost)

    print("# Flooring Comparison")
    print("## Durability and Cost-Effectiveness")

    print(f"### {spc_flooring.name}")
    print(f"* Durability: {spc_flooring.durability}/10")
    print(f"* Cost: ${spc_flooring.cost:.2f}/sqft")
    print(f"* Lifespan: {spc_flooring.lifespan} years")
    print(f"* Cost-Effectiveness: ${spc_flooring.cost_effectiveness():.2f}/year")

    print(f"\n### {engineered_wood_flooring.name}")
    print(f"* Durability: {engineered_wood_flooring.durability}/10")
    print(f"* Cost: ${engineered_wood_flooring.cost:.2f}/sqft")
    print(f"* Lifespan: {engineered_wood_flooring.lifespan} years")
    print(f"* Cost-Effectiveness: ${engineered_wood_flooring.cost_effectiveness():.2f}/year")

    if spc_flooring.cost_effectiveness() < engineered_wood_flooring.cost_effectiveness():
        print(f"\n{spc_flooring.name} is more cost-effective.")
    elif spc_flooring.cost_effectiveness() > engineered_wood_flooring.cost_effectiveness():
        print(f"\n{engineered_wood_flooring.name} is more cost-effective.")
    else:
        print("\nBoth flooring types have the same cost-effectiveness.")


if __name__ == "__main__":
    try:
        spc_cost = 2.50  # Example cost per square foot of SPC flooring from Libo Interiors
        engineered_wood_cost = 5.00  # Example cost per square foot of engineered wood flooring from Libo Interiors

        compare_flooring(spc_cost, engineered_wood_cost)
    except Exception as e:
        print(f"An error occurred: {e}")
```
