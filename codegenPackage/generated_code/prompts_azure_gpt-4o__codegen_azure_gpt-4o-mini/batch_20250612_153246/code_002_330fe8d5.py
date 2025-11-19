"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Generate code to calculate the load capacity of heavy-duty pipeline rollers, incorporating parameters like PU coating and multidirectional movement as mentioned on the SPM Equipment site.
Generated: DETERMINISTIC_330fe8d5fff6e391
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PipelineRoller:
    """
    A class to represent a heavy-duty pipeline roller and calculate its load capacity.
    """

    def __init__(self, diameter: float, width: float, pu_coating_thickness: float, 
                 num_rollers: int, is_multidirectional: bool):
        """
        Initializes the PipelineRoller with the given parameters.

        :param diameter: Diameter of the roller in meters.
        :param width: Width of the roller in meters.
        :param pu_coating_thickness: Thickness of the PU coating in meters.
        :param num_rollers: Number of rollers in the system.
        :param is_multidirectional: Boolean indicating if the roller can move in multiple directions.
        """
        self.diameter = diameter
        self.width = width
        self.pu_coating_thickness = pu_coating_thickness
        self.num_rollers = num_rollers
        self.is_multidirectional = is_multidirectional

    def calculate_load_capacity(self) -> float:
        """
        Calculates the load capacity of the pipeline roller based on its dimensions and properties.

        :return: Load capacity in kilograms.
        :raises ValueError: If any of the parameters are invalid (negative or zero).
        """
        # Validate parameters
        if self.diameter <= 0 or self.width <= 0 or self.pu_coating_thickness < 0 or self.num_rollers <= 0:
            raise ValueError("All dimensions must be positive and num_rollers must be greater than zero.")

        # Base load capacity calculation (simplified for demonstration)
        base_capacity = (self.diameter * self.width * 1000)  # in kg, assuming a base factor
        coating_factor = 1 + (self.pu_coating_thickness * 10)  # Adjusting capacity based on coating thickness
        direction_factor = 1.2 if self.is_multidirectional else 1.0  # Multidirectional movement increases capacity

        # Total load capacity
        total_capacity = base_capacity * coating_factor * direction_factor * self.num_rollers
        return total_capacity

def main():
    """
    Main function to demonstrate the usage of the PipelineRoller class.
    """
    try:
        # Example parameters for the pipeline roller
        roller = PipelineRoller(diameter=0.5, width=0.3, pu_coating_thickness=0.01, 
                                num_rollers=4, is_multidirectional=True)

        # Calculate and print the load capacity
        load_capacity = roller.calculate_load_capacity()
        print(f"Load Capacity of the Pipeline Roller: {load_capacity:.2f} kg")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
