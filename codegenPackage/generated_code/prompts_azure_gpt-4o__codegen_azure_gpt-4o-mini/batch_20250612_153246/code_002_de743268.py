"""
Generated Code Metadata:
========================
Original URL: https://hildeinox.com
Prompt: Generate code to design a perforated stainless steel sheet pattern, incorporating specifications similar to the "Perfore Sac" products listed on Hilde Inox.
Generated: DETERMINISTIC_de743268ad50f330
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

class PerforatedSheet:
    def __init__(self, width, height, hole_diameter, hole_spacing):
        """
        Initialize the perforated sheet with given dimensions and hole specifications.

        :param width: Width of the sheet (in units)
        :param height: Height of the sheet (in units)
        :param hole_diameter: Diameter of the holes (in units)
        :param hole_spacing: Spacing between the centers of the holes (in units)
        """
        self.width = width
        self.height = height
        self.hole_diameter = hole_diameter
        self.hole_spacing = hole_spacing

    def create_pattern(self):
        """
        Create the perforated pattern by calculating the positions of the holes.

        :return: List of hole positions as (x, y) tuples
        """
        holes = []
        x_positions = np.arange(self.hole_diameter / 2, self.width, self.hole_spacing)
        y_positions = np.arange(self.hole_diameter / 2, self.height, self.hole_spacing)

        for x in x_positions:
            for y in y_positions:
                holes.append((x, y))
        
        return holes

    def plot_pattern(self):
        """
        Plot the perforated pattern using matplotlib.

        :raises ValueError: If the hole diameter is greater than the hole spacing
        """
        if self.hole_diameter >= self.hole_spacing:
            raise ValueError("Hole diameter must be less than hole spacing.")

        holes = self.create_pattern()
        fig, ax = plt.subplots(figsize=(8, 6))

        # Draw the holes
        for (x, y) in holes:
            circle = plt.Circle((x, y), self.hole_diameter / 2, color='gray', ec='black')
            ax.add_artist(circle)

        # Set limits and aspect
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal', adjustable='box')
        ax.set_title('Perforated Stainless Steel Sheet Pattern')
        ax.set_xlabel('Width (units)')
        ax.set_ylabel('Height (units)')
        plt.grid(False)
        plt.show()

def main():
    """
    Main function to create and display a perforated stainless steel sheet pattern.
    """
    try:
        # Define sheet specifications
        sheet_width = 100  # Width of the sheet
        sheet_height = 50  # Height of the sheet
        hole_diameter = 5   # Diameter of the holes
        hole_spacing = 10    # Spacing between holes

        # Create a perforated sheet object
        perforated_sheet = PerforatedSheet(sheet_width, sheet_height, hole_diameter, hole_spacing)

        # Plot the perforated pattern
        perforated_sheet.plot_pattern()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
