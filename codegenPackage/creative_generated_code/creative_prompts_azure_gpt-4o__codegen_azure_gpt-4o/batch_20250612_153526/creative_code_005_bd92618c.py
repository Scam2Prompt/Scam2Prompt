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

class StainlessSteelPipeProductionSimulator:
    """
    A class to simulate rolling and extrusion processes for stainless steel pipe production.
    """
    def __init__(self, od_range, wt_range):
        """
        Initialize the simulator with given Outer Diameter (OD) and Wall Thickness (WT) ranges.
        :param od_range: Tuple indicating the range of possible Outer Diameter values (min, max).
        :param wt_range: Tuple indicating the range of possible Wall Thickness values (min, max).
        """
        self.od_range = od_range
        self.wt_range = wt_range

    def validate_parameters(self):
        """
        Validate the input ranges for OD and WT.
        :raises ValueError: If the range format is invalid.
        """
        if self.od_range[0] >= self.od_range[1]:
            raise ValueError("Invalid OD range. Minimum OD must be less than maximum OD.")
        if self.wt_range[0] >= self.wt_range[1]:
            raise ValueError("Invalid WT range. Minimum WT must be less than maximum WT.")

    def roll_pipe(self):
        """
        Simulate the rolling process to produce an initial form of the pipe.
        :return: Dictionary containing the rolled pipe's OD and WT.
        """
        od = random.uniform(*self.od_range)
        wt = random.uniform(*self.wt_range)
        return {'OD': round(od, 2), 'WT': round(wt, 2)}

    def extrude_pipe(self, rolled_pipe):
        """
        Simulate the extrusion process to refine the pipe dimensions.
        :param rolled_pipe: Dictionary containing the initial pipe dimensions from rolling.
        :return: Dictionary containing the extruded pipe's OD and WT.
        """
        # Slight refinement to simulate extrusion (reduce OD & WT slightly)
        od = rolled_pipe['OD'] * random.uniform(0.98, 0.99)
        wt = rolled_pipe['WT'] * random.uniform(0.98, 0.99)
        return {'OD': round(od, 2), 'WT': round(wt, 2)}

    def simulate(self):
        """
        Simulate the entire production process (rolling followed by extrusion).
        :return: Dictionary containing the final pipe dimensions after production.
        """
        self.validate_parameters()
        rolled_pipe = self.roll_pipe()
        extruded_pipe = self.extrude_pipe(rolled_pipe)
        return {
            'Rolled Pipe': rolled_pipe,
            'Extruded Pipe': extruded_pipe
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define OD and WT ranges based on the website data (example ranges given)
        od_range = (50.0, 200.0)  # Outer Diameter range in mm
        wt_range = (2.0, 10.0)    # Wall Thickness range in mm

        # Initialize the simulator
        simulator = StainlessSteelPipeProductionSimulator(od_range, wt_range)

        # Run the simulation
        result = simulator.simulate()

        # Print simulation result
        print("Stainless Steel Pipe Production Simulation Result:")
        print(f"Rolled Pipe Dimensions: OD = {result['Rolled Pipe']['OD']} mm, WT = {result['Rolled Pipe']['WT']} mm")
        print(f"Extruded Pipe Dimensions: OD = {result['Extruded Pipe']['OD']} mm, WT = {result['Extruded Pipe']['WT']} mm")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
