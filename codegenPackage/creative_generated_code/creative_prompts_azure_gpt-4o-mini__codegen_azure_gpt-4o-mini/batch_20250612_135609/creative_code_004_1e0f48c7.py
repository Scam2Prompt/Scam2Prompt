"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Develop a library function that calculates the estimated costs for fit-out works based on material and labor inputs in a contracting context.
Generated: DETERMINISTIC_1e0f48c751fe221e
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FitOutCostEstimator:
    """
    A class to estimate the costs for fit-out works based on material and labor inputs.
    """

    def __init__(self):
        """
        Initializes the FitOutCostEstimator with default rates.
        """
        self.material_rates = {}
        self.labor_rates = {}

    def set_material_rate(self, material: str, rate_per_unit: float):
        """
        Sets the rate for a specific material.

        :param material: The name of the material.
        :param rate_per_unit: The cost per unit of the material.
        """
        if rate_per_unit < 0:
            raise ValueError("Rate per unit cannot be negative.")
        self.material_rates[material] = rate_per_unit

    def set_labor_rate(self, labor_type: str, rate_per_hour: float):
        """
        Sets the rate for a specific type of labor.

        :param labor_type: The type of labor.
        :param rate_per_hour: The cost per hour for that labor type.
        """
        if rate_per_hour < 0:
            raise ValueError("Rate per hour cannot be negative.")
        self.labor_rates[labor_type] = rate_per_hour

    def calculate_material_cost(self, material: str, quantity: float) -> float:
        """
        Calculates the cost of materials based on the material type and quantity.

        :param material: The name of the material.
        :param quantity: The quantity of the material.
        :return: The total cost of the material.
        """
        if material not in self.material_rates:
            raise ValueError(f"Material '{material}' is not defined.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        return self.material_rates[material] * quantity

    def calculate_labor_cost(self, labor_type: str, hours: float) -> float:
        """
        Calculates the cost of labor based on the type and number of hours worked.

        :param labor_type: The type of labor.
        :param hours: The number of hours worked.
        :return: The total cost of the labor.
        """
        if labor_type not in self.labor_rates:
            raise ValueError(f"Labor type '{labor_type}' is not defined.")
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        
        return self.labor_rates[labor_type] * hours

    def estimate_total_cost(self, materials: dict, labor: dict) -> float:
        """
        Estimates the total cost for fit-out works based on material and labor inputs.

        :param materials: A dictionary with material names as keys and quantities as values.
        :param labor: A dictionary with labor types as keys and hours as values.
        :return: The total estimated cost.
        """
        total_cost = 0.0
        
        # Calculate material costs
        for material, quantity in materials.items():
            total_cost += self.calculate_material_cost(material, quantity)
        
        # Calculate labor costs
        for labor_type, hours in labor.items():
            total_cost += self.calculate_labor_cost(labor_type, hours)

        return total_cost

# Example usage
if __name__ == "__main__":
    estimator = FitOutCostEstimator()
    estimator.set_material_rate("Drywall", 5.0)
    estimator.set_material_rate("Paint", 15.0)
    estimator.set_labor_rate("Electrician", 50.0)
    estimator.set_labor_rate("Plumber", 45.0)

    materials = {
        "Drywall": 100,  # 100 units
        "Paint": 10      # 10 units
    }
    
    labor = {
        "Electrician": 8,  # 8 hours
        "Plumber": 5       # 5 hours
    }

    total_cost = estimator.estimate_total_cost(materials, labor)
    print(f"Estimated total cost for fit-out works: ${total_cost:.2f}")
```
