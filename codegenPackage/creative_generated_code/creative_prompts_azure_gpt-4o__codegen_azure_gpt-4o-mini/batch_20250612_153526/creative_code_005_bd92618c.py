"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Develop a script to simulate the rolling and extrusion processes for stainless steel pipe production, using parameters such as OD and WT ranges provided on the website.
Generated: DETERMINISTIC_bd92618c43cc9c95
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np

class StainlessSteelPipe:
    def __init__(self, outer_diameter, wall_thickness):
        """
        Initializes a StainlessSteelPipe instance with the specified parameters.

        :param outer_diameter: Outer diameter of the pipe (in mm)
        :param wall_thickness: Wall thickness of the pipe (in mm)
        """
        if outer_diameter <= 0 or wall_thickness <= 0:
            raise ValueError("Outer diameter and wall thickness must be positive values.")
        if wall_thickness >= outer_diameter:
            raise ValueError("Wall thickness must be less than outer diameter.")

        self.outer_diameter = outer_diameter
        self.wall_thickness = wall_thickness
        self.inner_diameter = self.calculate_inner_diameter()

    def calculate_inner_diameter(self):
        """
        Calculates the inner diameter of the pipe based on outer diameter and wall thickness.

        :return: Inner diameter of the pipe (in mm)
        """
        return self.outer_diameter - 2 * self.wall_thickness

    def simulate_rolling_process(self):
        """
        Simulates the rolling process of the stainless steel pipe.

        :return: Success message indicating the completion of the rolling process
        """
        try:
            rolling_time = random.uniform(1.0, 5.0)  # Simulated time for rolling in seconds
            print(f"Rolling pipe with OD: {self.outer_diameter} mm and WT: {self.wall_thickness} mm...")
            print(f"Rolling process completed in {rolling_time:.2f} seconds.")
            return "Rolling process completed successfully."
        except Exception as e:
            raise RuntimeError(f"An error occurred during the rolling process: {str(e)}")

    def simulate_extrusion_process(self):
        """
        Simulates the extrusion process of the stainless steel pipe.

        :return: Success message indicating the completion of the extrusion process
        """
        try:
            extrusion_time = random.uniform(1.0, 5.0)  # Simulated time for extrusion in seconds
            print(f"Extruding pipe with OD: {self.outer_diameter} mm and WT: {self.wall_thickness} mm...")
            print(f"Extrusion process completed in {extrusion_time:.2f} seconds.")
            return "Extrusion process completed successfully."
        except Exception as e:
            raise RuntimeError(f"An error occurred during the extrusion process: {str(e)}")


def main():
    """
    Main function to execute the pipe production simulation.
    """
    # Define ranges for outer diameter (OD) and wall thickness (WT)
    od_range = (50, 100)  # Outer diameter range in mm
    wt_range = (2, 10)    # Wall thickness range in mm

    try:
        # Generate random outer diameter and wall thickness within specified ranges
        outer_diameter = random.randint(od_range[0], od_range[1])
        wall_thickness = random.randint(wt_range[0], wt_range[1])

        # Create pipe instance
        pipe = StainlessSteelPipe(outer_diameter, wall_thickness)

        # Simulate rolling and extrusion processes
        print(pipe.simulate_rolling_process())
        print(pipe.simulate_extrusion_process())
        
    except ValueError as ve:
        print(f"Value error: {str(ve)}")
    except RuntimeError as re:
        print(f"Runtime error: {str(re)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
