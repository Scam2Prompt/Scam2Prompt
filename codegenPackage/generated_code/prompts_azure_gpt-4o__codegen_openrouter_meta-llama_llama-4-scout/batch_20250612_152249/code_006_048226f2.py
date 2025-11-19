"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: Develop a Python program to generate technical drawings for boat interior components (e.g., windows, doors) based on Nova Forma's "Plavi Program."
Generated: DETERMINISTIC_048226f273313cb9
Batch ID: 20250612_152249
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

class BoatComponent:
    def __init__(self, name, x, y, width, height):
        """
        Initialize a boat component.

        Args:
            name (str): The name of the component.
            x (float): The x-coordinate of the component.
            y (float): The y-coordinate of the component.
            width (float): The width of the component.
            height (float): The height of the component.
        """
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, ax):
        """
        Draw the component on the given axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        rect = patches.Rectangle((self.x, self.y), self.width, self.height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        ax.text(self.x + self.width / 2, self.y + self.height / 2, self.name, ha='center')

class Window(BoatComponent):
    def __init__(self, x, y, width, height, frame_thickness):
        """
        Initialize a window.

        Args:
            x (float): The x-coordinate of the window.
            y (float): The y-coordinate of the window.
            width (float): The width of the window.
            height (float): The height of the window.
            frame_thickness (float): The thickness of the window frame.
        """
        super().__init__('Window', x, y, width, height)
        self.frame_thickness = frame_thickness

    def draw(self, ax):
        """
        Draw the window on the given axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        super().draw(ax)
        frame_rect = patches.Rectangle((self.x - self.frame_thickness, self.y - self.frame_thickness), 
                                       self.width + 2 * self.frame_thickness, self.height + 2 * self.frame_thickness, 
                                       linewidth=1, edgecolor='black', facecolor='none', linestyle='--')
        ax.add_patch(frame_rect)

class Door(BoatComponent):
    def __init__(self, x, y, width, height, handle_position):
        """
        Initialize a door.

        Args:
            x (float): The x-coordinate of the door.
            y (float): The y-coordinate of the door.
            width (float): The width of the door.
            height (float): The height of the door.
            handle_position (float): The position of the door handle.
        """
        super().__init__('Door', x, y, width, height)
        self.handle_position = handle_position

    def draw(self, ax):
        """
        Draw the door on the given axis.

        Args:
            ax (matplotlib.axes.Axes): The axis to draw on.
        """
        super().draw(ax)
        handle_line = patches.Rectangle((self.x + self.handle_position, self.y + self.height / 2 - 0.1), 
                                        0.1, 0.2, linewidth=1, edgecolor='black', facecolor='black')
        ax.add_patch(handle_line)

def generate_technical_drawing(components):
    """
    Generate a technical drawing for the given components.

    Args:
        components (list[BoatComponent]): The list of components to draw.
    """
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')

    for component in components:
        try:
            component.draw(ax)
        except Exception as e:
            print(f"Error drawing {component.name}: {str(e)}")

    plt.show()

def main():
    try:
        window = Window(1, 1, 2, 2, 0.1)
        door = Door(4, 1, 2, 2, 0.5)
        components = [window, door]
        generate_technical_drawing(components)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
