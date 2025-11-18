"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Develop a tool to recommend the best packaging material (e.g., corrugated cardboard, stretch film, or adhesive tape) for specific product dimensions and weights, using the product attributes from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_49e41aaad183175e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to handle packaging recommendations
class PackagingRecommender:
    def __init__(self):
        # Predefined packaging materials with their weight limits and dimensions
        self.packaging_materials = [
            {
                "name": "Corrugated Cardboard",
                "max_weight": 10.0,  # Maximum weight in kg
                "max_dimensions": (60, 40, 20)  # Maximum dimensions in cm (length, width, height)
            },
            {
                "name": "Stretch Film",
                "max_weight": 15.0,
                "max_dimensions": (50, 50, 50)
            },
            {
                "name": "Adhesive Tape",
                "max_weight": 2.0,
                "max_dimensions": (10, 10, 10)
            }
        ]

    def recommend_packaging(self, weight, dimensions):
        """
        Recommend the best packaging material based on product weight and dimensions.

        :param weight: Weight of the product in kg
        :param dimensions: Tuple containing (length, width, height) in cm
        :return: List of recommended packaging materials
        """

        recommended_materials = []

        # Validate input
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")
        
        if not (isinstance(dimensions, tuple) and len(dimensions) == 3):
            raise ValueError("Dimensions must be a tuple of three numbers (length, width, height).")
        
        length, width, height = dimensions
        
        # Check each packaging material against the product weight and dimensions
        for material in self.packaging_materials:
            max_weight = material["max_weight"]
            max_dimensions = material["max_dimensions"]

            if weight <= max_weight and all(dim <= max_dim for dim, max_dim in zip(dimensions, max_dimensions)):
                recommended_materials.append(material["name"])

        return recommended_materials

if __name__ == "__main__":
    # Example usage
    recommender = PackagingRecommender()

    # Input product attributes
    product_weight = 5.0  # in kg
    product_dimensions = (50, 30, 15)  # in cm (length, width, height)

    try:
        recommendations = recommender.recommend_packaging(product_weight, product_dimensions)
        if recommendations:
            print("Recommended Packaging Materials:", ", ".join(recommendations))
        else:
            print("No suitable packaging materials found.")
    except ValueError as e:
        print(f"Error: {e}")
```
