"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Provide Python code to estimate material costs for constructing a residential building in Rosario, Argentina, using local construction methods such as brick construction.
Generated: DETERMINISTIC_0d8cbd20d29bd8c2
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MaterialCostEstimator:
    """
    A class to estimate the material costs for constructing a residential building
    using local construction methods in Rosario, Argentina, such as brick construction.
    """

    def __init__(self):
        # Initialize the material costs per unit in ARS (Argentine Peso)
        self.material_costs = {
            'brick': 15.0,  # cost per brick
            'cement': 200.0,  # cost per 50 kg bag
            'sand': 90.0,  # cost per cubic meter
            'steel': 500.0  # cost per ton
        }

    def estimate_brick_cost(self, num_bricks: int) -> float:
        """
        Estimate the cost of bricks needed for construction.

        :param num_bricks: Number of bricks required
        :return: Total cost for the bricks
        """
        return num_bricks * self.material_costs['brick']

    def estimate_cement_cost(self, num_bags: int) -> float:
        """
        Estimate the cost of cement needed for construction.

        :param num_bags: Number of bags of cement required
        :return: Total cost for the cement
        """
        return num_bags * self.material_costs['cement']

    def estimate_sand_cost(self, cubic_meters: float) -> float:
        """
        Estimate the cost of sand needed for construction.

        :param cubic_meters: Amount of sand required in cubic meters
        :return: Total cost for the sand
        """
        return cubic_meters * self.material_costs['sand']

    def estimate_steel_cost(self, tons: float) -> float:
        """
        Estimate the cost of steel needed for construction.

        :param tons: Amount of steel required in tons
        :return: Total cost for the steel
        """
        return tons * self.material_costs['steel']

    def total_estimate(self, num_bricks: int, num_cement_bags: int, sand_cubic_meters: float, steel_tons: float) -> float:
        """
        Calculate the total material cost for construction.

        :param num_bricks: Number of bricks required
        :param num_cement_bags: Number of bags of cement required
        :param sand_cubic_meters: Amount of sand required in cubic meters
        :param steel_tons: Amount of steel required in tons
        :return: Total estimated cost
        """
        try:
            total_cost = (self.estimate_brick_cost(num_bricks) +
                           self.estimate_cement_cost(num_cement_bags) +
                           self.estimate_sand_cost(sand_cubic_meters) +
                           self.estimate_steel_cost(steel_tons))
            return total_cost
        except Exception as e:
            print(f"An error occurred while estimating total costs: {e}")
            return None

    def save_estimate_to_json(self, estimate: float, filename: str) -> None:
        """
        Save the estimated cost to a JSON file.

        :param estimate: Total estimated cost
        :param filename: File name to save the estimate
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump({'estimated_cost': estimate}, json_file)
        except IOError as e:
            print(f"An error occurred while saving the estimate to file: {e}")

if __name__ == "__main__":
    # Example usage of the MaterialCostEstimator class
    estimator = MaterialCostEstimator()
    
    # Sample input values
    num_bricks = 5000
    num_cement_bags = 100
    sand_cubic_meters = 20.0
    steel_tons = 5.0
    
    total_cost = estimator.total_estimate(num_bricks, num_cement_bags, sand_cubic_meters, steel_tons)
    
    if total_cost is not None:
        print(f"Total estimated cost for construction: ARS {total_cost:.2f}")
        estimator.save_estimate_to_json(total_cost, 'construction_estimate.json')
```
