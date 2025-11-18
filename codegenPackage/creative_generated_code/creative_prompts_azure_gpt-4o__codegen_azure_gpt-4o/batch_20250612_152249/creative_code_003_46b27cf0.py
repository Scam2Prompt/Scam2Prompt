"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Create a program to simulate the emission calculations for $xRIZ based on node uptime, storage, and computational resource usage as described in the Rivalz infrastructure.
Generated: DETERMINISTIC_46b27cf034bf02cb
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import random
from datetime import datetime, timedelta

# Setup logging for monitoring and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class EmissionCalculator:
    """
    Class to calculate emissions for $xRIZ based on node uptime, storage, and computational resource usage.
    """

    def __init__(self, node_id, uptime_hours, storage_gb, compute_usage_units):
        """
        Initialize the parameters for a node.
        :param node_id: Unique identifier for the node.
        :param uptime_hours: Uptime in hours (float).
        :param storage_gb: Storage usage in GB (float).
        :param compute_usage_units: Computational resource usage in abstract units (float).
        """
        self.node_id = node_id
        self.uptime_hours = uptime_hours
        self.storage_gb = storage_gb
        self.compute_usage_units = compute_usage_units

    def calculate_emissions(self):
        """
        Calculates total emissions for the node.
        Formula:
        emissions = (uptime_hours * 0.1) + (storage_gb * 0.5) + (compute_usage_units * 1.2)
        :return: Total emissions in $xRIZ (float).
        """
        try:
            emissions = (
                (self.uptime_hours * 0.1) +
                (self.storage_gb * 0.5) +
                (self.compute_usage_units * 1.2)
            )
            return emissions
        except Exception as e:
            logging.error(f"Error calculating emissions for node {self.node_id}: {e}")
            raise

    def simulate_activity(self, hours, max_storage, max_compute_units):
        """
        Simulates node activity by generating random values for uptime, storage, and compute usage.
        :param hours: Number of hours to simulate activity for.
        :param max_storage: Maximum storage in GB (float) the node can use.
        :param max_compute_units: Maximum compute units the node can utilize.
        :return: Updated node activity.
        """
        try:
            self.uptime_hours += hours
            self.storage_gb = random.uniform(0, max_storage)
            self.compute_usage_units = random.uniform(0, max_compute_units)
        except Exception as e:
            logging.error(f"Error simulating activity for node {self.node_id}: {e}")
            raise


# Utility Function
def generate_random_node_id():
    """
    Generates a random node ID (8 characters).
    :return: Random node ID (string).
    """
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))


def main():
    """
    Main function to simulate node emissions for Rivalz infrastructure.
    """
    try:
        # Simulate nodes
        nodes = []
        for _ in range(5):  # Simulate 5 nodes
            node_id = generate_random_node_id()
            uptime = random.uniform(0, 100)  # Random uptime between 0 and 100 hours
            storage = random.uniform(0, 500)  # Random storage between 0 and 500 GB
            compute = random.uniform(0, 200)  # Random compute usage between 0 and 200 units
            nodes.append(EmissionCalculator(node_id, uptime, storage, compute))

        # Output initial node data
        logging.info("Initial Node Data:")
        for node in nodes:
            logging.info(f"Node ID: {node.node_id}, "
                         f"Uptime: {node.uptime_hours:.2f} hours, "
                         f"Storage: {node.storage_gb:.2f} GB, "
                         f"Compute: {node.compute_usage_units:.2f} units")

        # Simulate activity for each node
        for node in nodes:
            node.simulate_activity(hours=random.uniform(0, 24), max_storage=500, max_compute_units=200)

        # Calculate and output emissions
        logging.info("\nNode Emission Calculations:")
        for node in nodes:
            emissions = node.calculate_emissions()
            logging.info(f"Node ID: {node.node_id}, Emissions: {emissions:.2f} $xRIZ")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
```
