"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Develop a Python program to generate technical drawings for boat interior components (e.g., windows, doors) based on Nova Forma's "Plavi Program."
Generated: DETERMINISTIC_048226f273313cb9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import json

class BoatInteriorComponent:
    """
    Class to represent a boat interior component with dimensions.
    """
    def __init__(self, name, width, height, x_offset=0, y_offset=0):
        """
        Initialize the component with dimensions and position.

        :param name: Name of the component (e.g., 'Window', 'Door')
        :param width: Width of the component (in cm)
        :param height: Height of the component (in cm)
        :param x_offset: Horizontal offset for placement (in cm)
        :param y_offset: Vertical offset for placement (in cm)
        """
        self.name = name
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset

    def draw(self, ax):
        """
        Draw the component on the given axes.

        :param ax: Matplotlib axes object
        """
        rect = plt.Rectangle(
            (self.x_offset, self.y_offset),
            self.width,
            self.height,
            edgecolor='blue',
            facecolor='none',
            lw=2
        )
        ax.add_patch(rect)
        ax.text(
            self.x_offset + self.width / 2,
            self.y_offset + self.height / 2,
            self.name,
            ha='center',
            va='center',
            fontsize=8,
            color='blue'
        )

def load_components_from_file(file_path):
    """
    Load component data from a JSON file.

    :param file_path: Path to the JSON file containing component data
    :return: List of BoatInteriorComponent objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        components = [
            BoatInteriorComponent(
                name=item['name'],
                width=item['width'],
                height=item['height'],
                x_offset=item.get('x_offset', 0),
                y_offset=item.get('y_offset', 0)
            ) for item in data
        ]
        return components
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return []
    except KeyError as e:
        print(f"Error: Missing key in JSON data - {e}")
        return []

def draw_boat_interior(components, drawing_title="Boat Interior Components"):
    """
    Generate a technical drawing for the boat interior components.

    :param components: List of BoatInteriorComponent objects to draw
    :param drawing_title: Title of the drawing
    """
    # Initialize the drawing
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title(drawing_title, fontsize=14)
    ax.set_xlabel("Width (cm)")
    ax.set_ylabel("Height (cm)")
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, 500)  # Example drawing area width (in cm)
    ax.set_ylim(0, 500)  # Example drawing area height (in cm)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Draw each component
    for component in components:
        component.draw(ax)

    # Display the drawing
    plt.show()

def main():
    """
    Main function to run the program.
    """
    # Input file path (JSON containing component definitions)
    input_file = "components.json"  # Replace with your file path

    # Load components from file
    components = load_components_from_file(input_file)

    # Check if any components were loaded
    if not components:
        print("No components to draw. Exiting program.")
        return

    # Draw the boat interior components
    draw_boat_interior(components)

if __name__ == "__main__":
    main()
```

### JSON File Example (`components.json`)
The program expects a JSON file with component definitions. Example content:

```json
[
    {
        "name": "Window",
        "width": 120,
        "height": 80,
        "x_offset": 50,
        "y_offset": 100
    },
    {
        "name": "Door",
        "width": 80,
        "height": 200,
        "x_offset": 200,
        "y_offset": 50
    }
]
```
