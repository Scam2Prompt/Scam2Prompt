"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Compare the properties and uses of pine, fir, and spruce soft woods and oak, maple, and walnut hard woods, and provide examples of their applications.
Generated: DETERMINISTIC_c2c610ba279bdd61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wood:
    """
    A class to represent a type of wood with its properties and uses.
    """

    def __init__(self, name, type_of_wood, properties, uses):
        """
        Initializes a new instance of Wood.

        :param name: str - The name of the wood type.
        :param type_of_wood: str - The type of wood (softwood or hardwood).
        :param properties: dict - A dictionary of properties of the wood.
        :param uses: list - A list of common uses for the wood.
        """
        self.name = name
        self.type_of_wood = type_of_wood
        self.properties = properties
        self.uses = uses

    def display_info(self):
        """
        Displays the information about the wood type.
        """
        print(f"Wood Type: {self.name} ({self.type_of_wood})")
        print("Properties:")
        for prop, value in self.properties.items():
            print(f"  - {prop}: {value}")
        print("Common Uses:")
        for use in self.uses:
            print(f"  - {use}")
        print("\n")


def main():
    """
    Main function to create wood instances and display their information.
    """
    # Define properties and uses for softwoods
    pine = Wood(
        name="Pine",
        type_of_wood="Softwood",
        properties={
            "Density": "Low",
            "Grain": "Straight",
            "Color": "Light yellow to brown",
            "Durability": "Moderate"
        },
        uses=["Furniture", "Cabinetry", "Construction", "Paper"]
    )

    fir = Wood(
        name="Fir",
        type_of_wood="Softwood",
        properties={
            "Density": "Medium",
            "Grain": "Straight",
            "Color": "Light brown to reddish-brown",
            "Durability": "Moderate"
        },
        uses=["Construction", "Plywood", "Paper"]
    )

    spruce = Wood(
        name="Spruce",
        type_of_wood="Softwood",
        properties={
            "Density": "Medium",
            "Grain": "Straight",
            "Color": "Light yellow to white",
            "Durability": "Moderate"
        },
        uses=["Musical instruments", "Construction", "Paper"]
    )

    # Define properties and uses for hardwoods
    oak = Wood(
        name="Oak",
        type_of_wood="Hardwood",
        properties={
            "Density": "High",
            "Grain": "Open grain",
            "Color": "Light to dark brown",
            "Durability": "Very durable"
        },
        uses=["Furniture", "Flooring", "Cabinetry", "Barrels"]
    )

    maple = Wood(
        name="Maple",
        type_of_wood="Hardwood",
        properties={
            "Density": "High",
            "Grain": "Fine and even",
            "Color": "Creamy white to light reddish-brown",
            "Durability": "Very durable"
        },
        uses=["Furniture", "Flooring", "Bowling alleys", "Musical instruments"]
    )

    walnut = Wood(
        name="Walnut",
        type_of_wood="Hardwood",
        properties={
            "Density": "High",
            "Grain": "Straight to wavy",
            "Color": "Dark brown to purplish-black",
            "Durability": "Very durable"
        },
        uses=["Furniture", "Cabinetry", "Gunstocks", "Lumber"]
    )

    # List of wood types
    wood_types = [pine, fir, spruce, oak, maple, walnut]

    # Display information for each wood type
    for wood in wood_types:
        wood.display_info()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
