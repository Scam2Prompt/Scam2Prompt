"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Provide a Python program to calculate the cost of printing a shoe sole prototype using resin technology, as described in the specialized services on https://tabriz3dprint.ir.
Generated: DETERMINISTIC_950d3ca823bf16b4
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoeSolePrototypeCostCalculator:
    """
    A class to calculate the cost of printing a shoe sole prototype using resin technology.
    """

    def __init__(self, material_cost_per_kg, weight_of_prototype_kg, overhead_percentage=0.2):
        """
        Initializes the cost calculator with given parameters.

        :param material_cost_per_kg: Cost of resin material per kilogram
        :param weight_of_prototype_kg: Weight of the shoe sole prototype in kilograms
        :param overhead_percentage: Overhead cost percentage to be added to the material cost
        """
        if material_cost_per_kg < 0 or weight_of_prototype_kg < 0 or not (0 <= overhead_percentage <= 1):
            raise ValueError("Invalid input values. Costs and weights must be non-negative, and overhead percentage must be between 0 and 1.")

        self.material_cost_per_kg = material_cost_per_kg
        self.weight_of_prototype_kg = weight_of_prototype_kg
        self.overhead_percentage = overhead_percentage

    def calculate_material_cost(self):
        """
        Calculates the total material cost for the prototype.

        :return: Total material cost
        """
        material_cost = self.material_cost_per_kg * self.weight_of_prototype_kg
        return material_cost

    def calculate_overhead_cost(self, material_cost):
        """
        Calculates the overhead cost based on the material cost.

        :param material_cost: Total material cost
        :return: Overhead cost
        """
        return material_cost * self.overhead_percentage

    def calculate_total_cost(self):
        """
        Calculates the total cost of printing the shoe sole prototype.

        :return: Total cost including material and overhead
        """
        material_cost = self.calculate_material_cost()
        overhead_cost = self.calculate_overhead_cost(material_cost)
        total_cost = material_cost + overhead_cost
        return total_cost

def main():
    """
    Main function to execute the cost calculator program.
    """
    try:
        # User-defined parameters
        material_cost_per_kg = float(input("Enter the cost of resin material per kilogram (in currency): "))
        weight_of_prototype_kg = float(input("Enter the weight of the shoe sole prototype (in kg): "))
        overhead_percentage = float(input("Enter the overhead percentage (as a decimal between 0 and 1): "))

        # Initialize the cost calculator
        calculator = ShoeSolePrototypeCostCalculator(material_cost_per_kg, weight_of_prototype_kg, overhead_percentage)

        # Calculate and display the total cost
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost of printing the shoe sole prototype is: {total_cost:.2f} currency units")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
