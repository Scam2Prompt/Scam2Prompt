"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Design a custom box packaging for a food product using a material like cardboard or paperbag, considering factors like durability and sustainability.
Generated: DETERMINISTIC_6e8040eae9d3060d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PackagingDesign:
    """
    A class to represent a custom box packaging for a food product.
    
    Attributes:
        material (str): The material used for packaging (e.g., cardboard, paperbag).
        dimensions (tuple): The dimensions of the box (length, width, height).
        durability (str): The durability rating of the packaging.
        sustainability (str): The sustainability rating of the packaging.
    """

    def __init__(self, material: str, dimensions: tuple, durability: str, sustainability: str):
        """
        Initializes the PackagingDesign with the specified material, dimensions, durability, and sustainability.

        Args:
            material (str): The material for the packaging.
            dimensions (tuple): A tuple containing the length, width, and height of the box.
            durability (str): The durability rating of the packaging.
            sustainability (str): The sustainability rating of the packaging.
        
        Raises:
            ValueError: If dimensions are not positive numbers.
        """
        if not all(isinstance(d, (int, float)) and d > 0 for d in dimensions):
            raise ValueError("Dimensions must be positive numbers.")
        
        self.material = material
        self.dimensions = dimensions
        self.durability = durability
        self.sustainability = sustainability

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the packaging box.

        Returns:
            float: The volume of the box in cubic units.
        """
        length, width, height = self.dimensions
        return length * width * height

    def display_info(self) -> None:
        """
        Displays the information about the packaging design.
        """
        print(f"Packaging Material: {self.material}")
        print(f"Dimensions (LxWxH): {self.dimensions}")
        print(f"Durability Rating: {self.durability}")
        print(f"Sustainability Rating: {self.sustainability}")
        print(f"Volume: {self.calculate_volume()} cubic units")

# Example usage
if __name__ == "__main__":
    try:
        # Create a custom packaging design
        box = PackagingDesign(
            material="Cardboard",
            dimensions=(10, 5, 3),  # Length, Width, Height
            durability="High",
            sustainability="Recyclable"
        )
        
        # Display the packaging information
        box.display_info()
    except ValueError as e:
        print(f"Error: {e}")
```
