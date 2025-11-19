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
import random
import time
from datetime import datetime, timedelta

class OilRefinery:
    def __init__(self, name, capacity):
        """
        Initialize the OilRefinery with a name and capacity.
        
        :param name: str - The name of the refinery
        :param capacity: float - The maximum capacity of the refinery in barrels
        """
        self.name = name
        self.capacity = capacity
        self.current_stock = 0
        self.supply_rate = 1000  # barrels per hour
        self.pipeline_supply_rate = 500  # barrels per hour to Vancouver

    def simulate_supply(self):
        """
        Simulate the supply of crude oil to the refinery.
        This method increases the current stock of oil in the refinery.
        """
        while True:
            if self.current_stock < self.capacity:
                supply_amount = min(self.supply_rate, self.capacity - self.current_stock)
                self.current_stock += supply_amount
                print(f"{datetime.now()}: Supplied {supply_amount} barrels to {self.name}. Current stock: {self.current_stock} barrels.")
            else:
                print(f"{datetime.now()}: {self.name} is at full capacity.")
            time.sleep(3600)  # Simulate hourly supply

    def send_to_pipeline(self):
        """
        Simulate sending oil to the pipeline for distribution to Vancouver.
        This method decreases the current stock of oil in the refinery.
        """
        while True:
            if self.current_stock >= self.pipeline_supply_rate:
                self.current_stock -= self.pipeline_supply_rate
                print(f"{datetime.now()}: Sent {self.pipeline_supply_rate} barrels to Vancouver. Current stock: {self.current_stock} barrels.")
            else:
                print(f"{datetime.now()}: Not enough stock to send to Vancouver. Current stock: {self.current_stock} barrels.")
            time.sleep(3600)  # Simulate hourly dispatch

    def run(self):
        """
        Start the supply and dispatch simulation in separate threads.
        """
        import threading

        supply_thread = threading.Thread(target=self.simulate_supply)
        pipeline_thread = threading.Thread(target=self.send_to_pipeline)

        supply_thread.start()
        pipeline_thread.start()

        supply_thread.join()
        pipeline_thread.join()

if __name__ == "__main__":
    try:
        refinery = OilRefinery(name="Vancouver Refinery", capacity=10000)
        refinery.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
