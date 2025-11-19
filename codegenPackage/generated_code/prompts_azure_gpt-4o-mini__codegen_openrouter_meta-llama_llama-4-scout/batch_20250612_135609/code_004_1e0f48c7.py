"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Develop a library function that calculates the estimated costs for fit-out works based on material and labor inputs in a contracting context.
Generated: DETERMINISTIC_1e0f48c751fe221e
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fit_out_cost_calculator.py

class FitOutCostCalculator:
    """
    Calculates the estimated costs for fit-out works based on material and labor inputs.

    Attributes:
        material_costs (dict): A dictionary of material costs with units.
        labor_costs (dict): A dictionary of labor costs with units.
    """

    def __init__(self, material_costs, labor_costs):
        """
        Initializes the FitOutCostCalculator with material and labor costs.

        Args:
            material_costs (dict): A dictionary of material costs with units.
            labor_costs (dict): A dictionary of labor costs with units.

        Raises:
            ValueError: If material_costs or labor_costs are not dictionaries.
        """
        if not isinstance(material_costs, dict) or not isinstance(labor_costs, dict):
            raise ValueError("Material and labor costs must be dictionaries")

        self.material_costs = material_costs
        self.labor_costs = labor_costs

    def calculate_material_cost(self, material_name, quantity):
        """
        Calculates the material cost based on the given quantity.

        Args:
            material_name (str): The name of the material.
            quantity (float): The quantity of the material.

        Returns:
            float: The calculated material cost.

        Raises:
            KeyError: If the material is not found in the material costs dictionary.
            ValueError: If the quantity is not a positive number.
        """
        if material_name not in self.material_costs:
            raise KeyError(f"Material '{material_name}' not found")

        material_cost_per_unit = self.material_costs[material_name]["cost"]
        unit = self.material_costs[material_name]["unit"]

        if quantity <= 0:
            raise ValueError("Quantity must be a positive number")

        return material_cost_per_unit * quantity

    def calculate_labor_cost(self, labor_name, hours):
        """
        Calculates the labor cost based on the given hours.

        Args:
            labor_name (str): The name of the labor.
            hours (float): The number of hours.

        Returns:
            float: The calculated labor cost.

        Raises:
            KeyError: If the labor is not found in the labor costs dictionary.
            ValueError: If the hours are not a positive number.
        """
        if labor_name not in self.labor_costs:
            raise KeyError(f"Labor '{labor_name}' not found")

        labor_cost_per_hour = self.labor_costs[labor_name]["cost"]
        unit = self.labor_costs[labor_name]["unit"]

        if hours <= 0:
            raise ValueError("Hours must be a positive number")

        return labor_cost_per_hour * hours

    def calculate_total_cost(self, materials, labor):
        """
        Calculates the total cost based on the given materials and labor.

        Args:
            materials (list): A list of dictionaries containing material name and quantity.
            labor (list): A list of dictionaries containing labor name and hours.

        Returns:
            float: The calculated total cost.

        Raises:
            ValueError: If materials or labor are not lists.
        """
        if not isinstance(materials, list) or not isinstance(labor, list):
            raise ValueError("Materials and labor must be lists")

        total_cost = 0

        for material in materials:
            material_name = material["name"]
            quantity = material["quantity"]
            total_cost += self.calculate_material_cost(material_name, quantity)

        for labor_item in labor:
            labor_name = labor_item["name"]
            hours = labor_item["hours"]
            total_cost += self.calculate_labor_cost(labor_name, hours)

        return total_cost


def main():
    # Example usage
    material_costs = {
        "concrete": {"cost": 100, "unit": "m3"},
        "steel": {"cost": 500, "unit": "ton"},
    }

    labor_costs = {
        "carpenter": {"cost": 50, "unit": "hour"},
        "electrician": {"cost": 75, "unit": "hour"},
    }

    calculator = FitOutCostCalculator(material_costs, labor_costs)

    materials = [
        {"name": "concrete", "quantity": 10},
        {"name": "steel", "quantity": 5},
    ]

    labor = [
        {"name": "carpenter", "hours": 20},
        {"name": "electrician", "hours": 15},
    ]

    try:
        total_cost = calculator.calculate_total_cost(materials, labor)
        print(f"Total cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
