"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pahubel.com
Prompt: Write Python code to automate the generation of floor plans for healthcare facilities, incorporating specific design elements mentioned by Pahubel Ibérica S.L., such as dental clinic layouts and optical center spaces.
Generated: DETERMINISTIC_5994067f7ba81252
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
import matplotlib.patches as patches
import numpy as np

class FloorPlanGenerator:
    """
    A class to generate automated floor plans for healthcare facilities,
    including specific layouts for dental clinics and optical centers.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.set_aspect('equal')
        self.ax.axis('off')  # Hide axes for better visualization

    def add_room(self, x, y, room_width, room_height, label):
        """
        Adds a rectangular room to the floor plan.

        :param x: x-coordinate of the bottom left corner of the room
        :param y: y-coordinate of the bottom left corner of the room
        :param room_width: width of the room
        :param room_height: height of the room
        :param label: label to display in the room
        """
        try:
            room = patches.Rectangle((x, y), room_width, room_height, 
                                     linewidth=1, edgecolor='black', facecolor='lightgray')
            self.ax.add_patch(room)
            self.ax.text(x + room_width / 2, y + room_height / 2, 
                         label, fontsize=10, ha='center', va='center')
        except Exception as e:
            print(f"Error adding room: {e}")

    def generate_dental_clinic(self):
        """
        Generates a floor plan for a dental clinic.
        """
        try:
            # Define rooms specific for a dental clinic
            self.add_room(0, 0, 5, 5, "Reception")
            self.add_room(5, 0, 5, 5, "Waiting Area")
            self.add_room(0, 5, 5, 5, "Dental Room 1")
            self.add_room(5, 5, 5, 5, "Dental Room 2")
            self.add_room(0, 10, 5, 5, "Sterilization Room")
            self.add_room(5, 10, 5, 5, "Restroom")

            plt.title("Dental Clinic Floor Plan")
            plt.show()
        except Exception as e:
            print(f"Error generating dental clinic: {e}")

    def generate_optical_center(self):
        """
        Generates a floor plan for an optical center.
        """
        try:
            # Define rooms specific for an optical center
            self.add_room(0, 0, 5, 5, "Reception")
            self.add_room(5, 0, 5, 5, "Waiting Area")
            self.add_room(0, 5, 5, 5, "Examination Room 1")
            self.add_room(5, 5, 5, 5, "Examination Room 2")
            self.add_room(0, 10, 5, 5, "Dispensary")
            self.add_room(5, 10, 5, 5, "Restroom")

            plt.title("Optical Center Floor Plan")
            plt.show()
        except Exception as e:
            print(f"Error generating optical center: {e}")

def main():
    """
    Main function to run floor plan generation for healthcare facilities.
    """
    try:
        # Initialize the floor plan generator with dimensions
        generator = FloorPlanGenerator(width=10, height=15)

        # Generate floor plans
        generator.generate_dental_clinic()
        generator.generate_optical_center()
        
    except Exception as e:
        print(f"An error occurred in main: {e}")

if __name__ == "__main__":
    main()
```
