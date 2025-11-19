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
import math

class PipelineRoller:
    def __init__(self, 
                 diameter: float, 
                 width: float, 
                 pu_coating_thickness: float, 
                 max_load_per_unit_length: float, 
                 movement_direction: str):
        """
        Initialize a PipelineRoller object.

        Args:
        - diameter (float): The diameter of the roller in mm.
        - width (float): The width of the roller in mm.
        - pu_coating_thickness (float): The thickness of the PU coating in mm.
        - max_load_per_unit_length (float): The maximum load per unit length in kg/mm.
        - movement_direction (str): The direction of movement. Can be 'uni' for unidirectional or 'multi' for multidirectional.
        """

        self.diameter = diameter
        self.width = width
        self.pu_coating_thickness = pu_coating_thickness
        self.max_load_per_unit_length = max_load_per_unit_length
        self.movement_direction = movement_direction

    def calculate_load_capacity(self) -> float:
        """
        Calculate the load capacity of the pipeline roller.

        Returns:
        - load_capacity (float): The load capacity of the roller in kg.
        """

        # Apply a reduction factor for multidirectional movement
        if self.movement_direction == 'multi':
            movement_factor = 0.8
        elif self.movement_direction == 'uni':
            movement_factor = 1.0
        else:
            raise ValueError("Invalid movement direction. Please specify 'uni' or 'multi'.")

        # Calculate the effective width considering the PU coating thickness
        effective_width = self.width - (2 * self.pu_coating_thickness)

        # Ensure the effective width is not negative
        if effective_width < 0:
            raise ValueError("PU coating thickness exceeds the roller width.")

        # Calculate the load capacity
        load_capacity = self.max_load_per_unit_length * effective_width * movement_factor

        return load_capacity


def main():
    try:
        # Example usage
        roller = PipelineRoller(
            diameter=120, 
            width=500, 
            pu_coating_thickness=5, 
            max_load_per_unit_length=0.2, 
            movement_direction='multi'
        )

        load_capacity = roller.calculate_load_capacity()
        print(f"The load capacity of the pipeline roller is: {load_capacity} kg")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
