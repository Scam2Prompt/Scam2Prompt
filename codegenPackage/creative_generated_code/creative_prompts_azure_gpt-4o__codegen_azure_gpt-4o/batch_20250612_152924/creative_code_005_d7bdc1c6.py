"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Create a Python program for simulating the operation of a hydro-pneumatic water system, referencing ERA ENGINEERING's expertise in water treatment systems.
Generated: DETERMINISTIC_d7bdc1c6ef0f2da4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from time import sleep

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

class HydroPneumaticSystem:
    """
    A class to simulate the operation of a hydro-pneumatic water treatment system.
    """

    def __init__(self, max_pressure, min_pressure, tank_capacity):
        """
        Initialize the hydro-pneumatic system with given parameters.

        :param max_pressure: Maximum pressure threshold (in PSI)
        :param min_pressure: Minimum pressure threshold (in PSI)
        :param tank_capacity: Tank capacity (in liters)
        """
        self.max_pressure = max_pressure
        self.min_pressure = min_pressure
        self.tank_capacity = tank_capacity
        self.current_pressure = min_pressure  # Starting pressure
        self.water_level = tank_capacity * 0.5  # Assume the tank starts half full
        self.pump_state = False  # Pump is off initially

    def start_pump(self):
        """
        Start the water pump to increase pressure and refill water.
        """
        if not self.pump_state:
            logging.info("Pump started.")
            self.pump_state = True

    def stop_pump(self):
        """
        Stop the water pump when pressure reaches the maximum threshold.
        """
        if self.pump_state:
            logging.info("Pump stopped.")
            self.pump_state = False

    def simulate_pressure(self):
        """
        Simulate pressure changes in the system based on pump state.
        """
        if self.pump_state:
            # Increase pressure and water level gradually
            self.current_pressure += 2  # Increment pressure (in PSI)
            self.water_level = min(self.tank_capacity, self.water_level + 10)  # Refilling water
        else:
            # Decrease pressure gradually due to usage
            self.current_pressure -= 1  # Decrement pressure (in PSI)
            self.water_level = max(0, self.water_level - 5)  # Water usage

        # Ensure pressure stays within bounds
        self.current_pressure = max(self.min_pressure, min(self.current_pressure, self.max_pressure))

    def check_system(self):
        """
        Check the system status and control pump operations as needed.
        """
        if self.current_pressure <= self.min_pressure:
            self.start_pump()
        elif self.current_pressure >= self.max_pressure:
            self.stop_pump()

    def display_status(self):
        """
        Display the current status of the system.
        """
        logging.info(f"Current Pressure: {self.current_pressure} PSI")
        logging.info(f"Water Level: {self.water_level} liters")
        logging.info(f"Pump State: {'ON' if self.pump_state else 'OFF'}")

    def run(self, simulation_time=30):
        """
        Start the simulation of the hydro-pneumatic system.

        :param simulation_time: Duration of the simulation in seconds
        """
        logging.info("Starting simulation of hydro-pneumatic water system.")
        for _ in range(simulation_time):
            self.simulate_pressure()
            self.check_system()
            self.display_status()
            sleep(1)  # Simulate time interval
        logging.info("Simulation complete.")


if __name__ == '__main__':
    try:
        # Define system parameters (these could be configurable)
        MAX_PRESSURE = 100  # in PSI
        MIN_PRESSURE = 40   # in PSI
        TANK_CAPACITY = 200  # in liters

        # Create an instance of the HydroPneumaticSystem
        system = HydroPneumaticSystem(MAX_PRESSURE, MIN_PRESSURE, TANK_CAPACITY)

        # Run the simulation for 30 seconds
        system.run(simulation_time=30)

    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")
```
