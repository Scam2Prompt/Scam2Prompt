"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Generate code to design a perforated stainless steel sheet pattern, incorporating specifications similar to the "Perfore Sac" products listed on Hilde Inox.
Generated: DETERMINISTIC_de743268ad50f330
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

class PerforatedSheet:
    def __init__(self, sheet_length, sheet_width, hole_diameter, hole_spacing):
        """
        Initializes the PerforatedSheet object with dimensions and hole specifications.

        Parameters:
        sheet_length (float): Length of the sheet in millimeters.
        sheet_width (float): Width of the sheet in millimeters.
        hole_diameter (float): Diameter of the holes in millimeters.
        hole_spacing (float): Distance between the centers of adjacent holes in millimeters.
        """
        self.sheet_length = sheet_length
        self.sheet_width = sheet_width
        self.hole_diameter = hole_diameter
        self.hole_spacing = hole_spacing

        # Validate inputs
        self._validate_inputs()

    def _validate_inputs(self):
        """Validates the input parameters to ensure they are positive values."""
        if self.sheet_length <= 0 or self.sheet_width <= 0:
            raise ValueError("Sheet dimensions must be positive values.")
        if self.hole_diameter <= 0 or self.hole_spacing <= 0:
            raise ValueError("Hole diameter and spacing must be positive values.")

    def generate_pattern(self):
        """Generates the coordinates for the perforated sheet pattern."""
        # Calculate number of holes in each dimension
        num_holes_x = int(self.sheet_length // self.hole_spacing)
        num_holes_y = int(self.sheet_width // self.hole_spacing)

        # Create arrays for hole positions
        x_positions = np.linspace(self.hole_spacing / 2, self.sheet_length - self.hole_spacing / 2, num_holes_x)
        y_positions = np.linspace(self.hole_spacing / 2, self.sheet_width - self.hole_spacing / 2, num_holes_y)

        # Create meshgrid for hole positions
        x_grid, y_grid = np.meshgrid(x_positions, y_positions)

        return x_grid.flatten(), y_grid.flatten()

    def plot_pattern(self):
        """Plots the perforated sheet pattern using matplotlib."""
        try:
            x_coords, y_coords = self.generate_pattern()

            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(10, 6))

            # Plot holes
            for x, y in zip(x_coords, y_coords):
                circle = plt.Circle((x, y), self.hole_diameter / 2, color='black')
                ax.add_artist(circle)

            # Set the limits and aspect of the plot
            ax.set_xlim(0, self.sheet_length)
            ax.set_ylim(0, self.sheet_width)
            ax.set_aspect('equal', adjustable='box')

            # Set grid and labels
            plt.grid(False)
            plt.title('Perforated Stainless Steel Sheet Pattern')
            plt.xlabel('Sheet Length (mm)')
            plt.ylabel('Sheet Width (mm)')
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting the pattern: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Define specifications for the perforated sheet
        sheet_length = 1000  # Length in mm
        sheet_width = 500     # Width in mm
        hole_diameter = 10    # Hole diameter in mm
        hole_spacing = 20     # Spacing between holes in mm

        # Create a perforated sheet object
        perforated_sheet = PerforatedSheet(sheet_length, sheet_width, hole_diameter, hole_spacing)

        # Plot the perforated pattern
        perforated_sheet.plot_pattern()
    except Exception as e:
        print(f"An error occurred while creating the perforated sheet: {e}")
```
