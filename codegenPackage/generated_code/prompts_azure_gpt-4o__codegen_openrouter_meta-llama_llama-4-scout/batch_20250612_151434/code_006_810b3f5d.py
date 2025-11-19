"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Develop a Python program to model the operation of industrial refrigeration pumps, incorporating safety and technology features similar to those described by TROMBA.
Generated: DETERMINISTIC_810b3f5dc0634b64
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_refrigeration_pump.py

class RefrigerationPump:
    """
    Models the operation of an industrial refrigeration pump.

    Attributes:
        pump_id (str): Unique identifier for the pump.
        flow_rate (float): Flow rate of the pump in m³/h.
        pressure (float): Pressure of the pump in bar.
        temperature (float): Temperature of the pump in °C.
        is_running (bool): Indicates if the pump is running.
    """

    def __init__(self, pump_id, flow_rate, pressure, temperature):
        """
        Initializes a RefrigerationPump object.

        Args:
            pump_id (str): Unique identifier for the pump.
            flow_rate (float): Flow rate of the pump in m³/h.
            pressure (float): Pressure of the pump in bar.
            temperature (float): Temperature of the pump in °C.
        """
        self.pump_id = pump_id
        self.flow_rate = flow_rate
        self.pressure = pressure
        self.temperature = temperature
        self.is_running = False

    def start_pump(self):
        """
        Starts the refrigeration pump.

        Raises:
            Exception: If the pump is already running.
        """
        if self.is_running:
            raise Exception(f"Pump {self.pump_id} is already running.")
        self.is_running = True
        print(f"Pump {self.pump_id} started.")

    def stop_pump(self):
        """
        Stops the refrigeration pump.

        Raises:
            Exception: If the pump is not running.
        """
        if not self.is_running:
            raise Exception(f"Pump {self.pump_id} is not running.")
        self.is_running = False
        print(f"Pump {self.pump_id} stopped.")

    def update_status(self, flow_rate=None, pressure=None, temperature=None):
        """
        Updates the status of the refrigeration pump.

        Args:
            flow_rate (float, optional): New flow rate in m³/h. Defaults to None.
            pressure (float, optional): New pressure in bar. Defaults to None.
            temperature (float, optional): New temperature in °C. Defaults to None.

        Raises:
            ValueError: If any of the provided values are invalid.
        """
        if flow_rate is not None and flow_rate <= 0:
            raise ValueError("Flow rate must be greater than zero.")
        if pressure is not None and pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        if temperature is not None and temperature < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")

        if flow_rate is not None:
            self.flow_rate = flow_rate
        if pressure is not None:
            self.pressure = pressure
        if temperature is not None:
            self.temperature = temperature

    def __str__(self):
        """
        Returns a string representation of the RefrigerationPump object.

        Returns:
            str: String representation of the RefrigerationPump object.
        """
        status = "Running" if self.is_running else "Stopped"
        return f"Pump {self.pump_id} - Status: {status}, Flow Rate: {self.flow_rate} m³/h, Pressure: {self.pressure} bar, Temperature: {self.temperature} °C"


class SafetyFeatures:
    """
    Models the safety features of an industrial refrigeration pump.

    Attributes:
        pump (RefrigerationPump): The refrigeration pump object.
    """

    def __init__(self, pump):
        """
        Initializes a SafetyFeatures object.

        Args:
            pump (RefrigerationPump): The refrigeration pump object.
        """
        self.pump = pump

    def check_over_pressure(self, max_pressure):
        """
        Checks if the pump pressure exceeds the maximum allowed pressure.

        Args:
            max_pressure (float): Maximum allowed pressure in bar.

        Raises:
            Exception: If the pump pressure exceeds the maximum allowed pressure.
        """
        if self.pump.pressure > max_pressure:
            raise Exception(f"Pump {self.pump.pump_id} over pressure: {self.pump.pressure} bar > {max_pressure} bar")

    def check_over_temperature(self, max_temperature):
        """
        Checks if the pump temperature exceeds the maximum allowed temperature.

        Args:
            max_temperature (float): Maximum allowed temperature in °C.

        Raises:
            Exception: If the pump temperature exceeds the maximum allowed temperature.
        """
        if self.pump.temperature > max_temperature:
            raise Exception(f"Pump {self.pump.pump_id} over temperature: {self.pump.temperature} °C > {max_temperature} °C")


def main():
    try:
        pump = RefrigerationPump("P001", 10.0, 5.0, 20.0)
        safety_features = SafetyFeatures(pump)

        print(pump)

        pump.start_pump()
        print(pump)

        pump.update_status(pressure=6.0, temperature=22.0)
        print(pump)

        safety_features.check_over_pressure(7.0)
        safety_features.check_over_temperature(25.0)

        pump.stop_pump()
        print(pump)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
