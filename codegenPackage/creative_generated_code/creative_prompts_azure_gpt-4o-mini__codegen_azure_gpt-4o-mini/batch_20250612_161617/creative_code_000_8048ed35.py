"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Generate a code snippet to create a custom packaging box design using the specifications mentioned on the Metis website, including color accuracy and material quality.
Generated: DETERMINISTIC_8048ed35df7d30f8
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class PackagingBox:
    """Class to create a custom packaging box design."""
    
    def __init__(self, width, height, depth, color, material):
        """
        Initialize the packaging box design.

        Parameters:
        width (float): Width of the box.
        height (float): Height of the box.
        depth (float): Depth of the box.
        color (str): Color of the box in hex format.
        material (str): Material quality of the box.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color
        self.material = material

    def draw_box(self):
        """Draw the packaging box based on the specified dimensions and color."""
        try:
            # Create a new figure and axis
            fig, ax = plt.subplots()

            # Create a 3D box representation (2D projection)
            box = patches.Rectangle((0, 0), self.width, self.height, linewidth=1, edgecolor='black', facecolor=self.color)

            # Add the box patch to the axes
            ax.add_patch(box)

            # Set the limits and aspect
            ax.set_xlim(-self.depth, self.width + self.depth)
            ax.set_ylim(-self.depth, self.height + self.depth)
            ax.set_aspect('equal', adjustable='box')
            ax.set_title(f'Custom Packaging Box\nMaterial: {self.material}', fontsize=12)
            ax.set_xlabel('Width', fontsize=10)
            ax.set_ylabel('Height', fontsize=10)

            # Display the box
            plt.grid()
            plt.show()

        except Exception as e:
            print(f"Error while drawing box: {e}")

# Example usage
if __name__ == "__main__":
    # Define box specifications
    box_width = 5.0    # Width of the box
    box_height = 3.0   # Height of the box
    box_depth = 2.0    # Depth of the box
    box_color = '#FF5733'  # Box color in hex format
    box_material = 'Recycled Cardboard'  # Material quality

    # Create a PackagingBox instance
    packaging_box = PackagingBox(box_width, box_height, box_depth, box_color, box_material)

    # Draw the box
    packaging_box.draw_box()
```
