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
import math

class CCTVPowerSupplyCalculator:
    """
    A class to calculate and recommend a suitable power supply unit (PSU) for a CCTV camera system.
    """

    def __init__(self, camera_power, num_cameras, accessory_power, num_accessories, safety_margin=0.2):
        """
        Initialize the calculator with system specifications.

        :param camera_power: Power consumption of a single camera in watts (W).
        :param num_cameras: Number of cameras in the system.
        :param accessory_power: Power consumption of a single accessory in watts (W).
        :param num_accessories: Number of accessories in the system.
        :param safety_margin: Safety margin as a percentage (default is 20%).
        """
        self.camera_power = camera_power
        self.num_cameras = num_cameras
        self.accessory_power = accessory_power
        self.num_accessories = num_accessories
        self.safety_margin = safety_margin

    def calculate_total_power(self):
        """
        Calculate the total power requirement for the system.

        :return: Total power requirement in watts (W).
        """
        try:
            # Calculate power for cameras and accessories
            total_camera_power = self.camera_power * self.num_cameras
            total_accessory_power = self.accessory_power * self.num_accessories

            # Calculate total power with safety margin
            total_power = total_camera_power + total_accessory_power
            total_power_with_margin = total_power * (1 + self.safety_margin)

            return math.ceil(total_power_with_margin)  # Round up to the nearest whole number
        except Exception as e:
            raise ValueError(f"Error calculating total power: {e}")

    def recommend_psu(self):
        """
        Recommend a suitable power supply unit (PSU) based on the total power requirement.

        :return: Recommended PSU wattage in watts (W).
        """
        try:
            total_power = self.calculate_total_power()

            # Recommend a PSU with a wattage slightly higher than the calculated requirement
            recommended_psu = math.ceil(total_power / 10) * 10  # Round up to the nearest 10W
            return recommended_psu
        except Exception as e:
            raise ValueError(f"Error recommending PSU: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Define system specifications
        camera_power = 5  # Power consumption of a single camera in watts
        num_cameras = 8   # Number of cameras
        accessory_power = 2  # Power consumption of a single accessory in watts
        num_accessories = 4  # Number of accessories

        # Create an instance of the calculator
        calculator = CCTVPowerSupplyCalculator(camera_power, num_cameras, accessory_power, num_accessories)

        # Calculate total power and recommend PSU
        total_power = calculator.calculate_total_power()
        recommended_psu = calculator.recommend_psu()

        # Display results
        print(f"Total Power Requirement: {total_power}W")
        print(f"Recommended PSU Wattage: {recommended_psu}W")
    except Exception as e:
        print(f"An error occurred: {e}")
```
