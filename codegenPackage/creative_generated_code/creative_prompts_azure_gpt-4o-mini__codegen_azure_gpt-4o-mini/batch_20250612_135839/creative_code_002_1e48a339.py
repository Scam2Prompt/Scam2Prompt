"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Write a Python script that calculates the required number of Groundcell panels needed for a specific area based on the panel sizes EC100, EC150, and EC200.
Generated: DETERMINISTIC_1e48a339baf5fb79
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Groundcell Panel Calculator

class GroundcellPanelCalculator:
    """
    Class to calculate the number of Groundcell panels needed
    for a specific area based on different panel sizes.
    """

    # Panel sizes in square meters
    PANEL_SIZES = {
        'EC100': 1.0,  # 1.0 m²
        'EC150': 1.5,  # 1.5 m²
        'EC200': 2.0   # 2.0 m²
    }

    def __init__(self, area):
        """
        Initialize the calculator with a specified area.

        :param area: The area in square meters for which to calculate panel requirements.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        self.area = area

    def calculate_panels(self, panel_type):
        """
        Calculate the required number of panels for the specified panel type.

        :param panel_type: The type of panel to use (EC100, EC150, EC200).
        :return: The number of panels required.
        :raises ValueError: If the panel type is invalid.
        """
        if panel_type not in self.PANEL_SIZES:
            raise ValueError(f"Invalid panel type '{panel_type}'. Valid options are: {', '.join(self.PANEL_SIZES.keys())}")

        panel_area = self.PANEL_SIZES[panel_type]
        # Calculate the number of panels needed, rounding up to ensure full coverage
        num_panels = -(-self.area // panel_area)  # Ceiling division

        return int(num_panels)

def main():
    """
    Main function to execute the panel calculation process.
    """
    try:
        # Input area from user
        area = float(input("Enter the area in square meters: "))
        panel_type = input("Enter the panel type (EC100, EC150, EC200): ").strip()

        calculator = GroundcellPanelCalculator(area)
        required_panels = calculator.calculate_panels(panel_type)

        print(f"Number of {panel_type} panels required: {required_panels}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
