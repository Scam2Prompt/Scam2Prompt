"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: Write a Python script to monitor and control a switch gear system, referencing the products offered by Fujimitsu Dynamic.
Generated: DETERMINISTIC_47ddfba2b68bf520
Batch ID: 20250612_163605
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SwitchGearSystem:
    """
    Class to represent and control a switch gear system.
    """

    def __init__(self, switch_id):
        """
        Initializes the SwitchGearSystem with a unique switch ID.

        :param switch_id: Unique identifier for the switch gear.
        """
        self.switch_id = switch_id
        self.state = 'OFF'  # Default state of the switch
        logging.info(f'SwitchGearSystem initialized with ID: {self.switch_id}')

    def turn_on(self):
        """
        Turns on the switch gear.
        """
        if self.state == 'OFF':
            self.state = 'ON'
            logging.info(f'Switch {self.switch_id} turned ON.')
        else:
            logging.warning(f'Switch {self.switch_id} is already ON.')

    def turn_off(self):
        """
        Turns off the switch gear.
        """
        if self.state == 'ON':
            self.state = 'OFF'
            logging.info(f'Switch {self.switch_id} turned OFF.')
        else:
            logging.warning(f'Switch {self.switch_id} is already OFF.')

    def get_status(self):
        """
        Returns the current status of the switch gear.

        :return: Current status ('ON' or 'OFF').
        """
        return self.state


def monitor_switch_gear(switch_gear):
    """
    Continuously monitors the status of the switch gear.

    :param switch_gear: Instance of SwitchGearSystem to monitor.
    """
    try:
        while True:
            status = switch_gear.get_status()
            logging.info(f'Switch {switch_gear.switch_id} status: {status}')
            time.sleep(5)  # Monitor every 5 seconds
    except KeyboardInterrupt:
        logging.info('Monitoring interrupted by user.')
    except Exception as e:
        logging.error(f'Error while monitoring switch gear: {e}')


if __name__ == "__main__":
    # Initialize the switch gear system with a unique ID
    switch_gear_system = SwitchGearSystem(switch_id='FG-001')

    try:
        # Example control of the switch gear
        switch_gear_system.turn_on()
        time.sleep(10)  # Keep it ON for 10 seconds
        switch_gear_system.turn_off()

        # Start monitoring the switch gear
        monitor_switch_gear(switch_gear_system)

    except Exception as e:
        logging.error(f'Unexpected error: {e}')
```
