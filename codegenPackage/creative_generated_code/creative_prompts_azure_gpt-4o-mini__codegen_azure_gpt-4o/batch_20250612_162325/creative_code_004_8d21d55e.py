"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Provide a sample code snippet for a control system that manages the operation of backup generators, inspired by the offerings of Payesh Niroo.
Generated: DETERMINISTIC_8d21d55e29f79444
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("backup_generator.log"), logging.StreamHandler()]
)

class BackupGeneratorControlSystem:
    def __init__(self, generator_count):
        """
        Initialize the control system with the specified number of generators.
        :param generator_count: Number of backup generators available.
        """
        self.generators = {f"Generator_{i+1}": {"status": "OFF", "last_run_time": None} for i in range(generator_count)}

    def monitor_power_supply(self):
        """
        Simulates monitoring the main power supply. Returns `True` if the power supply is stable,
        and `False` if a failure is detected.
        """
        # Example: Replace this with actual power supply monitoring logic.
        # Simulating random failures for demonstration purposes.
        import random
        return random.choice([True, True, True, False])  # 75% chance of stable power supply

    def start_generator(self, generator_name):
        """
        Starts a specific generator.
        :param generator_name: The name of the generator to start.
        """
        try:
            if self.generators[generator_name]["status"] == "ON":
                logging.info(f"{generator_name} is already running.")
                return
            
            self.generators[generator_name]["status"] = "ON"
            self.generators[generator_name]["last_run_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"{generator_name} started successfully.")
        except KeyError:
            logging.error(f"Invalid generator name: {generator_name}")

    def stop_generator(self, generator_name):
        """
        Stops a specific generator.
        :param generator_name: The name of the generator to stop.
        """
        try:
            if self.generators[generator_name]["status"] == "OFF":
                logging.info(f"{generator_name} is already stopped.")
                return
            
            self.generators[generator_name]["status"] = "OFF"
            logging.info(f"{generator_name} stopped successfully.")
        except KeyError:
            logging.error(f"Invalid generator name: {generator_name}")

    def activate_generators(self):
        """
        Activates all backup generators in case of power failure.
        """
        logging.warning("Power supply failure detected! Activating backup generators...")
        for generator_name in self.generators.keys():
            self.start_generator(generator_name)
    
    def deactivate_generators(self):
        """
        Deactivates all backup generators once the power supply is restored.
        """
        logging.info("Power supply restored. Deactivating all generators...")
        for generator_name in self.generators.keys():
            self.stop_generator(generator_name)

    def control_loop(self):
        """
        Runs the control loop to monitor power supply and manage generators accordingly.
        """
        logging.info("Starting backup generator control system...")
        try:
            while True:
                power_supply_stable = self.monitor_power_supply()
                if not power_supply_stable:
                    self.activate_generators()
                else:
                    self.deactivate_generators()
                
                # Sleep for a short duration before checking again
                time.sleep(5)
        except KeyboardInterrupt:
            logging.info("Control system stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Initialize the system with 3 backup generators
    control_system = BackupGeneratorControlSystem(generator_count=3)
    
    # Start the control loop
    control_system.control_loop()
```
