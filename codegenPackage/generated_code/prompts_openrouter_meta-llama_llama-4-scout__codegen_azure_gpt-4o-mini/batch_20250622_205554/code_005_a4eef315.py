"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Compare and recommend different types of solar panels and inverters suitable for residential and commercial projects in Brazil, considering factors like efficiency, durability, and cost.
Generated: DETERMINISTIC_a4eef315d29fbbcb
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class SolarPanel:
    def __init__(self, brand, efficiency, durability, cost):
        """
        Initialize a SolarPanel instance.

        :param brand: str - Brand name of the solar panel
        :param efficiency: float - Efficiency rating of the solar panel (percentage)
        :param durability: int - Durability rating (years)
        :param cost: float - Cost of the solar panel (in BRL)
        """
        self.brand = brand
        self.efficiency = efficiency
        self.durability = durability
        self.cost = cost

    def __repr__(self):
        return f"{self.brand} - Efficiency: {self.efficiency}%, Durability: {self.durability} years, Cost: R${self.cost}"

class Inverter:
    def __init__(self, brand, efficiency, warranty, cost):
        """
        Initialize an Inverter instance.

        :param brand: str - Brand name of the inverter
        :param efficiency: float - Efficiency rating of the inverter (percentage)
        :param warranty: int - Warranty period (years)
        :param cost: float - Cost of the inverter (in BRL)
        """
        self.brand = brand
        self.efficiency = efficiency
        self.warranty = warranty
        self.cost = cost

    def __repr__(self):
        return f"{self.brand} - Efficiency: {self.efficiency}%, Warranty: {self.warranty} years, Cost: R${self.cost}"

def recommend_solar_system(panels, inverters, budget):
    """
    Recommend solar panels and inverters based on efficiency, durability, and cost.

    :param panels: list - List of SolarPanel instances
    :param inverters: list - List of Inverter instances
    :param budget: float - Total budget for the solar system (in BRL)
    :return: list - Recommended combinations of solar panels and inverters
    """
    recommendations = []

    for panel in panels:
        for inverter in inverters:
            total_cost = panel.cost + inverter.cost
            if total_cost <= budget:
                recommendations.append((panel, inverter, total_cost))

    # Sort recommendations by efficiency and then by cost
    recommendations.sort(key=lambda x: (-(x[0].efficiency + x[1].efficiency), x[2]))

    return recommendations

def main():
    # Sample data for solar panels and inverters
    panels = [
        SolarPanel("Brand A", 20.5, 25, 15000),
        SolarPanel("Brand B", 18.0, 20, 12000),
        SolarPanel("Brand C", 22.0, 30, 18000)
    ]

    inverters = [
        Inverter("Inverter X", 95.0, 10, 5000),
        Inverter("Inverter Y", 92.0, 8, 4000),
        Inverter("Inverter Z", 90.0, 12, 4500)
    ]

    # Define budget for the solar system
    budget = 25000

    try:
        recommendations = recommend_solar_system(panels, inverters, budget)

        if recommendations:
            print("Recommended Solar Panel and Inverter Combinations:")
            for panel, inverter, total_cost in recommendations:
                print(f"{panel} + {inverter} = Total Cost: R${total_cost}")
        else:
            print("No suitable combinations found within the budget.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
