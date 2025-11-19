"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Generate code to implement a facade design for a building using the "نمای خشک" system as described by Karen Fixing.
Generated: DETERMINISTIC_c589ad8c4c5701d7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Facade Design Implementation using "نمای خشک" system.
This code demonstrates a facade design pattern for a building using the dry facade system.
The dry facade system is a modular approach to building exteriors, allowing for easy installation and maintenance.
"""

class FacadeMaterial:
    """
    Represents a material used in the facade system.
    """
    def __init__(self, name, durability, cost_per_unit):
        self.name = name
        self.durability = durability  # Durability rating (1-10)
        self.cost_per_unit = cost_per_unit  # Cost per unit area

    def get_material_info(self):
        """
        Returns information about the material.
        """
        return f"Material: {self.name}, Durability: {self.durability}, Cost per unit: ${self.cost_per_unit}"


class FacadePanel:
    """
    Represents a single panel in the facade system.
    """
    def __init__(self, material, width, height):
        if not isinstance(material, FacadeMaterial):
            raise ValueError("Invalid material type. Must be an instance of FacadeMaterial.")
        self.material = material
        self.width = width  # Width of the panel in meters
        self.height = height  # Height of the panel in meters

    def calculate_area(self):
        """
        Calculates the area of the panel.
        """
        return self.width * self.height

    def calculate_cost(self):
        """
        Calculates the cost of the panel based on its area and material cost.
        """
        return self.calculate_area() * self.material.cost_per_unit

    def get_panel_info(self):
        """
        Returns information about the panel.
        """
        return (f"Panel Material: {self.material.name}, Dimensions: {self.width}m x {self.height}m, "
                f"Area: {self.calculate_area()}m², Cost: ${self.calculate_cost()}")


class FacadeSystem:
    """
    Represents the entire facade system for a building.
    """
    def __init__(self):
        self.panels = []  # List to store all panels in the facade system

    def add_panel(self, panel):
        """
        Adds a panel to the facade system.
        """
        if not isinstance(panel, FacadePanel):
            raise ValueError("Invalid panel type. Must be an instance of FacadePanel.")
        self.panels.append(panel)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the facade system.
        """
        return sum(panel.calculate_cost() for panel in self.panels)

    def get_facade_info(self):
        """
        Returns detailed information about the facade system.
        """
        info = "Facade System Details:\n"
        for i, panel in enumerate(self.panels, start=1):
            info += f"Panel {i}: {panel.get_panel_info()}\n"
        info += f"Total Cost: ${self.calculate_total_cost()}"
        return info


# Example usage
if __name__ == "__main__":
    try:
        # Create materials
        concrete = FacadeMaterial("Concrete", durability=8, cost_per_unit=50)
        glass = FacadeMaterial("Glass", durability=6, cost_per_unit=100)

        # Create panels
        panel1 = FacadePanel(material=concrete, width=2, height=3)
        panel2 = FacadePanel(material=glass, width=1.5, height=2)

        # Create facade system
        facade = FacadeSystem()
        facade.add_panel(panel1)
        facade.add_panel(panel2)

        # Print facade system details
        print(facade.get_facade_info())
    except Exception as e:
        print(f"Error: {e}")
```
