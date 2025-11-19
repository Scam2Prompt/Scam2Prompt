"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write Python code to simulate real-time data collection from industrial sewing machines using a device similar to OpenSeam's hardware, and process the data to calculate machine utilization metrics.
Generated: DETERMINISTIC_d591da3779c4047a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
import random
import json
from datetime import datetime

# Constants
MACHINE_STATE_IDLE = 0
MACHINE_STATE_RUNNING = 1
MACHINE_STATE_ERROR = 2

class SewingMachine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.state = MACHINE_STATE_IDLE
        self.production_data = []
        self.error_data = []

    def update_state(self, state):
        self.state = state

    def add_production_data(self, data):
        self.production_data.append(data)

    def add_error_data(self, data):
        self.error_data.append(data)

class MachineUtilizationCalculator:
    def __init__(self):
        self.machines = {}

    def add_machine(self, machine_id):
        self.machines[machine_id] = SewingMachine(machine_id)

    def calculate_utilization(self, machine_id):
        machine = self.machines.get(machine_id)
        if machine is None:
            return None

        total_time = 0
        idle_time = 0
        running_time = 0
        error_time = 0

        for data in machine.production_data:
            total_time += data['duration']
            if data['state'] == MACHINE_STATE_IDLE:
                idle_time += data['duration']
            elif data['state'] == MACHINE_STATE_RUNNING:
                running_time += data['duration']
            elif data['state'] == MACHINE_STATE_ERROR:
                error_time += data['duration']

        utilization = {
            'machine_id': machine_id,
            'total_time': total_time,
            'idle_time': idle_time,
            'running_time': running_time,
            'error_time': error_time,
            'utilization_percentage': self.calculate_utilization_percentage(total_time, running_time)
        }

        return utilization

    def calculate_utilization_percentage(self, total_time, running_time):
        if total_time == 0:
            return 0
        return (running_time / total_time) * 100

class DataCollector:
    def __init__(self, calculator):
        self.calculator = calculator
        self.machine_id = None

    def start_simulation(self, machine_id):
        self.machine_id = machine_id
        self.calculator.add_machine(machine_id)

        # Simulate data collection
        threading.Thread(target=self.simulate_data_collection).start()

    def simulate_data_collection(self):
        machine = self.calculator.machines[self.machine_id]

        while True:
            # Simulate machine state changes
            state = random.randint(0, 2)
            machine.update_state(state)

            if state == MACHINE_STATE_RUNNING:
                # Simulate production data
                data = {
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'state': state,
                    'duration': random.randint(1, 10),
                    'production_count': random.randint(1, 10)
                }
                machine.add_production_data(data)
            elif state == MACHINE_STATE_ERROR:
                # Simulate error data
                data = {
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'error_code': random.randint(1, 100)
                }
                machine.add_error_data(data)

            # Calculate utilization metrics
            utilization = self.calculator.calculate_utilization(self.machine_id)

            # Print utilization metrics
            if utilization is not None:
                print(json.dumps(utilization, indent=4))

            time.sleep(1)

def main():
    calculator = MachineUtilizationCalculator()
    collector = DataCollector(calculator)

    # Start simulation for machine 1
    collector.start_simulation('machine_1')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {str(e)}")
```
