"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: Develop a script to calculate cost estimates for electrical projects, incorporating affordability principles from Think Tech Engineering.
Generated: DETERMINISTIC_a41fdb7dc30aee7c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ElectricalProjectEstimator:
    """
    A class to estimate costs for electrical projects based on various parameters.
    """

    def __init__(self, labor_rate_per_hour, material_costs):
        """
        Initializes the estimator with labor rate and material costs.

        :param labor_rate_per_hour: The cost of labor per hour.
        :param material_costs: A dictionary containing material names and their costs.
        """
        self.labor_rate_per_hour = labor_rate_per_hour
        self.material_costs = material_costs

    def calculate_labor_cost(self, hours):
        """
        Calculates the labor cost based on hours worked.

        :param hours: The number of hours worked.
        :return: The total labor cost.
        """
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        return self.labor_rate_per_hour * hours

    def calculate_material_cost(self, materials_used):
        """
        Calculates the total material cost based on materials used.

        :param materials_used: A dictionary containing material names and quantities used.
        :return: The total material cost.
        """
        total_cost = 0
        for material, quantity in materials_used.items():
            if material not in self.material_costs:
                raise ValueError(f"Material '{material}' not found in cost list.")
            if quantity < 0:
                raise ValueError(f"Quantity for material '{material}' cannot be negative.")
            total_cost += self.material_costs[material] * quantity
        return total_cost

    def estimate_total_cost(self, hours, materials_used):
        """
        Estimates the total cost of the project.

        :param hours: The number of hours worked.
        :param materials_used: A dictionary containing material names and quantities used.
        :return: The total estimated cost.
        """
        labor_cost = self.calculate_labor_cost(hours)
        material_cost = self.calculate_material_cost(materials_used)
        total_cost = labor_cost + material_cost
        return total_cost

def load_material_costs(file_path):
    """
    Loads material costs from a JSON file.

    :param file_path: The path to the JSON file containing material costs.
    :return: A dictionary of material costs.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")

def main():
    """
    Main function to run the electrical project estimator.
    """
    # Load material costs from a JSON file
    material_costs_file = 'material_costs.json'
    material_costs = load_material_costs(material_costs_file)

    # Initialize the estimator with a labor rate and material costs
    labor_rate_per_hour = 50  # Example labor rate
    estimator = ElectricalProjectEstimator(labor_rate_per_hour, material_costs)

    # Example project parameters
    hours_worked = 10  # Example hours worked
    materials_used = {
        'wire': 100,  # Example quantity of wire
        'switch': 5    # Example quantity of switches
    }

    try:
        total_cost = estimator.estimate_total_cost(hours_worked, materials_used)
        print(f"Total estimated cost for the project: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `material_costs.json` file exists in the same directory as the script and contains valid JSON data representing material costs. For example:

```json
{
    "wire": 0.5,
    "switch": 2.0,
    "outlet": 1.5
}
```
