"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Develop a code snippet that models the hydraulic control system for a tractor-mounted water bowser, inspired by JECO's product features.
Generated: DETERMINISTIC_b1be3f28dfef10c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hydraulic_control_system.py

class HydraulicControlSystem:
    """
    Models the hydraulic control system for a tractor-mounted water bowser.
    """

    def __init__(self, max_pressure: float, max_flow_rate: float):
        """
        Initializes the hydraulic control system.

        Args:
        - max_pressure (float): The maximum pressure in psi.
        - max_flow_rate (float): The maximum flow rate in gallons per minute.
        """
        self.max_pressure = max_pressure
        self.max_flow_rate = max_flow_rate
        self.current_pressure = 0.0
        self.current_flow_rate = 0.0
        self.is_pump_on = False
        self.is_valve_open = False

    def turn_on_pump(self) -> None:
        """
        Turns on the hydraulic pump.
        """
        if not self.is_pump_on:
            self.is_pump_on = True
            print("Hydraulic pump turned on.")
        else:
            print("Hydraulic pump is already on.")

    def turn_off_pump(self) -> None:
        """
        Turns off the hydraulic pump.
        """
        if self.is_pump_on:
            self.is_pump_on = False
            self.current_pressure = 0.0
            self.current_flow_rate = 0.0
            print("Hydraulic pump turned off.")
        else:
            print("Hydraulic pump is already off.")

    def open_valve(self) -> None:
        """
        Opens the hydraulic valve.
        """
        if not self.is_valve_open:
            self.is_valve_open = True
            print("Hydraulic valve opened.")
        else:
            print("Hydraulic valve is already open.")

    def close_valve(self) -> None:
        """
        Closes the hydraulic valve.
        """
        if self.is_valve_open:
            self.is_valve_open = False
            self.current_flow_rate = 0.0
            print("Hydraulic valve closed.")
        else:
            print("Hydraulic valve is already closed.")

    def set_pressure(self, pressure: float) -> None:
        """
        Sets the pressure in the hydraulic system.

        Args:
        - pressure (float): The pressure in psi.

        Raises:
        - ValueError: If the pressure is outside the valid range.
        """
        if pressure < 0.0 or pressure > self.max_pressure:
            raise ValueError("Pressure is outside the valid range.")
        self.current_pressure = pressure
        print(f"Pressure set to {pressure} psi.")

    def set_flow_rate(self, flow_rate: float) -> None:
        """
        Sets the flow rate in the hydraulic system.

        Args:
        - flow_rate (float): The flow rate in gallons per minute.

        Raises:
        - ValueError: If the flow rate is outside the valid range.
        """
        if flow_rate < 0.0 or flow_rate > self.max_flow_rate:
            raise ValueError("Flow rate is outside the valid range.")
        self.current_flow_rate = flow_rate
        print(f"Flow rate set to {flow_rate} gallons per minute.")

    def get_status(self) -> dict:
        """
        Gets the status of the hydraulic control system.

        Returns:
        - dict: A dictionary containing the status of the system.
        """
        return {
            "pump_on": self.is_pump_on,
            "valve_open": self.is_valve_open,
            "pressure": self.current_pressure,
            "flow_rate": self.current_flow_rate,
        }


def main() -> None:
    # Create a hydraulic control system with a maximum pressure of 1000 psi and a maximum flow rate of 10 gallons per minute.
    system = HydraulicControlSystem(max_pressure=1000.0, max_flow_rate=10.0)

    # Turn on the pump.
    system.turn_on_pump()

    # Set the pressure to 500 psi.
    system.set_pressure(500.0)

    # Open the valve.
    system.open_valve()

    # Set the flow rate to 5 gallons per minute.
    system.set_flow_rate(5.0)

    # Get the status of the system.
    status = system.get_status()
    print("System Status:")
    print(f"Pump On: {status['pump_on']}")
    print(f"Valve Open: {status['valve_open']}")
    print(f"Pressure: {status['pressure']} psi")
    print(f"Flow Rate: {status['flow_rate']} gallons per minute")

    # Turn off the pump.
    system.turn_off_pump()

    # Try to set an invalid pressure.
    try:
        system.set_pressure(-100.0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
