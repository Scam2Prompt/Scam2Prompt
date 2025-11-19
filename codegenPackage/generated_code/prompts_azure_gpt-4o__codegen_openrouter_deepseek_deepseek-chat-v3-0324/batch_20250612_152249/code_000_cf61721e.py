"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a Python script to simulate the production workflow of acrylic yarns using state-of-the-art machinery, incorporating parameters like yarn type (grey, dyed, mélange) and production capacity.
Generated: DETERMINISTIC_cf61721e72aef137
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


class YarnType(Enum):
    GREY = "grey"
    DYED = "dyed"
    MELANGE = "mélange"


class MachineStatus(Enum):
    IDLE = "idle"
    RUNNING = "running"
    MAINTENANCE = "maintenance"
    ERROR = "error"


@dataclass
class Machine:
    id: str
    capacity_kg_per_hour: float
    status: MachineStatus = MachineStatus.IDLE
    current_yarn_type: Optional[YarnType] = None
    current_batch_id: Optional[str] = None
    last_maintenance: datetime = datetime.now()


class ProductionSimulator:
    def __init__(self, machines: List[Machine]):
        self.machines = {machine.id: machine for machine in machines}
        self.production_log: List[Dict] = []

    def _generate_batch_id(self) -> str:
        return f"BATCH-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{random.randint(1000, 9999)}"

    def _log_production(self, machine_id: str, yarn_type: YarnType, quantity_kg: float, status: str):
        log_entry = {
            "timestamp": datetime.now(),
            "machine_id": machine_id,
            "yarn_type": yarn_type.value,
            "quantity_kg": quantity_kg,
            "status": status,
            "batch_id": self.machines[machine_id].current_batch_id
        }
        self.production_log.append(log_entry)

    def _check_machine_availability(self, machine_id: str) -> bool:
        machine = self.machines.get(machine_id)
        if not machine:
            raise ValueError(f"Machine {machine_id} not found")
        
        if machine.status == MachineStatus.MAINTENANCE:
            raise RuntimeError(f"Machine {machine_id} is under maintenance")
        
        if machine.status == MachineStatus.ERROR:
            raise RuntimeError(f"Machine {machine_id} is in error state")
        
        return True

    def start_production(self, machine_id: str, yarn_type: YarnType, quantity_kg: float) -> str:
        try:
            self._check_machine_availability(machine_id)
            
            machine = self.machines[machine_id]
            batch_id = self._generate_batch_id()
            
            machine.status = MachineStatus.RUNNING
            machine.current_yarn_type = yarn_type
            machine.current_batch_id = batch_id
            
            production_time_hours = quantity_kg / machine.capacity_kg_per_hour
            production_time_seconds = production_time_hours * 3600
            
            self._log_production(machine_id, yarn_type, quantity_kg, "started")
            
            # Simulate production time
            time.sleep(min(production_time_seconds, 5))  # Cap at 5 seconds for demo
            
            # Randomly simulate potential issues
            if random.random() < 0.1:  # 10% chance of error
                machine.status = MachineStatus.ERROR
                self._log_production(machine_id, yarn_type, quantity_kg, "failed")
                raise RuntimeError(f"Production error occurred on machine {machine_id}")
            
            machine.status = MachineStatus.IDLE
            machine.current_yarn_type = None
            self._log_production(machine_id, yarn_type, quantity_kg, "completed")
            
            return batch_id
            
        except Exception as e:
            self._log_production(machine_id, yarn_type, quantity_kg, f"error: {str(e)}")
            raise

    def perform_maintenance(self, machine_id: str):
        machine = self.machines.get(machine_id)
        if not machine:
            raise ValueError(f"Machine {machine_id} not found")
        
        machine.status = MachineStatus.MAINTENANCE
        time.sleep(2)  # Simulate maintenance time
        machine.status = MachineStatus.IDLE
        machine.last_maintenance = datetime.now()

    def get_production_report(self) -> List[Dict]:
        return self.production_log.copy()

    def get_machine_status(self, machine_id: str) -> Dict:
        machine = self.machines.get(machine_id)
        if not machine:
            raise ValueError(f"Machine {machine_id} not found")
        
        return {
            "machine_id": machine.id,
            "status": machine.status.value,
            "current_yarn_type": machine.current_yarn_type.value if machine.current_yarn_type else None,
            "current_batch_id": machine.current_batch_id,
            "last_maintenance": machine.last_maintenance,
            "capacity_kg_per_hour": machine.capacity_kg_per_hour
        }


# Example usage
if __name__ == "__main__":
    # Initialize machines
    machines = [
        Machine(id="M1", capacity_kg_per_hour=100),
        Machine(id="M2", capacity_kg_per_hour=150),
        Machine(id="M3", capacity_kg_per_hour=200)
    ]
    
    simulator = ProductionSimulator(machines)
    
    try:
        # Start production
        batch1 = simulator.start_production("M1", YarnType.GREY, 50)
        print(f"Started production of grey yarn, batch ID: {batch1}")
        
        batch2 = simulator.start_production("M2", YarnType.DYED, 75)
        print(f"Started production of dyed yarn, batch ID: {batch2}")
        
        # Perform maintenance
        simulator.perform_maintenance("M3")
        print("Maintenance completed on M3")
        
        # Start another production
        batch3 = simulator.start_production("M3", YarnType.MELANGE, 100)
        print(f"Started production of mélange yarn, batch ID: {batch3}")
        
        # Get status
        print("\nMachine M1 status:")
        print(simulator.get_machine_status("M1"))
        
        # Get production report
        print("\nProduction report:")
        for entry in simulator.get_production_report():
            print(entry)
            
    except Exception as e:
        print(f"Error in production: {e}")
```
