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
"""
Business Process Optimization Simulation using SimPy.

This script simulates a business process with multiple stages (e.g., order processing)
to identify bottlenecks and optimize resource allocation.
"""

import simpy
import random
from collections import defaultdict

# Configuration parameters
SIMULATION_TIME = 480  # Minutes in a work day
NUM_CUSTOMERS = 100    # Number of customers to process
PROCESSING_TIMES = {
    'order_receipt': (2, 5),    # Min, max time in minutes
    'payment_processing': (1, 3),
    'inventory_check': (3, 7),
    'shipping': (5, 10)
}
RESOURCES = {
    'order_clerk': 2,
    'payment_processor': 3,
    'inventory_staff': 2,
    'shipping_staff': 4
}

class BusinessProcessSimulation:
    """Simulate a business process workflow."""
    
    def __init__(self, env):
        """Initialize simulation environment and resources."""
        self.env = env
        self.resources = {
            'order_clerk': simpy.Resource(env, capacity=RESOURCES['order_clerk']),
            'payment_processor': simpy.Resource(env, capacity=RESOURCES['payment_processor']),
            'inventory_staff': simpy.Resource(env, capacity=RESOURCES['inventory_staff']),
            'shipping_staff': simpy.Resource(env, capacity=RESOURCES['shipping_staff'])
        }
        self.metrics = defaultdict(list)
    
    def process_order(self, customer_id):
        """Simulate the complete order processing workflow."""
        start_time = self.env.now
        
        # Stage 1: Order Receipt
        with self.resources['order_clerk'].request() as request:
            yield request
            processing_time = random.uniform(*PROCESSING_TIMES['order_receipt'])
            yield self.env.timeout(processing_time)
            self.metrics['order_receipt'].append(processing_time)
        
        # Stage 2: Payment Processing
        with self.resources['payment_processor'].request() as request:
            yield request
            processing_time = random.uniform(*PROCESSING_TIMES['payment_processing'])
            yield self.env.timeout(processing_time)
            self.metrics['payment_processing'].append(processing_time)
        
        # Stage 3: Inventory Check
        with self.resources['inventory_staff'].request() as request:
            yield request
            processing_time = random.uniform(*PROCESSING_TIMES['inventory_check'])
            yield self.env.timeout(processing_time)
            self.metrics['inventory_check'].append(processing_time)
        
        # Stage 4: Shipping
        with self.resources['shipping_staff'].request() as request:
            yield request
            processing_time = random.uniform(*PROCESSING_TIMES['shipping'])
            yield self.env.timeout(processing_time)
            self.metrics['shipping'].append(processing_time)
        
        total_time = self.env.now - start_time
        self.metrics['total_processing'].append(total_time)
        print(f"Customer {customer_id} order completed in {total_time:.2f} minutes")

def customer_generator(env, simulation):
    """Generate customer orders for processing."""
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        env.process(simulation.process_order(customer_id))
        # Random arrival time between customers
        yield env.timeout(random.expovariate(1.0))

def run_simulation():
    """Run the simulation and print results."""
    env = simpy.Environment()
    simulation = BusinessProcessSimulation(env)
    env.process(customer_generator(env, simulation))
    env.run(until=SIMULATION_TIME)
    
    # Print summary statistics
    print("\nSimulation Results:")
    print(f"Total customers processed: {len(simulation.metrics['total_processing'])}")
    print(f"Simulation time: {SIMULATION_TIME} minutes")
    
    print("\nAverage processing times per stage:")
    for stage, times in simulation.metrics.items():
        if stage != 'total_processing':
            avg_time = sum(times) / len(times) if times else 0
            print(f"{stage.replace('_', ' ').title()}: {avg_time:.2f} minutes")
    
    avg_total = sum(simulation.metrics['total_processing']) / len(simulation.metrics['total_processing'])
    print(f"\nAverage total processing time: {avg_total:.2f} minutes")

if __name__ == "__main__":
    run_simulation()
```
