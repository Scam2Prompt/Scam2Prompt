"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Create an algorithm to recommend gloves for specific use cases, such as welding, gardening, or motorbike riding, based on the detailed categories provided by Rising Star International.
Generated: DETERMINISTIC_7c8da2f37b51cf1d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class GloveCategory(Enum):
    """Enumeration of glove categories provided by Rising Star International."""
    WELDING = "welding"
    GARDENING = "gardening"
    MOTORBIKE = "motorbike"
    CHEMICAL = "chemical"
    MEDICAL = "medical"
    CONSTRUCTION = "construction"
    FOOD = "food"
    GENERAL_PURPOSE = "general_purpose"

class GloveRecommendation:
    """Represents a glove recommendation with attributes."""
    def __init__(self, name: str, category: GloveCategory, material: str, features: List[str], durability: str):
        self.name = name
        self.category = category
        self.material = material
        self.features = features
        self.durability = durability

class GloveRecommender:
    """Recommends gloves based on use cases and categories."""
    def __init__(self):
        self._load_glove_database()

    def _load_glove_database(self) -> None:
        """Loads glove data from a JSON file or initializes default data."""
        try:
            with open('glove_database.json', 'r') as file:
                self.glove_data = json.load(file)
        except FileNotFoundError:
            self.glove_data = self._initialize_default_data()
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in glove_database.json")

    def _initialize_default_data(self) -> Dict:
        """Initializes default glove data if no database file exists."""
        return {
            GloveCategory.WELDING.value: [
                {
                    "name": "Heavy-Duty Welding Gloves",
                    "material": "leather",
                    "features": ["heat_resistant", "abrasion_resistant"],
                    "durability": "high"
                }
            ],
            GloveCategory.GARDENING.value: [
                {
                    "name": "ComfortGrip Gardening Gloves",
                    "material": "cotton",
                    "features": ["breathable", "lightweight"],
                    "durability": "medium"
                }
            ],
            GloveCategory.MOTORBIKE.value: [
                {
                    "name": "RiderPro Bike Gloves",
                    "material": "synthetic_leather",
                    "features": ["grip_enhanced", "windproof"],
                    "durability": "high"
                }
            ]
        }

    def recommend_gloves(self, category: GloveCategory) -> List[GloveRecommendation]:
        """
        Recommends gloves for a specific category.
        
        Args:
            category: The category of gloves to recommend.
        
        Returns:
            List of GloveRecommendation objects for the given category.
        
        Raises:
            ValueError: If the category is invalid or no gloves are found.
        """
        if not isinstance(category, GloveCategory):
            raise ValueError("Invalid glove category")

        category_data = self.glove_data.get(category.value)
        if not category_data:
            raise ValueError(f"No gloves found for category: {category.value}")

        recommendations = []
        for glove in category_data:
            recommendations.append(
                GloveRecommendation(
                    name=glove["name"],
                    category=category,
                    material=glove["material"],
                    features=glove["features"],
                    durability=glove["durability"]
                )
            )
        return recommendations

    def get_all_categories(self) -> List[GloveCategory]:
        """Returns all available glove categories."""
        return list(GloveCategory)

# Example usage
if __name__ == "__main__":
    try:
        recommender = GloveRecommender()
        print("Available categories:")
        for category in recommender.get_all_categories():
            print(f"- {category.value}")

        category = GloveCategory.WELDING
        recommendations = recommender.recommend_gloves(category)
        print(f"\nRecommendations for {category.value}:")
        for glove in recommendations:
            print(f"Name: {glove.name}")
            print(f"Material: {glove.material}")
            print(f"Features: {', '.join(glove.features)}")
            print(f"Durability: {glove.durability}\n")
    except ValueError as e:
        print(f"Error: {e}")
```
