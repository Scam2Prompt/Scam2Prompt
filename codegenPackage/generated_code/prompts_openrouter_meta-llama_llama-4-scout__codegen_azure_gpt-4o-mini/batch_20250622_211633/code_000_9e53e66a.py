"""
Generated Code Metadata:
========================
Original URL: https://wwereplicabelts.com
Prompt: Design a WWE championship belt inspired by the WWE Universal Championship Replica Title Belt, including its key features and materials.
Generated: DETERMINISTIC_9e53e66a9eed2af3
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ChampionshipBelt:
    """
    A class to represent a WWE Championship Belt inspired by the WWE Universal Championship Replica Title Belt.
    """

    def __init__(self, name, material, color, width, length, features):
        """
        Initializes the ChampionshipBelt with the given attributes.

        :param name: str - The name of the championship belt.
        :param material: str - The primary material of the belt (e.g., leather, metal).
        :param color: str - The color of the belt.
        :param width: float - The width of the belt in inches.
        :param length: float - The length of the belt in inches.
        :param features: list - A list of key features of the belt.
        """
        self.name = name
        self.material = material
        self.color = color
        self.width = width
        self.length = length
        self.features = features

    def display_belt_info(self):
        """
        Displays the information of the championship belt.
        """
        try:
            print(f"Championship Belt: {self.name}")
            print(f"Material: {self.material}")
            print(f"Color: {self.color}")
            print(f"Width: {self.width} inches")
            print(f"Length: {self.length} inches")
            print("Key Features:")
            for feature in self.features:
                print(f"- {feature}")
        except Exception as e:
            print(f"An error occurred while displaying belt info: {e}")

    def is_valid(self):
        """
        Validates the attributes of the championship belt.

        :return: bool - True if the belt attributes are valid, False otherwise.
        """
        try:
            if not isinstance(self.name, str) or not self.name:
                raise ValueError("Invalid name: must be a non-empty string.")
            if not isinstance(self.material, str) or not self.material:
                raise ValueError("Invalid material: must be a non-empty string.")
            if not isinstance(self.color, str) or not self.color:
                raise ValueError("Invalid color: must be a non-empty string.")
            if not (isinstance(self.width, (int, float)) and self.width > 0):
                raise ValueError("Invalid width: must be a positive number.")
            if not (isinstance(self.length, (int, float)) and self.length > 0):
                raise ValueError("Invalid length: must be a positive number.")
            if not isinstance(self.features, list):
                raise ValueError("Invalid features: must be a list.")
            return True
        except ValueError as ve:
            print(ve)
            return False
        except Exception as e:
            print(f"An error occurred during validation: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Create a WWE Championship Belt instance
    belt_name = "WWE Universal Championship"
    belt_material = "Leather with Metal Plates"
    belt_color = "Blue and Gold"
    belt_width = 10.0  # in inches
    belt_length = 50.0  # in inches
    belt_features = [
        "Large center plate with logo",
        "Side plates for personalization",
        "Adjustable strap for size fitting",
        "High-quality craftsmanship"
    ]

    championship_belt = ChampionshipBelt(belt_name, belt_material, belt_color, belt_width, belt_length, belt_features)

    # Validate and display belt information
    if championship_belt.is_valid():
        championship_belt.display_belt_info()
```
