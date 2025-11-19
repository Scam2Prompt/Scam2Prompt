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
# Import necessary modules
import json

class FurniturePiece:
    """
    A class to represent a custom furniture piece.
    """

    def __init__(self, name, material, dimensions):
        """
        Initialize the furniture piece with name, material, and dimensions.

        :param name: Name of the furniture piece (e.g., "Table", "Chair").
        :param material: Material of the furniture piece (e.g., "Wood", "Metal").
        :param dimensions: Dimensions of the furniture piece as a dictionary 
                           with keys 'length', 'width', and 'height' (in cm).
        """
        self.name = name
        self.material = material
        self.dimensions = dimensions

    def validate_dimensions(self):
        """
        Validate that dimensions are positive numbers.

        :raises ValueError: If any dimension is not positive.
        """
        for key, value in self.dimensions.items():
            if value <= 0:
                raise ValueError(f"{key.capitalize()} must be a positive number. Got {value}.")

    def to_dict(self):
        """
        Convert the furniture piece to a dictionary representation.

        :return: Dictionary containing furniture details.
        """
        return {
            "name": self.name,
            "material": self.material,
            "dimensions": self.dimensions
        }

    def __str__(self):
        """
        Return a string representation of the furniture piece.

        :return: String describing the furniture piece.
        """
        return f"Furniture Piece: {self.name}\nMaterial: {self.material}\nDimensions: {self.dimensions}"


def create_furniture_piece():
    """
    Function to create a custom furniture piece based on user input.

    :return: FurniturePiece object.
    """
    try:
        # Get user input for furniture details
        name = input("Enter the name of the furniture piece (e.g., Table, Chair): ").strip()
        material = input("Enter the material of the furniture piece (e.g., Wood, Metal): ").strip()

        # Get dimensions from user
        print("Enter the dimensions of the furniture piece (in cm):")
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))

        # Create dimensions dictionary
        dimensions = {"length": length, "width": width, "height": height}

        # Create FurniturePiece object
        furniture = FurniturePiece(name, material, dimensions)

        # Validate dimensions
        furniture.validate_dimensions()

        # Return the created furniture piece
        return furniture

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_furniture_to_file(furniture, filename="furniture.json"):
    """
    Save the furniture piece details to a JSON file.

    :param furniture: FurniturePiece object to save.
    :param filename: Name of the file to save the details to.
    """
    try:
        # Convert furniture piece to dictionary
        furniture_data = furniture.to_dict()

        # Save to JSON file
        with open(filename, "w") as file:
            json.dump(furniture_data, file, indent=4)
        print(f"Furniture details saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")


if __name__ == "__main__":
    # Create a custom furniture piece
    furniture = create_furniture_piece()

    # If furniture creation was successful, save to file
    if furniture:
        print("\nFurniture created successfully:")
        print(furniture)
        save_furniture_to_file(furniture)
```
