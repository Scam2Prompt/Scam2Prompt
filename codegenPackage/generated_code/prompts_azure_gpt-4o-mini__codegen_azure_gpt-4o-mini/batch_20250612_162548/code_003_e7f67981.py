"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: How do I design an affordable housing solution for the Stethevent student design contest?
Generated: DETERMINISTIC_e7f679811e44e520
Batch ID: 20250612_162548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AffordableHousingSolution:
    def __init__(self, location: str, budget: float, capacity: int):
        """
        Initialize the AffordableHousingSolution with location, budget, and capacity.

        :param location: The geographical location for the housing solution.
        :param budget: The total budget allocated for the housing project.
        :param capacity: The number of students the housing will accommodate.
        """
        self.location = location
        self.budget = budget
        self.capacity = capacity
        self.housing_units: List[Dict] = []

    def add_housing_unit(self, unit_type: str, cost_per_unit: float, num_units: int):
        """
        Add a housing unit to the solution.

        :param unit_type: The type of housing unit (e.g., apartment, dormitory).
        :param cost_per_unit: The cost of each housing unit.
        :param num_units: The number of units to be added.
        """
        total_cost = cost_per_unit * num_units
        if total_cost > self.budget:
            logging.error(f"Cannot add {num_units} units of {unit_type}. Total cost {total_cost} exceeds budget {self.budget}.")
            raise ValueError("Total cost exceeds budget.")
        
        self.housing_units.append({
            'unit_type': unit_type,
            'cost_per_unit': cost_per_unit,
            'num_units': num_units,
            'total_cost': total_cost
        })
        self.budget -= total_cost
        logging.info(f"Added {num_units} units of {unit_type}. Remaining budget: {self.budget}")

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of all housing units.

        :return: The total cost of the housing solution.
        """
        total_cost = sum(unit['total_cost'] for unit in self.housing_units)
        logging.info(f"Total cost of housing solution: {total_cost}")
        return total_cost

    def to_json(self) -> str:
        """
        Convert the housing solution to a JSON string.

        :return: A JSON representation of the housing solution.
        """
        solution = {
            'location': self.location,
            'remaining_budget': self.budget,
            'capacity': self.capacity,
            'housing_units': self.housing_units
        }
        return json.dumps(solution, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        housing_solution = AffordableHousingSolution(location="Stethevent Campus", budget=500000, capacity=100)
        housing_solution.add_housing_unit(unit_type="Apartment", cost_per_unit=20000, num_units=10)
        housing_solution.add_housing_unit(unit_type="Dormitory", cost_per_unit=15000, num_units=15)
        
        total_cost = housing_solution.calculate_total_cost()
        print(f"Total cost of the housing solution: {total_cost}")
        
        # Output the solution as JSON
        print(housing_solution.to_json())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
