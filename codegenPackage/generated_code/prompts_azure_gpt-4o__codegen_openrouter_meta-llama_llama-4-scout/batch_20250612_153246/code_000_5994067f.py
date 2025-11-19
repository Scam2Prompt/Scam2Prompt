"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Write Python code to automate the generation of floor plans for healthcare facilities, incorporating specific design elements mentioned by Pahubel Ibérica S.L., such as dental clinic layouts and optical center spaces.
Generated: DETERMINISTIC_5994067f7ba81252
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
import matplotlib.patches as patches

class Room:
    """Represents a room in the floor plan."""
    
    def __init__(self, name, x, y, width, height):
        """
        Initializes a Room object.

        Args:
            name (str): The name of the room.
            x (float): The x-coordinate of the room's bottom-left corner.
            y (float): The y-coordinate of the room's bottom-left corner.
            width (float): The width of the room.
            height (float): The height of the room.
        """
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class FloorPlan:
    """Represents a floor plan for a healthcare facility."""
    
    def __init__(self, width, height):
        """
        Initializes a FloorPlan object.

        Args:
            width (float): The width of the floor plan.
            height (float): The height of the floor plan.
        """
        self.width = width
        self.height = height
        self.rooms = []

    def add_room(self, room):
        """
        Adds a room to the floor plan.

        Args:
            room (Room): The room to add.
        """
        self.rooms.append(room)

    def draw(self):
        """
        Draws the floor plan using matplotlib.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)

        for room in self.rooms:
            rect = patches.Rectangle((room.x, room.y), room.width, room.height, linewidth=1, edgecolor='black', facecolor='none')
            ax.add_patch(rect)
            ax.text(room.x + room.width / 2, room.y + room.height / 2, room.name, ha='center')

        plt.show()

def create_dental_clinic_layout():
    """
    Creates a floor plan for a dental clinic.
    """
    clinic = FloorPlan(20, 15)

    # Waiting area
    clinic.add_room(Room('Waiting Area', 1, 1, 5, 5))

    # Dental chairs
    clinic.add_room(Room('Dental Chair 1', 7, 1, 3, 3))
    clinic.add_room(Room('Dental Chair 2', 7, 5, 3, 3))

    # X-ray room
    clinic.add_room(Room('X-ray Room', 1, 7, 4, 4))

    # Office
    clinic.add_room(Room('Office', 10, 1, 4, 4))

    clinic.draw()

def create_optical_center_layout():
    """
    Creates a floor plan for an optical center.
    """
    center = FloorPlan(25, 20)

    # Waiting area
    center.add_room(Room('Waiting Area', 1, 1, 6, 6))

    # Optical display
    center.add_room(Room('Optical Display', 8, 1, 8, 4))

    # Exam rooms
    center.add_room(Room('Exam Room 1', 1, 8, 4, 4))
    center.add_room(Room('Exam Room 2', 6, 8, 4, 4))

    # Office
    center.add_room(Room('Office', 15, 1, 4, 4))

    center.draw()

def main():
    try:
        create_dental_clinic_layout()
        create_optical_center_layout()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
