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

class FloorPlanGenerator:
    def __init__(self, width, height):
        """
        Initialize the FloorPlanGenerator with specified dimensions.

        :param width: Width of the floor plan in meters.
        :param height: Height of the floor plan in meters.
        """
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.set_aspect('equal')
        self.ax.axis('off')  # Hide axes

    def add_room(self, x, y, room_width, room_height, label):
        """
        Add a rectangular room to the floor plan.

        :param x: X-coordinate of the bottom-left corner of the room.
        :param y: Y-coordinate of the bottom-left corner of the room.
        :param room_width: Width of the room.
        :param room_height: Height of the room.
        :param label: Label for the room.
        """
        room = patches.Rectangle((x, y), room_width, room_height, fill=True, edgecolor='black', facecolor='lightgrey')
        self.ax.add_patch(room)
        self.ax.text(x + room_width / 2, y + room_height / 2, label, ha='center', va='center', fontsize=10)

    def add_dental_clinic(self):
        """
        Add specific layout for a dental clinic to the floor plan.
        """
        try:
            # Define dental clinic layout
            self.add_room(1, 1, 4, 3, 'Reception')
            self.add_room(1, 4, 2, 3, 'Dental Room 1')
            self.add_room(3, 4, 2, 3, 'Dental Room 2')
            self.add_room(1, 7, 4, 2, 'Waiting Area')
            self.add_room(5, 1, 2, 3, 'Restroom')
        except Exception as e:
            print(f"Error adding dental clinic layout: {e}")

    def add_optical_center(self):
        """
        Add specific layout for an optical center to the floor plan.
        """
        try:
            # Define optical center layout
            self.add_room(1, 1, 3, 3, 'Reception')
            self.add_room(1, 4, 3, 3, 'Optical Exam Room')
            self.add_room(4, 1, 3, 3, 'Frame Display')
            self.add_room(4, 4, 3, 3, 'Contact Lens Room')
            self.add_room(1, 7, 6, 2, 'Waiting Area')
        except Exception as e:
            print(f"Error adding optical center layout: {e}")

    def show_floor_plan(self):
        """
        Display the generated floor plan.
        """
        plt.title('Healthcare Facility Floor Plan')
        plt.show()

if __name__ == "__main__":
    # Create a floor plan generator instance
    floor_plan = FloorPlanGenerator(width=10, height=10)

    # Generate layouts for dental clinic and optical center
    floor_plan.add_dental_clinic()
    floor_plan.add_optical_center()

    # Show the final floor plan
    floor_plan.show_floor_plan()
```
