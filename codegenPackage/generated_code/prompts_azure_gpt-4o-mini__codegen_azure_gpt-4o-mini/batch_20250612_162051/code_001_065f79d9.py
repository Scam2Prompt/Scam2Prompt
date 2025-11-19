"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write a Python script that automates the cost estimation process for construction projects, similar to the services offered by C&M Pinnacle.
Generated: DETERMINISTIC_065f79d9d60b91b6
Batch ID: 20250612_162051
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
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionCostEstimator:
    def __init__(self, labor_rate: float, material_costs: Dict[str, float]):
        """
        Initialize the cost estimator with labor rate and material costs.

        :param labor_rate: Hourly labor rate in currency units.
        :param material_costs: Dictionary of material names and their costs.
        """
        self.labor_rate = labor_rate
        self.material_costs = material_costs

    def estimate_labor_cost(self, hours: float) -> float:
        """
        Estimate labor cost based on hours worked.

        :param hours: Number of hours worked.
        :return: Estimated labor cost.
        """
        if hours < 0:
            logging.error("Hours worked cannot be negative.")
            raise ValueError("Hours worked cannot be negative.")
        labor_cost = self.labor_rate * hours
        logging.info(f"Estimated labor cost for {hours} hours: {labor_cost}")
        return labor_cost

    def estimate_material_cost(self, materials_used: Dict[str, float]) -> float:
        """
        Estimate material cost based on materials used.

        :param materials_used: Dictionary of material names and quantities used.
        :return: Estimated material cost.
        """
        total_material_cost = 0.0
        for material, quantity in materials_used.items():
            if material not in self.material_costs:
                logging.error(f"Material '{material}' not found in cost list.")
                raise ValueError(f"Material '{material}' not found in cost list.")
            if quantity < 0:
                logging.error(f"Quantity for material '{material}' cannot be negative.")
                raise ValueError(f"Quantity for material '{material}' cannot be negative.")
            cost = self.material_costs[material] * quantity
            total_material_cost += cost
            logging.info(f"Cost for {quantity} of {material}: {cost}")
        logging.info(f"Total material cost: {total_material_cost}")
        return total_material_cost

    def estimate_total_cost(self, hours: float, materials_used: Dict[str, float]) -> float:
        """
        Estimate the total cost of the construction project.

        :param hours: Number of labor hours.
        :param materials_used: Dictionary of materials and quantities used.
        :return: Total estimated cost.
        """
        labor_cost = self.estimate_labor_cost(hours)
        material_cost = self.estimate_material_cost(materials_used)
        total_cost = labor_cost + material_cost
        logging.info(f"Total estimated cost: {total_cost}")
        return total_cost

def load_material_costs(file_path: str) -> Dict[str, float]:
    """
    Load material costs from a JSON file.

    :param file_path: Path to the JSON file containing material costs.
    :return: Dictionary of material costs.
    """
    try:
        with open(file_path, 'r') as file:
            material_costs = json.load(file)
            logging.info("Material costs loaded successfully.")
            return material_costs
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the file.")
        raise

def main():
    # Example usage
    try:
        # Load material costs from a JSON file
        material_costs = load_material_costs('material_costs.json')
        
        # Initialize the cost estimator
        estimator = ConstructionCostEstimator(labor_rate=50.0, material_costs=material_costs)
        
        # Define hours worked and materials used
        hours_worked = 40
        materials_used = {
            'Concrete': 10,  # 10 cubic meters
            'Steel': 5       # 5 tons
        }
        
        # Estimate total cost
        total_cost = estimator.estimate_total_cost(hours_worked, materials_used)
        print(f"Total estimated cost for the project: {total_cost}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `material_costs.json` file in the same directory with the appropriate structure, for example:
```json
{
    "Concrete": 75.0,
    "Steel": 200.0,
    "Wood": 50.0
}
```
