"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Write code to automate the process of tube removal using a hydraulic tube pulling system, referencing the Continuous Tube Puller and Master Tugger tools described on the DBX Tools website.
Generated: DETERMINISTIC_2ab118e5e1216589
Batch ID: 20250612_154302
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HydraulicTubePuller:
    def __init__(self, max_pressure: int, pull_speed: int):
        """
        Initialize the HydraulicTubePuller with specified parameters.

        :param max_pressure: Maximum pressure (in psi) for the hydraulic system.
        :param pull_speed: Speed of tube pulling (in inches per second).
        """
        self.max_pressure = max_pressure
        self.pull_speed = pull_speed
        self.is_active = False

    def activate_system(self):
        """
        Activates the hydraulic system for tube removal.
        """
        logging.info("Activating hydraulic tube pulling system.")
        self.is_active = True

    def deactivate_system(self):
        """
        Deactivates the hydraulic system.
        """
        logging.info("Deactivating hydraulic tube pulling system.")
        self.is_active = False

    def pull_tube(self, tube_length: int):
        """
        Pulls the tube using the hydraulic system.

        :param tube_length: Length of the tube to be removed (in inches).
        :raises RuntimeError: If the system is not active or if unsafe conditions are detected.
        """
        if not self.is_active:
            logging.error("Cannot pull tube: Hydraulic system is not activated.")
            raise RuntimeError("Hydraulic system is not activated.")

        if tube_length <= 0:
            logging.error("Invalid tube length: Must be greater than zero.")
            raise ValueError("Tube length must be greater than zero.")

        logging.info(f"Starting to pull a tube of length {tube_length} inches at speed {self.pull_speed} IPS.")
        
        # Simulate the tube pulling process
        for length in range(0, tube_length, self.pull_speed):
            logging.info(f"Pulling tube: {min(length + self.pull_speed, tube_length)} / {tube_length} inches pulled.")
            time.sleep(1)  # Simulating time taken to pull the tube

        logging.info("Tube removal completed.")

def main():
    try:
        # Instantiate the hydraulic tube puller with specific parameters
        tube_puller = HydraulicTubePuller(max_pressure=3000, pull_speed=2)

        # Activate the hydraulic system
        tube_puller.activate_system()

        # Pull the tube of specified length
        tube_length = 10  # Length in inches
        tube_puller.pull_tube(tube_length)

    except ValueError as ve:
        logging.error(f"Value error encountered: {ve}")
    except RuntimeError as re:
        logging.error(f"Runtime error encountered: {re}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        # Ensure that the system is deactivated at the end of the process
        tube_puller.deactivate_system()

if __name__ == "__main__":
    main()
```
