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
class Furniture:
    """
    A class to represent a custom furniture piece.

    Attributes:
        material (str): The material of the furniture.
        dimensions (dict): A dictionary containing the dimensions of the furniture.
                           Expected keys are 'width', 'height', and 'depth'.
    """

    def __init__(self, material: str, dimensions: dict):
        """
        Initializes the Furniture object with specified material and dimensions.

        Args:
            material (str): The material of the furniture.
            dimensions (dict): A dictionary containing the dimensions of the furniture.

        Raises:
            ValueError: If dimensions are not provided or are invalid.
        """
        self.material = material
        self.dimensions = self.validate_dimensions(dimensions)

    def validate_dimensions(self, dimensions: dict) -> dict:
        """
        Validates the dimensions provided for the furniture.

        Args:
            dimensions (dict): A dictionary containing the dimensions of the furniture.

        Returns:
            dict: The validated dimensions.

        Raises:
            ValueError: If any dimension is missing or not a positive number.
        """
        required_keys = ['width', 'height', 'depth']
        for key in required_keys:
            if key not in dimensions or not isinstance(dimensions[key], (int, float)) or dimensions[key] <= 0:
                raise ValueError(f"Invalid dimension for '{key}': must be a positive number.")
        return dimensions

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the furniture piece.

        Returns:
            float: The volume of the furniture in cubic units.
        """
        return self.dimensions['width'] * self.dimensions['height'] * self.dimensions['depth']

    def __str__(self) -> str:
        """
        Returns a string representation of the furniture piece.

        Returns:
            str: A description of the furniture piece.
        """
        return (f"Furniture Piece:\n"
                f"Material: {self.material}\n"
                f"Dimensions (W x H x D): {self.dimensions['width']} x {self.dimensions['height']} x {self.dimensions['depth']}\n"
                f"Volume: {self.calculate_volume()} cubic units")


def main():
    """
    Main function to create a custom furniture piece based on user input.
    """
    try:
        # User input for material and dimensions
        material = input("Enter the material for the furniture: ")
        width = float(input("Enter the width of the furniture (positive number): "))
        height = float(input("Enter the height of the furniture (positive number): "))
        depth = float(input("Enter the depth of the furniture (positive number): "))

        # Create dimensions dictionary
        dimensions = {'width': width, 'height': height, 'depth': depth}

        # Create a Furniture object
        custom_furniture = Furniture(material, dimensions)

        # Print the details of the custom furniture
        print(custom_furniture)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
