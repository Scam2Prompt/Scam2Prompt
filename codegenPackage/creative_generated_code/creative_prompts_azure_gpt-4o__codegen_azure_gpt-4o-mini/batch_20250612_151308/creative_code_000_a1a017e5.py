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
class PoolCostEstimator:
    """
    A class to estimate the cost of a swimming pool based on dimensions, materials, and additional features.
    """

    def __init__(self, length: float, width: float, depth: float, material: str, features: list):
        """
        Initializes the PoolCostEstimator with dimensions, material, and features.
        
        :param length: Length of the pool in meters
        :param width: Width of the pool in meters
        :param depth: Depth of the pool in meters
        :param material: Material of the pool (e.g., 'concrete', 'fiberglass', 'vinyl')
        :param features: List of additional features (e.g., ['heater', 'lighting'])
        """
        self.length = length
        self.width = width
        self.depth = depth
        self.material = material.lower()
        self.features = features
        self.base_cost_per_cubic_meter = self.get_cost_per_material()
        self.feature_costs = self.get_feature_costs()
    
    def get_cost_per_material(self) -> float:
        """
        Retrieves the cost per cubic meter based on the selected material.
        
        :return: Cost per cubic meter
        :raises ValueError: If the material is not recognized
        """
        material_costs = {
            'concrete': 350,
            'fiberglass': 450,
            'vinyl': 250
        }
        
        if self.material not in material_costs:
            raise ValueError(f"Material '{self.material}' is not recognized. Please choose from {list(material_costs.keys())}.")
        
        return material_costs[self.material]

    def get_feature_costs(self) -> float:
        """
        Calculates the total cost of additional features.
        
        :return: Total cost of features
        """
        feature_costs = {
            'heater': 1500,
            'lighting': 800,
            'cover': 500,
            'waterfall': 1200
        }
        
        total_feature_cost = 0
        for feature in self.features:
            if feature in feature_costs:
                total_feature_cost += feature_costs[feature]
            else:
                print(f"Warning: Feature '{feature}' is not recognized and will be ignored.")
        
        return total_feature_cost
    
    def calculate_volume(self) -> float:
        """
        Calculates the volume of the pool in cubic meters.
        
        :return: Volume of the pool
        """
        return self.length * self.width * self.depth

    def estimate_cost(self) -> float:
        """
        Estimates the total cost of the swimming pool including base cost and features.
        
        :return: Estimated total cost
        """
        volume = self.calculate_volume()
        base_cost = volume * self.base_cost_per_cubic_meter
        total_cost = base_cost + self.feature_costs
        return total_cost

if __name__ == "__main__":
    try:
        # Example usage
        length = 10.0  # Length in meters
        width = 5.0    # Width in meters
        depth = 1.5    # Depth in meters
        material = 'concrete'
        features = ['heater', 'lighting']

        estimator = PoolCostEstimator(length, width, depth, material, features)
        total_cost = estimator.estimate_cost()
        print(f"The estimated cost of the swimming pool is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
