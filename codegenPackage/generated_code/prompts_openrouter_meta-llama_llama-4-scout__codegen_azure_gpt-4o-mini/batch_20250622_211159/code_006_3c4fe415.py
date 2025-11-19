"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Write a code snippet to automate the process of generating quotes for custom stainless steel fabrication projects, considering factors like material cost, labor, and equipment usage."
Generated: DETERMINISTIC_3c4fe415e69b5118
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from decimal import Decimal, InvalidOperation

class QuoteGenerator:
    def __init__(self, material_cost_per_kg, labor_cost_per_hour, equipment_cost_per_hour):
        """
        Initialize the QuoteGenerator with cost parameters.

        :param material_cost_per_kg: Cost of stainless steel per kilogram
        :param labor_cost_per_hour: Cost of labor per hour
        :param equipment_cost_per_hour: Cost of equipment usage per hour
        """
        self.material_cost_per_kg = Decimal(material_cost_per_kg)
        self.labor_cost_per_hour = Decimal(labor_cost_per_hour)
        self.equipment_cost_per_hour = Decimal(equipment_cost_per_hour)

    def calculate_material_cost(self, weight_kg):
        """
        Calculate the material cost based on weight.

        :param weight_kg: Weight of the stainless steel in kilograms
        :return: Material cost as Decimal
        """
        return self.material_cost_per_kg * Decimal(weight_kg)

    def calculate_labor_cost(self, hours):
        """
        Calculate the labor cost based on hours worked.

        :param hours: Number of hours worked
        :return: Labor cost as Decimal
        """
        return self.labor_cost_per_hour * Decimal(hours)

    def calculate_equipment_cost(self, hours):
        """
        Calculate the equipment cost based on hours used.

        :param hours: Number of hours equipment is used
        :return: Equipment cost as Decimal
        """
        return self.equipment_cost_per_hour * Decimal(hours)

    def generate_quote(self, weight_kg, labor_hours, equipment_hours):
        """
        Generate a quote for the fabrication project.

        :param weight_kg: Weight of the stainless steel in kilograms
        :param labor_hours: Number of labor hours
        :param equipment_hours: Number of equipment hours
        :return: Total quote as a dictionary
        """
        try:
            material_cost = self.calculate_material_cost(weight_kg)
            labor_cost = self.calculate_labor_cost(labor_hours)
            equipment_cost = self.calculate_equipment_cost(equipment_hours)

            total_cost = material_cost + labor_cost + equipment_cost

            quote = {
                "material_cost": str(material_cost),
                "labor_cost": str(labor_cost),
                "equipment_cost": str(equipment_cost),
                "total_cost": str(total_cost)
            }

            return quote

        except InvalidOperation as e:
            raise ValueError("Invalid input for cost calculation: {}".format(e))

def main():
    # Example parameters for the quote generator
    material_cost_per_kg = "2.50"  # Cost per kg of stainless steel
    labor_cost_per_hour = "20.00"   # Labor cost per hour
    equipment_cost_per_hour = "15.00"  # Equipment cost per hour

    # Create an instance of QuoteGenerator
    quote_generator = QuoteGenerator(material_cost_per_kg, labor_cost_per_hour, equipment_cost_per_hour)

    # Example project parameters
    weight_kg = 100  # Weight of stainless steel in kg
    labor_hours = 5  # Labor hours required
    equipment_hours = 3  # Equipment hours required

    # Generate the quote
    quote = quote_generator.generate_quote(weight_kg, labor_hours, equipment_hours)

    # Output the quote in JSON format
    print(json.dumps(quote, indent=4))

if __name__ == "__main__":
    main()
```
