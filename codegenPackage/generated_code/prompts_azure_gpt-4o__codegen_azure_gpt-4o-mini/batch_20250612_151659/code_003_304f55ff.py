"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write code to calculate the load-bearing capacity of Groundcell panels beneath access roads, using the specifications provided in the Groundcell technical data sheet.
Generated: DETERMINISTIC_304f55ff17230fe9
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Groundcell:
    """
    A class to represent a Groundcell panel and calculate its load-bearing capacity.
    """

    def __init__(self, panel_area: float, compressive_strength: float, safety_factor: float = 1.5):
        """
        Initializes the Groundcell panel with its area and compressive strength.

        :param panel_area: Area of the Groundcell panel in square meters.
        :param compressive_strength: Compressive strength of the material in Pascals (Pa).
        :param safety_factor: Safety factor to apply to the load-bearing capacity (default is 1.5).
        """
        if panel_area <= 0:
            raise ValueError("Panel area must be greater than zero.")
        if compressive_strength <= 0:
            raise ValueError("Compressive strength must be greater than zero.")
        if safety_factor <= 0:
            raise ValueError("Safety factor must be greater than zero.")

        self.panel_area = panel_area
        self.compressive_strength = compressive_strength
        self.safety_factor = safety_factor

    def calculate_load_bearing_capacity(self) -> float:
        """
        Calculates the load-bearing capacity of the Groundcell panel.

        :return: Load-bearing capacity in Newtons (N).
        """
        # Calculate the maximum load without safety factor
        max_load = self.panel_area * self.compressive_strength
        
        # Apply the safety factor
        load_bearing_capacity = max_load / self.safety_factor
        
        return load_bearing_capacity

def main():
    """
    Main function to demonstrate the load-bearing capacity calculation.
    """
    try:
        # Example specifications for Groundcell panels
        panel_area = 1.0  # in square meters
        compressive_strength = 20000000  # in Pascals (20 MPa)

        # Create a Groundcell instance
        groundcell_panel = Groundcell(panel_area, compressive_strength)

        # Calculate and print the load-bearing capacity
        capacity = groundcell_panel.calculate_load_bearing_capacity()
        print(f"Load-bearing capacity of the Groundcell panel: {capacity:.2f} N")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
