"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Design an algorithm for optimizing the use of Nordson's FoamMelt and SureFoam machines in a foam dispensing application.
Generated: DETERMINISTIC_5b9593572086831b
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Tuple, Optional
from enum import Enum

class MachineType(Enum):
    FOAM_MELT = "FoamMelt"
    SURE_FOAM = "SureFoam"

class Machine:
    def __init__(self, machine_id: str, machine_type: MachineType, capacity: float, efficiency: float):
        """
        Initialize a foam dispensing machine.
        
        Args:
            machine_id: Unique identifier for the machine
            machine_type: Type of machine (FoamMelt or SureFoam)
            capacity: Maximum foam output per hour (in kg)
            efficiency: Efficiency factor (0.0 to 1.0)
        """
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.capacity = capacity
        self.efficiency = efficiency
        self.current_load = 0.0

    def can_handle(self, required_output: float) -> bool:
        """
        Check if machine can handle additional output requirement.
        
        Args:
            required_output: Additional output needed (in kg)
            
        Returns:
            bool: True if machine can handle the load, False otherwise
        """
        available_capacity = (self.capacity * self.efficiency) - self.current_load
        return available_capacity >= required_output

    def assign_load(self, load: float) -> None:
        """
        Assign a load to the machine.
        
        Args:
            load: Load to assign (in kg)
            
        Raises:
            ValueError: If load exceeds available capacity
        """
        if not self.can_handle(load):
            raise ValueError(f"Machine {self.machine_id} cannot handle load {load}")
        self.current_load += load

    def reset_load(self) -> None:
        """Reset the machine's current load to zero."""
        self.current_load = 0.0

    def __repr__(self) -> str:
        return f"{self.machine_type.value} {self.machine_id} (Load: {self.current_load}/{self.capacity * self.efficiency})"

class FoamDispensingOptimizer:
    def __init__(self, machines: List[Machine]):
        """
        Initialize the foam dispensing optimizer with available machines.
        
        Args:
            machines: List of available machines
        """
        self.machines = machines
        self.reset_all_machines()

    def reset_all_machines(self) -> None:
        """Reset all machines to zero load."""
        for machine in self.machines:
            machine.reset_load()

    def optimize_dispensing(self, required_output: float) -> Dict[str, float]:
        """
        Optimize foam dispensing across available machines.
        
        Args:
            required_output: Total foam output needed (in kg)
            
        Returns:
            Dict[str, float]: Mapping of machine IDs to assigned loads
            
        Raises:
            ValueError: If total required output exceeds combined capacity
        """
        if required_output <= 0:
            raise ValueError("Required output must be positive")

        total_capacity = sum(m.capacity * m.efficiency for m in self.machines)
        if required_output > total_capacity:
            raise ValueError(f"Required output {required_output} exceeds total capacity {total_capacity}")

        self.reset_all_machines()
        remaining_output = required_output
        assignments = {}

        # Priority queue: (-available_capacity, machine)
        # We use negative to simulate max-heap behavior
        heap = []
        for machine in self.machines:
            available_capacity = machine.capacity * machine.efficiency
            heapq.heappush(heap, (-available_capacity, machine))

        while remaining_output > 0 and heap:
            neg_capacity, machine = heapq.heappop(heap)
            available_capacity = -neg_capacity

            # Assign as much as possible to this machine
            assign_amount = min(available_capacity, remaining_output)
            machine.assign_load(assign_amount)
            assignments[machine.machine_id] = assign_amount
            remaining_output -= assign_amount

            # If there's remaining capacity, push back to heap
            remaining_capacity = available_capacity - assign_amount
            if remaining_capacity > 0:
                heapq.heappush(heap, (-remaining_capacity, machine))

        return assignments

    def get_utilization_report(self) -> Dict[str, float]:
        """
        Generate a utilization report for all machines.
        
        Returns:
            Dict[str, float]: Mapping of machine IDs to utilization percentage (0-100)
        """
        report = {}
        for machine in self.machines:
            if machine.capacity * machine.efficiency > 0:
                utilization = (machine.current_load / (machine.capacity * machine.efficiency)) * 100
            else:
                utilization = 0.0
            report[machine.machine_id] = round(utilization, 2)
        return report

# Example usage
if __name__ == "__main__":
    # Create machines
    machines = [
        Machine("FM-001", MachineType.FOAM_MELT, 10.0, 0.9),
        Machine("FM-002", MachineType.FOAM_MELT, 8.0, 0.85),
        Machine("SF-001", MachineType.SURE_FOAM, 12.0, 0.95),
        Machine("SF-002", MachineType.SURE_FOAM, 15.0, 0.92)
    ]

    optimizer = FoamDispensingOptimizer(machines)

    try:
        # Optimize for required output
        required_output = 30.0
        assignments = optimizer.optimize_dispensing(required_output)
        
        print(f"Optimized assignments for {required_output} kg:")
        for machine_id, load in assignments.items():
            print(f"{machine_id}: {load} kg")
        
        # Generate utilization report
        print("\nMachine utilization:")
        utilization = optimizer.get_utilization_report()
        for machine_id, percent in utilization.items():
            print(f"{machine_id}: {percent}%")
    
    except ValueError as e:
        print(f"Error: {e}")
```
