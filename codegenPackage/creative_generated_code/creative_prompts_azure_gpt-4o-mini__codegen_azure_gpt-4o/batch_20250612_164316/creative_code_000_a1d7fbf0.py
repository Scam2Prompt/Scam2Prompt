"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nordson.vn
Prompt: Generate code to integrate the EasyOn glue gun with a temperature control system using the Nordson temperature controller.
Generated: DETERMINISTIC_a1d7fbf0e91c9a03
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Integration Code for EasyOn Glue Gun with Nordson Temperature Controller

This script interfaces with the EasyOn glue gun and the Nordson temperature controller
to maintain desired glue gun temperature. It uses a simulated hardware control library
for communication with the devices.

Dependencies:
- Python standard library
- Simulated `hardware_api` library (for demonstration purposes)

Author: Your Name
Date: YYYY-MM-DD
"""

import logging
from hardware_api import EasyOnGlueGun, NordsonTemperatureController, HardwareConnectionError

# Set up logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Target temperature for the glue gun in Celsius
TARGET_TEMPERATURE = 180  # Adjust as needed

def main():
    """
    Main function to initialize and manage the temperature control system.
    """
    try:
        # Initialize EasyOn glue gun interface
        logging.info("Initializing EasyOn glue gun...")
        glue_gun = EasyOnGlueGun()

        # Initialize Nordson temperature controller interface
        logging.info("Initializing Nordson temperature controller...")
        temp_controller = NordsonTemperatureController()

        # Perform initial device checks
        logging.info("Performing initial device checks...")
        if not glue_gun.is_connected():
            raise HardwareConnectionError("EasyOn glue gun is not connected.")

        if not temp_controller.is_connected():
            raise HardwareConnectionError("Nordson temperature controller is not connected.")

        logging.info("Device checks passed.")

        # Set initial temperature on the Nordson controller
        logging.info(f"Setting target temperature to {TARGET_TEMPERATURE}°C...")
        temp_controller.set_target_temperature(TARGET_TEMPERATURE)

        # Continuous monitoring and adjustment loop
        while True:
            current_temperature = temp_controller.read_temperature()

            # Log the current temperature
            logging.info(f"Current glue gun temperature: {current_temperature}°C")

            # Adjust temperature if deviation exceeds tolerance
            if abs(current_temperature - TARGET_TEMPERATURE) > 2:  # Tolerance of 2°C
                logging.warning(
                    f"Temperature deviation detected: {current_temperature}°C. Adjusting to target..."
                )
                temp_controller.set_target_temperature(TARGET_TEMPERATURE)

    except HardwareConnectionError as e:
        logging.error(f"Hardware connection error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        logging.info("Shutting down system...")
        # Ensure devices are safely shut down
        try:
            glue_gun.shutdown()
            temp_controller.shutdown()
        except Exception as e:
            logging.error(f"Error during shutdown: {e}")
        logging.info("System has been safely shut down.")

if __name__ == "__main__":
    main()
```
