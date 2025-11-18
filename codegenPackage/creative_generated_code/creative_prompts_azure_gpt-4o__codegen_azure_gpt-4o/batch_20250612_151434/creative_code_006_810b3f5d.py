"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Develop a Python program to model the operation of industrial refrigeration pumps, incorporating safety and technology features similar to those described by TROMBA.
Generated: DETERMINISTIC_810b3f5dc0634b64
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RefrigerationPump:
    """
    A class to model the operation of an industrial refrigeration pump with safety and technology features.
    """

    def __init__(self, max_pressure: float, max_temperature: float, pump_id: Optional[str] = "Unknown"):
        """
        Initialize the refrigeration pump with safety thresholds.
        
        :param max_pressure: Maximum allowable pressure (in bar) before safety shutdown
        :param max_temperature: Maximum allowable temperature (in °C) before safety shutdown
        :param pump_id: Optional ID for the pump
        """
        self.max_pressure = max_pressure
        self.max_temperature = max_temperature
        self.pump_id = pump_id
        self.current_pressure = 0.0  # Current pressure in bar
        self.current_temperature = 0.0  # Current temperature in °C
        self.is_running = False  # Pump state

    def start(self):
        """
        Start the refrigeration pump if it's not already running.
        """
        if self.is_running:
            logging.warning(f"Pump {self.pump_id} is already running.")
            return
        self.is_running = True
        logging.info(f"Pump {self.pump_id} started successfully.")

    def stop(self):
        """
        Stop the refrigeration pump if it is running.
        """
        if not self.is_running:
            logging.warning(f"Pump {self.pump_id} is already stopped.")
            return
        self.is_running = False
        logging.info(f"Pump {self.pump_id} stopped successfully.")

    def update_conditions(self, pressure: float, temperature: float):
        """
        Update the current pressure and temperature of the pump. Trigger safety shutdown if thresholds are exceeded.

        :param pressure: Current pressure in bar
        :param temperature: Current temperature in °C
        :raises: RuntimeError if safety thresholds are exceeded
        """
        if not self.is_running:
            logging.error(f"Cannot update conditions for Pump {self.pump_id} because it is not running.")
            return

        self.current_pressure = pressure
        self.current_temperature = temperature

        logging.info(f"Pump {self.pump_id} conditions updated: Pressure = {pressure} bar, Temperature = {temperature} °C")

        # Check safety thresholds
        if self.current_pressure > self.max_pressure:
            self.trigger_safety_shutdown(f"Pressure exceeded: {self.current_pressure} bar > {self.max_pressure} bar")
        if self.current_temperature > self.max_temperature:
            self.trigger_safety_shutdown(f"Temperature exceeded: {self.current_temperature} °C > {self.max_temperature} °C")

    def trigger_safety_shutdown(self, reason: str):
        """
        Trigger a safety shutdown of the pump and log the reason.

        :param reason: The reason for the safety shutdown
        """
        self.stop()  # Stop the pump
        logging.critical(f"Safety shutdown for Pump {self.pump_id} due to: {reason}")
        raise RuntimeError(f"Safety shutdown triggered: {reason}")


# Example usage (can be removed or adapted for production use)
if __name__ == "__main__":
    try:
        # Initialize a pump with safety thresholds
        pump = RefrigerationPump(max_pressure=10.0, max_temperature=80.0, pump_id="PUMP-001")

        # Start the pump
        pump.start()

        # Update pump conditions (values within safe range)
        pump.update_conditions(pressure=8.0, temperature=70.0)

        # Update pump conditions (values exceeding thresholds, triggers safety shutdown)
        pump.update_conditions(pressure=12.0, temperature=85.0)

    except RuntimeError as e:
        logging.error(f"An error occurred: {e}")
```
