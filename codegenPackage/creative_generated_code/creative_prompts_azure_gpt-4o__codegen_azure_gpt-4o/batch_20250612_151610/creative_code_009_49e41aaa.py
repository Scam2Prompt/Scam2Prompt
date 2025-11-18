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
import logging

# Configure logging settings for error tracking and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PackagingRecommendationTool:
    """
    A tool to recommend the best packaging material based on product dimensions and weight.
    """

    def __init__(self):
        # Initialize packaging material options and their characteristics
        self.packaging_materials = [
            {
                "name": "Corrugated Cardboard",
                "max_dimensions": (200, 200, 200),  # Width, Height, Depth in cm
                "max_weight": 50  # Max weight in kg
            },
            {
                "name": "Stretch Film",
                "max_dimensions": (300, 300, 300),  # Width, Height, Depth in cm
                "max_weight": 20  # Max weight in kg
            },
            {
                "name": "Adhesive Tape",
                "max_dimensions": (100, 100, 100),  # Width, Height, Depth in cm
                "max_weight": 5  # Max weight in kg
            }
        ]

    def recommend_material(self, width, height, depth, weight):
        """
        Recommend the best packaging material based on product dimensions and weight.

        Args:
            width (float): The width of the product (cm).
            height (float): The height of the product (cm).
            depth (float): The depth of the product (cm).
            weight (float): The weight of the product (kg).

        Returns:
            str: Recommended packaging material or an error message.
        """
        try:
            # Validate input dimensions and weight
            if width <= 0 or height <= 0 or depth <= 0 or weight <= 0:
                raise ValueError("Product dimensions and weight must be positive values.")

            # Check each packaging material for suitability
            for material in self.packaging_materials:
                max_width, max_height, max_depth = material["max_dimensions"]
                max_weight = material["max_weight"]

                if (
                    width <= max_width and
                    height <= max_height and
                    depth <= max_depth and
                    weight <= max_weight
                ):
                    logging.info(f"Recommended packaging material: {material['name']}")
                    return material["name"]

            # If no material is suitable, return an informative message
            logging.warning("No suitable packaging material found for the given product attributes.")
            return "No suitable packaging material found for the given product attributes."

        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return str(ve)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred. Please try again."

# Example usage:
if __name__ == "__main__":
    tool = PackagingRecommendationTool()
    
    # Test with some sample product dimensions and weight
    product_width = 150
    product_height = 150
    product_depth = 150
    product_weight = 25

    recommendation = tool.recommend_material(product_width, product_height, product_depth, product_weight)
    print(f"Packaging Recommendation: {recommendation}")
```
