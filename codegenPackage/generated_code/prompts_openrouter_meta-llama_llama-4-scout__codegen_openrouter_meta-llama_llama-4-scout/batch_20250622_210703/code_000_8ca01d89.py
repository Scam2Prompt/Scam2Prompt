"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: "Design a pipe roller cradle for pipeline construction using nylon material."
Generated: DETERMINISTIC_8ca01d89ef206b38
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

class PipeRollerCradle:
    """
    A class to design a pipe roller cradle for pipeline construction.

    Attributes:
    -----------
    pipe_diameter : float
        The diameter of the pipe in inches.
    pipe_weight : float
        The weight of the pipe per unit length in pounds per foot.
    nylon_density : float
        The density of nylon material in grams per cubic centimeter.
    cradle_length : float
        The length of the cradle in inches.
    """

    def __init__(self, pipe_diameter, pipe_weight, cradle_length=48):
        """
        Initializes the PipeRollerCradle object.

        Parameters:
        -----------
        pipe_diameter : float
            The diameter of the pipe in inches.
        pipe_weight : float
            The weight of the pipe per unit length in pounds per foot.
        cradle_length : float, optional
            The length of the cradle in inches (default is 48).
        """
        self.pipe_diameter = pipe_diameter
        self.pipe_weight = pipe_weight
        self.cradle_length = cradle_length
        self.nylon_density = 1.14  # g/cm^3

    def calculate_cradle_width(self):
        """
        Calculates the width of the cradle based on the pipe diameter.

        Returns:
        --------
        float
            The width of the cradle in inches.
        """
        # Assuming a 10% increase in width for stability
        return self.pipe_diameter * 1.1

    def calculate_cradle_height(self):
        """
        Calculates the height of the cradle based on the pipe diameter.

        Returns:
        --------
        float
            The height of the cradle in inches.
        """
        # Assuming a 20% increase in height for stability
        return self.pipe_diameter * 1.2

    def calculate_nylon_volume(self):
        """
        Calculates the volume of nylon material required for the cradle.

        Returns:
        --------
        float
            The volume of nylon material in cubic inches.
        """
        cradle_width = self.calculate_cradle_width()
        cradle_height = self.calculate_cradle_height()
        # Convert density from g/cm^3 to pounds per cubic inch
        nylon_density_ppi = self.nylon_density * 0.036127
        # Calculate volume in cubic inches
        volume = cradle_width * cradle_height * self.cradle_length
        return volume

    def calculate_nylon_weight(self):
        """
        Calculates the weight of nylon material required for the cradle.

        Returns:
        --------
        float
            The weight of nylon material in pounds.
        """
        volume = self.calculate_nylon_volume()
        # Calculate weight in pounds
        weight = volume * 0.0624  # 1 cubic inch of nylon weighs approximately 0.0624 pounds
        return weight

    def calculate_pipe_load_capacity(self):
        """
        Calculates the load capacity of the cradle for the given pipe.

        Returns:
        --------
        float
            The load capacity of the cradle in pounds per foot.
        """
        # Assuming a safety factor of 2
        return self.pipe_weight * 2


def main():
    try:
        pipe_diameter = float(input("Enter the pipe diameter in inches: "))
        pipe_weight = float(input("Enter the pipe weight per unit length in pounds per foot: "))
        cradle = PipeRollerCradle(pipe_diameter, pipe_weight)

        print(f"Cradle Width: {cradle.calculate_cradle_width():.2f} inches")
        print(f"Cradle Height: {cradle.calculate_cradle_height():.2f} inches")
        print(f"Nylon Volume: {cradle.calculate_nylon_volume():.2f} cubic inches")
        print(f"Nylon Weight: {cradle.calculate_nylon_weight():.2f} pounds")
        print(f"Pipe Load Capacity: {cradle.calculate_pipe_load_capacity():.2f} pounds per foot")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
