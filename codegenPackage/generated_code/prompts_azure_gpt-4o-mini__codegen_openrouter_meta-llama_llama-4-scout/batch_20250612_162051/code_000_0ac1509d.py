"""
Generated Code Metadata:
========================
Original URL: https://topgraininteriors.com
Prompt: Generate a code snippet for a custom kitchen design application that allows users to visualize built-in cabinets and wine cellars, similar to the services offered by Top Grain Interiors.
Generated: DETERMINISTIC_0ac1509dc5ac4a25
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kitchen_designer.py

class Cabinet:
    """Represents a built-in cabinet in the kitchen design."""

    def __init__(self, width, height, depth, material, color):
        """
        Initializes a Cabinet object.

        Args:
            width (float): The width of the cabinet in inches.
            height (float): The height of the cabinet in inches.
            depth (float): The depth of the cabinet in inches.
            material (str): The material of the cabinet (e.g., wood, metal).
            color (str): The color of the cabinet.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.material = material
        self.color = color

    def __str__(self):
        return f"Cabinet - Width: {self.width}in, Height: {self.height}in, Depth: {self.depth}in, Material: {self.material}, Color: {self.color}"


class WineCellar:
    """Represents a wine cellar in the kitchen design."""

    def __init__(self, width, height, depth, capacity, material, color):
        """
        Initializes a WineCellar object.

        Args:
            width (float): The width of the wine cellar in inches.
            height (float): The height of the wine cellar in inches.
            depth (float): The depth of the wine cellar in inches.
            capacity (int): The number of wine bottles the cellar can hold.
            material (str): The material of the wine cellar (e.g., wood, metal).
            color (str): The color of the wine cellar.
        """
        self.width = width
        self.height = height
        self.depth = depth
        self.capacity = capacity
        self.material = material
        self.color = color

    def __str__(self):
        return f"Wine Cellar - Width: {self.width}in, Height: {self.height}in, Depth: {self.depth}in, Capacity: {self.capacity} bottles, Material: {self.material}, Color: {self.color}"


class KitchenDesigner:
    """Provides methods for designing a kitchen with built-in cabinets and wine cellars."""

    def __init__(self):
        self.cabinets = []
        self.wine_cellars = []

    def add_cabinet(self, cabinet):
        """
        Adds a cabinet to the kitchen design.

        Args:
            cabinet (Cabinet): The cabinet to add.
        """
        self.cabinets.append(cabinet)

    def add_wine_cellar(self, wine_cellar):
        """
        Adds a wine cellar to the kitchen design.

        Args:
            wine_cellar (WineCellar): The wine cellar to add.
        """
        self.wine_cellars.append(wine_cellar)

    def visualize_design(self):
        """
        Prints out the current kitchen design.
        """
        print("Kitchen Design:")
        for i, cabinet in enumerate(self.cabinets):
            print(f"Cabinet {i+1}: {cabinet}")
        for i, wine_cellar in enumerate(self.wine_cellars):
            print(f"Wine Cellar {i+1}: {wine_cellar}")


def main():
    designer = KitchenDesigner()

    while True:
        print("\nOptions:")
        print("1. Add Cabinet")
        print("2. Add Wine Cellar")
        print("3. Visualize Design")
        print("4. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                width = float(input("Enter cabinet width (in): "))
                height = float(input("Enter cabinet height (in): "))
                depth = float(input("Enter cabinet depth (in): "))
                material = input("Enter cabinet material: ")
                color = input("Enter cabinet color: ")
                cabinet = Cabinet(width, height, depth, material, color)
                designer.add_cabinet(cabinet)
            elif choice == "2":
                width = float(input("Enter wine cellar width (in): "))
                height = float(input("Enter wine cellar height (in): "))
                depth = float(input("Enter wine cellar depth (in): "))
                capacity = int(input("Enter wine cellar capacity (bottles): "))
                material = input("Enter wine cellar material: ")
                color = input("Enter wine cellar color: ")
                wine_cellar = WineCellar(width, height, depth, capacity, material, color)
                designer.add_wine_cellar(wine_cellar)
            elif choice == "3":
                designer.visualize_design()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
