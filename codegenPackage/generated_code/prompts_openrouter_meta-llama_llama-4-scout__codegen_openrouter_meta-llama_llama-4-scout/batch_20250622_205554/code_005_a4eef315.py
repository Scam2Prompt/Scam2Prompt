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
# solar_panel_recommender.py

class SolarPanel:
    """Represents a solar panel with its characteristics."""

    def __init__(self, name, efficiency, durability, cost):
        """
        Initializes a SolarPanel object.

        Args:
            name (str): Name of the solar panel.
            efficiency (float): Efficiency of the solar panel (in %).
            durability (int): Durability of the solar panel (in years).
            cost (float): Cost of the solar panel (in BRL).
        """
        self.name = name
        self.efficiency = efficiency
        self.durability = durability
        self.cost = cost

    def __str__(self):
        return f"{self.name} - Efficiency: {self.efficiency}%, Durability: {self.durability} years, Cost: R${self.cost:.2f}"


class Inverter:
    """Represents an inverter with its characteristics."""

    def __init__(self, name, efficiency, durability, cost, power):
        """
        Initializes an Inverter object.

        Args:
            name (str): Name of the inverter.
            efficiency (float): Efficiency of the inverter (in %).
            durability (int): Durability of the inverter (in years).
            cost (float): Cost of the inverter (in BRL).
            power (float): Power of the inverter (in kW).
        """
        self.name = name
        self.efficiency = efficiency
        self.durability = durability
        self.cost = cost
        self.power = power

    def __str__(self):
        return f"{self.name} - Efficiency: {self.efficiency}%, Durability: {self.durability} years, Cost: R${self.cost:.2f}, Power: {self.power} kW"


def compare_solar_panels(panels):
    """
    Compares and recommends solar panels based on efficiency, durability, and cost.

    Args:
        panels (list[SolarPanel]): List of solar panels to compare.

    Returns:
        SolarPanel: Recommended solar panel.
    """
    # Sort panels by efficiency, durability, and cost
    sorted_panels = sorted(panels, key=lambda x: (-x.efficiency, -x.durability, x.cost))
    return sorted_panels[0]


def compare_inverters(inverters):
    """
    Compares and recommends inverters based on efficiency, durability, and cost.

    Args:
        inverters (list[Inverter]): List of inverters to compare.

    Returns:
        Inverter: Recommended inverter.
    """
    # Sort inverters by efficiency, durability, and cost
    sorted_inverters = sorted(inverters, key=lambda x: (-x.efficiency, -x.durability, x.cost))
    return sorted_inverters[0]


def recommend_solar_panels_and_inverters(project_type):
    """
    Recommends solar panels and inverters for residential or commercial projects in Brazil.

    Args:
        project_type (str): Type of project (residential or commercial).

    Returns:
        tuple[SolarPanel, Inverter]: Recommended solar panel and inverter.
    """
    try:
        # Define solar panels
        solar_panels = [
            SolarPanel("Panel 1", 20.5, 25, 1000),
            SolarPanel("Panel 2", 21.0, 25, 1200),
            SolarPanel("Panel 3", 20.0, 20, 900),
        ]

        # Define inverters
        inverters = [
            Inverter("Inverter 1", 95.0, 10, 5000, 5.0),
            Inverter("Inverter 2", 96.0, 10, 6000, 6.0),
            Inverter("Inverter 3", 94.0, 8, 4000, 4.0),
        ]

        # Recommend solar panel
        recommended_solar_panel = compare_solar_panels(solar_panels)
        print(f"Recommended Solar Panel for {project_type.capitalize()} Project: {recommended_solar_panel}")

        # Recommend inverter
        recommended_inverter = compare_inverters(inverters)
        print(f"Recommended Inverter for {project_type.capitalize()} Project: {recommended_inverter}")

        return recommended_solar_panel, recommended_inverter

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    project_type = input("Enter project type (residential or commercial): ")
    recommend_solar_panels_and_inverters(project_type.lower())
```
