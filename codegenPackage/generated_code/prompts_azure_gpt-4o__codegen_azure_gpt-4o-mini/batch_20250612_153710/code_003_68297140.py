"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Provide Python code to simulate business process optimization scenarios using a library like SimPy or similar tools.
Generated: DETERMINISTIC_682971408e5e1b6a
Batch ID: 20250612_153710
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

class BusinessProcess:
    """A class to simulate a business process using SimPy."""
    
    def __init__(self, env, name, process_time, arrival_rate):
        """
        Initialize the business process.

        Parameters:
        env (simpy.Environment): The simulation environment.
        name (str): The name of the business process.
        process_time (float): The average time taken to complete the process.
        arrival_rate (float): The average rate of arrival of tasks.
        """
        self.env = env
        self.name = name
        self.process_time = process_time
        self.arrival_rate = arrival_rate
        self.action = env.process(self.run())

    def run(self):
        """Run the business process simulation."""
        while True:
            # Wait for the next task to arrive
            yield self.env.timeout(random.expovariate(1.0 / self.arrival_rate))
            print(f'{self.name} received a task at {self.env.now:.2f}')
            yield self.env.process(self.process_task())

    def process_task(self):
        """Process a single task."""
        processing_time = random.expovariate(1.0 / self.process_time)
        print(f'{self.name} started processing a task at {self.env.now:.2f}')
        yield self.env.timeout(processing_time)
        print(f'{self.name} finished processing a task at {self.env.now:.2f}')


def run_simulation(processes, simulation_time):
    """Run the business process simulation.

    Parameters:
    processes (list): A list of BusinessProcess instances.
    simulation_time (int): The total time to run the simulation.
    """
    # Create a SimPy environment
    env = simpy.Environment()

    # Initialize business processes
    for process in processes:
        BusinessProcess(env, **process)

    # Run the simulation
    env.run(until=simulation_time)


if __name__ == "__main__":
    # Define business processes with their parameters
    processes = [
        {'name': 'Process A', 'process_time': 5, 'arrival_rate': 2},
        {'name': 'Process B', 'process_time': 3, 'arrival_rate': 1.5},
        {'name': 'Process C', 'process_time': 4, 'arrival_rate': 1},
    ]

    # Set the total simulation time
    simulation_time = 30

    try:
        # Run the simulation
        run_simulation(processes, simulation_time)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
