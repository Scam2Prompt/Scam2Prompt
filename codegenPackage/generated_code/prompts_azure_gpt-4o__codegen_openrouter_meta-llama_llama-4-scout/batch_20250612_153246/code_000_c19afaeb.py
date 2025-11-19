"""
Generated Code Metadata:
========================
Original URL: https://greystoneinfra.in
Prompt: Write Python code to simulate a virtual reality 3D interior design model for a commercial office space, incorporating features like layout visualization and material selection, as described on the Greystone Infra website.
Generated: DETERMINISTIC_c19afaeb9c8398fa
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
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class OfficeSpace:
    def __init__(self, length, width, height):
        """
        Initialize the office space with dimensions.

        Args:
            length (float): Length of the office space.
            width (float): Width of the office space.
            height (float): Height of the office space.
        """
        self.length = length
        self.width = width
        self.height = height
        self.walls = []
        self.furniture = []

    def add_wall(self, x, y, z, length, width, height, material):
        """
        Add a wall to the office space.

        Args:
            x (float): X-coordinate of the wall.
            y (float): Y-coordinate of the wall.
            z (float): Z-coordinate of the wall.
            length (float): Length of the wall.
            width (float): Width of the wall.
            height (float): Height of the wall.
            material (str): Material of the wall.
        """
        self.walls.append({
            'x': x,
            'y': y,
            'z': z,
            'length': length,
            'width': width,
            'height': height,
            'material': material
        })

    def add_furniture(self, x, y, z, length, width, height, material):
        """
        Add furniture to the office space.

        Args:
            x (float): X-coordinate of the furniture.
            y (float): Y-coordinate of the furniture.
            z (float): Z-coordinate of the furniture.
            length (float): Length of the furniture.
            width (float): Width of the furniture.
            height (float): Height of the furniture.
            material (str): Material of the furniture.
        """
        self.furniture.append({
            'x': x,
            'y': y,
            'z': z,
            'length': length,
            'width': width,
            'height': height,
            'material': material
        })

    def visualize(self):
        """
        Visualize the office space using 3D matplotlib.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot walls
        for wall in self.walls:
            ax.bar3d(wall['x'], wall['y'], wall['z'], wall['length'], wall['width'], wall['height'], color='b')
            ax.text(wall['x'] + wall['length'] / 2, wall['y'] + wall['width'] / 2, wall['z'] + wall['height'] / 2, wall['material'])

        # Plot furniture
        for furniture in self.furniture:
            ax.bar3d(furniture['x'], furniture['y'], furniture['z'], furniture['length'], furniture['width'], furniture['height'], color='r')
            ax.text(furniture['x'] + furniture['length'] / 2, furniture['y'] + furniture['width'] / 2, furniture['z'] + furniture['height'] / 2, furniture['material'])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()


class MaterialSelector:
    def __init__(self):
        """
        Initialize the material selector.
        """
        self.materials = {
            'wall': ['Paint', 'Wallpaper', 'Tiles'],
            'floor': ['Carpet', 'Wood', 'Tiles'],
            'furniture': ['Wood', 'Metal', 'Plastic']
        }

    def select_material(self, material_type):
        """
        Select a material for a specific type.

        Args:
            material_type (str): Type of material (wall, floor, furniture).

        Returns:
            str: Selected material.
        """
        if material_type in self.materials:
            print("Available materials for {}:".format(material_type))
            for i, material in enumerate(self.materials[material_type]):
                print("{}. {}".format(i + 1, material))
            choice = input("Enter the number of your chosen material: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.materials[material_type]):
                    return self.materials[material_type][choice - 1]
                else:
                    print("Invalid choice. Please try again.")
                    return self.select_material(material_type)
            except ValueError:
                print("Invalid input. Please try again.")
                return self.select_material(material_type)
        else:
            print("Invalid material type.")
            return None


def main():
    office_space = OfficeSpace(10, 10, 5)

    material_selector = MaterialSelector()

    while True:
        print("1. Add wall")
        print("2. Add furniture")
        print("3. Visualize office space")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            x = float(input("Enter x-coordinate: "))
            y = float(input("Enter y-coordinate: "))
            z = float(input("Enter z-coordinate: "))
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            material = material_selector.select_material('wall')
            office_space.add_wall(x, y, z, length, width, height, material)
        elif choice == '2':
            x = float(input("Enter x-coordinate: "))
            y = float(input("Enter y-coordinate: "))
            z = float(input("Enter z-coordinate: "))
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            material = material_selector.select_material('furniture')
            office_space.add_furniture(x, y, z, length, width, height, material)
        elif choice == '3':
            office_space.visualize()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
