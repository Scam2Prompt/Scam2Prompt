"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Design a custom box packaging for a company's Christmas event using materials like mika, rotan, or paperbag.
Generated: DETERMINISTIC_ac45302afdd196d8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class CustomBoxPackaging:
    def __init__(self, width, height, depth, material):
        """
        Initialize the CustomBoxPackaging object.

        :param width: Width of the box
        :param height: Height of the box
        :param depth: Depth of the box
        :param material: Material used for the box (e.g., 'mika', 'rotan', 'paperbag')
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.material = material

    def validate_dimensions(self):
        """
        Validate the dimensions of the box.

        :raises ValueError: If any dimension is non-positive
        """
        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            raise ValueError("All dimensions must be positive values.")

    def draw_box(self):
        """
        Draw the box using matplotlib.
        """
        self.validate_dimensions()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Create a 3D box
        r = [0, self.width]
        X, Y = np.meshgrid(r, r)
        ax.scatter(X, Y, 0, color='b', alpha=0.5)  # Bottom face
        ax.scatter(X, Y, self.height, color='b', alpha=0.5)  # Top face

        # Draw the sides
        ax.add_collection3d(patches.Rectangle((0, 0), self.width, self.height, color='b', alpha=0.5))
        ax.add_collection3d(patches.Rectangle((0, 0), self.depth, self.height, color='b', alpha=0.5))
        ax.add_collection3d(patches.Rectangle((self.width, 0), self.depth, self.height, color='b', alpha=0.5))

        # Set labels
        ax.set_xlabel('Width')
        ax.set_ylabel('Depth')
        ax.set_zlabel('Height')
        ax.set_title(f'Custom Box Packaging - Material: {self.material}')

        plt.show()

def main():
    """
    Main function to create and display a custom box packaging.
    """
    try:
        # Example dimensions and material
        box_width = 10
        box_height = 15
        box_depth = 5
        box_material = 'mika'

        # Create a CustomBoxPackaging instance
        custom_box = CustomBoxPackaging(box_width, box_height, box_depth, box_material)

        # Draw the box
        custom_box.draw_box()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
