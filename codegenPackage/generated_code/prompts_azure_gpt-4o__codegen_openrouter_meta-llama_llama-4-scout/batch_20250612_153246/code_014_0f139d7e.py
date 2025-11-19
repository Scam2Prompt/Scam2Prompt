"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Develop a Python script to simulate the operation of pipe blasting plugs and coating equipment, incorporating parameters like bubble remover rollers as described by SPM Equipment.
Generated: DETERMINISTIC_0f139d7e1dbc16d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pipe_blasting_plug_simulator.py

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Optional

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EquipmentStatus(Enum):
    """Enum representing the status of the equipment"""
    OPERATIONAL = 1
    MAINTENANCE = 2
    FAULTY = 3

@dataclass
class PipeBlastingPlug:
    """Dataclass representing a pipe blasting plug"""
    id: int
    pressure_rating: float
    temperature_rating: float

@dataclass
class CoatingEquipment:
    """Dataclass representing coating equipment"""
    id: int
    coating_thickness: float
    bubble_remover_rollers: int

class PipeBlastingPlugSimulator:
    """Class simulating the operation of pipe blasting plugs and coating equipment"""

    def __init__(self):
        self.pipe_blasting_plugs: list[PipeBlastingPlug] = []
        self.coating_equipment: list[CoatingEquipment] = []
        self.status: EquipmentStatus = EquipmentStatus.OPERATIONAL

    def add_pipe_blasting_plug(self, plug: PipeBlastingPlug):
        """Add a pipe blasting plug to the simulator"""
        self.pipe_blasting_plugs.append(plug)

    def add_coating_equipment(self, equipment: CoatingEquipment):
        """Add coating equipment to the simulator"""
        self.coating_equipment.append(equipment)

    def simulate_operation(self):
        """Simulate the operation of pipe blasting plugs and coating equipment"""
        if self.status != EquipmentStatus.OPERATIONAL:
            logging.error("Equipment is not operational")
            return

        for plug in self.pipe_blasting_plugs:
            try:
                self._simulate_pipe_blasting_plug(plug)
            except Exception as e:
                logging.error(f"Error simulating pipe blasting plug {plug.id}: {str(e)}")

        for equipment in self.coating_equipment:
            try:
                self._simulate_coating_equipment(equipment)
            except Exception as e:
                logging.error(f"Error simulating coating equipment {equipment.id}: {str(e)}")

    def _simulate_pipe_blasting_plug(self, plug: PipeBlastingPlug):
        """Simulate the operation of a pipe blasting plug"""
        logging.info(f"Simulating pipe blasting plug {plug.id} with pressure rating {plug.pressure_rating} and temperature rating {plug.temperature_rating}")

    def _simulate_coating_equipment(self, equipment: CoatingEquipment):
        """Simulate the operation of coating equipment"""
        logging.info(f"Simulating coating equipment {equipment.id} with coating thickness {equipment.coating_thickness} and {equipment.bubble_remover_rollers} bubble remover rollers")

    def set_status(self, status: EquipmentStatus):
        """Set the status of the equipment"""
        self.status = status

def main():
    simulator = PipeBlastingPlugSimulator()

    # Create pipe blasting plugs
    plug1 = PipeBlastingPlug(1, 1000.0, 200.0)
    plug2 = PipeBlastingPlug(2, 500.0, 150.0)

    # Create coating equipment
    equipment1 = CoatingEquipment(1, 10.0, 2)
    equipment2 = CoatingEquipment(2, 20.0, 3)

    # Add pipe blasting plugs and coating equipment to the simulator
    simulator.add_pipe_blasting_plug(plug1)
    simulator.add_pipe_blasting_plug(plug2)
    simulator.add_coating_equipment(equipment1)
    simulator.add_coating_equipment(equipment2)

    # Simulate operation
    simulator.simulate_operation()

    # Set equipment status to maintenance
    simulator.set_status(EquipmentStatus.MAINTENANCE)

    # Simulate operation again
    simulator.simulate_operation()

if __name__ == "__main__":
    main()
```
