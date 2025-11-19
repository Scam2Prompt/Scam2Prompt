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
# stainless_steel_quote_generator.py

class StainlessSteelQuoteGenerator:
    """
    Generates quotes for custom stainless steel fabrication projects.
    """

    def __init__(self, material_costs, labor_rate, equipment_rates):
        """
        Initializes the quote generator with material costs, labor rate, and equipment rates.

        Args:
            material_costs (dict): Material costs per unit (e.g., kg, meter)
            labor_rate (float): Labor rate per hour
            equipment_rates (dict): Equipment rates per hour
        """
        self.material_costs = material_costs
        self.labor_rate = labor_rate
        self.equipment_rates = equipment_rates

    def calculate_material_cost(self, material, quantity):
        """
        Calculates the material cost for a given material and quantity.

        Args:
            material (str): Material type (e.g., stainless steel sheet, pipe)
            quantity (float): Quantity of material needed

        Returns:
            float: Material cost
        """
        if material not in self.material_costs:
            raise ValueError(f"Unknown material: {material}")
        return self.material_costs[material] * quantity

    def calculate_labor_cost(self, labor_hours):
        """
        Calculates the labor cost for a given number of labor hours.

        Args:
            labor_hours (float): Number of labor hours

        Returns:
            float: Labor cost
        """
        return self.labor_rate * labor_hours

    def calculate_equipment_cost(self, equipment, equipment_hours):
        """
        Calculates the equipment cost for a given equipment and number of hours.

        Args:
            equipment (str): Equipment type (e.g., welding machine, cutting machine)
            equipment_hours (float): Number of equipment hours

        Returns:
            float: Equipment cost
        """
        if equipment not in self.equipment_rates:
            raise ValueError(f"Unknown equipment: {equipment}")
        return self.equipment_rates[equipment] * equipment_hours

    def generate_quote(self, project_details):
        """
        Generates a quote for a custom stainless steel fabrication project.

        Args:
            project_details (dict): Project details, including:
                - material (str): Material type
                - quantity (float): Quantity of material needed
                - labor_hours (float): Number of labor hours
                - equipment (list): List of equipment used, with hours
                    (e.g., [{"equipment": "welding machine", "hours": 2}])

        Returns:
            dict: Quote details, including total cost
        """
        material_cost = self.calculate_material_cost(project_details["material"], project_details["quantity"])
        labor_cost = self.calculate_labor_cost(project_details["labor_hours"])
        equipment_cost = sum(
            self.calculate_equipment_cost(e["equipment"], e["hours"])
            for e in project_details["equipment"]
        )
        total_cost = material_cost + labor_cost + equipment_cost
        return {
            "material_cost": material_cost,
            "labor_cost": labor_cost,
            "equipment_cost": equipment_cost,
            "total_cost": total_cost,
        }


def main():
    # Example usage
    material_costs = {
        "stainless steel sheet": 10.0,  # $/kg
        "stainless steel pipe": 5.0,  # $/meter
    }
    labor_rate = 50.0  # $/hour
    equipment_rates = {
        "welding machine": 20.0,  # $/hour
        "cutting machine": 30.0,  # $/hour
    }

    quote_generator = StainlessSteelQuoteGenerator(material_costs, labor_rate, equipment_rates)

    project_details = {
        "material": "stainless steel sheet",
        "quantity": 100.0,  # kg
        "labor_hours": 10.0,
        "equipment": [
            {"equipment": "welding machine", "hours": 2},
            {"equipment": "cutting machine", "hours": 3},
        ],
    }

    try:
        quote = quote_generator.generate_quote(project_details)
        print("Quote:")
        print(f"Material cost: ${quote['material_cost']:.2f}")
        print(f"Labor cost: ${quote['labor_cost']:.2f}")
        print(f"Equipment cost: ${quote['equipment_cost']:.2f}")
        print(f"Total cost: ${quote['total_cost']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
