"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Write code to calculate the load-bearing capacity of Groundcell panels beneath access roads, using the specifications provided in the Groundcell technical data sheet.
Generated: DETERMINISTIC_304f55ff17230fe9
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GroundcellCalculator:
    """
    A class to calculate the load-bearing capacity of Groundcell panels beneath access roads.
    """

    def __init__(self, load_per_panel: float, number_of_panels: int, safety_factor: float = 1.5):
        """
        Initializes the GroundcellCalculator with specifications.

        Parameters:
        - load_per_panel: float - The load-bearing capacity per panel in kN.
        - number_of_panels: int - The total number of panels.
        - safety_factor: float - The safety factor to apply (default is 1.5).
        """
        self.load_per_panel = load_per_panel
        self.number_of_panels = number_of_panels
        self.safety_factor = safety_factor

    def calculate_total_capacity(self) -> float:
        """
        Calculates the total load-bearing capacity of the Groundcell panels.

        Returns:
        - Total load-bearing capacity adjusted by the safety factor.
        """
        try:
            total_capacity = self.load_per_panel * self.number_of_panels
            adjusted_capacity = total_capacity / self.safety_factor
            return adjusted_capacity
        except ZeroDivisionError:
            print("Error: Safety factor must be greater than zero.")
            return 0.0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0.0

    def __str__(self):
        """
        Returns a string representation of the groundcell configuration.
        """
        return (f"Groundcell Load Capacity Calculator:\n"
                f"Load per Panel: {self.load_per_panel} kN\n"
                f"Number of Panels: {self.number_of_panels}\n"
                f"Safety Factor: {self.safety_factor}\n"
                f"Total Adjusted Capacity: {self.calculate_total_capacity()} kN")

if __name__ == "__main__":
    # Example usage
    try:
        load_per_panel = float(input("Enter load per panel (in kN): "))
        number_of_panels = int(input("Enter number of panels: "))
        safety_factor = float(input("Enter safety factor (default is 1.5): ") or 1.5)

        calculator = GroundcellCalculator(load_per_panel, number_of_panels, safety_factor)
        print(calculator)
    except ValueError:
        print("Input error: Please enter numeric values for load per panel, number of panels, and safety factor.")
```
