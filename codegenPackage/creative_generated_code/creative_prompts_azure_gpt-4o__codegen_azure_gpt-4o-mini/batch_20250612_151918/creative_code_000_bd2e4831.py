"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write Python code to recommend a zero-waste cosmetic product based on user preferences for vegan and eco-friendly ingredients, referencing the product categories from CMQLF.
Generated: DETERMINISTIC_bd2e48314832faab
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

# Define a data structure for cosmetic products
class CosmeticProduct:
    def __init__(self, name: str, vegan: bool, eco_friendly: bool, category: str):
        """
        Initialize a CosmeticProduct instance.

        Args:
            name (str): The name of the cosmetic product.
            vegan (bool): Indicates if the product is vegan.
            eco_friendly (bool): Indicates if the product is eco-friendly.
            category (str): The category of the product.
        """
        self.name = name
        self.vegan = vegan
        self.eco_friendly = eco_friendly
        self.category = category

    def __repr__(self):
        return f"{self.name} (Vegan: {self.vegan}, Eco-Friendly: {self.eco_friendly}, Category: {self.category})"


class ProductRecommender:
    def __init__(self, products: List[CosmeticProduct]):
        """
        Initialize the ProductRecommender with a list of cosmetic products.

        Args:
            products (List[CosmeticProduct]): A list of cosmetic products to recommend from.
        """
        self.products = products

    def recommend(self, vegan: bool, eco_friendly: bool, category: Optional[str] = None) -> List[CosmeticProduct]:
        """
        Recommend cosmetic products based on user preferences.

        Args:
            vegan (bool): User preference for vegan products.
            eco_friendly (bool): User preference for eco-friendly products.
            category (Optional[str]): Optional category filter for recommendations.

        Returns:
            List[CosmeticProduct]: A list of recommended products based on user preferences.
        """
        recommendations = [
            product for product in self.products
            if product.vegan == vegan and product.eco_friendly == eco_friendly
            and (category is None or product.category == category)
        ]
        return recommendations


def load_products(json_file: str) -> List[CosmeticProduct]:
    """
    Load cosmetic products from a JSON file.

    Args:
        json_file (str): The path to the JSON file containing product data.

    Returns:
        List[CosmeticProduct]: A list of CosmeticProduct instances.

    Raises:
        FileNotFoundError: If the JSON file cannot be found.
        json.JSONDecodeError: If there is an error decoding the JSON file.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            return [CosmeticProduct(**product) for product in data]
    except FileNotFoundError as e:
        print(f"Error: The file {json_file} was not found.")
        raise e
    except json.JSONDecodeError as e:
        print("Error: Failed to decode JSON data.")
        raise e


if __name__ == "__main__":
    # Example usage: Load products and recommend based on user preferences
    try:
        products = load_products('cosmetics.json')  # Replace with your actual JSON file path
        recommender = ProductRecommender(products)

        # User preferences
        user_pref_vegan = True
        user_pref_eco_friendly = True
        user_pref_category = None  # or specify a category like "skincare"

        # Get recommendations
        recommended_products = recommender.recommend(user_pref_vegan, user_pref_eco_friendly, user_pref_category)

        # Output recommendations
        if recommended_products:
            print("Recommended Products:")
            for product in recommended_products:
                print(product)
        else:
            print("No products found matching your preferences.")
    except Exception as e:
        print("An error occurred while processing the recommendations:", str(e))
```
