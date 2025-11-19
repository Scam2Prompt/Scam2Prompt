"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: What are the best practices for integrating industrial heaters into a control system, based on the solutions provided by Fujimitsu Dynamic?
Generated: DETERMINISTIC_61dc7fc156065728
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class IndustrialHeater:
    """
    A class to represent an industrial heater.

    Attributes
    ----------
    id : str
        Unique identifier for the heater.
    temperature : float
        Current temperature of the heater.
    power_status : bool
        Indicates whether the heater is on or off.
    target_temperature : float
        Desired temperature to maintain.

    Methods
    -------
    turn_on():
        Turns the heater on.
    turn_off():
        Turns the heater off.
    set_target_temperature(temp: float):
        Sets the desired target temperature for the heater.
    monitor_temperature():
        Monitor the current temperature and adjust as necessary.
    """

    def __init__(self, id: str):
        """
        Constructs all the necessary attributes for the Industrial Heater.

        Parameters
        ----------
        id : str
            Unique identifier for the heater.
        """
        self.id = id
        self.temperature = 20.0  # Default temperature
        self.power_status = False  # Heater is initially off
        self.target_temperature = 20.0  # Default target temperature

    def turn_on(self):
        """Turns the heater on, setting the power_status to True."""
        try:
            self.power_status = True
            logging.info(f"Heater {self.id} turned on.")
        except Exception as e:
            logging.error(f"Error turning on heater {self.id}: {e}")

    def turn_off(self):
        """Turns the heater off, setting the power_status to False."""
        try:
            self.power_status = False
            logging.info(f"Heater {self.id} turned off.")
        except Exception as e:
            logging.error(f"Error turning off heater {self.id}: {e}")

    def set_target_temperature(self, temp: float):
        """
        Sets the desired target temperature for the heater.

        Parameters
        ----------
        temp : float
            The desired temperature to maintain.

        Raises
        ------
        ValueError
            If the target temperature is out of acceptable range.
        """
        if temp < 0 or temp > 100:
            logging.error("Target temperature must be between 0 and 100 degrees Celsius.")
            raise ValueError("Target temperature must be between 0 and 100 degrees Celsius.")
        
        self.target_temperature = temp
        logging.info(f"Heater {self.id} target temperature set to {self.target_temperature}.")

    def monitor_temperature(self):
        """Monitor the current temperature and adjust the heater status as necessary."""
        try:
            if self.power_status and self.temperature < self.target_temperature:
                self.temperature += 1  # Simulate heating process
                logging.info(f"Heater {self.id} heating up. Current temperature: {self.temperature}.")
            elif self.power_status and self.temperature >= self.target_temperature:
                logging.info(f"Heater {self.id} reached target temperature: {self.temperature}.")
            elif not self.power_status:
                logging.info(f"Heater {self.id} is off. Current temperature: {self.temperature}.")
        except Exception as e:
            logging.error(f"Error monitoring heater {self.id}: {e}")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    heater = IndustrialHeater(id="Heater-01")
    
    heater.turn_on()
    heater.set_target_temperature(75)
    
    # Simulate temperature monitoring
    for _ in range(10):
        heater.monitor_temperature()
```

This code defines a simple model for an industrial heater with proper methods for controlling it and monitoring its state, including error handling and logging for production readiness.
