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
from typing import Dict
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class PipelineSupply:
    """Class to represent pipeline supply"""
    volume: float  # in barrels
    arrival_time: datetime

class OilRefinery:
    """Class to simulate oil refinery supply chain logistics"""
    def __init__(self, capacity: float, pipeline_supply_interval: timedelta):
        """
        Initialize oil refinery with capacity and pipeline supply interval.

        Args:
        - capacity (float): The maximum capacity of the refinery in barrels.
        - pipeline_supply_interval (timedelta): The interval between pipeline supplies.
        """
        self.capacity = capacity
        self.pipeline_supply_interval = pipeline_supply_interval
        self.current_stock = 0.0  # in barrels
        self.supply_schedule: Dict[datetime, PipelineSupply] = {}

    def schedule_pipeline_supply(self, supply: PipelineSupply):
        """
        Schedule a pipeline supply.

        Args:
        - supply (PipelineSupply): The pipeline supply to schedule.
        """
        self.supply_schedule[supply.arrival_time] = supply

    def simulate_supply_chain(self, start_time: datetime, end_time: datetime):
        """
        Simulate the supply chain logistics.

        Args:
        - start_time (datetime): The start time of the simulation.
        - end_time (datetime): The end time of the simulation.
        """
        current_time = start_time
        while current_time <= end_time:
            if current_time in self.supply_schedule:
                supply = self.supply_schedule[current_time]
                self.receive_pipeline_supply(supply)
            current_time += self.pipeline_supply_interval

    def receive_pipeline_supply(self, supply: PipelineSupply):
        """
        Receive a pipeline supply.

        Args:
        - supply (PipelineSupply): The pipeline supply to receive.
        """
        available_space = self.capacity - self.current_stock
        if available_space >= supply.volume:
            self.current_stock += supply.volume
            print(f"Received {supply.volume} barrels at {supply.arrival_time}. Current stock: {self.current_stock} barrels")
        else:
            print(f"Insufficient space to receive {supply.volume} barrels at {supply.arrival_time}. Current stock: {self.current_stock} barrels")

def main():
    # Create an oil refinery with a capacity of 10000 barrels and a pipeline supply interval of 1 day
    refinery = OilRefinery(10000, timedelta(days=1))

    # Schedule pipeline supplies
    supply1 = PipelineSupply(2000, datetime(2024, 9, 16))
    supply2 = PipelineSupply(3000, datetime(2024, 9, 17))
    supply3 = PipelineSupply(4000, datetime(2024, 9, 18))
    refinery.schedule_pipeline_supply(supply1)
    refinery.schedule_pipeline_supply(supply2)
    refinery.schedule_pipeline_supply(supply3)

    # Simulate the supply chain logistics
    start_time = datetime(2024, 9, 16)
    end_time = datetime(2024, 9, 20)
    refinery.simulate_supply_chain(start_time, end_time)

if __name__ == "__main__":
    main()
```
