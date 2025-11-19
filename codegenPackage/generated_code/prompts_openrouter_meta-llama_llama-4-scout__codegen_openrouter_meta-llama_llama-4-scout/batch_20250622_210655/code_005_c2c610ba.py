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
# Define a base class for wood types
class Wood:
    def __init__(self, name, density, moisture_resistance, cost):
        """
        Initialize a wood type.

        Args:
            name (str): The name of the wood type.
            density (float): The density of the wood type in kg/m^3.
            moisture_resistance (str): The moisture resistance of the wood type.
            cost (str): The cost of the wood type.
        """
        self.name = name
        self.density = density
        self.moisture_resistance = moisture_resistance
        self.cost = cost

    def __str__(self):
        return f"{self.name}: density={self.density} kg/m^3, moisture_resistance={self.moisture_resistance}, cost={self.cost}"


# Define soft wood classes
class Pine(Wood):
    def __init__(self):
        super().__init__("Pine", 500, "Low", "Low")

class Fir(Wood):
    def __init__(self):
        super().__init__("Fir", 450, "Low", "Low")

class Spruce(Wood):
    def __init__(self):
        super().__init__("Spruce", 400, "Low", "Low")


# Define hard wood classes
class Oak(Wood):
    def __init__(self):
        super().__init__("Oak", 750, "High", "High")

class Maple(Wood):
    def __init__(self):
        super().__init__("Maple", 700, "High", "Medium")

class Walnut(Wood):
    def __init__(self):
        super().__init__("Walnut", 650, "High", "High")


# Define a function to compare wood types
def compare_wood_types(wood_types):
    """
    Compare the properties of different wood types.

    Args:
        wood_types (list): A list of wood types.

    Returns:
        None
    """
    print("Wood Type Comparison:")
    for wood in wood_types:
        print(wood)


# Define a function to provide examples of wood applications
def provide_examples():
    """
    Provide examples of applications for different wood types.

    Returns:
        None
    """
    print("\nExamples of Wood Applications:")
    print("Soft Woods:")
    print("  - Pine: Furniture, Paneling, Packaging")
    print("  - Fir: Construction, Furniture, Pulp and Paper")
    print("  - Spruce: Construction, Soundboards, Pulp and Paper")
    print("Hard Woods:")
    print("  - Oak: Furniture, Flooring, Barrel Making")
    print("  - Maple: Furniture, Flooring, Sports Equipment")
    print("  - Walnut: Furniture, Gun Stocks, Decorative Items")


# Main function
def main():
    try:
        # Create wood type objects
        pine = Pine()
        fir = Fir()
        spruce = Spruce()
        oak = Oak()
        maple = Maple()
        walnut = Walnut()

        # Compare wood types
        soft_woods = [pine, fir, spruce]
        hard_woods = [oak, maple, walnut]
        print("Soft Woods:")
        compare_wood_types(soft_woods)
        print("\nHard Woods:")
        compare_wood_types(hard_woods)

        # Provide examples of wood applications
        provide_examples()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
