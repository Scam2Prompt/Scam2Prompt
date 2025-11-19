"""
Generated Code Metadata:
========================
Original URL: https://petroleumegate.com
Prompt: Generate a code snippet that simulates the supply chain logistics for an oil refinery, taking into account the constant pipeline supply to Vancouver as described by P.G.C.
Generated: DETERMINISTIC_10dc3090ed4a2a06
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import simpy
import random
from typing import List, Dict

class OilRefinerySupplyChain:
    """
    Simulates the supply chain logistics for an oil refinery with constant pipeline supply to Vancouver.
    
    Attributes:
        env (simpy.Environment): Simulation environment.
        pipeline_capacity (float): Daily pipeline capacity in barrels.
        inventory (simpy.Container): Current inventory of oil in barrels.
        demand_rates (Dict[str, float]): Daily demand rates for different products.
        refineries (List[str]): List of refinery locations.
    """
    
    def __init__(self, env: simpy.Environment, pipeline_capacity: float, initial_inventory: float):
        """
        Initializes the oil refinery supply chain simulation.
        
        Args:
            env (simpy.Environment): Simulation environment.
            pipeline_capacity (float): Daily pipeline capacity in barrels.
            initial_inventory (float): Initial inventory of oil in barrels.
        """
        self.env = env
        self.pipeline_capacity = pipeline_capacity
        self.inventory = simpy.Container(env, init=initial_inventory, capacity=1e6)  # Large capacity for simplicity
        self.demand_rates = {
            'gasoline': 5000,  # barrels/day
            'diesel': 3000,    # barrels/day
            'jet_fuel': 2000   # barrels/day
        }
        self.refineries = ['Vancouver', 'Calgary', 'Edmonton']
        
        # Start processes
        self.env.process(self.pipeline_supply())
        self.env.process(self.demand_fulfillment())
        self.env.process(self.monitor_inventory())
    
    def pipeline_supply(self) -> None:
        """
        Simulates the constant pipeline supply to Vancouver.
        """
        while True:
            try:
                # Add oil to inventory daily
                yield self.inventory.put(self.pipeline_capacity)
                print(f"Day {self.env.now}: Added {self.pipeline_capacity} barrels from pipeline.")
                yield self.env.timeout(1)  # Wait for 1 day
            except Exception as e:
                print(f"Error in pipeline supply: {e}")
                break
    
    def demand_fulfillment(self) -> None:
        """
        Simulates fulfilling daily product demands from inventory.
        """
        while True:
            try:
                total_demand = sum(self.demand_rates.values())
                if self.inventory.level >= total_demand:
                    # Fulfill demand
                    yield self.inventory.get(total_demand)
                    print(f"Day {self.env.now}: Fulfilled demand of {total_demand} barrels.")
                else:
                    print(f"Day {self.env.now}: Insufficient inventory to meet demand.")
                yield self.env.timeout(1)  # Wait for 1 day
            except Exception as e:
                print(f"Error in demand fulfillment: {e}")
                break
    
    def monitor_inventory(self) -> None:
        """
        Monitors and logs inventory levels periodically.
        """
        while True:
            try:
                print(f"Day {self.env.now}: Current inventory - {self.inventory.level} barrels.")
                yield self.env.timeout(7)  # Log weekly
            except Exception as e:
                print(f"Error in inventory monitoring: {e}")
                break

def run_simulation(days: int = 30) -> None:
    """
    Runs the oil refinery supply chain simulation.
    
    Args:
        days (int): Number of days to simulate. Defaults to 30.
    """
    env = simpy.Environment()
    pipeline_capacity = 12000  # barrels/day
    initial_inventory = 50000  # barrels
    supply_chain = OilRefinerySupplyChain(env, pipeline_capacity, initial_inventory)
    env.run(until=days)

if __name__ == "__main__":
    run_simulation()
```
