"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Write a program to automate the generation of detailed engineering drawings for industrial projects, inspired by the design services of Multiservicios Industriales 3L.
Generated: DETERMINISTIC_979fbd55f520fa84
Batch ID: 20250612_151610
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

class DrawingGenerator:
    """
    A class used to generate detailed engineering drawings for industrial projects.

    Attributes:
    ----------
    project_name : str
        The name of the industrial project.
    equipment_list : list
        A list of equipment to be included in the drawing.

    Methods:
    -------
    generate_drawing()
        Generates a detailed engineering drawing for the industrial project.
    add_equipment(equipment)
        Adds equipment to the drawing.
    """

    def __init__(self, project_name):
        """
        Initializes the DrawingGenerator class.

        Parameters:
        ----------
        project_name : str
            The name of the industrial project.
        """
        self.project_name = project_name
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Adds equipment to the drawing.

        Parameters:
        ----------
        equipment : dict
            A dictionary containing the equipment's properties (e.g., name, x, y, width, height).
        """
        self.equipment_list.append(equipment)

    def generate_drawing(self):
        """
        Generates a detailed engineering drawing for the industrial project.
        """
        # Create a new figure
        fig, ax = plt.subplots()

        # Set the title of the drawing
        ax.set_title(self.project_name)

        # Add equipment to the drawing
        for equipment in self.equipment_list:
            # Create a rectangle for the equipment
            rect = patches.Rectangle((equipment['x'], equipment['y']), equipment['width'], equipment['height'], linewidth=1, edgecolor='black', facecolor='none')
            ax.add_patch(rect)

            # Add a label for the equipment
            ax.text(equipment['x'] + equipment['width'] / 2, equipment['y'] + equipment['height'] / 2, equipment['name'], ha='center')

        # Set the limits of the drawing
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        # Display the drawing
        plt.show()

class GUI:
    """
    A class used to create a graphical user interface for the DrawingGenerator class.

    Attributes:
    ----------
    root : tk.Tk
        The root window of the GUI.
    drawing_generator : DrawingGenerator
        An instance of the DrawingGenerator class.

    Methods:
    -------
    create_widgets()
        Creates the widgets for the GUI.
    add_equipment()
        Adds equipment to the drawing.
    generate_drawing()
        Generates a detailed engineering drawing for the industrial project.
    """

    def __init__(self):
        """
        Initializes the GUI class.
        """
        self.root = tk.Tk()
        self.root.title("Industrial Drawing Generator")
        self.drawing_generator = DrawingGenerator("Industrial Project")

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the GUI.
        """
        # Create a label and entry for the project name
        tk.Label(self.root, text="Project Name:").grid(row=0, column=0)
        self.project_name_entry = tk.Entry(self.root)
        self.project_name_entry.grid(row=0, column=1)

        # Create a label and entry for the equipment name
        tk.Label(self.root, text="Equipment Name:").grid(row=1, column=0)
        self.equipment_name_entry = tk.Entry(self.root)
        self.equipment_name_entry.grid(row=1, column=1)

        # Create a label and entry for the equipment x position
        tk.Label(self.root, text="Equipment X Position:").grid(row=2, column=0)
        self.equipment_x_entry = tk.Entry(self.root)
        self.equipment_x_entry.grid(row=2, column=1)

        # Create a label and entry for the equipment y position
        tk.Label(self.root, text="Equipment Y Position:").grid(row=3, column=0)
        self.equipment_y_entry = tk.Entry(self.root)
        self.equipment_y_entry.grid(row=3, column=1)

        # Create a label and entry for the equipment width
        tk.Label(self.root, text="Equipment Width:").grid(row=4, column=0)
        self.equipment_width_entry = tk.Entry(self.root)
        self.equipment_width_entry.grid(row=4, column=1)

        # Create a label and entry for the equipment height
        tk.Label(self.root, text="Equipment Height:").grid(row=5, column=0)
        self.equipment_height_entry = tk.Entry(self.root)
        self.equipment_height_entry.grid(row=5, column=1)

        # Create a button to add equipment
        self.add_equipment_button = tk.Button(self.root, text="Add Equipment", command=self.add_equipment)
        self.add_equipment_button.grid(row=6, column=0)

        # Create a button to generate the drawing
        self.generate_drawing_button = tk.Button(self.root, text="Generate Drawing", command=self.generate_drawing)
        self.generate_drawing_button.grid(row=6, column=1)

    def add_equipment(self):
        """
        Adds equipment to the drawing.
        """
        try:
            equipment = {
                'name': self.equipment_name_entry.get(),
                'x': float(self.equipment_x_entry.get()),
                'y': float(self.equipment_y_entry.get()),
                'width': float(self.equipment_width_entry.get()),
                'height': float(self.equipment_height_entry.get())
            }
            self.drawing_generator.add_equipment(equipment)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def generate_drawing(self):
        """
        Generates a detailed engineering drawing for the industrial project.
        """
        self.drawing_generator.project_name = self.project_name_entry.get()
        self.drawing_generator.generate_drawing()

    def run(self):
        """
        Runs the GUI.
        """
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
```
