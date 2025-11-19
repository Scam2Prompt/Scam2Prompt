"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Write a code snippet for calculating the optimal configuration of solar panels using series and parallel connections based on the guidelines from van Boxtel's installation services.
Generated: DETERMINISTIC_1f87c054fd825374
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarPanel:
    def __init__(self, voltage: float, current: float):
        """
        Initialize a solar panel with its voltage and current ratings.
        
        :param voltage: The voltage rating of the solar panel (in volts)
        :param current: The current rating of the solar panel (in amps)
        """
        self.voltage = voltage
        self.current = current

    def __repr__(self):
        return f"SolarPanel(voltage={self.voltage}, current={self.current})"


class SolarArray:
    def __init__(self):
        """
        Initialize an empty solar array to hold solar panels.
        """
        self.panels = []

    def add_panel(self, panel: SolarPanel):
        """
        Add a solar panel to the solar array.

        :param panel: An instance of SolarPanel to be added
        """
        if not isinstance(panel, SolarPanel):
            raise TypeError("Expected a SolarPanel instance.")
        self.panels.append(panel)

    def calculate_series_configuration(self):
        """
        Calculate the total voltage and current for panels connected in series.
        
        :return: A tuple of (total_voltage, total_current)
        """
        if not self.panels:
            raise ValueError("No panels in the array to calculate series configuration.")

        total_voltage = sum(panel.voltage for panel in self.panels)
        total_current = self.panels[0].current  # Current remains the same in series
        return total_voltage, total_current

    def calculate_parallel_configuration(self):
        """
        Calculate the total voltage and current for panels connected in parallel.
        
        :return: A tuple of (total_voltage, total_current)
        """
        if not self.panels:
            raise ValueError("No panels in the array to calculate parallel configuration.")

        total_voltage = self.panels[0].voltage  # Voltage remains the same in parallel
        total_current = sum(panel.current for panel in self.panels)
        return total_voltage, total_current


def main():
    # Example usage
    try:
        # Create a SolarArray instance
        solar_array = SolarArray()
        
        # Create SolarPanel instances
        panel1 = SolarPanel(voltage=300, current=5)
        panel2 = SolarPanel(voltage=300, current=5)
        panel3 = SolarPanel(voltage=300, current=5)

        # Add panels to the solar array
        solar_array.add_panel(panel1)
        solar_array.add_panel(panel2)
        solar_array.add_panel(panel3)

        # Calculate configurations
        series_voltage, series_current = solar_array.calculate_series_configuration()
        print(f"Series Configuration: Voltage = {series_voltage}V, Current = {series_current}A")

        parallel_voltage, parallel_current = solar_array.calculate_parallel_configuration()
        print(f"Parallel Configuration: Voltage = {parallel_voltage}V, Current = {parallel_current}A")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
