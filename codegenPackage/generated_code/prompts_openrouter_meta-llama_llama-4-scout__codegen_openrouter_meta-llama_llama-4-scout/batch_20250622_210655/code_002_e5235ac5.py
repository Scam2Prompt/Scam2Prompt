"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: "Create a floor plan for a small bedroom with a bed loft, optimizing space for a comfortable and functional reading nook."
Generated: DETERMINISTIC_e5235ac5305486c6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Room:
    def __init__(self, width, height):
        """
        Initialize a Room object.

        Args:
            width (float): The width of the room in feet.
            height (float): The height of the room in feet.
        """
        self.width = width
        self.height = height

    def draw(self, ax):
        """
        Draw the room on a matplotlib axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        # Draw room rectangle
        room_rect = patches.Rectangle((0, 0), self.width, self.height, 
                                      edgecolor='black', facecolor='none', 
                                      linewidth=2)
        ax.add_patch(room_rect)


class BedLoft:
    def __init__(self, x, y, width, height):
        """
        Initialize a BedLoft object.

        Args:
            x (float): The x-coordinate of the bed loft in feet.
            y (float): The y-coordinate of the bed loft in feet.
            width (float): The width of the bed loft in feet.
            height (float): The height of the bed loft in feet.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, ax):
        """
        Draw the bed loft on a matplotlib axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        # Draw bed loft rectangle
        bed_loft_rect = patches.Rectangle((self.x, self.y), self.width, self.height, 
                                          edgecolor='black', facecolor='lightblue', 
                                          linewidth=2)
        ax.add_patch(bed_loft_rect)


class ReadingNook:
    def __init__(self, x, y, width, height):
        """
        Initialize a ReadingNook object.

        Args:
            x (float): The x-coordinate of the reading nook in feet.
            y (float): The y-coordinate of the reading nook in feet.
            width (float): The width of the reading nook in feet.
            height (float): The height of the reading nook in feet.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, ax):
        """
        Draw the reading nook on a matplotlib axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        # Draw reading nook rectangle
        reading_nook_rect = patches.Rectangle((self.x, self.y), self.width, self.height, 
                                             edgecolor='black', facecolor='lightgreen', 
                                             linewidth=2)
        ax.add_patch(reading_nook_rect)


def main():
    try:
        # Create a new room
        room = Room(10, 12)

        # Create a new bed loft
        bed_loft = BedLoft(2, 2, 6, 6)

        # Create a new reading nook
        reading_nook = ReadingNook(7, 8, 3, 3)

        # Create a new figure and axis
        fig, ax = plt.subplots()

        # Draw the room
        room.draw(ax)

        # Draw the bed loft
        bed_loft.draw(ax)

        # Draw the reading nook
        reading_nook.draw(ax)

        # Set limits and aspect ratio
        ax.set_xlim(0, room.width)
        ax.set_ylim(0, room.height)
        ax.set_aspect('equal')

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
