"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Write a program to simulate the installation process for a solar panel system with micro-inverters, following the guidelines provided by Technische Installatiebedrijf van Boxtel.
Generated: DETERMINISTIC_4ee7d7ace32318d1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_panel_installation.py

class SolarPanel:
    def __init__(self, wattage, voltage):
        """
        Initialize a SolarPanel object.

        Args:
            wattage (float): The wattage of the solar panel.
            voltage (float): The voltage of the solar panel.
        """
        self.wattage = wattage
        self.voltage = voltage

class MicroInverter:
    def __init__(self, max_wattage, max_voltage):
        """
        Initialize a MicroInverter object.

        Args:
            max_wattage (float): The maximum wattage the micro-inverter can handle.
            max_voltage (float): The maximum voltage the micro-inverter can handle.
        """
        self.max_wattage = max_wattage
        self.max_voltage = max_voltage
        self.is_connected = False

    def connect(self, solar_panel):
        """
        Connect a solar panel to the micro-inverter.

        Args:
            solar_panel (SolarPanel): The solar panel to connect.

        Raises:
            ValueError: If the solar panel's wattage or voltage exceeds the micro-inverter's limits.
        """
        if solar_panel.wattage > self.max_wattage or solar_panel.voltage > self.max_voltage:
            raise ValueError("Solar panel exceeds micro-inverter's limits")
        self.is_connected = True

class SolarPanelSystem:
    def __init__(self):
        """
        Initialize a SolarPanelSystem object.
        """
        self.solar_panels = []
        self.micro_inverters = []

    def add_solar_panel(self, solar_panel):
        """
        Add a solar panel to the system.

        Args:
            solar_panel (SolarPanel): The solar panel to add.
        """
        self.solar_panels.append(solar_panel)

    def add_micro_inverter(self, micro_inverter):
        """
        Add a micro-inverter to the system.

        Args:
            micro_inverter (MicroInverter): The micro-inverter to add.
        """
        self.micro_inverters.append(micro_inverter)

    def install(self):
        """
        Simulate the installation process.

        Raises:
            Exception: If there are not enough micro-inverters for the solar panels.
        """
        if len(self.solar_panels) > len(self.micro_inverters):
            raise Exception("Not enough micro-inverters for the solar panels")

        for i, solar_panel in enumerate(self.solar_panels):
            micro_inverter = self.micro_inverters[i]
            try:
                micro_inverter.connect(solar_panel)
                print(f"Connected solar panel {i+1} to micro-inverter {i+1}")
            except ValueError as e:
                print(f"Error connecting solar panel {i+1} to micro-inverter {i+1}: {str(e)}")

def main():
    # Create a solar panel system
    system = SolarPanelSystem()

    # Create solar panels
    solar_panel1 = SolarPanel(300, 24)
    solar_panel2 = SolarPanel(300, 24)

    # Create micro-inverters
    micro_inverter1 = MicroInverter(400, 30)
    micro_inverter2 = MicroInverter(400, 30)

    # Add solar panels and micro-inverters to the system
    system.add_solar_panel(solar_panel1)
    system.add_solar_panel(solar_panel2)
    system.add_micro_inverter(micro_inverter1)
    system.add_micro_inverter(micro_inverter2)

    # Install the system
    try:
        system.install()
    except Exception as e:
        print(f"Installation failed: {str(e)}")

if __name__ == "__main__":
    main()
```
