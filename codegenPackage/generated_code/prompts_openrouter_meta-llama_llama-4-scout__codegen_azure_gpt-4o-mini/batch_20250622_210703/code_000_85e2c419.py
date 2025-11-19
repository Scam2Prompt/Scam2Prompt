"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Design a smart pool system with underwater lighting and heating for a residential area in Brazil.
Generated: DETERMINISTIC_85e2c419bdb9bfb9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SmartPoolSystem:
    """
    A class to represent a smart pool system with underwater lighting and heating.
    """

    def __init__(self, pool_temperature=25.0, lighting_status=False):
        """
        Initializes the SmartPoolSystem with default temperature and lighting status.

        :param pool_temperature: Desired pool temperature in Celsius (default is 25.0)
        :param lighting_status: Status of the underwater lighting (default is False)
        """
        self.pool_temperature = pool_temperature
        self.lighting_status = lighting_status
        self.current_temperature = 25.0  # Initial temperature
        self.heater_on = False

    def set_temperature(self, desired_temperature):
        """
        Sets the desired pool temperature.

        :param desired_temperature: Desired temperature in Celsius
        :raises ValueError: If the desired temperature is out of range
        """
        if desired_temperature < 15.0 or desired_temperature > 40.0:
            raise ValueError("Temperature must be between 15.0 and 40.0 degrees Celsius.")
        self.pool_temperature = desired_temperature
        self.adjust_heater()

    def adjust_heater(self):
        """
        Adjusts the heater based on the current and desired temperature.
        Turns the heater on or off as needed.
        """
        if self.current_temperature < self.pool_temperature:
            self.heater_on = True
            self.current_temperature += 1  # Simulate heating
        else:
            self.heater_on = False

    def toggle_lighting(self):
        """
        Toggles the status of the underwater lighting.
        """
        self.lighting_status = not self.lighting_status

    def update_temperature(self, external_temperature):
        """
        Updates the current pool temperature based on external conditions.

        :param external_temperature: The current external temperature in Celsius
        """
        if external_temperature < 0 or external_temperature > 50:
            raise ValueError("External temperature must be between 0 and 50 degrees Celsius.")
        
        # Simulate temperature change based on external temperature
        if self.heater_on:
            self.current_temperature += 0.5  # Heating effect
        else:
            self.current_temperature -= 0.2  # Cooling effect

        # Ensure the temperature does not drop below 15 or exceed 40
        self.current_temperature = max(15.0, min(self.current_temperature, 40.0))

    def get_status(self):
        """
        Returns the current status of the pool system.

        :return: A dictionary containing the current temperature, desired temperature, 
                 lighting status, and heater status.
        """
        return {
            "current_temperature": self.current_temperature,
            "desired_temperature": self.pool_temperature,
            "lighting_status": self.lighting_status,
            "heater_status": self.heater_on
        }


# Example usage
if __name__ == "__main__":
    try:
        pool_system = SmartPoolSystem()
        pool_system.set_temperature(30.0)
        pool_system.toggle_lighting()
        pool_system.update_temperature(28.0)

        status = pool_system.get_status()
        print("Pool System Status:", status)

    except ValueError as e:
        print("Error:", e)
```
