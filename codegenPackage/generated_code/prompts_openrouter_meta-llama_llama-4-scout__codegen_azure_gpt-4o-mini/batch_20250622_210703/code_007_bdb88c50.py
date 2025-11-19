"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Provide a recommendation for a suitable power supply unit for a CCTV camera system with multiple cameras and accessories.
Generated: DETERMINISTIC_bdb88c50c1fb564e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PowerSupplyUnit:
    """
    A class to represent a power supply unit for a CCTV camera system.
    
    Attributes:
        voltage (float): The voltage output of the power supply unit.
        current (float): The current output of the power supply unit.
        total_power (float): The total power output in watts.
        camera_count (int): The number of cameras to be powered.
        accessories_count (int): The number of accessories to be powered.
    """

    def __init__(self, voltage: float, current: float):
        """
        Initializes the PowerSupplyUnit with voltage and current.

        Args:
            voltage (float): The voltage output of the power supply unit.
            current (float): The current output of the power supply unit.
        """
        self.voltage = voltage
        self.current = current
        self.total_power = self.calculate_total_power()

    def calculate_total_power(self) -> float:
        """
        Calculates the total power output in watts.

        Returns:
            float: The total power output in watts.
        """
        return self.voltage * self.current

    def recommend_power_supply(self, camera_power: float, accessory_power: float, camera_count: int, accessories_count: int) -> str:
        """
        Recommends a suitable power supply unit based on the power requirements of cameras and accessories.

        Args:
            camera_power (float): The power consumption of a single camera in watts.
            accessory_power (float): The power consumption of a single accessory in watts.
            camera_count (int): The number of cameras.
            accessories_count (int): The number of accessories.

        Returns:
            str: A recommendation message for the power supply unit.
        """
        total_camera_power = camera_power * camera_count
        total_accessory_power = accessory_power * accessories_count
        total_required_power = total_camera_power + total_accessory_power

        if total_required_power > self.total_power:
            return f"Insufficient power supply! Required: {total_required_power}W, Available: {self.total_power}W."
        else:
            return f"Sufficient power supply! Required: {total_required_power}W, Available: {self.total_power}W."

# Example usage
if __name__ == "__main__":
    try:
        # Create a power supply unit with 12V and 5A
        psu = PowerSupplyUnit(voltage=12.0, current=5.0)

        # Define power consumption for cameras and accessories
        camera_power = 2.0  # Power consumption per camera in watts
        accessory_power = 1.0  # Power consumption per accessory in watts
        camera_count = 4  # Number of cameras
        accessories_count = 2  # Number of accessories

        # Get recommendation for the power supply unit
        recommendation = psu.recommend_power_supply(camera_power, accessory_power, camera_count, accessories_count)
        print(recommendation)

    except Exception as e:
        print(f"An error occurred: {e}")
```
