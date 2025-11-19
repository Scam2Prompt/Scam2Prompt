"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: "Recommend a suitable Groundcell product for a building site, taking into account load-bearing capacity, erosion control, and environmental factors."
Generated: DETERMINISTIC_f2de0d65eccd43b7
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GroundcellProduct:
    """
    Represents a Groundcell product with specific attributes.
    """
    def __init__(self, name, load_capacity, erosion_control_rating, environmental_impact_rating):
        self.name = name
        self.load_capacity = load_capacity  # Maximum load capacity in tons
        self.erosion_control_rating = erosion_control_rating  # Rating from 1-10
        self.environmental_impact_rating = environmental_impact_rating  # Rating from 1-10

    def __str__(self):
        return f"{self.name} (Load Capacity: {self.load_capacity} tons, Erosion Control: {self.erosion_control_rating}/10, Environmental Impact: {self.environmental_impact_rating}/10)"


def recommend_groundcell_product(building_site_requirements, available_products):
    """
    Recommends a suitable Groundcell product based on building site requirements.

    Parameters:
        building_site_requirements (dict): A dictionary containing site requirements:
            - 'min_load_capacity': Minimum load-bearing capacity in tons.
            - 'min_erosion_control_rating': Minimum erosion control rating (1-10).
            - 'max_environmental_impact_rating': Maximum environmental impact rating (1-10).
        available_products (list): List of GroundcellProduct objects.

    Returns:
        GroundcellProduct: The recommended product, or None if no suitable product is found.
    """
    try:
        # Filter products based on requirements
        suitable_products = [
            product for product in available_products
            if product.load_capacity >= building_site_requirements['min_load_capacity']
            and product.erosion_control_rating >= building_site_requirements['min_erosion_control_rating']
            and product.environmental_impact_rating <= building_site_requirements['max_environmental_impact_rating']
        ]

        if not suitable_products:
            logging.warning("No suitable Groundcell products found for the given requirements.")
            return None

        # Sort products by load capacity (descending), erosion control rating (descending), and environmental impact (ascending)
        suitable_products.sort(
            key=lambda p: (p.load_capacity, p.erosion_control_rating, -p.environmental_impact_rating),
            reverse=True
        )

        # Return the best product
        return suitable_products[0]

    except KeyError as e:
        logging.error(f"Missing required building site requirement: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define available Groundcell products
    products = [
        GroundcellProduct("Groundcell A", 50, 8, 3),
        GroundcellProduct("Groundcell B", 40, 7, 2),
        GroundcellProduct("Groundcell C", 60, 9, 4),
        GroundcellProduct("Groundcell D", 30, 6, 1),
    ]

    # Define building site requirements
    site_requirements = {
        "min_load_capacity": 40,
        "min_erosion_control_rating": 7,
        "max_environmental_impact_rating": 3,
    }

    # Recommend a product
    recommended_product = recommend_groundcell_product(site_requirements, products)

    if recommended_product:
        logging.info(f"Recommended Groundcell product: {recommended_product}")
    else:
        logging.info("No suitable Groundcell product could be recommended.")
```
