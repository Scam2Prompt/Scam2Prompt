"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Design an electrical system for an industrial facility using Italian regulations and CEI standards.
Generated: DETERMINISTIC_dab353873986c244
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_system.py

from typing import List, Dict

class ElectricalComponent:
    """Base class for electrical components."""

    def __init__(self, name: str, voltage: float, current: float):
        """
        Initialize an electrical component.

        Args:
        - name (str): Component name.
        - voltage (float): Component voltage.
        - current (float): Component current.
        """
        self.name = name
        self.voltage = voltage
        self.current = current

    def __str__(self):
        return f"{self.name}: {self.voltage}V, {self.current}A"


class Transformer(ElectricalComponent):
    """Transformer class."""

    def __init__(self, name: str, voltage_primary: float, voltage_secondary: float, power: float):
        """
        Initialize a transformer.

        Args:
        - name (str): Transformer name.
        - voltage_primary (float): Primary voltage.
        - voltage_secondary (float): Secondary voltage.
        - power (float): Transformer power.
        """
        super().__init__(name, voltage_primary, 0)
        self.voltage_primary = voltage_primary
        self.voltage_secondary = voltage_secondary
        self.power = power

    def __str__(self):
        return f"Transformer {self.name}: {self.voltage_primary}V -> {self.voltage_secondary}V, {self.power}kVA"


class ElectricalPanel:
    """Electrical panel class."""

    def __init__(self, name: str, voltage: float, current: float):
        """
        Initialize an electrical panel.

        Args:
        - name (str): Panel name.
        - voltage (float): Panel voltage.
        - current (float): Panel current.
        """
        self.name = name
        self.voltage = voltage
        self.current = current
        self.components: List[ElectricalComponent] = []

    def add_component(self, component: ElectricalComponent):
        """Add a component to the panel."""
        self.components.append(component)

    def __str__(self):
        panel_info = f"Electrical Panel {self.name}: {self.voltage}V, {self.current}A\n"
        components_info = "\n".join(["  - " + str(component) for component in self.components])
        return panel_info + components_info


class ElectricalSystem:
    """Electrical system class."""

    def __init__(self):
        self.panels: Dict[str, ElectricalPanel] = {}

    def add_panel(self, panel: ElectricalPanel):
        """Add a panel to the system."""
        self.panels[panel.name] = panel

    def __str__(self):
        system_info = "Electrical System:\n"
        panels_info = "\n\n".join([str(panel) for panel in self.panels.values()])
        return system_info + panels_info


def calculate_system_power(system: ElectricalSystem) -> float:
    """
    Calculate the total power of the electrical system.

    Args:
    - system (ElectricalSystem): Electrical system.

    Returns:
    - float: Total power.
    """
    total_power = 0
    for panel in system.panels.values():
        for component in panel.components:
            if isinstance(component, Transformer):
                total_power += component.power
    return total_power


def design_electrical_system() -> ElectricalSystem:
    """
    Design an electrical system for an industrial facility using Italian regulations and CEI standards.

    Returns:
    - ElectricalSystem: Designed electrical system.
    """
    system = ElectricalSystem()

    # Create panels
    panel1 = ElectricalPanel("Panel 1", 400, 100)
    panel2 = ElectricalPanel("Panel 2", 230, 50)

    # Create components
    transformer1 = Transformer("Transformer 1", 400, 230, 1000)
    transformer2 = Transformer("Transformer 2", 230, 400, 500)

    # Add components to panels
    panel1.add_component(transformer1)
    panel2.add_component(transformer2)

    # Add panels to system
    system.add_panel(panel1)
    system.add_panel(panel2)

    return system


def main():
    try:
        system = design_electrical_system()
        print(system)
        total_power = calculate_system_power(system)
        print(f"\nTotal system power: {total_power}kVA")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
