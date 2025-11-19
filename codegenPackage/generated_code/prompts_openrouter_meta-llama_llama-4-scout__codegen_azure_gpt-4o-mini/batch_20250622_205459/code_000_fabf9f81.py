"""
Generated Code Metadata:
========================
Original URL: https://aavego.dk
Prompt: Design a Nordic-inspired holiday home in Denmark that incorporates natural materials and modern furniture classics to create a calm atmosphere.
Generated: DETERMINISTIC_fabf9f81094c72d6
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HolidayHome:
    """
    A class to represent a Nordic-inspired holiday home.

    Attributes:
        location (str): The location of the holiday home.
        materials (list): A list of natural materials used in the home.
        furniture (list): A list of modern furniture classics in the home.
        atmosphere (str): The overall atmosphere of the home.
    """

    def __init__(self, location):
        """
        Initializes the HolidayHome with a location and default materials and furniture.

        Args:
            location (str): The location of the holiday home.
        """
        self.location = location
        self.materials = ['wood', 'stone', 'wool', 'linen']
        self.furniture = ['Hans Wegner chair', 'Arne Jacobsen table', 'Finn Juhl sofa']
        self.atmosphere = 'calm'

    def add_material(self, material):
        """
        Adds a natural material to the holiday home.

        Args:
            material (str): The natural material to add.

        Raises:
            ValueError: If the material is not a string or is empty.
        """
        if not isinstance(material, str) or not material:
            raise ValueError("Material must be a non-empty string.")
        self.materials.append(material)

    def add_furniture(self, furniture_item):
        """
        Adds a modern furniture classic to the holiday home.

        Args:
            furniture_item (str): The furniture item to add.

        Raises:
            ValueError: If the furniture item is not a string or is empty.
        """
        if not isinstance(furniture_item, str) or not furniture_item:
            raise ValueError("Furniture item must be a non-empty string.")
        self.furniture.append(furniture_item)

    def describe_home(self):
        """
        Returns a description of the holiday home, including its location, materials, furniture, and atmosphere.

        Returns:
            str: A description of the holiday home.
        """
        materials_str = ', '.join(self.materials)
        furniture_str = ', '.join(self.furniture)
        return (f"Holiday Home located in {self.location}.\n"
                f"Materials used: {materials_str}.\n"
                f"Furniture classics: {furniture_str}.\n"
                f"Overall atmosphere: {self.atmosphere}.")

# Example usage
if __name__ == "__main__":
    try:
        my_holiday_home = HolidayHome("Copenhagen, Denmark")
        my_holiday_home.add_material("bamboo")
        my_holiday_home.add_furniture("Eero Saarinen chair")
        print(my_holiday_home.describe_home())
    except ValueError as e:
        print(f"Error: {e}")
```
