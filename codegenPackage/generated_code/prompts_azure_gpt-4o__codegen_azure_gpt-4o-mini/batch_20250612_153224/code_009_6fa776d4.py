"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Develop a recommendation system for Emanuelson Reels that suggests leather cases for purchased reels, such as "Salmon Wide," based on user preferences.
Generated: DETERMINISTIC_6fa776d4edf37c83
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class RecommendationSystem:
    def __init__(self, product_data: str):
        """
        Initializes the RecommendationSystem with product data.

        :param product_data: JSON string containing product information.
        """
        self.products = self.load_product_data(product_data)

    def load_product_data(self, product_data: str) -> List[Dict[str, Any]]:
        """
        Loads product data from a JSON string.

        :param product_data: JSON string containing product information.
        :return: List of products as dictionaries.
        """
        try:
            return json.loads(product_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid product data format") from e

    def get_recommendations(self, purchased_reel: str, user_preferences: Dict[str, Any]) -> List[str]:
        """
        Generates recommendations based on the purchased reel and user preferences.

        :param purchased_reel: The name of the purchased reel.
        :param user_preferences: A dictionary containing user preferences.
        :return: List of recommended leather cases.
        """
        recommendations = []
        for product in self.products:
            if self.is_recommendable(product, purchased_reel, user_preferences):
                recommendations.append(product['name'])
        return recommendations

    def is_recommendable(self, product: Dict[str, Any], purchased_reel: str, user_preferences: Dict[str, Any]) -> bool:
        """
        Determines if a product is recommendable based on the purchased reel and user preferences.

        :param product: The product to evaluate.
        :param purchased_reel: The name of the purchased reel.
        :param user_preferences: A dictionary containing user preferences.
        :return: True if the product is recommendable, False otherwise.
        """
        # Example logic for recommendation
        if product['type'] == 'leather_case' and purchased_reel in product['compatible_reels']:
            for key, value in user_preferences.items():
                if key in product and product[key] != value:
                    return False
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Sample product data in JSON format
    product_data = '''
    [
        {"name": "Leather Case A", "type": "leather_case", "compatible_reels": ["Salmon Wide"], "color": "brown"},
        {"name": "Leather Case B", "type": "leather_case", "compatible_reels": ["Trout Narrow"], "color": "black"},
        {"name": "Leather Case C", "type": "leather_case", "compatible_reels": ["Salmon Wide", "Trout Narrow"], "color": "tan"}
    ]
    '''

    # User preferences
    user_preferences = {
        "color": "brown"
    }

    # Create a recommendation system instance
    recommender = RecommendationSystem(product_data)

    # Get recommendations for a purchased reel
    recommendations = recommender.get_recommendations("Salmon Wide", user_preferences)

    # Output recommendations
    print("Recommended leather cases:", recommendations)
```
