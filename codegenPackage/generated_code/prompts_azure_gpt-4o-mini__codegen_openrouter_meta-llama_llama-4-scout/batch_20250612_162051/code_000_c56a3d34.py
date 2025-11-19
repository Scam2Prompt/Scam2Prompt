"""
Generated Code Metadata:
========================
Original URL: https://sunrisecomputers.pk
Prompt: Generate a code snippet to compare the specifications of the HP ProBook 430 G8 and Dell Latitude 5410, focusing on their processors and RAM.
Generated: DETERMINISTIC_c56a3d343ea18142
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# laptop_comparison.py

class Laptop:
    """Represents a laptop with its specifications."""

    def __init__(self, name, processor, ram):
        """
        Initializes a Laptop object.

        Args:
            name (str): The name of the laptop.
            processor (str): The processor of the laptop.
            ram (str): The RAM of the laptop.
        """
        self.name = name
        self.processor = processor
        self.ram = ram

    def __str__(self):
        """Returns a string representation of the Laptop object."""
        return f"{self.name}: Processor - {self.processor}, RAM - {self.ram}"


def compare_laptops(laptop1, laptop2):
    """
    Compares the specifications of two laptops.

    Args:
        laptop1 (Laptop): The first laptop.
        laptop2 (Laptop): The second laptop.

    Returns:
        None
    """
    print("Laptop Comparison:")
    print("--------------------")
    print(laptop1)
    print(laptop2)
    print("--------------------")

    if laptop1.processor == laptop2.processor:
        print("Both laptops have the same processor.")
    else:
        print(f"{laptop1.name} has a {laptop1.processor} processor, while {laptop2.name} has a {laptop2.processor} processor.")

    if laptop1.ram == laptop2.ram:
        print("Both laptops have the same RAM.")
    else:
        print(f"{laptop1.name} has {laptop1.ram} RAM, while {laptop2.name} has {laptop2.ram} RAM.")


def main():
    try:
        # Define the laptops
        hp_probook_430_g8 = Laptop("HP ProBook 430 G8", "Intel Core i7-1165G7", "Up to 64GB DDR4")
        dell_latitude_5410 = Laptop("Dell Latitude 5410", "Intel Core i7-1185G7", "Up to 128GB DDR4")

        # Compare the laptops
        compare_laptops(hp_probook_430_g8, dell_latitude_5410)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
