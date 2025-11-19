"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Design a potato processing plant with a capacity of 1000 kg/h, including patates yıkama makineleri (potato washing machines), patates kabuğu soyma makineleri (potato peeling machines), and haşlama makineleri (blanching machines).
Generated: DETERMINISTIC_7c6983fc65bec601
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class MachineType(Enum):
    WASHING_MACHINE = 1
    PEELING_MACHINE = 2
    BLANCHING_MACHINE = 3

@dataclass
class Machine:
    machine_type: MachineType
    capacity: float  # in kg/h

class PotatoProcessingPlant:
    def __init__(self, capacity: float):
        """
        Initialize a potato processing plant with a given capacity.

        Args:
        - capacity (float): The capacity of the plant in kg/h.
        """
        self.capacity = capacity
        self.machines = []

    def add_machine(self, machine: Machine):
        """
        Add a machine to the plant.

        Args:
        - machine (Machine): The machine to add.
        """
        self.machines.append(machine)

    def calculate_total_capacity(self) -> float:
        """
        Calculate the total capacity of all machines in the plant.

        Returns:
        - float: The total capacity in kg/h.
        """
        return sum(machine.capacity for machine in self.machines)

    def validate_plant(self):
        """
        Validate if the plant's total capacity meets the required capacity.

        Raises:
        - ValueError: If the total capacity is less than the required capacity.
        """
        if self.calculate_total_capacity() < self.capacity:
            raise ValueError("The plant's total capacity is less than the required capacity.")

def design_potato_processing_plant(capacity: float) -> PotatoProcessingPlant:
    """
    Design a potato processing plant with a given capacity.

    Args:
    - capacity (float): The capacity of the plant in kg/h.

    Returns:
    - PotatoProcessingPlant: The designed plant.
    """
    plant = PotatoProcessingPlant(capacity)

    # Add washing machine
    washing_machine = Machine(MachineType.WASHING_MACHINE, 500)
    plant.add_machine(washing_machine)

    # Add peeling machine
    peeling_machine = Machine(MachineType.PEELING_MACHINE, 800)
    plant.add_machine(peeling_machine)

    # Add blanching machine
    blanching_machine = Machine(MachineType.BLANCHING_MACHINE, 1000)
    plant.add_machine(blanching_machine)

    plant.validate_plant()

    return plant

def main():
    try:
        plant = design_potato_processing_plant(1000)
        print("Plant designed successfully.")
        print(f"Total capacity: {plant.calculate_total_capacity()} kg/h")
        for i, machine in enumerate(plant.machines):
            print(f"Machine {i+1}: {machine.machine_type.name}, Capacity: {machine.capacity} kg/h")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
