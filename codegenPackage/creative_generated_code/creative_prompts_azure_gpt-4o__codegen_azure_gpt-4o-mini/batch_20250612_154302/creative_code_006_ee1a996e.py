"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbxtools.in
Prompt: Develop a script to calculate the optimal settings for tube end facing using the TEF FA Series tools described on the DBX Tools website.
Generated: DETERMINISTIC_ee1a996e1a365289
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class TubeEndFacingCalculator:
    """
    A class to calculate optimal settings for tube end facing using TEF FA Series tools.
    """

    def __init__(self, tube_diameter, material_hardness, tool_type):
        """
        Initialize the calculator with required parameters.

        :param tube_diameter: Diameter of the tube (in mm)
        :param material_hardness: Hardness of the material (in Rockwell scale)
        :param tool_type: Type of TEF tool being used
        """
        self.tube_diameter = tube_diameter
        self.material_hardness = material_hardness
        self.tool_type = tool_type
        self.settings = {}

    def validate_inputs(self):
        """
        Validate the input parameters to ensure they are within acceptable ranges.

        :raises ValueError: If any input parameter is invalid
        """
        if not (10 <= self.tube_diameter <= 200):
            raise ValueError("Tube diameter must be between 10 and 200 mm.")
        if not (20 <= self.material_hardness <= 60):
            raise ValueError("Material hardness must be between 20 and 60 on the Rockwell scale.")
        if self.tool_type not in ['standard', 'premium']:
            raise ValueError("Tool type must be either 'standard' or 'premium'.")

    def calculate_feed_rate(self):
        """
        Calculate the optimal feed rate based on tube diameter and material hardness.

        :return: Optimal feed rate (in mm/min)
        """
        base_feed_rate = 100  # mm/min
        hardness_factor = (self.material_hardness - 20) / 40  # Normalize hardness
        diameter_factor = self.tube_diameter / 200  # Normalize diameter
        feed_rate = base_feed_rate * (1 - hardness_factor) * (1 - diameter_factor)
        return max(10, feed_rate)  # Ensure a minimum feed rate of 10 mm/min

    def calculate_rpm(self):
        """
        Calculate the optimal RPM based on tube diameter and tool type.

        :return: Optimal RPM
        """
        base_rpm = 2000  # base RPM
        if self.tool_type == 'premium':
            rpm_adjustment = 1.2  # Higher RPM for premium tools
        else:
            rpm_adjustment = 1.0  # Standard adjustment for standard tools
        return int(base_rpm * (self.tube_diameter / 100) * rpm_adjustment)

    def optimize_settings(self):
        """
        Calculate and store optimal settings for tube end facing.
        """
        try:
            self.validate_inputs()
            self.settings['feed_rate'] = self.calculate_feed_rate()
            self.settings['rpm'] = self.calculate_rpm()
        except ValueError as e:
            print(f"Input Error: {e}")
            return None

    def get_settings(self):
        """
        Return the calculated settings.

        :return: Dictionary containing optimal feed rate and RPM
        """
        return self.settings

if __name__ == "__main__":
    # Example usage
    try:
        # Instantiate the calculator with tube specifications
        calculator = TubeEndFacingCalculator(tube_diameter=100, material_hardness=30, tool_type='standard')
        calculator.optimize_settings()
        settings = calculator.get_settings()
        print(f"Optimal Feed Rate: {settings['feed_rate']} mm/min")
        print(f"Optimal RPM: {settings['rpm']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
