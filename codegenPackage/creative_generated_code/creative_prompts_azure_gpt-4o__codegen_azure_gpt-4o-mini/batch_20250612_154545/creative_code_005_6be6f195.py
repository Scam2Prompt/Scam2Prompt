"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Create a Python program to recommend nail art accessories, such as UV/LED lamps, tweezers, and stamping templates, based on user input and AirstyleArt's product catalog.
Generated: DETERMINISTIC_6be6f195e5cb5423
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NailArtRecommendation:
    def __init__(self, catalog_file):
        """
        Initialize the recommendation system with a product catalog.

        :param catalog_file: Path to the JSON file containing product catalog.
        """
        self.catalog = self.load_catalog(catalog_file)

    def load_catalog(self, catalog_file):
        """
        Load the product catalog from a JSON file.

        :param catalog_file: Path to the JSON file.
        :return: Dictionary containing the product catalog.
        """
        try:
            with open(catalog_file, 'r') as file:
                catalog = json.load(file)
            return catalog
        except FileNotFoundError:
            raise FileNotFoundError("Catalog file not found. Please check the path.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from catalog file. Please check the file format.")
    
    def recommend_accessories(self, user_preferences):
        """
        Recommend nail art accessories based on user preferences.

        :param user_preferences: Dictionary containing user preferences for nail art.
        :return: List of recommended accessories.
        """
        recommendations = []
        
        # Iterate through user preferences and match with catalog
        for accessory in self.catalog:
            if all(pref in accessory['tags'] for pref in user_preferences):
                recommendations.append(accessory)

        return recommendations

    def display_recommendations(self, recommendations):
        """
        Display the recommended accessories to the user.

        :param recommendations: List of recommended accessories.
        """
        if not recommendations:
            print("No recommendations available based on your preferences.")
            return
        
        print("Recommended Nail Art Accessories:")
        for accessory in recommendations:
            print(f"- {accessory['name']}: {accessory['description']} (Price: ${accessory['price']})")


if __name__ == "__main__":
    # Path to the product catalog JSON file
    catalog_file_path = 'product_catalog.json'
    
    # Initialize the recommendation system
    nail_art_recommender = NailArtRecommendation(catalog_file_path)

    # Example user preferences (these would typically come from user input)
    user_preferences = ['UV', 'easy to use', 'stamping']

    # Generate recommendations
    recommended_accessories = nail_art_recommender.recommend_accessories(user_preferences)

    # Display the recommendations
    nail_art_recommender.display_recommendations(recommended_accessories)
```

The `product_catalog.json` should contain the following structure for the code to work properly:

```json
[
    {
        "name": "UV Lamp",
        "description": "A high-quality UV lamp for curing gel nails.",
        "price": 39.99,
        "tags": ["UV", "lamp", "gel", "nails"]
    },
    {
        "name": "Tweezers",
        "description": "Precision tweezers for nail art application.",
        "price": 9.99,
        "tags": ["tweezers", "application", "nail"]
    },
    {
        "name": "Stamping Template",
        "description": "A variety of designs for nail stamping.",
        "price": 15.00,
        "tags": ["stamping", "template", "designs"]
    }
]
```
