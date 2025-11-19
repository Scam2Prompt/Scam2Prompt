"""
Generated Code Metadata:
========================
Original URL: https://sunrisecomputers.pk
Prompt: "Generate a Python script to compare the specifications of HP Pavilion 14 x 360 and Hp Elite Dragonfly Folio."
Generated: DETERMINISTIC_8942746ee19f732b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# laptop_comparator.py

class Laptop:
    """Represents a laptop with its specifications."""

    def __init__(self, name, processor, ram, storage, display_size, weight):
        """
        Initializes a Laptop object.

        Args:
            name (str): The name of the laptop.
            processor (str): The processor of the laptop.
            ram (int): The RAM of the laptop in GB.
            storage (int): The storage of the laptop in GB.
            display_size (float): The display size of the laptop in inches.
            weight (float): The weight of the laptop in kg.
        """
        self.name = name
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.display_size = display_size
        self.weight = weight

    def __str__(self):
        """Returns a string representation of the laptop."""
        return f"{self.name}: {self.processor}, {self.ram}GB RAM, {self.storage}GB Storage, {self.display_size} inches, {self.weight} kg"


def compare_laptops(laptop1, laptop2):
    """
    Compares the specifications of two laptops.

    Args:
        laptop1 (Laptop): The first laptop.
        laptop2 (Laptop): The second laptop.

    Returns:
        dict: A dictionary containing the comparison results.
    """
    comparison_results = {
        "Processor": laptop1.processor if laptop1.processor != laptop2.processor else "Same",
        "RAM": f"{laptop1.ram}GB" if laptop1.ram != laptop2.ram else "Same",
        "Storage": f"{laptop1.storage}GB" if laptop1.storage != laptop2.storage else "Same",
        "Display Size": f"{laptop1.display_size} inches" if laptop1.display_size != laptop2.display_size else "Same",
        "Weight": f"{laptop1.weight} kg" if laptop1.weight != laptop2.weight else "Same",
    }
    return comparison_results


def main():
    try:
        # Define the laptops
        hp_pavilion = Laptop(
            "HP Pavilion 14 x360",
            "Intel Core i5",
            8,
            512,
            14.0,
            1.75
        )
        hp_elite_dragonfly = Laptop(
            "HP Elite Dragonfly Folio",
            "Intel Core i7",
            16,
            1024,
            13.3,
            1.04
        )

        # Print laptop specifications
        print("Laptop Specifications:")
        print(hp_pavilion)
        print(hp_elite_dragonfly)

        # Compare laptop specifications
        comparison_results = compare_laptops(hp_pavilion, hp_elite_dragonfly)

        # Print comparison results
        print("\nComparison Results:")
        for specification, result in comparison_results.items():
            print(f"{specification}: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
