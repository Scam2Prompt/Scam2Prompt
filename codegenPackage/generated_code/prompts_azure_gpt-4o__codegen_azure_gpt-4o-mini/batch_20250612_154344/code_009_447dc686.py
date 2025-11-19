"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Write a Python function to compare the environmental impact of UltraPRO™ Premium with InstaHeat™ and UltraGLOW™ Snow and Ice Melt, using product specifications from PAVA Salt & Stone.
Generated: DETERMINISTIC_447dc68608603350
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class Product:
    """
    A class to represent a product and its environmental impact specifications.
    """
    def __init__(self, name, chloride_content, melting_point, eco_friendly_rating):
        """
        Initializes a new Product instance.

        :param name: str - The name of the product
        :param chloride_content: float - The chloride content of the product (in %)
        :param melting_point: float - The melting point of the product (in °F)
        :param eco_friendly_rating: int - Eco-friendly rating (1 to 5)
        """
        self.name = name
        self.chloride_content = chloride_content
        self.melting_point = melting_point
        self.eco_friendly_rating = eco_friendly_rating

    def environmental_impact_score(self):
        """
        Calculates an environmental impact score based on product specifications.

        :return: float - The calculated environmental impact score
        """
        # Lower chloride content and higher eco-friendly rating are better
        score = (self.chloride_content * 0.5) + (100 - self.eco_friendly_rating * 20)
        return score


def compare_products(products):
    """
    Compares the environmental impact of multiple products.

    :param products: list of Product - A list of Product instances to compare
    :return: str - A summary of the comparison results
    """
    if not products:
        raise ValueError("The product list cannot be empty.")

    # Create a DataFrame to hold product data for comparison
    product_data = {
        "Name": [],
        "Chloride Content (%)": [],
        "Melting Point (°F)": [],
        "Eco-Friendly Rating": [],
        "Impact Score": []
    }

    for product in products:
        product_data["Name"].append(product.name)
        product_data["Chloride Content (%)"].append(product.chloride_content)
        product_data["Melting Point (°F)"].append(product.melting_point)
        product_data["Eco-Friendly Rating"].append(product.eco_friendly_rating)
        product_data["Impact Score"].append(product.environmental_impact_score())

    df = pd.DataFrame(product_data)

    # Sort products by impact score (lower is better)
    df_sorted = df.sort_values(by="Impact Score")

    # Generate comparison summary
    summary = "Environmental Impact Comparison:\n"
    summary += df_sorted.to_string(index=False)

    return summary


# Example usage
if __name__ == "__main__":
    try:
        # Define product specifications
        ultra_pro = Product("UltraPRO™ Premium", chloride_content=20.0, melting_point=15, eco_friendly_rating=4)
        insta_heat = Product("InstaHeat™", chloride_content=25.0, melting_point=10, eco_friendly_rating=3)
        ultra_glow = Product("UltraGLOW™ Snow and Ice Melt", chloride_content=15.0, melting_point=5, eco_friendly_rating=5)

        # Compare products
        products = [ultra_pro, insta_heat, ultra_glow]
        comparison_result = compare_products(products)
        print(comparison_result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
