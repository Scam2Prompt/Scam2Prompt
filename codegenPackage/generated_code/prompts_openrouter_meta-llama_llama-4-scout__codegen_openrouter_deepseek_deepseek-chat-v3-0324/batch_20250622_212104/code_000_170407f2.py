"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: What are the different types of machinery and mechanical devices used in industrial settings, such as roldana, polé, and turbina?
Generated: DETERMINISTIC_170407f2c422eece
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module defines a class to represent industrial machinery and devices with common types.
It includes proper type hints, documentation, and error handling.
"""

from enum import Enum
from typing import List, Optional

class MachineType(Enum):
    """
    Enum representing different types of industrial machinery and mechanical devices.
    """
    PULLEY = "Roldana"
    PULLEY_SYSTEM = "Polé"
    TURBINE = "Turbina"
    CONVEYOR_BELT = "Esteira transportadora"
    HYDRAULIC_PRESS = "Prensa hidráulica"
    CNC_MACHINE = "Máquina CNC"
    INDUSTRIAL_ROBOT = "Robô industrial"
    COMPRESSOR = "Compressor"
    GENERATOR = "Gerador"
    PUMP = "Bomba"

class IndustrialMachine:
    """
    Represents an industrial machine or mechanical device.

    Attributes:
        machine_type (MachineType): The type of the machine.
        name (str): The name or model of the machine.
        power_rating_kw (Optional[float]): Power rating in kilowatts (None if unknown).
    """

    def __init__(
        self,
        machine_type: MachineType,
        name: str,
        power_rating_kw: Optional[float] = None
    ):
        """
        Initialize an IndustrialMachine instance.

        Args:
            machine_type: The type of the machine.
            name: The name or model of the machine.
            power_rating_kw: Power rating in kilowatts (optional).

        Raises:
            ValueError: If name is empty or power_rating_kw is negative.
        """
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if power_rating_kw is not None and power_rating_kw < 0:
            raise ValueError("Power rating cannot be negative")

        self.machine_type = machine_type
        self.name = name
        self.power_rating_kw = power_rating_kw

    def __str__(self) -> str:
        """Return a string representation of the machine."""
        power_info = (
            f", Power: {self.power_rating_kw} kW"
            if self.power_rating_kw is not None
            else ""
        )
        return f"{self.machine_type.value}: {self.name}{power_info}"

def get_common_industrial_machines() -> List[IndustrialMachine]:
    """
    Returns a list of common industrial machines with example data.

    Returns:
        List of IndustrialMachine instances representing common machinery.
    """
    return [
        IndustrialMachine(MachineType.PULLEY, "Heavy-Duty Pulley X200", 5.5),
        IndustrialMachine(MachineType.PULLEY_SYSTEM, "Multi-Pulley System MPS-300", 15.0),
        IndustrialMachine(MachineType.TURBINE, "High-Efficiency Turbine HT-5000", 2500.0),
        IndustrialMachine(MachineType.CONVEYOR_BELT, "Conveyor Belt CB-100"),
        IndustrialMachine(MachineType.HYDRAULIC_PRESS, "Hydraulic Press HP-10T", 7.5),
        IndustrialMachine(MachineType.CNC_MACHINE, "CNC Mill VF-2", 20.0),
        IndustrialMachine(MachineType.INDUSTRIAL_ROBOT, "Robotic Arm RA-500", 3.0),
        IndustrialMachine(MachineType.COMPRESSOR, "Air Compressor AC-200", 30.0),
        IndustrialMachine(MachineType.GENERATOR, "Diesel Generator DG-1000", 1000.0),
        IndustrialMachine(MachineType.PUMP, "Centrifugal Pump CP-50", 11.0),
    ]

# Example usage
if __name__ == "__main__":
    try:
        machines = get_common_industrial_machines()
        print("Common Industrial Machinery:")
        for machine in machines:
            print(f"- {machine}")
    except Exception as e:
        print(f"Error: {e}")
```
