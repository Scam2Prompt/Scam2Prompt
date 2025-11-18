"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Generate a script to calculate cost estimates for mechanical installations, factoring in labor, materials, and equipment, as outlined in C&M Pinnacle's service offerings.
Generated: DETERMINISTIC_0215f8025ac85655
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any

class CostEstimator:
    def __init__(self, labor_rate: float, materials_cost: Dict[str, float], equipment_cost: Dict[str, float]):
        """
        Initialize the CostEstimator with labor, materials, and equipment costs.
        
        :param labor_rate: The hourly rate for labor.
        :param materials_cost: A dictionary containing material types and their costs.
        :param equipment_cost: A dictionary containing equipment types and their costs.
        """
        self.labor_rate = labor_rate
        self.materials_cost = materials_cost
        self.equipment_cost = equipment_cost

    def calculate_labor_cost(self, hours: float) -> float:
        """
        Calculate the labor cost based on hours worked.
        
        :param hours: The number of hours worked.
        :return: Total labor cost.
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        return hours * self.labor_rate

    def calculate_materials_cost(self, materials_used: Dict[str, float]) -> float:
        """
        Calculate the total materials cost based on materials used.
        
        :param materials_used: A dictionary containing material types and their quantities used.
        :return: Total materials cost.
        """
        total_cost = 0.0
        for material, quantity in materials_used.items():
            if material not in self.materials_cost:
                raise ValueError(f"Material '{material}' not found in materials cost list.")
            if quantity < 0:
                raise ValueError(f"Quantity for material '{material}' cannot be negative.")
            total_cost += self.materials_cost[material] * quantity
        return total_cost

    def calculate_equipment_cost(self, equipment_used: Dict[str, float]) -> float:
        """
        Calculate the total equipment rental cost based on equipment used.
        
        :param equipment_used: A dictionary containing equipment types and their quantities used.
        :return: Total equipment cost.
        """
        total_cost = 0.0
        for equipment, quantity in equipment_used.items():
            if equipment not in self.equipment_cost:
                raise ValueError(f"Equipment '{equipment}' not found in equipment cost list.")
            if quantity < 0:
                raise ValueError(f"Quantity for equipment '{equipment}' cannot be negative.")
            total_cost += self.equipment_cost[equipment] * quantity
        return total_cost

    def estimate_total_cost(self, hours: float, materials_used: Dict[str, float], equipment_used: Dict[str, float]) -> float:
        """
        Estimate the total cost of the mechanical installation.
        
        :param hours: The number of labor hours.
        :param materials_used: A dictionary containing material types and their quantities used.
        :param equipment_used: A dictionary containing equipment types and their quantities used.
        :return: Total estimated cost.
        """
        labor_cost = self.calculate_labor_cost(hours)
        materials_cost = self.calculate_materials_cost(materials_used)
        equipment_cost = self.calculate_equipment_cost(equipment_used)
        
        total_cost = labor_cost + materials_cost + equipment_cost
        return total_cost

# Example usage
if __name__ == "__main__":
    # Define labor, materials, and equipment costs
    labor_rate = 50.0  # Example labor rate per hour
    materials_cost = {
        "Pipe": 10.0,
        "Fitting": 5.0,
        "Insulation": 2.0
    }
    equipment_cost = {
        "Drill": 15.0,
        "Wrench": 5.0
    }

    # Create an instance of CostEstimator
    estimator = CostEstimator(labor_rate, materials_cost, equipment_cost)

    # Define usage
    hours_worked = 10.0
    materials_used = {
        "Pipe": 5,
        "Fitting": 10
    }
    equipment_used = {
        "Drill": 2,
        "Wrench": 3
    }

    # Estimate total cost
    try:
        total_estimated_cost = estimator.estimate_total_cost(hours_worked, materials_used, equipment_used)
        print(f"Total Estimated Cost: ${total_estimated_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
