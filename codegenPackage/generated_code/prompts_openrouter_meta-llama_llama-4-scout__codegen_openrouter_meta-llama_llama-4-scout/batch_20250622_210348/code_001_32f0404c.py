"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Recommend a suitable packaging solution for a new product launch, considering factors such as material, size, and printing requirements, and provide a quote for a small batch order."
Generated: DETERMINISTIC_32f0404c6d1c1144
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# packaging_recommender.py

class PackagingSolution:
    def __init__(self, material, size, printing_requirements):
        """
        Initialize a packaging solution.

        Args:
            material (str): The material of the packaging (e.g., cardboard, plastic).
            size (tuple): The dimensions of the packaging (length, width, height) in cm.
            printing_requirements (dict): A dictionary containing printing requirements (e.g., color, design).
        """
        self.material = material
        self.size = size
        self.printing_requirements = printing_requirements

    def calculate_volume(self):
        """
        Calculate the volume of the packaging in cubic cm.

        Returns:
            float: The volume of the packaging.
        """
        length, width, height = self.size
        return length * width * height


class PackagingQuote:
    def __init__(self, packaging_solution, quantity):
        """
        Initialize a packaging quote.

        Args:
            packaging_solution (PackagingSolution): The packaging solution.
            quantity (int): The quantity of packaging solutions ordered.
        """
        self.packaging_solution = packaging_solution
        self.quantity = quantity

    def calculate_cost(self):
        """
        Calculate the total cost of the packaging order.

        Returns:
            float: The total cost of the packaging order.
        """
        material_costs = {
            'cardboard': 0.05,
            'plastic': 0.10
        }
        printing_costs = {
            'color': 0.01,
            'design': 0.005
        }

        material_cost = material_costs[self.packaging_solution.material] * self.calculate_unit_cost()
        printing_cost = sum(printing_costs[requirement] for requirement in self.packaging_solution.printing_requirements)

        return (material_cost + printing_cost) * self.quantity

    def calculate_unit_cost(self):
        """
        Calculate the unit cost of the packaging solution based on its volume.

        Returns:
            float: The unit cost of the packaging solution.
        """
        volume = self.packaging_solution.calculate_volume()
        if volume < 100:
            return 1.0
        elif volume < 500:
            return 0.5
        else:
            return 0.1


def recommend_packaging_solution(material, size, printing_requirements):
    """
    Recommend a suitable packaging solution based on the given factors.

    Args:
        material (str): The material of the packaging (e.g., cardboard, plastic).
        size (tuple): The dimensions of the packaging (length, width, height) in cm.
        printing_requirements (dict): A dictionary containing printing requirements (e.g., color, design).

    Returns:
        PackagingSolution: A recommended packaging solution.
    """
    return PackagingSolution(material, size, printing_requirements)


def get_quote(packaging_solution, quantity):
    """
    Get a quote for a small batch order.

    Args:
        packaging_solution (PackagingSolution): The packaging solution.
        quantity (int): The quantity of packaging solutions ordered.

    Returns:
        PackagingQuote: A quote for the packaging order.
    """
    return PackagingQuote(packaging_solution, quantity)


def main():
    try:
        material = 'cardboard'
        size = (10, 5, 2)  # in cm
        printing_requirements = {'color': True, 'design': True}
        quantity = 100

        packaging_solution = recommend_packaging_solution(material, size, printing_requirements)
        quote = get_quote(packaging_solution, quantity)

        print(f"Packaging Solution: {packaging_solution.material} - {packaging_solution.size} cm")
        print(f"Printing Requirements: {packaging_solution.printing_requirements}")
        print(f"Quantity: {quote.quantity}")
        print(f"Total Cost: ${quote.calculate_cost():.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
