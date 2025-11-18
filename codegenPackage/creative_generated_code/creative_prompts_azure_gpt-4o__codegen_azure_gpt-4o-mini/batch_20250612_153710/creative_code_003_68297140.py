"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Provide Python code to simulate business process optimization scenarios using a library like SimPy or similar tools.
Generated: DETERMINISTIC_682971408e5e1b6a
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import simpy
import random

class BusinessProcess:
    """A class to simulate a simple business process using SimPy."""
    
    def __init__(self, env, name):
        """Initialize the business process with an environment and name.
        
        Args:
            env (simpy.Environment): The SimPy environment for simulation.
            name (str): The name of the business process.
        """
        self.env = env
        self.name = name
        self.process = env.process(self.run())
    
    def run(self):
        """Simulate the execution of the business process."""
        while True:
            # Simulate a process task
            task_duration = random.uniform(1, 5)  # Duration between 1 and 5 time units
            yield self.env.timeout(task_duration)  # Wait for the task to complete
            
            # Log the completion of a task
            print(f'{self.name} completed a task at {self.env.now:.2f}')
            
            # Simulate a decision-making process
            decision_time = random.uniform(0.5, 2)  # Decision time between 0.5 and 2 time units
            yield self.env.timeout(decision_time)  # Wait for the decision process
            
            # Log the decision made
            print(f'{self.name} made a decision at {self.env.now:.2f}')

def run_simulation():
    """Run the business process optimization simulation."""
    # Create a SimPy environment
    env = simpy.Environment()
    
    # Create multiple business processes
    process_count = 3
    processes = [BusinessProcess(env, f'Process {i + 1}') for i in range(process_count)]
    
    # Run the simulation for a defined duration
    simulation_duration = 20  # Run for 20 time units
    env.run(until=simulation_duration)
    print("Simulation completed.")

if __name__ == '__main__':
    try:
        run_simulation()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
