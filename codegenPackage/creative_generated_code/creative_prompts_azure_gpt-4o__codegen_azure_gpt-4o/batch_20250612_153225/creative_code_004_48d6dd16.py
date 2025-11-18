"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Provide code examples for tracking and logging generator usage data, focusing on the types of generators listed on Birlik Jeneratör's website (diesel, portable diesel, and portable gasoline).
Generated: DETERMINISTIC_48d6dd16d2c263a1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='generator_usage.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define a base class for generators
class Generator:
    def __init__(self, generator_type: str, model: str):
        """
        Initialize a generator object.

        :param generator_type: Type of the generator (e.g., diesel, portable diesel, portable gasoline)
        :param model: Specific model of the generator
        """
        self.generator_type = generator_type
        self.model = model
        self.running = False
        self.start_time = None
        self.total_runtime = 0  # Total time in seconds

    def start(self):
        """
        Start the generator. Logs the start action and records the start time.
        """
        if self.running:
            logging.warning(f"Generator '{self.model}' is already running.")
            return

        self.running = True
        self.start_time = datetime.now()
        logging.info(f"Generator '{self.model}' of type '{self.generator_type}' started.")

    def stop(self):
        """
        Stop the generator. Logs the stop action and updates the total runtime.
        """
        if not self.running:
            logging.warning(f"Generator '{self.model}' is not running.")
            return

        stop_time = datetime.now()
        runtime = (stop_time - self.start_time).total_seconds()
        self.total_runtime += runtime
        self.running = False
        self.start_time = None
        logging.info(
            f"Generator '{self.model}' of type '{self.generator_type}' stopped. "
            f"Runtime this session: {runtime:.2f} seconds. Total runtime: {self.total_runtime:.2f} seconds."
        )

    def get_usage_data(self):
        """
        Retrieve generator usage data.

        :return: A dictionary containing generator usage data.
        """
        return {
            "generator_type": self.generator_type,
            "model": self.model,
            "running": self.running,
            "total_runtime_seconds": self.total_runtime
        }


# Example usage: Tracking and logging generator usage
if __name__ == "__main__":
    try:
        # Create generator instances
        diesel_generator = Generator(generator_type="Diesel", model="DG-1000")
        portable_diesel_generator = Generator(generator_type="Portable Diesel", model="PD-500")
        portable_gasoline_generator = Generator(generator_type="Portable Gasoline", model="PG-200")

        # Start generators
        diesel_generator.start()
        portable_diesel_generator.start()

        # Simulate runtime with sleep (for demonstration purposes)
        import time
        time.sleep(2)  # Simulate 2 seconds of runtime

        # Stop generators
        diesel_generator.stop()
        portable_diesel_generator.stop()

        # Log usage data
        logging.info(f"Usage data for diesel generator: {diesel_generator.get_usage_data()}")
        logging.info(f"Usage data for portable diesel generator: {portable_diesel_generator.get_usage_data()}")
        logging.info(f"Usage data for portable gasoline generator: {portable_gasoline_generator.get_usage_data()}")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
```
