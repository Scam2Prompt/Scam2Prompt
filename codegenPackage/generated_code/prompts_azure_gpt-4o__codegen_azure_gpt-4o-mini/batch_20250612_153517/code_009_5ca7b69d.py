"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write code to simulate the installation and operation of electrical panels for specialized environments like greenhouses or parking ventilation systems, as described by پایش نیرو.
Generated: DETERMINISTIC_5ca7b69d700f64be
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricalPanel:
    """
    A class to represent an electrical panel for specialized environments.
    """

    def __init__(self, panel_id, environment_type):
        """
        Initializes the electrical panel with an ID and environment type.

        :param panel_id: Unique identifier for the electrical panel
        :param environment_type: Type of environment (e.g., 'greenhouse', 'parking')
        """
        self.panel_id = panel_id
        self.environment_type = environment_type
        self.status = 'OFF'
        self.power_consumption = 0  # in watts

    def install(self):
        """
        Simulates the installation of the electrical panel.
        """
        logging.info(f"Installing electrical panel {self.panel_id} for {self.environment_type}...")
        time.sleep(1)  # Simulate installation time
        logging.info(f"Electrical panel {self.panel_id} installed successfully.")

    def operate(self):
        """
        Simulates the operation of the electrical panel.
        """
        if self.status == 'OFF':
            self.status = 'ON'
            self.power_consumption = random.randint(100, 500)  # Random power consumption
            logging.info(f"Electrical panel {self.panel_id} is now ON. Power consumption: {self.power_consumption}W.")
        else:
            logging.warning(f"Electrical panel {self.panel_id} is already ON.")

    def shut_down(self):
        """
        Shuts down the electrical panel.
        """
        if self.status == 'ON':
            logging.info(f"Shutting down electrical panel {self.panel_id}...")
            self.status = 'OFF'
            self.power_consumption = 0
            logging.info(f"Electrical panel {self.panel_id} is now OFF.")
        else:
            logging.warning(f"Electrical panel {self.panel_id} is already OFF.")

    def get_status(self):
        """
        Returns the current status of the electrical panel.

        :return: A string representing the status of the panel
        """
        return self.status

    def get_power_consumption(self):
        """
        Returns the current power consumption of the electrical panel.

        :return: An integer representing the power consumption in watts
        """
        return self.power_consumption


def main():
    """
    Main function to simulate the installation and operation of electrical panels.
    """
    try:
        # Create electrical panels for different environments
        greenhouse_panel = ElectricalPanel(panel_id='GP-001', environment_type='greenhouse')
        parking_panel = ElectricalPanel(panel_id='PP-001', environment_type='parking')

        # Install panels
        greenhouse_panel.install()
        parking_panel.install()

        # Operate panels
        greenhouse_panel.operate()
        parking_panel.operate()

        # Get and log status and power consumption
        logging.info(f"Greenhouse Panel Status: {greenhouse_panel.get_status()}, Power Consumption: {greenhouse_panel.get_power_consumption()}W")
        logging.info(f"Parking Panel Status: {parking_panel.get_status()}, Power Consumption: {parking_panel.get_power_consumption()}W")

        # Shut down panels
        greenhouse_panel.shut_down()
        parking_panel.shut_down()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
