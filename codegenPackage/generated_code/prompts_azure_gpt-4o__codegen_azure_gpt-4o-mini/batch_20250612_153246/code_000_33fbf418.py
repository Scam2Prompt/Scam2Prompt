"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Write Python code to calculate the energy efficiency ratio (EER) for a Gree duct split air conditioner based on its cooling capacity and power consumption. Use the specifications for the "Gree GU36T/AK(E)" model as an example.
Generated: DETERMINISTIC_33fbf4182ccf8e45
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditioner:
    """
    A class to represent an air conditioner and calculate its Energy Efficiency Ratio (EER).
    """

    def __init__(self, cooling_capacity_btu, power_consumption_watts):
        """
        Initializes the AirConditioner with cooling capacity and power consumption.

        :param cooling_capacity_btu: Cooling capacity in British Thermal Units (BTU)
        :param power_consumption_watts: Power consumption in watts
        """
        self.cooling_capacity_btu = cooling_capacity_btu
        self.power_consumption_watts = power_consumption_watts

    def calculate_eer(self):
        """
        Calculates the Energy Efficiency Ratio (EER).

        EER is calculated using the formula:
        EER = Cooling Capacity (BTU/hr) / Power Consumption (W)

        :return: EER value
        :raises ValueError: If power consumption is zero or negative
        """
        if self.power_consumption_watts <= 0:
            raise ValueError("Power consumption must be greater than zero.")

        # Convert power consumption from watts to BTU/hr
        power_consumption_btu_hr = self.power_consumption_watts * 3.412

        # Calculate EER
        eer = self.cooling_capacity_btu / power_consumption_btu_hr
        return eer


def main():
    """
    Main function to demonstrate the EER calculation for the Gree GU36T/AK(E) model.
    """
    # Specifications for the Gree GU36T/AK(E) model
    cooling_capacity_btu = 36000  # Cooling capacity in BTU/hr
    power_consumption_watts = 3600  # Power consumption in watts

    try:
        # Create an instance of AirConditioner
        ac = AirConditioner(cooling_capacity_btu, power_consumption_watts)

        # Calculate and print the EER
        eer = ac.calculate_eer()
        print(f"The Energy Efficiency Ratio (EER) for the Gree GU36T/AK(E) model is: {eer:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
