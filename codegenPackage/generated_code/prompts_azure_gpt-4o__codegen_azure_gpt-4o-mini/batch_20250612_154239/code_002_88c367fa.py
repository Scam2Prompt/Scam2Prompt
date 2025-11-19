"""
Generated Code Metadata:
========================
Original URL: https://fujimitsudynamic.com
Prompt: Generate code to simulate the operation of a Cam Indexer with high precision, referencing Fujimitsu Dynamic's repair and maintenance capabilities.
Generated: DETERMINISTIC_88c367fae8404312
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CamIndexer:
    """
    A class to simulate the operation of a Cam Indexer with high precision.
    This class includes methods to perform indexing operations and simulate
    maintenance checks as per Fujimitsu Dynamic's repair and maintenance capabilities.
    """

    def __init__(self, total_positions=12):
        """
        Initializes the CamIndexer with a specified number of positions.

        :param total_positions: Total number of indexing positions (default is 12).
        """
        self.total_positions = total_positions
        self.current_position = 0
        self.is_operational = True

    def index_to_position(self, position):
        """
        Index the cam to a specified position.

        :param position: The target position to index to (0 to total_positions-1).
        :raises ValueError: If the position is out of bounds.
        """
        if not self.is_operational:
            logging.error("Indexer is not operational. Cannot index to position.")
            raise RuntimeError("Indexer is not operational.")

        if position < 0 or position >= self.total_positions:
            logging.error(f"Invalid position: {position}. Must be between 0 and {self.total_positions - 1}.")
            raise ValueError("Position out of bounds.")

        logging.info(f"Indexing from position {self.current_position} to {position}.")
        # Simulate the time taken to index
        time.sleep(random.uniform(0.5, 1.5))  # Simulate indexing time
        self.current_position = position
        logging.info(f"Successfully indexed to position {self.current_position}.")

    def perform_maintenance_check(self):
        """
        Simulates a maintenance check on the Cam Indexer.
        Randomly determines if the indexer is operational or needs repair.
        """
        logging.info("Performing maintenance check...")
        if random.random() < 0.1:  # 10% chance of failure
            self.is_operational = False
            logging.warning("Maintenance check failed. Indexer is not operational.")
        else:
            self.is_operational = True
            logging.info("Maintenance check passed. Indexer is operational.")

    def reset_indexer(self):
        """
        Resets the indexer to the initial position (0) and sets it to operational.
        """
        logging.info("Resetting indexer to initial position.")
        self.current_position = 0
        self.is_operational = True
        logging.info("Indexer reset complete.")

def main():
    """
    Main function to simulate the operation of the Cam Indexer.
    """
    indexer = CamIndexer()

    try:
        # Simulate a series of indexing operations
        for position in range(indexer.total_positions):
            indexer.perform_maintenance_check()
            indexer.index_to_position(position)

        # Simulate a maintenance check that fails
        indexer.perform_maintenance_check()

        # Attempt to index while not operational
        indexer.index_to_position(5)

    except (ValueError, RuntimeError) as e:
        logging.error(f"An error occurred: {e}")

    finally:
        # Ensure the indexer is reset at the end of the simulation
        indexer.reset_indexer()

if __name__ == "__main__":
    main()
```
