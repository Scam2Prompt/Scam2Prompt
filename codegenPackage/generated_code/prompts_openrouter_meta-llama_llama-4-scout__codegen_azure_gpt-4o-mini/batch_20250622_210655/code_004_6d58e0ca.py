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
    def __init__(self, name, width, height, position=(0, 0)):
        """
        Initialize a room with a name, dimensions, and position.

        :param name: Name of the room
        :param width: Width of the room
        :param height: Height of the room
        :param position: Tuple (x, y) representing the bottom-left corner of the room
        """
        self.name = name
        self.width = width
        self.height = height
        self.position = position

    def draw(self, ax):
        """
        Draw the room on the given axes.

        :param ax: Matplotlib axes to draw the room on
        """
        rect = patches.Rectangle(self.position, self.width, self.height, fill=True, edgecolor='black', facecolor='lightgrey')
        ax.add_patch(rect)
        ax.text(self.position[0] + self.width / 2, self.position[1] + self.height / 2, self.name,
                horizontalalignment='center', verticalalignment='center', fontsize=10)

class Furniture:
    def __init__(self, name, width, height, position):
        """
        Initialize a piece of furniture with a name, dimensions, and position.

        :param name: Name of the furniture
        :param width: Width of the furniture
        :param height: Height of the furniture
        :param position: Tuple (x, y) representing the bottom-left corner of the furniture
        """
        self.name = name
        self.width = width
        self.height = height
        self.position = position

    def draw(self, ax):
        """
        Draw the furniture on the given axes.

        :param ax: Matplotlib axes to draw the furniture on
        """
        rect = patches.Rectangle(self.position, self.width, self.height, fill=True, edgecolor='black', facecolor='brown')
        ax.add_patch(rect)
        ax.text(self.position[0] + self.width / 2, self.position[1] + self.height / 2, self.name,
                horizontalalignment='center', verticalalignment='center', fontsize=8, color='white')

def create_floor_plan(rooms, furniture_list):
    """
    Create a floor plan with rooms and furniture.

    :param rooms: List of Room objects
    :param furniture_list: List of Furniture objects
    """
    try:
        fig, ax = plt.subplots()
        ax.set_xlim(0, 20)  # Set x-axis limits
        ax.set_ylim(0, 20)  # Set y-axis limits
        ax.set_aspect('equal', adjustable='box')
        ax.set_title('Floor Plan Layout')

        # Draw rooms
        for room in rooms:
            room.draw(ax)

        # Draw furniture
        for furniture in furniture_list:
            furniture.draw(ax)

        plt.grid()
        plt.show()
    except Exception as e:
        print(f"An error occurred while creating the floor plan: {e}")

if __name__ == "__main__":
    # Define rooms
    living_room = Room("Living Room", 10, 8, position=(0, 0))
    kitchen = Room("Kitchen", 8, 6, position=(10, 0))
    bedroom = Room("Bedroom", 8, 8, position=(0, 8))

    # Define furniture
    sofa = Furniture("Sofa", 3, 1, position=(1, 1))
    table = Furniture("Table", 2, 2, position=(5, 1))
    bed = Furniture("Bed", 3, 2, position=(1, 9))

    # Create floor plan
    create_floor_plan([living_room, kitchen, bedroom], [sofa, table, bed])
```
