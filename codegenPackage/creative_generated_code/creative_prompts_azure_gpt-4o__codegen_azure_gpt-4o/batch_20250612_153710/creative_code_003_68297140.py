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
"""
Business Process Optimization Simulation using SimPy.

This script simulates a simple business process workflow where customers arrive,
are served by a resource (e.g., staff), and depart. Metrics such as wait time and
system utilization are tracked to optimize the process.
"""

import simpy
import random

# Constants
RANDOM_SEED = 42        # Seed for reproducibility
SIMULATION_TIME = 100   # Total simulation time in minutes
INTER_ARRIVAL_TIME = 5  # Average time between arrivals (minutes)
SERVICE_TIME = 3        # Average service time per customer (minutes)
NUM_RESOURCES = 2       # Number of available resources (e.g., staff)

def customer(env, name, resource):
    """
    Customer process: Represents a customer arriving, waiting,
    receiving service, and departing.
    
    :param env: SimPy environment
    :param name: Name of the customer
    :param resource: SimPy Resource representing staff or equipment
    """
    arrival_time = env.now
    print(f"{name} arrives at {arrival_time:.2f}")

    # Request a resource (e.g., staff)
    with resource.request() as req:
        yield req  # Wait for resource to become available
        wait_time = env.now - arrival_time
        print(f"{name} starts service at {env.now:.2f} after waiting {wait_time:.2f}")

        # Service time
        service_duration = random.expovariate(1.0 / SERVICE_TIME)
        yield env.timeout(service_duration)
        print(f"{name} leaves at {env.now:.2f}")

def generate_customers(env, resource):
    """
    Generates customers at random intervals based on the inter-arrival time.

    :param env: SimPy environment
    :param resource: SimPy Resource representing staff or equipment
    """
    customer_count = 0
    while True:
        inter_arrival_duration = random.expovariate(1.0 / INTER_ARRIVAL_TIME)
        yield env.timeout(inter_arrival_duration)
        customer_count += 1
        env.process(customer(env, f"Customer{customer_count}", resource))

def main():
    """
    Sets up and runs the simulation of the business process optimization scenario.
    """
    print("Business Process Optimization Simulation")
    print("=" * 50)

    # Initialize random seed for reproducibility
    random.seed(RANDOM_SEED)

    # Create the SimPy environment
    env = simpy.Environment()

    # Create the resource (e.g., staff or equipment)
    resource = simpy.Resource(env, capacity=NUM_RESOURCES)

    # Start the customer generation process
    env.process(generate_customers(env, resource))

    # Run the simulation
    env.run(until=SIMULATION_TIME)

if __name__ == "__main__":
    main()
```
