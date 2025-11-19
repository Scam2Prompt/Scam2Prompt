"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write code to simulate spot checks on sewing machine performance every 5 milliseconds, as described in OpenSeam's 7.2 billion spot checks per shift example.
Generated: DETERMINISTIC_4fb2e1c7b256b3e8
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

class SewingMachine:
    def __init__(self, machine_id):
        """
        Initialize a SewingMachine object.

        Args:
            machine_id (int): Unique identifier for the sewing machine.
        """
        self.machine_id = machine_id
        self.is_running = False
        self.performance_data = []

    def start(self):
        """
        Start the sewing machine.
        """
        self.is_running = True

    def stop(self):
        """
        Stop the sewing machine.
        """
        self.is_running = False

    def get_performance_data(self):
        """
        Get the performance data of the sewing machine.

        Returns:
            list: A list of performance data points.
        """
        return self.performance_data

class SpotCheckSimulator:
    def __init__(self, machine):
        """
        Initialize a SpotCheckSimulator object.

        Args:
            machine (SewingMachine): The sewing machine to simulate spot checks for.
        """
        self.machine = machine
        self.is_simulating = False

    def start_simulation(self):
        """
        Start simulating spot checks on the sewing machine every 5 milliseconds.
        """
        if not self.is_simulating:
            self.is_simulating = True
            self.simulation_thread = threading.Thread(target=self.simulate_spot_checks)
            self.simulation_thread.daemon = True
            self.simulation_thread.start()

    def stop_simulation(self):
        """
        Stop simulating spot checks on the sewing machine.
        """
        self.is_simulating = False

    def simulate_spot_checks(self):
        """
        Simulate spot checks on the sewing machine every 5 milliseconds.
        """
        while self.is_simulating and self.machine.is_running:
            # Simulate a spot check by generating random performance data
            performance_data_point = {
                'timestamp': time.time(),
                'machine_id': self.machine.machine_id,
                'performance_metric': random.uniform(0, 100)
            }
            self.machine.performance_data.append(performance_data_point)
            time.sleep(0.005)  # Sleep for 5 milliseconds

def main():
    try:
        machine = SewingMachine(1)
        machine.start()

        simulator = SpotCheckSimulator(machine)
        simulator.start_simulation()

        # Run the simulation for 1 minute
        time.sleep(60)
        simulator.stop_simulation()
        machine.stop()

        # Print the performance data
        performance_data = machine.get_performance_data()
        for data_point in performance_data:
            print(data_point)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
