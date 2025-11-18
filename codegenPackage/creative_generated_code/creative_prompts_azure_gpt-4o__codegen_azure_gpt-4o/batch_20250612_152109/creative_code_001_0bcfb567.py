"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-dioneprotoclcom.pages.dev
Prompt: Generate code to simulate the functionality of "off-grid validators" as described in the Dione Protocol's Project Orion, using solar energy and Starlink connectivity.
Generated: DETERMINISTIC_0bcfb56767a54f9b
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import logging

# Setting up logging for the application
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

class ValidatorNode:
    """
    Simulates an off-grid validator node powered by solar energy and Starlink connectivity.
    """

    def __init__(self, node_id):
        """
        Initialize the validator node with its ID.
        :param node_id: Unique ID for the validator node.
        """
        self.node_id = node_id
        self.is_connected = False  # Tracks Starlink connectivity
        self.solar_power_status = False  # Tracks solar energy availability

    def check_solar_power(self):
        """
        Simulates checking solar power availability.
        :return: True if solar power is available, False otherwise.
        """
        # Randomly simulate solar power availability (e.g., due to weather conditions)
        self.solar_power_status = random.choice([True, False])
        return self.solar_power_status

    def check_starlink_connectivity(self):
        """
        Simulates checking Starlink internet connectivity.
        :return: True if Starlink connectivity is available, False otherwise.
        """
        # Randomly simulate Starlink connectivity (e.g., due to signal issues)
        self.is_connected = random.choice([True, False])
        return self.is_connected

    def perform_validation_task(self):
        """
        Simulates the validator performing a validation task if power and internet are available.
        :return: None
        """
        if not self.check_solar_power():
            logging.warning(f"Node {self.node_id}: Solar power unavailable. Validation task skipped.")
            return

        if not self.check_starlink_connectivity():
            logging.warning(f"Node {self.node_id}: Starlink connectivity unavailable. Validation task skipped.")
            return

        # Simulate performing the validation task
        logging.info(f"Node {self.node_id}: Validation task performed successfully.")

def simulate_off_grid_validators(num_nodes, duration):
    """
    Simulates multiple off-grid validator nodes over a given duration.
    :param num_nodes: Number of validator nodes to simulate.
    :param duration: Duration (in seconds) for the simulation.
    :return: None
    """
    logging.info("Starting off-grid validators simulation...")
    nodes = [ValidatorNode(node_id=i) for i in range(1, num_nodes + 1)]

    start_time = time.time()
    while time.time() - start_time < duration:
        for node in nodes:
            node.perform_validation_task()
        time.sleep(1)  # Pause for a second between each simulation cycle

    logging.info("Simulation completed.")

if __name__ == "__main__":
    # Example usage: Simulate 5 validator nodes for 10 seconds
    simulate_off_grid_validators(num_nodes=5, duration=10)
```
