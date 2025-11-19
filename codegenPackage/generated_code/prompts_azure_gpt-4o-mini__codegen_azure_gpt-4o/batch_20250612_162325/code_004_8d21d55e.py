"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Provide a sample code snippet for a control system that manages the operation of backup generators, inspired by the offerings of Payesh Niroo.
Generated: DETERMINISTIC_8d21d55e29f79444
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging

# Configure logging for the system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BackupGeneratorControlSystem:
    """
    A control system for managing the operation of backup generators.
    """

    def __init__(self, generators):
        """
        Initialize the control system with a list of generators.

        :param generators: List of generator names or IDs.
        """
        self.generators = {gen: False for gen in generators}  # False indicates the generator is off
        self.primary_power_status = True  # True indicates primary power is available

    def check_primary_power(self):
        """
        Simulate checking the status of the primary power supply.
        In a real-world scenario, this would interface with a power monitoring system.
        """
        # Simulated power check (this could be replaced with actual hardware monitoring code)
        return self.primary_power_status

    def start_generator(self, generator_id):
        """
        Start a specific backup generator.

        :param generator_id: The ID of the generator to start.
        """
        if generator_id in self.generators:
            if not self.generators[generator_id]:
                self.generators[generator_id] = True
                logging.info(f"Generator {generator_id} started successfully.")
            else:
                logging.warning(f"Generator {generator_id} is already running.")
        else:
            logging.error(f"Generator {generator_id} not found in the system.")

    def stop_generator(self, generator_id):
        """
        Stop a specific backup generator.

        :param generator_id: The ID of the generator to stop.
        """
        if generator_id in self.generators:
            if self.generators[generator_id]:
                self.generators[generator_id] = False
                logging.info(f"Generator {generator_id} stopped successfully.")
            else:
                logging.warning(f"Generator {generator_id} is already stopped.")
        else:
            logging.error(f"Generator {generator_id} not found in the system.")

    def manage_generators(self):
        """
        Main control loop to manage the operation of backup generators.
        """
        try:
            while True:
                primary_power = self.check_primary_power()

                if not primary_power:
                    logging.warning("Primary power is down. Activating backup generators...")
                    for generator_id in self.generators:
                        self.start_generator(generator_id)
                else:
                    logging.info("Primary power is stable. Shutting down backup generators...")
                    for generator_id in self.generators:
                        self.stop_generator(generator_id)

                # Wait for a short interval before checking again
                time.sleep(5)

        except KeyboardInterrupt:
            logging.info("Control system shutting down...")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the control system with a list of generator IDs
    generator_system = BackupGeneratorControlSystem(generators=["Gen1", "Gen2", "Gen3"])

    # Simulate a power outage after 10 seconds
    def simulate_power_outage():
        time.sleep(10)
        generator_system.primary_power_status = False

    # Run the power outage simulation in a separate thread
    import threading
    threading.Thread(target=simulate_power_outage, daemon=True).start()

    # Start the generator control system
    generator_system.manage_generators()
```
