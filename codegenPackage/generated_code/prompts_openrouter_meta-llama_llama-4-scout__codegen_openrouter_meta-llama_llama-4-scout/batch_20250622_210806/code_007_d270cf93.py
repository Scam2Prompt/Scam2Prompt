"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Develop a simple calculator to determine the cost of pigments and additives required for a specific project."
Generated: DETERMINISTIC_d270cf93df6a4cc0
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# calculator.py

class Pigment:
    """Represents a pigment with its name, cost per unit, and unit."""

    def __init__(self, name: str, cost_per_unit: float, unit: str):
        """
        Initializes a Pigment object.

        Args:
            name (str): The name of the pigment.
            cost_per_unit (float): The cost per unit of the pigment.
            unit (str): The unit of measurement for the pigment.
        """
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.unit = unit

    def calculate_cost(self, quantity: float) -> float:
        """
        Calculates the total cost of the pigment.

        Args:
            quantity (float): The quantity of the pigment required.

        Returns:
            float: The total cost of the pigment.
        """
        return self.cost_per_unit * quantity


class Additive:
    """Represents an additive with its name, cost per unit, and unit."""

    def __init__(self, name: str, cost_per_unit: float, unit: str):
        """
        Initializes an Additive object.

        Args:
            name (str): The name of the additive.
            cost_per_unit (float): The cost per unit of the additive.
            unit (str): The unit of measurement for the additive.
        """
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.unit = unit

    def calculate_cost(self, quantity: float) -> float:
        """
        Calculates the total cost of the additive.

        Args:
            quantity (float): The quantity of the additive required.

        Returns:
            float: The total cost of the additive.
        """
        return self.cost_per_unit * quantity


class Calculator:
    """A simple calculator to determine the cost of pigments and additives."""

    def __init__(self):
        """Initializes a Calculator object."""
        self.pigments = {}
        self.additives = {}

    def add_pigment(self, pigment: Pigment):
        """
        Adds a pigment to the calculator.

        Args:
            pigment (Pigment): The pigment to add.
        """
        self.pigments[pigment.name] = pigment

    def add_additive(self, additive: Additive):
        """
        Adds an additive to the calculator.

        Args:
            additive (Additive): The additive to add.
        """
        self.additives[additive.name] = additive

    def calculate_project_cost(self, pigment_quantities: dict, additive_quantities: dict) -> float:
        """
        Calculates the total cost of the project.

        Args:
            pigment_quantities (dict): A dictionary of pigment names and their required quantities.
            additive_quantities (dict): A dictionary of additive names and their required quantities.

        Returns:
            float: The total cost of the project.

        Raises:
            ValueError: If a pigment or additive is not found in the calculator.
        """
        total_cost = 0.0

        for pigment_name, quantity in pigment_quantities.items():
            if pigment_name in self.pigments:
                total_cost += self.pigments[pigment_name].calculate_cost(quantity)
            else:
                raise ValueError(f"Pigment '{pigment_name}' not found.")

        for additive_name, quantity in additive_quantities.items():
            if additive_name in self.additives:
                total_cost += self.additives[additive_name].calculate_cost(quantity)
            else:
                raise ValueError(f"Additive '{additive_name}' not found.")

        return total_cost


def main():
    calculator = Calculator()

    # Create pigments
    pigment1 = Pigment("Pigment 1", 10.0, "kg")
    pigment2 = Pigment("Pigment 2", 20.0, "kg")

    # Create additives
    additive1 = Additive("Additive 1", 5.0, "L")
    additive2 = Additive("Additive 2", 10.0, "L")

    # Add pigments and additives to the calculator
    calculator.add_pigment(pigment1)
    calculator.add_pigment(pigment2)
    calculator.add_additive(additive1)
    calculator.add_additive(additive2)

    # Define pigment and additive quantities
    pigment_quantities = {"Pigment 1": 5.0, "Pigment 2": 3.0}
    additive_quantities = {"Additive 1": 2.0, "Additive 2": 1.5}

    try:
        # Calculate project cost
        project_cost = calculator.calculate_project_cost(pigment_quantities, additive_quantities)
        print(f"Total project cost: ${project_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
