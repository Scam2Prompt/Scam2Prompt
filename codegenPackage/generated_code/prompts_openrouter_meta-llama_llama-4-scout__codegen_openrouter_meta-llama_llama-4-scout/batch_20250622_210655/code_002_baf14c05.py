"""
Generated Code Metadata:
========================
Original URL: https://internor.pt
Prompt: Design a custom furniture piece using code, taking into account user-specified materials and dimensions, like Internor's mobiliário por medida service.
Generated: DETERMINISTIC_baf14c055e203fe2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_designer.py

class Furniture:
    def __init__(self, name, material, dimensions):
        """
        Initialize a Furniture object.

        Args:
            name (str): Name of the furniture piece.
            material (str): Material of the furniture piece.
            dimensions (dict): Dimensions of the furniture piece (e.g., length, width, height).
        """
        self.name = name
        self.material = material
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} - {self.material}"

    def get_description(self):
        """
        Generate a description of the furniture piece.

        Returns:
            str: Description of the furniture piece.
        """
        description = f"{self.name} made of {self.material} with dimensions:\n"
        for dimension, value in self.dimensions.items():
            description += f"  - {dimension.capitalize()}: {value} cm\n"
        return description


class FurnitureDesigner:
    def __init__(self):
        """
        Initialize a FurnitureDesigner object.
        """
        self.materials = ["Wood", "Metal", "Glass", "Plastic"]
        self.furniture_pieces = []

    def design_furniture(self, name, material, dimensions):
        """
        Design a custom furniture piece.

        Args:
            name (str): Name of the furniture piece.
            material (str): Material of the furniture piece.
            dimensions (dict): Dimensions of the furniture piece (e.g., length, width, height).

        Raises:
            ValueError: If the material is not valid.
        """
        if material not in self.materials:
            raise ValueError("Invalid material. Please choose from: {}".format(", ".join(self.materials)))

        furniture_piece = Furniture(name, material, dimensions)
        self.furniture_pieces.append(furniture_piece)
        return furniture_piece

    def get_furniture_pieces(self):
        """
        Get a list of designed furniture pieces.

        Returns:
            list: List of Furniture objects.
        """
        return self.furniture_pieces


def main():
    designer = FurnitureDesigner()

    while True:
        print("\n1. Design Furniture")
        print("2. View Furniture Pieces")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter furniture name: ")
            print("Choose a material:")
            for i, material in enumerate(designer.materials):
                print(f"{i+1}. {material}")
            material_choice = int(input("Enter material number: "))
            material = designer.materials[material_choice - 1]

            dimensions = {}
            dimensions["length"] = float(input("Enter length (cm): "))
            dimensions["width"] = float(input("Enter width (cm): "))
            dimensions["height"] = float(input("Enter height (cm): "))

            try:
                furniture_piece = designer.design_furniture(name, material, dimensions)
                print("\nFurniture piece designed:")
                print(furniture_piece.get_description())
            except ValueError as e:
                print(str(e))

        elif choice == "2":
            furniture_pieces = designer.get_furniture_pieces()
            if furniture_pieces:
                for i, piece in enumerate(furniture_pieces):
                    print(f"\nFurniture Piece {i+1}:")
                    print(piece.get_description())
            else:
                print("No furniture pieces designed yet.")

        elif choice == "3":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
