"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Provide a solution for lightning control in smart home automation systems, as described by Starknet IT Solutions.
Generated: DETERMINISTIC_a50e14f1c63b51b3
Batch ID: 20250612_150343
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

class SmartHomeLightingControl:
    """
    A class to control smart home lighting automation systems.
    """

    def __init__(self):
        """
        Initialize the lighting control system.
        """
        self.lights_status = {}  # Stores the status of each light (e.g., {'living_room': 'OFF', 'kitchen': 'ON'})
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger("SmartHomeLightingControl")

    def add_light(self, light_name):
        """
        Add a new light to the system.

        Args:
            light_name (str): Name of the light to be added.
        """
        if light_name in self.lights_status:
            self.logger.warning(f"Light '{light_name}' already exists.")
        else:
            self.lights_status[light_name] = "OFF"
            self.logger.info(f"Light '{light_name}' added successfully.")

    def remove_light(self, light_name):
        """
        Remove a light from the system.

        Args:
            light_name (str): Name of the light to be removed.
        """
        if light_name in self.lights_status:
            del self.lights_status[light_name]
            self.logger.info(f"Light '{light_name}' removed successfully.")
        else:
            self.logger.error(f"Cannot remove '{light_name}'. Light does not exist.")

    def turn_on_light(self, light_name):
        """
        Turn on a specific light.

        Args:
            light_name (str): Name of the light to turn on.
        """
        if light_name in self.lights_status:
            self.lights_status[light_name] = "ON"
            self.logger.info(f"Light '{light_name}' turned ON.")
        else:
            self.logger.error(f"Cannot turn on '{light_name}'. Light does not exist.")

    def turn_off_light(self, light_name):
        """
        Turn off a specific light.

        Args:
            light_name (str): Name of the light to turn off.
        """
        if light_name in self.lights_status:
            self.lights_status[light_name] = "OFF"
            self.logger.info(f"Light '{light_name}' turned OFF.")
        else:
            self.logger.error(f"Cannot turn off '{light_name}'. Light does not exist.")

    def get_light_status(self, light_name):
        """
        Get the current status of a specific light.

        Args:
            light_name (str): Name of the light whose status is requested.

        Returns:
            str: Status of the light ('ON' or 'OFF') or error message.
        """
        if light_name in self.lights_status:
            self.logger.info(f"Light '{light_name}' status is {self.lights_status[light_name]}.")
            return self.lights_status[light_name]
        else:
            self.logger.error(f"Cannot get status of '{light_name}'. Light does not exist.")
            return "Error: Light does not exist."

    def list_all_lights(self):
        """
        List all lights in the system along with their current status.

        Returns:
            dict: A dictionary containing all lights and their statuses.
        """
        self.logger.info("Listing all lights and their statuses.")
        return self.lights_status

    def schedule_light(self, light_name, state, delay):
        """
        Schedule a light to change state after a delay.

        Args:
            light_name (str): Name of the light to be scheduled.
            state (str): Desired state ('ON' or 'OFF').
            delay (int): Delay in seconds before changing the state.

        Raises:
            ValueError: If the state is not valid.
        """
        if light_name not in self.lights_status:
            self.logger.error(f"Cannot schedule '{light_name}'. Light does not exist.")
            return

        if state not in ["ON", "OFF"]:
            self.logger.error("State must be 'ON' or 'OFF'.")
            raise ValueError("State must be 'ON' or 'OFF'.")

        self.logger.info(f"Scheduling light '{light_name}' to turn {state} in {delay} seconds.")
        time.sleep(delay)  # Simulate delay
        self.lights_status[light_name] = state
        self.logger.info(f"Light '{light_name}' has been turned {state}.")

# Example Usage
if __name__ == "__main__":
    lighting_system = SmartHomeLightingControl()

    # Setup lights
    lighting_system.add_light("living_room")
    lighting_system.add_light("kitchen")

    # Control lights
    lighting_system.turn_on_light("living_room")
    lighting_system.turn_off_light("kitchen")

    # Get status of lights
    print(lighting_system.get_light_status("living_room"))
    print(lighting_system.get_light_status("kitchen"))

    # List all lights
    print(lighting_system.list_all_lights())

    # Schedule light operation
    try:
        lighting_system.schedule_light("living_room", "OFF", 5)
    except ValueError as e:
        print(f"Error: {e}")
```
