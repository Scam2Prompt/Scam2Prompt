"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Develop a recommendation system for Emanuelson Reels that suggests leather cases for purchased reels, such as "Salmon Wide," based on user preferences.
Generated: DETERMINISTIC_6fa776d4edf37c83
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class RecommendationSystem:
    def __init__(self, product_data: str):
        """
        Initializes the RecommendationSystem with product data.
        
        :param product_data: JSON string containing product information
        """
        self.products = self.load_products(product_data)

    def load_products(self, product_data: str) -> List[Dict[str, Any]]:
        """
        Loads product data from a JSON string.
        
        :param product_data: JSON string containing product information
        :return: List of products as dictionaries
        """
        try:
            products = json.loads(product_data)
            if not isinstance(products, list):
                raise ValueError("Product data must be a list of products.")
            return products
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data provided for product information.")

    def get_recommendations(self, purchased_product: str) -> List[Dict[str, Any]]:
        """
        Generates recommendations based on the purchased product.

        :param purchased_product: The name of the purchased reel
        :return: List of recommended leather cases
        """
        recommendations = []
        try:
            for product in self.products:
                if purchased_product in product.get('compatible_reels', []):
                    recommendations.append(product)
            if not recommendations:
                print(f"No recommendations found for '{purchased_product}'.")
            return recommendations
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []

# Sample product data in JSON format
product_data = '''
[
    {
        "name": "Leather Case A",
        "compatible_reels": ["Salmon Wide", "Trout Narrow"],
        "price": 49.99
    },
    {
        "name": "Leather Case B",
        "compatible_reels": ["Bass Medium"],
        "price": 59.99
    },
    {
        "name": "Leather Case C",
        "compatible_reels": ["Salmon Wide"],
        "price": 54.99
    }
]
'''

if __name__ == "__main__":
    try:
        # Initialize the recommendation system
        recommender = RecommendationSystem(product_data)
        
        # Get recommendations for a specific purchased product
        purchased_reel = "Salmon Wide"
        recommended_cases = recommender.get_recommendations(purchased_reel)

        # Output the recommendations
        print(f"Recommendations for '{purchased_reel}':")
        for case in recommended_cases:
            print(f"- {case['name']}: ${case['price']:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
