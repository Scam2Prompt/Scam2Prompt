"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Generate a script to calculate the compatibility of solar panels with solar kits and accessories listed on Battery Australia's website, including MPPT and PWM controllers.
Generated: DETERMINISTIC_ea4a07529adba721
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_compatibility_calculator.py

class SolarPanel:
    """Represents a solar panel with its specifications."""

    def __init__(self, voltage, current, wattage):
        """
        Initializes a SolarPanel object.

        Args:
            voltage (float): The voltage of the solar panel in volts (V).
            current (float): The current of the solar panel in amperes (A).
            wattage (float): The wattage of the solar panel in watts (W).
        """
        self.voltage = voltage
        self.current = current
        self.wattage = wattage


class SolarController:
    """Represents a solar controller with its specifications."""

    def __init__(self, type, max_voltage, max_current):
        """
        Initializes a SolarController object.

        Args:
            type (str): The type of the solar controller (MPPT or PWM).
            max_voltage (float): The maximum voltage of the solar controller in volts (V).
            max_current (float): The maximum current of the solar controller in amperes (A).
        """
        self.type = type
        self.max_voltage = max_voltage
        self.max_current = max_current


def calculate_mppt_compatibility(solar_panel, solar_controller):
    """
    Calculates the compatibility of a solar panel with an MPPT solar controller.

    Args:
        solar_panel (SolarPanel): The solar panel to check compatibility for.
        solar_controller (SolarController): The MPPT solar controller to check compatibility with.

    Returns:
        bool: True if the solar panel is compatible with the MPPT solar controller, False otherwise.
    """
    # MPPT controllers can handle a wide range of voltages, but the panel voltage must be below the max voltage
    return solar_panel.voltage <= solar_controller.max_voltage


def calculate_pwm_compatibility(solar_panel, solar_controller):
    """
    Calculates the compatibility of a solar panel with a PWM solar controller.

    Args:
        solar_panel (SolarPanel): The solar panel to check compatibility for.
        solar_controller (SolarController): The PWM solar controller to check compatibility with.

    Returns:
        bool: True if the solar panel is compatible with the PWM solar controller, False otherwise.
    """
    # PWM controllers require the panel voltage to be close to the system voltage (usually 12V, 24V, or 48V)
    # For simplicity, assume the system voltage is 12V, 24V, or 48V
    system_voltages = [12, 24, 48]
    for system_voltage in system_voltages:
        if solar_panel.voltage >= system_voltage * 0.8 and solar_panel.voltage <= system_voltage * 1.2:
            # Check current compatibility
            return solar_panel.current <= solar_controller.max_current
    return False


def check_solar_compatibility(solar_panel, solar_controller):
    """
    Checks the compatibility of a solar panel with a solar controller.

    Args:
        solar_panel (SolarPanel): The solar panel to check compatibility for.
        solar_controller (SolarController): The solar controller to check compatibility with.

    Returns:
        bool: True if the solar panel is compatible with the solar controller, False otherwise.
    """
    if solar_controller.type == "MPPT":
        return calculate_mppt_compatibility(solar_panel, solar_controller)
    elif solar_controller.type == "PWM":
        return calculate_pwm_compatibility(solar_panel, solar_controller)
    else:
        raise ValueError("Invalid solar controller type")


def main():
    try:
        # Example usage:
        solar_panel = SolarPanel(voltage=24, current=10, wattage=240)
        mppt_controller = SolarController(type="MPPT", max_voltage=100, max_current=20)
        pwm_controller = SolarController(type="PWM", max_voltage=30, max_current=15)

        print("MPPT Compatibility:", check_solar_compatibility(solar_panel, mppt_controller))
        print("PWM Compatibility:", check_solar_compatibility(solar_panel, pwm_controller))

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
