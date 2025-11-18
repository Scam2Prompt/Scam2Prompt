"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Write code to simulate the hybrid design of the Settled Collection fireplaces, combining furniture and fireplace elements in a single piece.
Generated: DETERMINISTIC_0c73fef2b40cd0a4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class Fireplace:
    """
    Represents the fireplace element in the hybrid design.
    """
    def __init__(self, heat_output: int, fuel_type: str):
        """
        Initializes the fireplace with heat output and fuel type.

        :param heat_output: Heat output in BTUs
        :param fuel_type: Type of fuel used (e.g., 'wood', 'electric', 'gas')
        """
        self.heat_output = heat_output
        self.fuel_type = fuel_type

    def ignite(self):
        """
        Simulates lighting the fireplace.
        """
        if self.fuel_type in ['wood', 'gas', 'electric']:
            print(f"The fireplace is now lit using {self.fuel_type}.")
        else:
            raise ValueError("Unsupported fuel type.")

    def adjust_heat(self, new_heat_output: int):
        """
        Adjusts the heat output of the fireplace.

        :param new_heat_output: New heat output in BTUs
        """
        if new_heat_output <= 0:
            raise ValueError("Heat output must be a positive value.")
        print(f"Adjusting heat output from {self.heat_output} BTUs to {new_heat_output} BTUs.")
        self.heat_output = new_heat_output


class Furniture:
    """
    Represents the furniture element in the hybrid design.
    """
    def __init__(self, material: str, style: str):
        """
        Initializes the furniture with material and style.

        :param material: Material of the furniture (e.g., 'wood', 'metal', 'fabric')
        :param style: Style of the furniture (e.g., 'modern', 'classic', 'rustic')
        """
        self.material = material
        self.style = style

    def describe(self):
        """
        Prints the description of the furniture.
        """
        print(f"This piece of furniture is made of {self.material} and designed in {self.style} style.")


class SettledCollection:
    """
    Combines elements of fireplace and furniture into a single hybrid design.
    """
    def __init__(self, fireplace: Fireplace, furniture: Furniture):
        """
        Initializes the Settled Collection with a fireplace and furniture.

        :param fireplace: Fireplace object
        :param furniture: Furniture object
        """
        self.fireplace = fireplace
        self.furniture = furniture

    def display_details(self):
        """
        Displays the details of the Settled Collection.
        """
        print("Settled Collection Details:")
        self.furniture.describe()
        print(f"The fireplace provides {self.fireplace.heat_output} BTUs of heat and uses {self.fireplace.fuel_type} fuel.")

    def use_fireplace(self):
        """
        Simulates using the fireplace in the hybrid design.
        """
        try:
            self.fireplace.ignite()
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize fireplace and furniture objects
    fireplace = Fireplace(heat_output=random.randint(5000, 15000), fuel_type="electric")
    furniture = Furniture(material="wood", style="modern")

    # Create SettledCollection object
    settled_collection = SettledCollection(fireplace=fireplace, furniture=furniture)

    # Display details and simulate usage
    settled_collection.display_details()
    settled_collection.use_fireplace()
    settled_collection.fireplace.adjust_heat(new_heat_output=10000)
```
