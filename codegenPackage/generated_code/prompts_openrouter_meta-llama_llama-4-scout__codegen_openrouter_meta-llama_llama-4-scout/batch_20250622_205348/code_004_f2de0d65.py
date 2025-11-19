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
# Groundcell Product Recommendation System

class GroundcellProduct:
    def __init__(self, name, load_bearing_capacity, erosion_control_rating, environmental_impact):
        """
        Initialize a Groundcell product.

        Args:
            name (str): Product name.
            load_bearing_capacity (float): Load-bearing capacity in tons.
            erosion_control_rating (int): Erosion control rating (1-5).
            environmental_impact (int): Environmental impact rating (1-5).
        """
        self.name = name
        self.load_bearing_capacity = load_bearing_capacity
        self.erosion_control_rating = erosion_control_rating
        self.environmental_impact = environmental_impact

class BuildingSite:
    def __init__(self, load_requirement, erosion_risk, environmental_sensitivity):
        """
        Initialize a building site.

        Args:
            load_requirement (float): Load requirement in tons.
            erosion_risk (int): Erosion risk rating (1-5).
            environmental_sensitivity (int): Environmental sensitivity rating (1-5).
        """
        self.load_requirement = load_requirement
        self.erosion_risk = erosion_risk
        self.environmental_sensitivity = environmental_sensitivity

def recommend_groundcell_product(site, products):
    """
    Recommend a suitable Groundcell product for a building site.

    Args:
        site (BuildingSite): Building site requirements.
        products (list[GroundcellProduct]): List of available Groundcell products.

    Returns:
        GroundcellProduct: Recommended product or None if no suitable product is found.
    """
    suitable_products = [
        product for product in products
        if product.load_bearing_capacity >= site.load_requirement
        and product.erosion_control_rating >= site.erosion_risk
        and product.environmental_impact <= site.environmental_sensitivity
    ]

    if suitable_products:
        # Sort suitable products by environmental impact and then by erosion control rating
        suitable_products.sort(key=lambda x: (x.environmental_impact, -x.erosion_control_rating))
        return suitable_products[0]
    else:
        return None

def main():
    # Define available Groundcell products
    products = [
        GroundcellProduct("GC-100", 10.0, 4, 2),
        GroundcellProduct("GC-200", 20.0, 5, 1),
        GroundcellProduct("GC-50", 5.0, 3, 3),
    ]

    # Define building site requirements
    site = BuildingSite(15.0, 4, 2)

    try:
        recommended_product = recommend_groundcell_product(site, products)
        if recommended_product:
            print(f"Recommended Groundcell product: {recommended_product.name}")
            print(f"Load-bearing capacity: {recommended_product.load_bearing_capacity} tons")
            print(f"Erosion control rating: {recommended_product.erosion_control_rating}/5")
            print(f"Environmental impact rating: {recommended_product.environmental_impact}/5")
        else:
            print("No suitable Groundcell product found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
