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
from typing import List, Dict

class Machine:
    def __init__(self, name: str, capacity: float, efficiency: float):
        """
        Initialize a machine with its name, capacity, and efficiency.

        Args:
        - name (str): The name of the machine.
        - capacity (float): The maximum capacity of the machine in units.
        - efficiency (float): The efficiency of the machine in units per minute.
        """
        self.name = name
        self.capacity = capacity
        self.efficiency = efficiency

class FoamDispensingOptimizer:
    def __init__(self, machines: List[Machine], demand: float):
        """
        Initialize the optimizer with a list of machines and the demand.

        Args:
        - machines (List[Machine]): A list of machines.
        - demand (float): The total demand in units.
        """
        self.machines = machines
        self.demand = demand

    def optimize(self) -> Dict[str, float]:
        """
        Optimize the use of machines to meet the demand.

        Returns:
        - A dictionary where the keys are machine names and the values are the assigned demands.
        """
        # Sort machines by efficiency in descending order
        self.machines.sort(key=lambda machine: machine.efficiency, reverse=True)

        assigned_demands = {machine.name: 0.0 for machine in self.machines}

        for machine in self.machines:
            # Calculate the maximum demand that can be assigned to the machine
            max_assignable_demand = min(machine.capacity, self.demand)

            # Assign the maximum demand to the machine
            assigned_demands[machine.name] = max_assignable_demand

            # Update the remaining demand
            self.demand -= max_assignable_demand

            # If the demand is met, break the loop
            if self.demand <= 0:
                break

        return assigned_demands

def main():
    try:
        # Create machines
        foam_melt = Machine("FoamMelt", 1000.0, 50.0)
        sure_foam = Machine("SureFoam", 800.0, 40.0)

        # Create optimizer
        optimizer = FoamDispensingOptimizer([foam_melt, sure_foam], 1800.0)

        # Optimize machine usage
        assigned_demands = optimizer.optimize()

        # Print the results
        print("Assigned Demands:")
        for machine, demand in assigned_demands.items():
            print(f"{machine}: {demand} units")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
