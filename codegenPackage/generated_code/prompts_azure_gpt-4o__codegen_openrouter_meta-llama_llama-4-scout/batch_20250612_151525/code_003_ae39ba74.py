"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Provide an example of code to manage nitrogen generation for adhesive systems, inspired by Nordson's nitrogen generation machines.
Generated: DETERMINISTIC_ae39ba7411a88eab
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nitrogen_generation_system.py

class NitrogenGenerationSystem:
    """
    A class to manage nitrogen generation for adhesive systems.

    Attributes:
    -----------
    flow_rate : float
        The flow rate of nitrogen gas in liters per minute (L/min).
    purity : float
        The purity of nitrogen gas as a percentage (%).
    pressure : float
        The pressure of nitrogen gas in pounds per square inch (PSI).

    Methods:
    --------
    generate_nitrogen()
        Generates nitrogen gas based on the provided settings.
    adjust_flow_rate(new_flow_rate)
        Adjusts the flow rate of nitrogen gas.
    adjust_purity(new_purity)
        Adjusts the purity of nitrogen gas.
    adjust_pressure(new_pressure)
        Adjusts the pressure of nitrogen gas.
    """

    def __init__(self, flow_rate=10.0, purity=99.9, pressure=80.0):
        """
        Initializes the nitrogen generation system.

        Args:
        -----
        flow_rate (float, optional): The flow rate of nitrogen gas in L/min. Defaults to 10.0.
        purity (float, optional): The purity of nitrogen gas as a percentage (%). Defaults to 99.9.
        pressure (float, optional): The pressure of nitrogen gas in PSI. Defaults to 80.0.
        """
        self.flow_rate = flow_rate
        self.purity = purity
        self.pressure = pressure

    def generate_nitrogen(self):
        """
        Generates nitrogen gas based on the provided settings.

        Returns:
        -------
        dict
            A dictionary containing the generated nitrogen gas settings.

        Raises:
        ------
        ValueError
            If the flow rate, purity, or pressure is outside the valid range.
        """
        if not (0.0 <= self.flow_rate <= 20.0):
            raise ValueError("Flow rate must be between 0.0 and 20.0 L/min")
        if not (90.0 <= self.purity <= 100.0):
            raise ValueError("Purity must be between 90.0 and 100.0 %")
        if not (0.0 <= self.pressure <= 100.0):
            raise ValueError("Pressure must be between 0.0 and 100.0 PSI")

        # Simulate nitrogen generation
        nitrogen_settings = {
            "flow_rate": self.flow_rate,
            "purity": self.purity,
            "pressure": self.pressure,
        }
        return nitrogen_settings

    def adjust_flow_rate(self, new_flow_rate):
        """
        Adjusts the flow rate of nitrogen gas.

        Args:
        -----
        new_flow_rate (float): The new flow rate of nitrogen gas in L/min.

        Raises:
        ------
        ValueError
            If the new flow rate is outside the valid range.
        """
        if not (0.0 <= new_flow_rate <= 20.0):
            raise ValueError("Flow rate must be between 0.0 and 20.0 L/min")
        self.flow_rate = new_flow_rate

    def adjust_purity(self, new_purity):
        """
        Adjusts the purity of nitrogen gas.

        Args:
        -----
        new_purity (float): The new purity of nitrogen gas as a percentage (%).

        Raises:
        ------
        ValueError
            If the new purity is outside the valid range.
        """
        if not (90.0 <= new_purity <= 100.0):
            raise ValueError("Purity must be between 90.0 and 100.0 %")
        self.purity = new_purity

    def adjust_pressure(self, new_pressure):
        """
        Adjusts the pressure of nitrogen gas.

        Args:
        -----
        new_pressure (float): The new pressure of nitrogen gas in PSI.

        Raises:
        ------
        ValueError
            If the new pressure is outside the valid range.
        """
        if not (0.0 <= new_pressure <= 100.0):
            raise ValueError("Pressure must be between 0.0 and 100.0 PSI")
        self.pressure = new_pressure


def main():
    try:
        # Create a nitrogen generation system with default settings
        nitrogen_system = NitrogenGenerationSystem()

        # Generate nitrogen gas with default settings
        nitrogen_settings = nitrogen_system.generate_nitrogen()
        print("Generated Nitrogen Settings:")
        print(f"Flow Rate: {nitrogen_settings['flow_rate']} L/min")
        print(f"Purity: {nitrogen_settings['purity']}%")
        print(f"Pressure: {nitrogen_settings['pressure']} PSI")

        # Adjust the flow rate and generate nitrogen gas again
        nitrogen_system.adjust_flow_rate(15.0)
        nitrogen_settings = nitrogen_system.generate_nitrogen()
        print("\nAdjusted Nitrogen Settings:")
        print(f"Flow Rate: {nitrogen_settings['flow_rate']} L/min")
        print(f"Purity: {nitrogen_settings['purity']}%")
        print(f"Pressure: {nitrogen_settings['pressure']} PSI")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
