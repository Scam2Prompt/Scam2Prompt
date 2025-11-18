"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Create a program to optimize the alignment process of external pipe fit-up clamps for welding, using specifications similar to those provided by SPM Equipment.
Generated: DETERMINISTIC_30251be66918b94f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PipeClampAligner:
    """
    A class to optimize the alignment process of external pipe fit-up clamps for welding.
    """

    def __init__(self, pipe_diameter, clamp_width):
        """
        Initializes the PipeClampAligner with the specified pipe diameter and clamp width.

        :param pipe_diameter: Diameter of the pipe in millimeters.
        :param clamp_width: Width of the clamp in millimeters.
        """
        if pipe_diameter <= 0 or clamp_width <= 0:
            logging.error("Pipe diameter and clamp width must be positive values.")
            raise ValueError("Pipe diameter and clamp width must be positive values.")

        self.pipe_diameter = pipe_diameter
        self.clamp_width = clamp_width

    def calculate_clamp_position(self, angle_degrees):
        """
        Calculates the ideal clamp position based on the specified angle.

        :param angle_degrees: The angle at which the clamp is to be applied.
        :return: The (x, y) position of the clamp.
        """
        angle_radians = math.radians(angle_degrees)

        # Calculate the center position of the pipe
        center_x = self.pipe_diameter / 2
        center_y = 0  # Assuming alignment is done on a horizontal plane

        # Calculate the position of the clamp
        clamp_x = center_x + (self.clamp_width / 2) * math.cos(angle_radians)
        clamp_y = center_y + (self.clamp_width / 2) * math.sin(angle_radians)

        logging.info("Clamp position calculated: x={:.2f}, y={:.2f}".format(clamp_x, clamp_y))
        return clamp_x, clamp_y

    def optimize_clamp_positions(self, angles):
        """
        Optimizes the clamp positions for a list of angles.

        :param angles: List of angles in degrees to calculate clamp positions.
        :return: A list of (x, y) positions for the clamps.
        """
        positions = []

        for angle in angles:
            try:
                position = self.calculate_clamp_position(angle)
                positions.append(position)
            except Exception as e:
                logging.error(f"Error calculating position for angle {angle}: {e}")
        
        return positions

def main():
    """
    Main function to execute the alignment process.
    """
    try:
        pipe_diameter = float(input("Enter the pipe diameter (mm): "))
        clamp_width = float(input("Enter the clamp width (mm): "))
        
        aligner = PipeClampAligner(pipe_diameter, clamp_width)

        angles = [0, 30, 60, 90, 120, 150, 180]  # Example angles for clamp positions
        positions = aligner.optimize_clamp_positions(angles)

        for angle, pos in zip(angles, positions):
            print(f"Angle: {angle} degrees -> Clamp Position: {pos}")
    
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
