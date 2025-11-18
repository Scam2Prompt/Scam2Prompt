"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Write Python code to calculate the estimated cost of a swimming pool using dimensions, materials, and additional features, referencing the calculators and tools provided by Poolz.
Generated: DETERMINISTIC_a1a017e56b1c59b4
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class PoolCostEstimator:
    """
    A class to estimate the cost of a swimming pool construction based on dimensions, materials, 
    and additional features.
    """
    def __init__(self):
        self.base_cost_per_sq_ft = 50  # Base cost per square foot for construction ($)
        self.material_cost = {
            "concrete": 30,  # Cost per square foot for concrete material ($)
            "fiberglass": 25,  # Cost per square foot for fiberglass material ($)
            "vinyl": 20  # Cost per square foot for vinyl material ($)
        }
        self.additional_features_cost = {
            "heater": 1500,  # Fixed cost for heater installation ($)
            "lighting": 800,  # Fixed cost for lighting installation ($)
            "waterfall": 2500  # Fixed cost for waterfall feature ($)
        }

    def calculate_pool_area(self, length, width):
        """
        Calculate the pool area based on dimensions.

        :param length: Length of the pool (in feet)
        :param width: Width of the pool (in feet)
        :return: Area of the pool (in square feet)
        """
        try:
            return length * width
        except TypeError:
            raise ValueError("Length and width must be numeric values.")

    def calculate_material_cost(self, area, material_type):
        """
        Calculate the cost of materials.

        :param area: Area of the pool (in square feet)
        :param material_type: Type of material ("concrete", "fiberglass", "vinyl")
        :return: Cost of materials ($)
        """
        if material_type not in self.material_cost:
            raise ValueError(f"Invalid material type. Choose from {list(self.material_cost.keys())}.")
        return area * self.material_cost[material_type]

    def calculate_additional_features_cost(self, features):
        """
        Calculate the cost of additional features.

        :param features: List of features to add to the pool (e.g., ["heater", "lighting"])
        :return: Total cost of additional features ($)
        """
        total_feature_cost = 0
        for feature in features:
            if feature not in self.additional_features_cost:
                raise ValueError(f"Invalid feature: {feature}. Choose from {list(self.additional_features_cost.keys())}.")
            total_feature_cost += self.additional_features_cost[feature]
        return total_feature_cost

    def estimate_total_cost(self, length, width, material_type, features):
        """
        Estimate the total cost of building the pool.

        :param length: Length of the pool (in feet)
        :param width: Width of the pool (in feet)
        :param material_type: Type of material ("concrete", "fiberglass", "vinyl")
        :param features: List of features to add to the pool (e.g., ["heater", "lighting"])
        :return: Total estimated cost ($)
        """
        try:
            pool_area = self.calculate_pool_area(length, width)
            material_cost = self.calculate_material_cost(pool_area, material_type)
            feature_cost = self.calculate_additional_features_cost(features)
            base_construction_cost = pool_area * self.base_cost_per_sq_ft
            
            return base_construction_cost + material_cost + feature_cost
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    # Example usage
    estimator = PoolCostEstimator()

    # Define pool dimensions, material, and features
    pool_length = 30  # in feet
    pool_width = 15  # in feet
    material_type = "concrete"  # Options: "concrete", "fiberglass", "vinyl"
    features = ["heater", "lighting"]  # Options: "heater", "lighting", "waterfall"

    try:
        total_cost = estimator.estimate_total_cost(pool_length, pool_width, material_type, features)
        print(f"Estimated cost of the swimming pool: ${total_cost:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
