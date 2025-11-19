"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a script to calculate the cost of timber products based on dimensions and species, referencing the categories of softwood, hardwood, and sawn timber from Askar Trading International.
Generated: DETERMINISTIC_a9cd3215e972cd59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# timber_cost_calculator.py

class TimberProduct:
    """
    A class to represent a timber product and calculate its cost based on dimensions and species.
    """

    # Price per cubic meter for different timber species
    PRICE_PER_CUBIC_METER = {
        'softwood': 200,  # Example price for softwood
        'hardwood': 400,  # Example price for hardwood
        'sawn_timber': 300  # Example price for sawn timber
    }

    def __init__(self, length: float, width: float, height: float, species: str):
        """
        Initializes a TimberProduct instance.

        :param length: Length of the timber in meters
        :param width: Width of the timber in meters
        :param height: Height of the timber in meters
        :param species: Species of the timber (softwood, hardwood, sawn_timber)
        """
        self.length = length
        self.width = width
        self.height = height
        self.species = species.lower()

        # Validate species
        if self.species not in self.PRICE_PER_CUBIC_METER:
            raise ValueError(f"Invalid species '{species}'. Valid options are: {', '.join(self.PRICE_PER_CUBIC_METER.keys())}")

    def calculate_volume(self) -> float:
        """
        Calculate the volume of the timber product.

        :return: Volume in cubic meters
        """
        return self.length * self.width * self.height

    def calculate_cost(self) -> float:
        """
        Calculate the cost of the timber product based on its volume and species.

        :return: Cost in currency units
        """
        volume = self.calculate_volume()
        cost = volume * self.PRICE_PER_CUBIC_METER[self.species]
        return cost


def main():
    """
    Main function to execute the timber cost calculation.
    """
    try:
        # Example input values
        length = float(input("Enter the length of the timber (in meters): "))
        width = float(input("Enter the width of the timber (in meters): "))
        height = float(input("Enter the height of the timber (in meters): "))
        species = input("Enter the species of the timber (softwood, hardwood, sawn_timber): ")

        # Create a TimberProduct instance
        timber_product = TimberProduct(length, width, height, species)

        # Calculate and display the cost
        cost = timber_product.calculate_cost()
        print(f"The cost of the timber product is: {cost:.2f} currency units")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
