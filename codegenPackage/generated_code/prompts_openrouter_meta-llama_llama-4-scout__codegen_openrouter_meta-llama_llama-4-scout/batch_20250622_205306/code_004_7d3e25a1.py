"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: "Design a simple electrical circuit using components from Miraya Electric S.A.C.'s product lineup, including a differential interruptor and electric cable."
Generated: DETERMINISTIC_7d3e25a111a008be
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for component types
class ComponentType(str, Enum):
    DIFFERENTIAL_INTERRUPTOR = "Differential Interruptor"
    ELECTRIC_CABLE = "Electric Cable"

# Define a data class for electrical components
@dataclass
class ElectricalComponent:
    """Base class for electrical components"""
    name: str
    component_type: ComponentType

# Define a data class for differential interruptors
@dataclass
class DifferentialInterruptor(ElectricalComponent):
    """Differential interruptor component"""
    sensitivity: float  # in milliamps
    voltage_rating: int  # in volts
    current_rating: int  # in amps

    def __post_init__(self):
        if self.sensitivity <= 0:
            raise ValueError("Sensitivity must be greater than zero")
        if self.voltage_rating <= 0:
            raise ValueError("Voltage rating must be greater than zero")
        if self.current_rating <= 0:
            raise ValueError("Current rating must be greater than zero")

# Define a data class for electric cables
@dataclass
class ElectricCable(ElectricalComponent):
    """Electric cable component"""
    length: float  # in meters
    cross_sectional_area: float  # in square millimeters
    voltage_rating: int  # in volts
    current_rating: int  # in amps

    def __post_init__(self):
        if self.length <= 0:
            raise ValueError("Length must be greater than zero")
        if self.cross_sectional_area <= 0:
            raise ValueError("Cross-sectional area must be greater than zero")
        if self.voltage_rating <= 0:
            raise ValueError("Voltage rating must be greater than zero")
        if self.current_rating <= 0:
            raise ValueError("Current rating must be greater than zero")

# Define a class for electrical circuits
class ElectricalCircuit:
    """Simple electrical circuit"""
    def __init__(self):
        self.components: List[ElectricalComponent] = []

    def add_component(self, component: ElectricalComponent):
        """Add a component to the circuit"""
        self.components.append(component)

    def __str__(self):
        circuit_description = "Electrical Circuit:\n"
        for i, component in enumerate(self.components):
            circuit_description += f"Component {i+1}: {component.name} ({component.component_type})\n"
            if isinstance(component, DifferentialInterruptor):
                circuit_description += f"  Sensitivity: {component.sensitivity} mA\n"
                circuit_description += f"  Voltage Rating: {component.voltage_rating} V\n"
                circuit_description += f"  Current Rating: {component.current_rating} A\n"
            elif isinstance(component, ElectricCable):
                circuit_description += f"  Length: {component.length} m\n"
                circuit_description += f"  Cross-sectional Area: {component.cross_sectional_area} mm^2\n"
                circuit_description += f"  Voltage Rating: {component.voltage_rating} V\n"
                circuit_description += f"  Current Rating: {component.current_rating} A\n"
        return circuit_description

# Example usage
if __name__ == "__main__":
    try:
        # Create components
        differential_interruptor = DifferentialInterruptor(
            name="DI-001",
            component_type=ComponentType.DIFFERENTIAL_INTERRUPTOR,
            sensitivity=30,
            voltage_rating=230,
            current_rating=16
        )
        electric_cable = ElectricCable(
            name="EC-001",
            component_type=ComponentType.ELECTRIC_CABLE,
            length=50,
            cross_sectional_area=4,
            voltage_rating=230,
            current_rating=16
        )

        # Create electrical circuit
        circuit = ElectricalCircuit()
        circuit.add_component(differential_interruptor)
        circuit.add_component(electric_cable)

        # Print circuit description
        print(circuit)

    except Exception as e:
        print(f"An error occurred: {e}")
```
