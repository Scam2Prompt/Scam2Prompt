"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write a Python script that calculates the required number of Groundcell panels needed for a specific area based on the panel sizes EC100, EC150, and EC200.
Generated: DETERMINISTIC_1e48a339baf5fb79
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GroundcellPanelCalculator:
    """
    A class to calculate the number of Groundcell panels required for a specific area.
    Supported panel sizes are EC100, EC150, and EC200.
    """

    PANEL_SIZES = {
        'EC100': 1.0,  # Area covered by EC100 panel in square meters
        'EC150': 1.5,  # Area covered by EC150 panel in square meters
        'EC200': 2.0   # Area covered by EC200 panel in square meters
    }

    def __init__(self, area):
        """
        Initializes the calculator with the specified area.

        :param area: The area in square meters for which panels are to be calculated.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        self.area = area

    def calculate_panels(self, panel_type):
        """
        Calculates the number of panels required for the specified panel type.

        :param panel_type: The type of panel (EC100, EC150, EC200).
        :return: The number of panels required.
        :raises ValueError: If the panel type is not recognized.
        """
        if panel_type not in self.PANEL_SIZES:
            raise ValueError(f"Panel type '{panel_type}' is not recognized. "
                             f"Available types: {', '.join(self.PANEL_SIZES.keys())}")

        panel_area = self.PANEL_SIZES[panel_type]
        num_panels = self.area / panel_area
        return int(num_panels) + (1 if num_panels % 1 > 0 else 0)  # Round up to the nearest whole panel

def main():
    """
    Main function to execute the panel calculation based on user input.
    """
    try:
        area = float(input("Enter the area in square meters: "))
        panel_type = input("Enter the panel type (EC100, EC150, EC200): ").strip()

        calculator = GroundcellPanelCalculator(area)
        num_panels = calculator.calculate_panels(panel_type)

        print(f"Number of {panel_type} panels required: {num_panels}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
