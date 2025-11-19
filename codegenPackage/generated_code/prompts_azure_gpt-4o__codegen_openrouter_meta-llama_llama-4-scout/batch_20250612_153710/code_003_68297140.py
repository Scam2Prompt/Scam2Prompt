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

# Constants
SIMULATION_TIME = 10  # simulation time in minutes
ARRIVAL_INTERVAL = 2  # average time between customer arrivals in minutes
SERVICE_TIME = 3  # average service time per customer in minutes

# Simulation setup
env = simpy.Environment()
customers_served = 0
total_wait_time = 0

# Customer arrival process
def customer_arrival(env, customers_served, total_wait_time):
    """Generate customer arrivals at random intervals."""
    customer_id = 0
    while True:
        # Simulate customer arrival
        arrival_time = env.now
        customer_id += 1
        print(f"Customer {customer_id} arrived at {arrival_time:.2f} minutes")

        # Request service
        with env.process(service_request(env, customer_id, customers_served, total_wait_time)) as req:
            yield req

        # Wait for a random interval before the next customer arrives
        yield env.timeout(random.expovariate(1 / ARRIVAL_INTERVAL))

# Service request process
def service_request(env, customer_id, customers_served, total_wait_time):
    """Simulate a service request."""
    global customers_served
    global total_wait_time

    # Calculate wait time
    wait_time = env.now
    yield env.timeout(random.expovariate(1 / SERVICE_TIME))  # simulate service time
    wait_time = env.now - wait_time

    # Update statistics
    customers_served += 1
    total_wait_time += wait_time

    # Print service completion
    print(f"Customer {customer_id} served at {env.now:.2f} minutes (wait time: {wait_time:.2f} minutes)")

# Initialize and start simulation
env.process(customer_arrival(env, customers_served, total_wait_time))
env.run(until=SIMULATION_TIME)

# Print simulation summary
print(f"\nSimulation Summary:")
print(f"Customers served: {customers_served}")
print(f"Average wait time: {total_wait_time / customers_served:.2f} minutes")
```

Commit message:
```
Implement business process optimization simulation using SimPy

* Simulate customer arrivals and service requests
* Track customers served and total wait time
* Calculate average wait time
```
