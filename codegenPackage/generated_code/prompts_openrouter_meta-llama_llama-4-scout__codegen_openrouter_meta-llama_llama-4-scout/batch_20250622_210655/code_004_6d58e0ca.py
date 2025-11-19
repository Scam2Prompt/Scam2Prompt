"""
Generated Code Metadata:
========================
Original URL: https://internor.pt
Prompt: Generate a floor plan layout using a programming language, considering factors like room shape and furniture placement, as seen on Internor's projetos 3D page.
Generated: DETERMINISTIC_6d58e0ca146e642e
Batch ID: 20250622_210655
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

class Room:
    def __init__(self, x, y, width, height):
        """
        Initialize a Room object.

        Args:
            x (float): The x-coordinate of the room's bottom-left corner.
            y (float): The y-coordinate of the room's bottom-left corner.
            width (float): The width of the room.
            height (float): The height of the room.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.furniture = []

    def add_furniture(self, furniture):
        """
        Add furniture to the room.

        Args:
            furniture (Furniture): The furniture to add.
        """
        self.furniture.append(furniture)

    def draw(self, ax):
        """
        Draw the room on a matplotlib axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        room_patch = patches.Rectangle((self.x, self.y), self.width, self.height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(room_patch)
        for furniture in self.furniture:
            furniture.draw(ax)


class Furniture:
    def __init__(self, x, y, width, height, color):
        """
        Initialize a Furniture object.

        Args:
            x (float): The x-coordinate of the furniture's bottom-left corner.
            y (float): The y-coordinate of the furniture's bottom-left corner.
            width (float): The width of the furniture.
            height (float): The height of the furniture.
            color (str): The color of the furniture.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, ax):
        """
        Draw the furniture on a matplotlib axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        furniture_patch = patches.Rectangle((self.x, self.y), self.width, self.height, linewidth=1, edgecolor='black', facecolor=self.color)
        ax.add_patch(furniture_patch)


def main():
    try:
        # Create a new figure
        fig, ax = plt.subplots()

        # Set the aspect ratio to be equal so the rooms and furniture are not distorted
        ax.set_aspect('equal')

        # Create a room
        room = Room(0, 0, 10, 10)

        # Add furniture to the room
        room.add_furniture(Furniture(1, 1, 2, 2, 'blue'))  # Sofa
        room.add_furniture(Furniture(4, 4, 1, 1, 'red'))  # Chair
        room.add_furniture(Furniture(7, 2, 2, 1, 'green'))  # Table

        # Draw the room and furniture
        room.draw(ax)

        # Set the limits of the plot to the size of the room
        ax.set_xlim(-1, room.width + 1)
        ax.set_ylim(-1, room.height + 1)

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
